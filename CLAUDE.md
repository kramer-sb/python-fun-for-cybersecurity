# CLAUDE.md

This repo holds my work for **Coding for Cybersecurity: Python Fundamentals** by Brandon S. Keath (Just Hacking Training). I'm a student working through the course material and videos. I'm a beginner, and the point is for me to learn, not for Claude to do the labs for me.

## How to help me

- **Default to guiding questions.** When I'm stuck, ask questions that point me toward the answer. Give the full solution only when I explicitly ask for it.
- **Help me read errors.** When I paste a traceback, walk me through the file, line number, and error type, then ask what I think is going on before explaining.
- **Keep explanations short.** A brief summary is enough. I'll ask if I want more depth.
- **Don't write lab code for me unprompted.** Reviewing my code, pointing out bugs, and suggesting improvements is fine.
- **Tie it back to security.** When a concept has a clear cybersecurity use (log parsing, CLI tools, reporting), mention it.

## Environment

- **Coding machine:** `kali-python` (VM 201, `10.0.0.50`, `kali-python.lab`), a Kali Linux VM on my Proxmox home lab dedicated to this course. It is separate from the existing Kali VM (`10.0.0.25`), which stays as-is.
- **Home lab details:** see my `proxmox-homelab` repo. New machines follow its conventions: static IP in increments of 5, a `.lab` name in CoreDNS, and inclusion in the local, cloud, and USB backup jobs.
- **Editor:** VS Code on my Windows host, connected to the Kali VM with the Remote-SSH extension. Code, venvs, and scripts live and run on Kali.
- **Repo:** `python-fun-for-cybersecurity`, living at `~/python-fun-for-cybersecurity` on the Kali VM. That copy is the one I commit and push from. GitHub is the primary remote, and Gitea (`https://gitea.lab`) keeps a read-only mirror. Kali pushes to GitHub with its own SSH key.
- **Connecting:** from Windows, `ssh kali-python` (key-only, passphrase held by the Windows ssh-agent). Password and root SSH logins are disabled on the VM.
- Which machine a lab needs can vary. If it's unclear where a command should run, ask.
- **Python:** 3.14.7 on the VM, which meets the course recommendation. On Kali, use `python3`.
- **Docs:** the VM build itself is documented in `proxmox-homelab` (installation notes, functional doc, App Table row), not in this repo.
- **Packages:** Always use a virtual environment (`python3 -m venv .venv`, then `source .venv/bin/activate`). Never use `--break-system-packages`.
- Third-party packages used in the course: `fire`, `beautifulsoup4`.

## Repo layout

Follows the course's suggested structure:

```
python-fun-for-cybersecurity/
├── module-1-python-basics/
├── module-2-cli-tools/
├── module-3-ai-workflow/
├── module-4-projects/
├── notes.md
├── session-checklist.md
├── README.md
├── CLAUDE.md
├── .gitignore
└── .pre-commit-config.yaml
```

Project folders that need third-party packages get their own `.venv` and `requirements.txt`.

## Python conventions

Follow standard Python best practices:

- PEP 8 style, `snake_case` for variables and functions, descriptive names.
- Organize scripts with the input, processing, output (IPO) model the course uses.
- Put entry-point code under `if __name__ == "__main__":`.
- Use f-strings, `pathlib` for file paths, and `with` blocks for file handling.
- Catch specific exceptions, not bare `except:`.
- Short docstrings on functions. Comments explain *why*, not *what*.
- Use `argparse` for CLI tools once the course covers it.
- No hardcoded passwords, API keys, or tokens. Use environment variables or a placeholder value.

## Sessions

`session-checklist.md` lists what I do at the start and end of each study session. At the end of a session, remind me of anything from it I haven't done (notes entry, commit and push, progress update).

## Notes

I keep running notes in `notes.md`. At the end of each lesson (or when I ask), give me an entry to add in this format:

```
## [Module.Lesson] Title (YYYY-MM-DD)
**Key concepts:**
**Code I wrote:**
**Gotchas / errors I hit:**
**Questions to revisit:**
```

## Portfolio

I keep a separate public repo, `here-i-am`, as a running cybersecurity log. When something I build or learn would make a good write-up, flag it with one line starting with **Worth writing up:**. I'll handle the post myself.

## Security and the public repo

This repo is public and follows the same redaction rules as `proxmox-homelab`:

- **Fine to show:** private lab IPs (`10.0.0.x`, `192.168.x.x`).
- **Never committed:** passwords, API tokens, SSH keys, public-facing IPs or domains, or real logs from my systems. Use sample data for labs.
- **Secret scanning:** `gitleaks` runs before every commit through a `pre-commit` hook (same `.pre-commit-config.yaml` as the home lab repo). `pre-commit install` has to be run once in every fresh clone.
- **On Kali:** install the tools with `sudo apt install gitleaks pre-commit`, not `pip`, since Kali blocks global pip installs.
- `.gitignore` covers secret-shaped files (`.env`, `*.key`, `*.pem`, `credentials.json`, `secrets.yml`) plus Python clutter (`.venv/`, `__pycache__/`, `*.pyc`) and real log files (`*.log`).
- Credentials go in Vaultwarden, never in this repo.

Responsible use: scripts only run against my own machine, local sample files, localhost, lab systems, or systems I have explicit permission to test.

## Progress

- **Done:** Module 0 (setup). The `kali-python` VM is built, backed up, monitored, and documented in `proxmox-homelab`. The repo is on GitHub with the gitleaks hook and mirrored to Gitea. The Quick Test (`setup_test.py`) ran successfully.
- **Next:** Module 1, Python basics.