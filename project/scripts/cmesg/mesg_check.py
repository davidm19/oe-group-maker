#!/usr/bin/env python

import sys
import os
import re
import time
from subprocess import check_output
from collections import defaultdict

# Open hidden commits file
with open('.commits.txt', 'r') as f:
    print("Checking commit messages...")
    start = time.clock()
    content = f.read()
    lines = content.split("\n")
    is_blank_line = False

    # For each line, check the author; if it's not Mr. Devaughn-Brown,
    # check the commit message
    # if it doesn't start with the commit type, let the user know
    bad_commit_count = 0
    has_errors = False
    for line in lines:
        current_line = line.split("|")
        author = current_line[0]
        message = current_line[1]
        if current_line != "":
            if author != "J.D. DeVaughn-Brown":
                if (message.startswith("feat: ")
                    or message.startswith("fix: ")
                    or message.startswith("refactor: ")
                    or message.startswith("style: ")
                    or message.startswith("docs: ")
                    or message.startswith("test: ")
                    or message.startswith("chore: ")
                    or message.startswith("Merge ")
                        or message.startswith("Initial ")
                        or message.startswith("Associate ")):
                    pass
                else:
                    print("Bad commit: %s" % message)
                    has_errors = True
                    bad_commit_count += 1

    if has_errors:
        end = time.clock() - start
        print("*** Some commits don't follow the template. ***")
        print("Number of bad commits: %d" % bad_commit_count)
        print("Process took {} seconds".format(end))
        sys.exit(1)
