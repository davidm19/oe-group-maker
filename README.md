# About
Outdoor Education Group Maker
A project for Chadwick Outdoor Education offices by students from Post-AP Computer Science: Intro to Software Engineering
A generic group maker and group checker
Project intended to help Chadwick's Outdoor Ed offices have an easier time making groups for Outdoor Ed trips

Created by Ryan Hom

# Requirements
- Virtual Box
- Ubuntu Vagrant
- Unix based Command Line Utility

# Setup
- If no Vagrant file exists, put the Ubuntu Vagrant file in the root project director (If one already exists skip this step)
- Open your Command Line Utility
1. Navigate to the root project file (has the Vagrant file) type `vagrant up`
2. Type 'vagrant ssh'
3. Navigate inside the project directory `cd /vagrant/project/`
4. If there is a already a `database.db` delete it
5. Run `database_setup.py`

# Configure Database (Optional if integrating into another program)
1. Modify `database_populator.py` by filling all fields appropriately
  - All `Student` have a `first_name`, `last_name` and `gender`.
    - If no last name leave it blank.
    - Gender is either `M` or `F`
      - Genders aren't required but recommended either have gender for all or no gender.
3. Those who have no preference leave preferences blank.
4. Only have as many `Students` as you actually have
5. Run `database_populator.py`

# Run Example
1. Change how many `prefs` each person should have (must be exact)
2. Change how many `groups` should try to be primary_student
  * note that if too many groups are made extraneous groups will be left empty
3. run `improved_algorithm_interface.py`

# Integration
- Can run off of an existing database
- Recommend that `prefs` and `groups` are set by an outside UI
- Methods from `improved_algorithm_interface.py` need to be used in the order of the example

# Check Existing Trip
1. Trips should be in this format
  - A `Trip` is a `List` of `Group`
  - A `Group` is a `List` of `Student_class`
2. From `improved_algorithm_interface.py` Run
  1. `unassigned_students(YOUR_TRIP)`
  2. `print_stats(YOUR_TRIP)`
