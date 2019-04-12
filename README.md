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
1. In `improved_algorithm_interface.py`
  - Change how many `MAX_PREFS` each person should have (must be exact) on line 24
  - Change how many `NUM_OF_GROUPS` should try to be primary_student on line 25
  * note that if too many groups are made extraneous groups will be left empty
3. run `improved_algorithm_interface.py`
- If nothing is changed expected output is below
<details>
  <summary>Example Output</summary>
  Max Boys Per Group: 8.0
  Max Girls Per Group: 10.0
  Number of Groups:4

  Group 1: 7 Boys, 11 Girls Total: 18
  JoeC
  AmitA
  LucasS
  MatanL
  RafealaL
  BenedictT
  PadminiC
  SerenaM
  LorenaT
  KaterinaA
  DoruV
  LexiL
  DritaH
  PeterO
  AlexaD
  CorinnaV
  SamuelB
  LindseyG

  Group 2: 11 Boys, 7 Girls Total: 18
  SundarR
  JackR
  AlexanderC
  EugeneC
  AnarS
  ErwinP
  AseemO
  CharlesD
  BeatriseS
  LouiseD
  SamanthaA
  LilyK
  IsabelleC
  KenyaR
  AnitaO
  IreneS
  DarnellM
  FabioP

  Group 3: 8 Boys, 9 Girls Total: 17
  AlvinG
  AmosS
  JasmineE
  ShirleyN
  RonA
  KlemensH
  MikaelaM
  PatrickG
  SolomonP
  SusieD
  DanielD
  RosaE
  BiankaW
  AbelF
  MacG
  RoxanneA
  AriellaA

  Group 4: 5 Boys, 12 Girls Total: 17
  PaulaD
  ZenaK
  RanjitF
  WinonaB
  LucieM
  RachelS
  OlympiaL
  LeaS
  EstherJ
  MonicaM
  SilviaG
  OlegA
  AntonM
  AbrahamM
  KateF
  MartinM
  MiraA
  0 students are unable to be assigned

  0 matches = 0
  1 matches = 18
  2 matches = 33
  3 matches = 9

  The average group size is 17
  There are 0 empty groups
</details>

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

# Database Object Definitions
- `Student`
  - `id` an auto generated id number
  - `first_name` the student's first name
  - `last_name` the student's last name
  - `gender` the student's gender
  - `name` an automatic concatenation of `first_name` and `last_name`
- `Preference`
  - `id` an auto generated id number
  - `first_name1` the preference's first name
  - `last_name1` the preference's last name
  - `gender` the preference's gender
  - `name` an automatic concatenation of `first_name` and `last_name`
  - `student_id` the `id` of the `Student` who has this person as a `Preference`
  - `student` the `Student` who has this person as a `Preference`
