#!/usr/bin/env python

import sys, os, re
from subprocess import check_output
from collections import defaultdict

# Define commit types (keyword placed at beginning of commit message)
commit_types = ["feat: ", "fix: ", "refactor: ", "style: ", "docs: ", "test: ", "chore: ", "Merge ", "Initial"] 

# Open hidden commits file
with open('.commits.txt', 'r') as f:
    print("Checking commit messages...")
    content = f.read()
    lines = content.split("\n")
    is_blank_line = False

    # For each line, check if it starts with the commit type; if not, let the user know
    for line in lines:
        current_line = line
        if current_line is not "":
            if current_line.startswith("feat: ") or current_line.startswith("fix: ") or current_line.startswith("refactor: ") or current_line.startswith("style: ") or current_line.startswith("docs: ") or current_line.startswith("test: ") or current_line.startswith("chore: ") or current_line.startswith("Merge ") or current_line.startswith("Initial "):
                print("Success! Line '%s' starts with a valid commit type." % current_line)
            else:
                print("'%s' is invalid as it does not start with a commit type." % current_line)
