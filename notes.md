# 0 - Course Intro / Overview

## Build
- Installed Kali Linux (Kali-Python) in my home lab. SSH into it from VS Code, using my windows host. I don't want to fill up the VM with tools I already have and can use.
- Idea is to type code out and build that muscle memory!
- Installed fire and beautiful soup

# 1 - Intro to Python Fundamentals for Cybersecurity

## Labs and Practice Activities
- installed AREPL, really handy for seeing what prints & what the variables are in your python code. 
  
## [1.2] Python Syntax & Indentation 
- rules that indicate how code must be written to execute
- tab vs 4 spaces
- colons begin blocks
- common errors

## [1.3] Fix the Broken Script (Lab)
- [fix_the_broken_script.py](module-1-python-basics/fix_broken_script.py) - followed a 9-step process to see what the code was doing, what it should be doing, and fixing it.

## [1.4] Variables & Data Types
- Use case: Failed Login Tracker. variables and >= to determine if a login attempt was suspicious: is_suspicious = failed_logins >= threshold
  
## [1.5] Password Strength Tester (Lab)
- [password_strength_tester.py](module-1-python-basics/password_strength_tester.py) - fun way to test a fake password. I upped it to 16 char instead of the 12 the lesson called for. 

## [1.6] Conditional Logic
- if, if-else, elif
- booleans
- = and ==

### Git: divergent branches (2026-10-04) (Errors due to user actions!)
**Key concepts:** Branches diverge when local and remote each have commits the other lacks. Fast-forward only works when one side is strictly behind. Rebase replays my local commits on top of the remote ones; merge adds a merge commit. Neither loses work.  

**Code I wrote:** None for this one. Fix: `git pull --rebase origin main`, then `git push origin main`.

**Gotchas / errors I hit:** `git pull` failed with "fatal: Need to specify how to reconcile divergent branches." Cause: I edited README and notes in GitHub's web UI the day before, so the Kali clone was missing those commits. `git log --oneline --graph --all` showed the split. Use `q` to exit the pager.   

**Questions to revisit:** Merge vs. rebase for shared repos.  Set `pull.rebase true` for this repo (local scope, not global).

**Verified gitleaks:** Tested the pre-commit hook from VS Code Source Control with a scratch file containing a fake AWS-style access key (random characters, not a real credential). The commit was blocked. Gitleaks reported `RuleID: aws-access-token`, `File: gitleaks_test.py`, `Line: 2`. Deleted the scratch file afterward; nothing was committed or pushed.

## [1.7] Log Analyzer Lite (Lab) (2026-10-04)

Scenario: referring to separate auth.log, create a file & find how many failed login attempts there were. 

**Gotchas / errors I hit:** Syntax! First `if` statement, I capitalized "Password" where I should have left it lowercase. Here's the corrected code
```
if "Failed password" in line:
failed_attempts += 1
```

## [1.8]Loops + Lists