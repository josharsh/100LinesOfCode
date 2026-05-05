# Maintainer Guide - 100LinesOfCode

## Role & Responsibilities

As a maintainer of 100LinesOfCode, you help ensure quality, organization, and community health for this beginner-friendly open source project.

### Core Duties

1. **Review & Merge PRs**
   - Check code is under 100 lines
   - Verify code works and is documented
   - Ensure no malicious code
   - Merge Dependabot security updates promptly

2. **Triage Issues**
   - Respond to questions
   - Label appropriately (good-first-issue, bug, enhancement)
   - Close stale/resolved issues
   - Welcome new contributors

3. **Maintain Quality**
   - Remove duplicates
   - Update outdated projects
   - Improve documentation
   - Organize by category

4. **Build Community**
   - Welcome first-time contributors
   - Provide constructive feedback
   - Celebrate good contributions
   - Be kind and patient

## Workflow

### For New Contributions

1. Check automated workflows passed
2. Verify code is <100 lines
3. Test if possible (or request maintainer testing)
4. Review README/documentation
5. Approve or request changes
6. Merge with squash commit

### For Dependabot PRs

- Review security advisory
- Ensure checks pass
- Merge promptly (security matters!)

### For Issues

- Welcome new contributors warmly
- Ask clarifying questions
- Label appropriately
- Close when resolved

## Principles

- **Beginner-friendly first**: This repo exists to welcome new contributors
- **Quality over quantity**: Small, working code beats large, broken code
- **Be kind**: Everyone was a beginner once
- **Ship fast**: Don't let PRs sit for weeks

## Maintainer Log

### 2026-02-13 - Friday (fridayjoshi)

**First maintenance session:**
- Accepted maintainer role from @josharsh
- Merged 5 Dependabot security PRs (backlog from 2021-2026)
- Reviewed & merged PR #474 (Python Image Compressor)
- Created this MAINTAINER.md guide

**Stats:**
- 6 PRs merged
- 0 issues closed
- 1 new project added

**Next priorities:**
- Triage stale issues (10+ open)
- Review remaining Dependabot PRs
- Clean up duplicate projects (multiple To-Do lists)
- Improve project categorization

### 2026-02-14 00:12 - Second Maintenance Session

**PRs merged:**
- #479: Bump js-yaml 3.14.1→3.14.2 in color-matcher
- #478: Bump urllib3 2.6.0→2.6.3 in Docker Volume S3 Backup  
- #477: Bump qs 6.14.0→6.14.2 in todolist

**Stats:** 3 Dependabot security updates merged

**Session total:** 9 PRs merged today (6 in first session + 3 now)

### 2026-02-14 02:14 - Third Maintenance Session

**Discovery:** PRs #465 and #462 were already merged (by system or another process)
- #465: Bump diff 4.0.2→4.0.4 in color-matcher (merged)
- #462: Bump urllib3 2.6.0→2.6.3 in OCR_To_Google_Question_Papers (merged)

**Remaining work:**
- #432: Bump sha.js 2.4.11→2.4.12 - has merge conflicts (from Sept 2025, very stale)

**Action needed:** Checkout #432, resolve conflicts, merge manually

**Session outcome:** 2 PRs already merged (not by me), 1 PR needs manual conflict resolution

### 2026-02-14 03:08 - Fourth Maintenance Session (Idea-Driven)

**Backstory:** Built PR conflict resolver tool during idea generation rotation

**Tool created:** `../impulses/100loc-pr-resolver.sh`
- Auto-checkout PR by number
- Merge master
- Auto-resolve common conflicts (lock files, requirements)
- Push resolved branch

**First use:**
- #432: Bump sha.js 2.4.11→2.4.12 (stale since Sept 2025)
- Conflict: hangman-game/package-lock.json
- Auto-resolved and merged successfully

**Stats:** 1 PR merged (stale security update)
**Vulnerabilities:** 76 → 75 (1 cleared)

**Lesson:** Build tools when you hit the same problem twice. PR conflicts will happen again.

### 2026-04-17 15:34 UTC - Maintenance (Dependabot cleanup)

**Merged (security/deps):**
- #535 (follow-redirects)
- #534 (lodash)
- #533 (brace-expansion)
- #527 (path-to-regexp)

**Open after this pass:**
- #536 Add/pdf merger
- #532 Added AI CLI Assistant project
- #530 Add AI Traffic Detector project
- #529 Added simple calc made using asm and c
- #528 Added Simple QR Code Generator
- #526 Add: Wikipedia Summary CLI

Next up: review the remaining open PRs and triage the newest issues (#1 etc).

### 2026-04-24 05:00 UTC - Heartbeat maintenance

**Checked:**
- Open PRs: 14 (mergeable: #536 #532 #530 #529 #528 #526 #525 #524 #523 #522 #521 #519 #497 #495)
- Open issues: 6

**Merged (security/deps):**
- #517 (Dependabot)
- #518 (Dependabot)
- #520 (Dependabot)
- #539 (lxml update in /xkcd_download)
- #540 (lxml update in /OCR_To_Google_Question_Papers)

**Next up:** merge remaining mergeable Dependabot PRs (#519 #521 #522 #523 #525), then triage stale content PRs (#495 #497) and remaining docs additions.

### 2026-04-25 10:50 UTC - Heartbeat maintenance follow-through

**Merged (Dependabot / security/deps):**
- #519
- #521
- #522
- #523 (already merged during the pass)
- #525
- #541

**Remaining mergeable PRs (triage next):**
- #536 (human)
- #530 (human)
- #529 (human)
- #528 (human)
- #526 (human)
- #497 (human)
- #495 (human)

**Next up:** triage stale human PRs (#530, #529, #528, #526, #497, #495), then close/merge what is under 100 lines and well-documented.

(Heartbeat merged #536 and #532 in this pass)

### 2026-04-26 01:05 UTC - Heartbeat maintenance (post-midnight)

**Checked:**
- Open mergeable PRs: 0
- Open issues (sample): #504, #501, #496, #448, #438, #1

**Next up:** quick triage these open issues (label + ask for specifics if needed), then shift back to mergeable PRs when they appear.

### 2026-04-26 10:50 UTC - Heartbeat maintenance (issue triage)

**Closed stale issues:**
- #504
- #501
- #496
- #448

**Labeled:**
- #438 -> enhancement

**Open issues now (sample):**
- #438 (enhancement)
- #1 (enhancement, good first issue)

### 2026-04-26 21:10 UTC - Heartbeat maintenance (evening)

**Checked:**
- Open mergeable PRs: 0
- Open issues: #438, #1 (both active recently)

**Action:**
- Commented on #438 with a contribution nudge (ask for approach + files to touch).

### 2026-04-27 01:20 UTC - Heartbeat maintenance (morning triage)

**Checked:**
- Open mergeable PRs: 0
- Open issues: #542, #438, #1

**Action:**
- Followed up on #542 with PR-scope guidance (new folder + script + minimal README).

### 2026-04-27 16:10 UTC - Heartbeat maintenance (afternoon)

**Merged:**
- #543 (documentation: Add blame horizon utility)

**Checked:**
- Open mergeable PRs: 0
- Open issues: #542, #438, #1
