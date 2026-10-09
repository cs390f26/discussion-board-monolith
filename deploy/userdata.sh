#!/bin/bash

REPO_URL="https://github.com/YOUR_GITHUB_USERNAME/discussion-board-monolith.git"

sudo yum install -y python3.12 git

git clone $REPO_URL

cd discussion-board-monolith

python3 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r requirements.txt
.venv/bin/pip install -e .

cp deploy/discussion.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable --now discussion.service