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
