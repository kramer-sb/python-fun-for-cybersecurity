# Session Checklist

What to do at the start and end of each study session. One-time setup of the VM lives in [proxmox-homelab](https://github.com/kramer-sb/proxmox-homelab) (`functional-docs/kali-python.md`), not here.

## Starting a session

1. **Start the VM.** Proxmox (`https://10.0.0.5:8006`) > **201 (kali-python)** > **Start**. Give it a minute to boot.
2. **Resume the monitor** (if paused). Uptime Kuma (`https://kuma.lab`) > `kali-python Ping` > **Resume**.
3. **Connect VS Code.** Remote-SSH: Connect to Host > `kali-python`. Bottom-left should say **SSH: kali-python**.
4. **Open the repo.** File > Open Recent > `~/python-fun-for-cybersecurity`.
5. **Check the repo is clean.** In the VS Code terminal:

   ```bash
   git status
   ```

   "Nothing to commit, working tree clean" means last session was wrapped up properly. If there are leftover changes, commit or discard them before starting new work.
6. **Activate the venv** if the lab uses one:

   ```bash
   source .venv/bin/activate
   ```

   The prompt shows `(.venv)` when it's active.
7. **Open the course** to the next lesson, and glance at the end of `notes.md` to see where I left off.

## During a session

- Commit after each lesson or working script, not just at the end. Small commits are easier to read back later.
- Jot errors and gotchas in `notes.md` as they happen. They're easy to forget by the end.

## Ending a session

1. **Update `notes.md`** with the lesson entry (ask Claude for one in the usual format if needed).
2. **Review what changed:**

   ```bash
   git status
   git diff
   ```

   Look for anything that shouldn't be public: real IPs from outside the lab, usernames, passwords, real log files.
3. **Commit and push:**

   ```bash
   git add .
   git commit -m "Module X.Y: short description"
   git push
   ```

   Gitleaks runs on the commit. "Passed" means nothing secret-shaped was found.
4. **Check it landed.** `git status` should say "Your branch is up to date with 'origin/main'." Committed is not the same as pushed.
5. **Deactivate the venv** (if used): `deactivate`.
6. **Update progress** when a module is finished: the Progress section in `CLAUDE.md` (repo and Claude Project copies) and the Status line in `README.md`.
7. **Pause the monitor.** Uptime Kuma > `kali-python Ping` > **Pause**, so it doesn't alert while the VM is off.
8. **Shut down the VM.** Close VS Code, then Proxmox > 201 > **Shutdown** (not Stop). Or from the VS Code terminal before closing: `sudo shutdown now`.

## If something's off

| Problem | Likely cause | Fix |
|---|---|---|
| VS Code can't connect | VM is off or still booting | Start it in Proxmox, wait, retry |
| `ssh` asks for the key passphrase again | Windows ssh-agent lost the key | Admin PowerShell: `ssh-add $env:USERPROFILE\.ssh\kali-python` |
| `git push` rejected | GitHub has commits Kali doesn't (edited on the website?) | `git pull`, then push again |
| Commit blocked by gitleaks | Something secret-shaped was staged | Read the output, remove the secret, `git add` again. Don't bypass the hook |
| `pip install` says "externally-managed-environment" | venv not active | `source .venv/bin/activate` first |
