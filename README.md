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

# Group Assignment Explanation
- Key Requirements

Each student can provide a list of preferences
Each group should be gender balanced as close as possible
The algorithm should ensure that each student is matched into a group with at least one preference (if they provided the maximum number of preferences).  The fewer preferences a person provides the lower their chance to be matched into a group with a preference.  

- Algorithm Theory

Our algorithm will maximize the chance of a everyone being matched with at least one of their preference and possibly more.

The basic idea is that the best chance someone has to be matched into a group with one of their preferences is to “choose” which group to join, where the groups contain people who have preferred them the most (ie popular people).  Conversely, if groups are filled with people who are not highly preferred then the likelihood of joining a group with a preference is reduced.


For example, if Joan who has only one person who has her as a preference and she is pulled into a group early in the process, then she has to hope that one of her
preferences joins her group because that preference prefers someone else in her group.  She is hoping for a coincidence to occur.  Therefore, it is more ideal if she can choose a group towards the end of the process, when most other people are already assigned to almost ensure she will at least be matched with one preference.  

Conversely, for example, if John has many people who have he as a preference and John is assigned early in the process, then Johns creates more opportunities for people to join his group and match with a preference.

So in summary, the basic idea is to assign high preferred (popular) people to groups early in the process and assign lower preferred (less popular) people to
How the algorithm works
Calculate a preference score (pref-score)
The pref-score is the number of other students who have listed the student as a preference

- Calculate a mutual score (mutual-score)
The mutual-score is the number of preferences who have also listed the person as a preference.  For example, if Joan’s preferences include John, Sally, and Jennifer; and John and Jennifer also have Joan as a preference, then Joan’s mutual-score is 2.  The idea is to add people to the list early in the process to make room for others to choose their groups if possible.

- Sort the students by pref-score and mutual-score
Assigning students to groups in the order of pref-score and mutual-score will create more opportunities for lower pref-score students to choose their groups.

- Assign each student according to the algorithm theory
Students will be assigned to groups attempting to keep the groups balanced in size through the assignment process to maximize opportunities for students to choose their way into groups and therefore maximizing their chance for a preference match.

- Students who are pulled into groups will be selected based on highest pref-score while students who choose a group will choose the lowest group with a preference with the lowest pref-score.  

Here is a summary of the algorithm logic to when assigning each student to a group:

- If assigned to a group already						
 - Already Assigned With A Preference - If assigned to a group with a pref then do nothing and move to assign next student
 - Pull Highest Pref-score Preference Into Group - If any prefs not assigned, assign (pull) pref with highest pref-score to join the students assigned group if gender-limit permits 	
 - Cannot Be Matched - if all prefs assigned to other groups then this person does get a preference… add them to open groups at the end of the assignment process

- If not assigned to a group already					
  Find the least crowded group(s) (from left to right)			
  - Join Smallest Group With A Preference - If there is a preference in the smallest group, assign the person to this group, if gender-limit permits
  - Join Smallest Group With Lowest Pref-Score Preference - If there are multiple smallest groups, then assign to the group with a pref with the lowest pref-score, if gender-limit permits
  - Join Smallest Group along with Highest Pref-score Preference - if there is no preference in the smallest group(s) then assign the person to the smallest group, and pull into the group the preference with the highest pref-score (who is not yet assigned) and has a preferences-remaining > 1, if gender-limit permits
  - Join Smallest Group With Lowest Pref-Score Preference - otherwise, if the pref's preferences-remaining <=1 then assign the person to next smallest group which contains the lowest pref-score), if gender-limit permits
  - Join Smallest Group With Lowest Pref-Score Preference - But if all preferences are assigned (ie there aren't any to pull along) then choose the smallest group with a preference; and if there are multiple smallest groups choose the group with a pref with the lowest pref-score, if gender-limit permits
