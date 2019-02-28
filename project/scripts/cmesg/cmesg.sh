#!/bin/bash

# Create a hidden commits file; if the file still exists at script runtime, remove it
FILE1=.commits.txt

if [[ -e $FILE1 ]]; then
    rm $FILE1
fi

# Retrieve all commits and export them to the hidden file
# git log --pretty=format:"%s" > $FILE1
git log --pretty=format:"%an|%s" > $FILE1

# Run the commit message python script
python mesg_check.py
