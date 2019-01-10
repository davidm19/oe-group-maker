#!/bin/bash

echo -e "*** SETTING UP TEST DATABASE ***" 
python database_setup.py --test 
echo -e "\n*** POPULATING DATABASE ***"
python database_populator.py --test
echo -e "\n*** TESTING PROGRAMS ***"
python test_app.py
echo -e "\n*** DELETING DATABASE ***"
rm test.db
echo -e "\n*** TESTING COMPLETED ***"
