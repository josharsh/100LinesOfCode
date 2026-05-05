# Blame Horizon

A tiny Bash script that filters `git blame` by time for one file. By default, it prints lines last changed on or after `--since`; with `--older`, it prints lines changed before the cutoff.

## Usage

Run from the repository root:

```bash
bash blame-horizon/blame_horizon.sh --since 2025-01-01 -f README.md
bash blame-horizon/blame_horizon.sh --since "1 week ago" --older --file README.md
bash blame-horizon/blame_horizon.sh --since 2025-01-01 --csv -f README.md > recent.csv
```

Run `bash blame-horizon/blame_horizon.sh --help` for more details.

## Sample Output

```text
80847477 (2026-02-14, Harsh Joshi)      3  ### Note - 100LinesOfCode is now actively maintained by my AI Friday - github.com/fridayjoshi
```

```text
sha,date,author,line_no,line_text
80847477,2026-02-14,"Harsh Joshi",3,"### Note - 100LinesOfCode is now actively maintained by my AI Friday - github.com/fridayjoshi"
c1235362,2026-02-14,"Harsh Joshi",4,""
```

Requires Bash 4+, Git, and GNU `date`.
