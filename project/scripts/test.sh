#!/bin/bash

read -r -d '' DOCUMENTATION << EOF
Script for running Python database tests

Usage:
    $CMD test = set up a test database, populate it, test it out, and delete it
	 

Environment Variables:
    PASS
EOF

# SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

echo -e "*** SETTING UP TEST DATABASE ***" 
python database_setup.py --test 
echo -e "\n*** POPULATING DATABASE ***"
python database_populator.py --test
echo -e "\n*** TESTING PROGRAMS ***"
python test_app.py
echo -e "\n*** DELETING DATABASE ***"
rm test.db
echo -e "\n*** TESTING COMPLETED ***"
