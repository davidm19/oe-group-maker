#!/usr/bin/env python

import sys
import os
import re
from subprocess import check_output
from collections import defaultdict

# Open hidden commits file
with open('.commits.txt', 'r') as f:
    print("Checking commit messages...")
    content = f.read()
    lines = content.split("\n")
    is_blank_line = False

    # For each line, check the author; if it's not Mr. Devaughn-Brown,
    # check the commit message
    # if it doesn't start with the commit type, let the user know
    for line in lines:
        current_line = line.split("|")
        author = current_line[0]
        message = current_line[1]
        has_errors = False
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
                    # print(
                    #     "Success! Line '%s' starts with a valid commit type."
                    #     % message
                    #     )
                else:
                    has_errors = True
                    print(
                        "*** '%s' does not start with a commit type."
                        % message
                        )
                    sys.exit(1)

        if has_errors:
            print("*** Some commits don't follow the template. ***")
            sys.exit(1)
