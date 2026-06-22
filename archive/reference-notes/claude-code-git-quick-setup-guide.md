---
title: "Claude Code + Git Quick Setup Guide"
source_archive: "Software Projects"
source_path: "####Software Projects/1 - References/Claude Code + Git Quick Setup Guide.docx"
status: reference
privacy: private/internal
tags:
  - planning
---

# Claude Code + Git Quick Setup Guide

> Imported from the source archive and converted to Markdown for searchability. Treat the source path as provenance, not as the current canonical location.
Claude Code + Git Quick Setup Guide

1. One-time machine setup

Check Git is installed

git --version

Set your global Git identity

git config --global user.name "WhiteHatForHire"

git config --global user.email "stephensm2011@gmail.com"

Check it:

git config --global --list

Check GitHub CLI is installed

gh --version

If not installed on Windows:

winget install --id GitHub.cli

Then log in:

gh auth login

Recommended choices:

GitHub.com

HTTPS

Login with browser

Check login:

gh auth status

2. Starting a new Claude Code project and putting it on GitHub

Go into your project folder:

cd path/to/your/project

Initialize Git:

git init

Add files and commit:

git add .

git commit -m "Initial commit"

Create a GitHub repo and push:

gh repo create my-project-name --public --source . --push

Or private:

gh repo create my-project-name --private --source . --push

3. Everyday workflow

After making changes in Claude Code:

Check what changed

git status

Add everything

git add .

Commit with a message

git commit -m "Describe what changed"

Push to GitHub

git push

Main loop:

git add .

git commit -m "message"

git push

4. Most common Git commands

See current status

git status

See commit history

git log --oneline

See remote repo

git remote -v

See current branch

git branch

Rename branch to main

git branch -M main

Pull latest changes from GitHub

git pull

Clone a repo onto your machine

git clone https://github.com/WhiteHatForHire/REPO.git

5. Common use cases

A) I made edits and want to save them to GitHub

git add .

git commit -m "Update project"

git push

B) I forgot whether this folder is already a Git repo

git status

If it says not a git repository:

git init

C) I want to connect an existing local project to a GitHub repo

git remote add origin https://github.com/WhiteHatForHire/REPO.git

git branch -M main

git push -u origin main

D) I already have an origin and need to replace it

git remote remove origin

git remote add origin https://github.com/WhiteHatForHire/REPO.git

git push -u origin main

Or:

git remote set-url origin https://github.com/WhiteHatForHire/REPO.git

E) I want to create a repo from the current folder with GitHub CLI

gh repo create repo-name --public --source . --push

F) I want to download a repo from GitHub to my machine

git clone https://github.com/WhiteHatForHire/REPO.git

6. Useful branch workflow

Create a new branch

git checkout -b feature-name

Switch branches

git checkout main

Push a new branch

git push -u origin feature-name

For simple solo projects, staying on main is fine.

7. Handy fixes

“Author identity unknown”

git config --global user.name "WhiteHatForHire"

git config --global user.email "stephensm2011@gmail.com"

“gh is not recognized”

GitHub CLI is not installed or terminal needs reopening.

Check:

gh --version

“remote origin already exists”

You already added a remote.

Check:

git remote -v

Then either:

git remote remove origin

or:

git remote set-url origin https://github.com/WhiteHatForHire/REPO.git

“repository not found”

Usually means:

repo does not exist yet

wrong repo URL

wrong GitHub account

no access to that repo

Check auth:

gh auth status

Check remote:

git remote -v

“nothing to commit”

Git sees no changed files.

Check:

git status

“failed to push”

Usually means remote mismatch or branch mismatch.

Try:

git branch -M main

git push -u origin main

8. Best practices for Claude Code projects

Keep a README

echo "# Project Name" > README.md

git add README.md

git commit -m "Add README"

git push

Add a .gitignore

Basic example:

node_modules/

.env

.DS_Store

*.log

dist/

build/

Commit often

Good commit messages:

Add landing page layout

Fix navbar bug

Connect form submission

Clean up CSS

Bad commit messages:

stuff

update

asdf

9. My recommended minimal workflow

For most Claude Code sessions:

git status

git add .

git commit -m "Describe the work"

git push

For a brand new project:

cd path/to/project

git init

git add .

git commit -m "Initial commit"

gh repo create project-name --public --source . --push

10. Cheat sheet

First-time setup

git config --global user.name "WhiteHatForHire"

git config --global user.email "stephensm2011@gmail.com"

gh auth login

New project

git init

git add .

git commit -m "Initial commit"

gh repo create project-name --public --source . --push

Daily use

git add .

git commit -m "Update"

git push

Check things

git status

git remote -v

git branch

gh auth status

Fix remote

git remote remove origin

git remote add origin https://github.com/WhiteHatForHire/REPO.git

git push -u origin main

Clone one of your repos

git clone https://github.com/WhiteHatForHire/REPO.git

If you want, I can combine this and the Vite guide into one clean master setup doc.
