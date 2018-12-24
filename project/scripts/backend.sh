if [[ -e test.db ]]; then
	rm test.db
fi

echo -e "*** SETTING UP TEST DATABASE ***" 
python database_setup.py --test 
echo -e "\n*** POPULATING DATABASE ***"
python database_populator.py --test
echo -e "\n*** RUNNING SERVER ***"
python application.py
