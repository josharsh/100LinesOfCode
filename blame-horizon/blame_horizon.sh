#!/usr/bin/env bash
# Filter `git blame` by cutoff time; --older flips the comparison.
# Requires: bash 4+, git, GNU date (coreutils).
set -euo pipefail

PROG=${0##*/}
DATE_BIN=${DATE_BIN:-date}

BH_TMPFILE=""
trap '[[ -n $BH_TMPFILE ]] && rm -f -- "$BH_TMPFILE"' EXIT

die() { printf 'error: %s\n' "$*" >&2; exit 1; }

usage() {
	cat >&2 <<EOF
Usage: $PROG --since <date|datetime> --file <path> [--older] [--csv]
       $PROG -h | --help

Options:
  --since <when>   Required. YYYY-MM-DD (UTC midnight) or any GNU date string.
  --file, -f <p>   Required. Path passed to \`git blame\`.
  --older          Show lines last changed BEFORE --since (default: on/after).
  --csv            Emit CSV (header + RFC 4180 quoting) instead of text.
  -h, --help       Show this help and exit.

Requires: bash 4+, git, GNU date.
EOF
}

# Bare YYYY-MM-DD is normalized to 00:00:00 UTC that day (same as README).
since_epoch() {
	local s=$1 out
	[[ $s =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]] && s="$s 00:00:00"
	out=$("$DATE_BIN" -u -d "$s" +%s 2>/dev/null) || true
	[[ $out =~ ^[0-9]+$ ]] || die "invalid --since: not a valid GNU date string: $1"
	printf '%s\n' "$out"
}

# CSV doubles embedded quotes (RFC 4180).
emit_row() {
	local mode=$1 ts=$2 author=$3 line=$4 line_no=$5 sha=$6 day qa ql
	day=$("$DATE_BIN" -u -d "@$ts" +%F)
	if ((mode)); then
		qa=${author//\"/\"\"}
		ql=${line:1}; ql=${ql//\"/\"\"}
		printf '%s,%s,"%s",%d,"%s"\n' "${sha:0:8}" "$day" "$qa" "$line_no" "$ql"
	else
		printf '%s (%s, %s) %6d  %s\n' "${sha:0:8}" "$day" "$author" "$line_no" "${line:1}"
	fi
}

main() {
	local since="" path="" older=0 csv=0 cutoff sha line_no author="" author_time="" committer_time="" ts n=0 line
	while (($#)); do
		case $1 in
		--since)
			(($# >= 2)) || { usage; die "--since requires a value"; }
			since=$2
			shift 2
			;;
		--file | -f)
			(($# >= 2)) || { usage; die "--file requires a path"; }
			path=$2
			shift 2
			;;
		--older) older=1; shift ;;
		--csv) csv=1; shift ;;
		-h | --help) usage; exit 0 ;;
		*) usage; die "unexpected argument: $1 (use --file/-f for the path)" ;;
		esac
	done
	[[ -n $since ]] || { usage; die "--since is required"; }
	[[ -n $path ]] || { usage; die "--file is required"; }

	command -v git >/dev/null 2>&1 || die "git not found in PATH"
	if ! "$DATE_BIN" --version >/dev/null 2>&1; then
		if command -v gdate >/dev/null 2>&1 && gdate --version >/dev/null 2>&1; then
			DATE_BIN=gdate
		else
			die "GNU date required; install coreutils or set DATE_BIN=/path/to/gdate"
		fi
	fi

	cutoff=$(since_epoch "$since")

	BH_TMPFILE=$(mktemp "${TMPDIR:-/tmp}/${PROG}.XXXXXX") || die "mktemp failed"
	git blame --line-porcelain -- "$path" >"$BH_TMPFILE" || die "git blame failed"
	((csv)) && echo 'sha,date,author,line_no,line_text'

	# Porcelain records end with the TAB-prefixed source line.
	while IFS= read -r line || [[ -n $line ]]; do
		case $line in
		author\ *) author=${line#author } ;;
		author-time\ *) author_time=${line#author-time } ;;
		committer-time\ *) committer_time=${line#committer-time } ;;
		$'\t'*)
			ts=${author_time:-${committer_time:-0}}
			if (( (ts >= cutoff) ^ older )); then
				emit_row "$csv" "$ts" "${author:-?}" "$line" "$line_no" "$sha"
				((++n))
			fi
			;;
		*)
			# Header: SHA, source line no., final line no.
			[[ $line =~ ^([0-9a-fA-F]{40}|[0-9a-fA-F]{64})[[:space:]]+[0-9]+[[:space:]]+([0-9]+) ]] && {
				sha=${BASH_REMATCH[1],,}
				line_no=${BASH_REMATCH[2]}
				author="" author_time="" committer_time=""
			}
			;;
		esac
	done <"$BH_TMPFILE"

	((n)) || echo "No matching lines." >&2
}

main "$@"
