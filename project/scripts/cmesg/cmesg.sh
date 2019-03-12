#!/bin/bash

# Create a hidden commits file for the python script to collect commits
FILE1=.commits.txt

# If hidden commits file still exists, then remove it
if [[ -e $FILE1 ]]; then
    rm $FILE1
fi

# Retrieve all commits and export them to the hidden file
git log --pretty=format:"%an|%s" > $FILE1

# Run the commit message python script
python project/scripts/cmesg/mesg_check.py
