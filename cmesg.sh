#!/bin/bash

# Create a hidden commits file; if it exists at script runtime, remove it
FILE1=.commits.txt

if [[ -e $FILE1 ]]; then
    rm $FILE1
fi

# Retrieve all commits (messages only; still need to work how authors get)
git log --pretty=format:"%s" > $FILE1

# Run commit message python script
python mesg_check.py
