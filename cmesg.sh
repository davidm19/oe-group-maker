#!/bin/bash

# ========================================================================
# FOR TESTING ONLY! Make a test file holding all commits. If the test file is already present at execution, delete it
FILE1=a.txt
FILE2=b.txt

if [[ -e $FILE1 ]]; then
    rm $FILE1
fi
# ========================================================================

# Retrieve all commits and their authors
# git log --pretty=format:"%an: %s" > $FILE1
git log --pretty=format:"%s" > $FILE1
# git log --pretty=format:"%s" | head -n 1 > $FILE1

# INPUT FILE1 TO COMMIT MSG. SCRIPT (USE THE WITH OPEN AS (VAR) THINGY) AND EXPORT THAT TO FILE2 (b.txt)
python mesg_check.py

# FOR TESTING ONLY! Show file
# less $FILE1
