#!/bin/bash

read -r -d '' DOCUMENTATION << EOF
Script for running Python database tests

Usage:
    $CMD test = set up a test database, populate it, test it out, and delete it
	 

Environment Variables:
    PASS
EOF

# SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

function test {
	echo -e "*** SETTING UP TEST DATABASE ***\n" 
	python database_setup.py --test 
	# (RIGHT NOW REAL DATABASE POPULATION CAN'T FUNCTION WHILE A TEST DATABASE IS CREATED)
	echo -e "*** POPULATING DATABASE ***\n"
	python database_populator.py --test
	echo -e "*** TESTING PROGRAMS ***\n"
	python test_app.py
	echo -e "*** DELETING DATABASE ***\n"
	rm test.db
	echo -e "\nTesting completed."
}

ACTION=$1
function main {
	case $ACTION in
		test) test;;
		*) echo "Invalid argument"
			exit 1
	esac
}

main
