#!/bin/bash

# If there is a test database already present, delete it
if [[ -e test.db ]]; then
	rm test.db
fi

# Create new test database and populate it
echo -e "*** SETTING UP TEST DATABASE ***" 
python database_setup.py --test 
echo -e "\n*** POPULATING DATABASE ***"
python database_populator.py --test