#!/bin/bash

# FOR TESTING ONLY! Make a test file holding all commits. If the test file is already present at execution, delete it
FILE=a.txt

if [[ -e $FILE ]]; then
    rm $FILE
fi

# Retrieve all commits and their authors
git log --pretty=format:"%an: %s" > $FILE

# Show file
less $FILE
