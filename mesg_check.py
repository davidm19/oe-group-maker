#!/usr/bin/env python

import sys, os, re
from subprocess import check_output
from collections import defaultdict

commit_types = ["feat: ", "fix: ", "refactor: ", "style: ", "docs: ", "test: ", "chore: ", "Merge ", "Initial"] 

with open('a.txt', 'r') as f:
    print("Checking commit messages...")
    content = f.read()
    lines = content.split("\n")
    is_blank_line = False
    for line in lines:
        current_line = line
        # print("Checking line: %s" % current_line)
        if current_line is not "":
            if current_line.startswith("feat: ") or current_line.startswith("fix: ") or current_line.startswith("refactor: ") or current_line.startswith("style: ") or current_line.startswith("docs: ") or current_line.startswith("test: ") or current_line.startswith("chore: ") or current_line.startswith("Merge ") or current_line.startswith("Initial "):
                print("Current line: %s" % current_line)
                print("******************************* SUCCESS! *******************************")
                # sys.exit(0)
            else:
                print("'%s' does not start with a commit type." % current_line)
                # print("Line '%s' does not start with a commit type. Exiting..." % current_line)
                # sys.exit(1)

    # for i in range(len(lines)):
    #     print(len(lines))
    #     current_line = lines[i].strip()
    #     print("Checking line: %s" % current_line)
    #     if current_line is not "":
    #         for commit_type in commit_types:
    #             if current_line.startswith(commit_type):
    #                 print("Current line: %s" % current_line)
    #                 print("******************************* SUCCESS! *******************************")
    #                 # sys.exit(0)
    #             print("'%s' does not start with a commit type." % current_line)
    #                 # print("Line '%s' does not start with a commit type. Exiting..." % current_line)
    #                 # sys.exit(1)

        # if current_line.startswith("fix: ") or current_line.startswith("refactor: "):
        #     print("Line %s starts with fix/refactor" % current_line)
        #     if lines[i+1] is "":
        #         print("************************* IF YOU'RE READING THIS, THEN MY PROGRAM IS WORKING HERE AND IT IS CURRENTLY CHECKING %s" % current_line)
        #         is_blank_line = True
        #         if lines[i+2] is "" or lines[i+2].startswith("#"):
        #             print "You did not specify a description for your fix/refactor. Exiting..."
        #             sys.exit(1)
        #         elif lines[i+2] is not None:
        #             sys.exit(0)
