# python-fun-for-cybersecurity

My coursework for **Coding for Cybersecurity: Python Fundamentals**, taught by Brandon S. Keath on [Just Hacking Training](https://www.justhacking.com/course/coding-for-cybersecurity-python-fundamentals/). The course teaches Python by building small security tools: log parsing, CLI tools, data parsing, reporting, and safe automation.

I'm a beginner, so this repo is a learning log as much as a code collection. Everything here is typed, broken, and fixed by me as I work through the course.

## Repo structure

```
python-fun-for-cybersecurity/
  README.md
  CLAUDE.md
  notes.md
  .gitignore
  .pre-commit-config.yaml
  module-1-python-basics/
  module-2-cli-tools/
  module-3-ai-workflow/
  module-4-projects/
```

- **`module-*/`** - scripts and labs, organized the way the course suggests.
- **`notes.md`** - running notes for each lesson: key concepts, the code I wrote, errors I hit, and questions to come back to.
- **`CLAUDE.md`** - instructions for Claude, which I use as a tutor for this course. The short version: guiding questions first, full solutions only when I ask. The course encourages using AI as a helper, not a replacement, and this file is how I hold it to that.

## Environment

- Code lives and runs on a dedicated Kali Linux VM in my Proxmox home lab (documented in [proxmox-homelab](https://github.com/kramer-sb/proxmox-homelab)).
- I edit from VS Code on Windows, connected to the VM with the Remote-SSH extension.
- Python 3.14. Any project that needs third-party packages gets its own virtual environment.

## Security

This repo is public, so it follows the same rules as my home lab repo:

- Labs use sample data only. No real logs, credentials, or public-facing addresses from my systems.
- `gitleaks` runs before every commit through a `pre-commit` hook and blocks anything that looks like a secret.
- `.gitignore` keeps secret-shaped files, virtual environments, and log files out of Git.
- Every script here is meant to run only against my own machine, local files, lab systems, or systems I have permission to test.

## Status

In progress. Currently on Module 0 (setup).