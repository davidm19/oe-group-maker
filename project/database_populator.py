from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Student, engine, Preference

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

student1 = Student(first_name = "Samantha", last_name = "A", gender = "F")
session.add(student1)
session.commit()

student2 = Student(first_name = "Alexander", last_name = "C", gender = "M")
session.add(student2)
session.commit()

student3 = Student(first_name = "Kate", last_name = "F", gender = "F")
session.add(student3)
session.commit()

student4 = Student(first_name = "Samuel", last_name = "B", gender = "M")
session.add(student4)
session.commit()

student5 = Student(first_name = "Jack", last_name = "R", gender = "M")
session.add(student5)
session.commit()

student6 = Student(first_name = "Lexi", last_name = "L", gender = "F")
session.add(student6)
session.commit()

student7 = Student(first_name = "Joe", last_name = "C", gender = "M")
session.add(student7)
session.commit()

student8 = Student(first_name = "Ron", last_name = "A", gender = "M")
session.add(student8)
session.commit()

student9 = Student(first_name = "Peter", last_name = "O", gender = "M")
session.add(student9)
session.commit()

student10 = Student(first_name = "Charles", last_name = "D", gender = "M")
session.add(student10)
session.commit()

student11 = Student(first_name = "Esther", last_name = "J", gender = "F")
session.add(student11)
session.commit()

student12 = Student(first_name = "Silvia", last_name = "G", gender = "F")
session.add(student12)
session.commit()

student13 = Student(first_name = "Jasmine", last_name = "E", gender = "F")
session.add(student13)
session.commit()

student14 = Student(first_name = "Zena", last_name = "K", gender = "F")
session.add(student14)
session.commit()

student15 = Student(first_name = "Alexa", last_name = "D", gender = "F")
session.add(student15)
session.commit()

student16 = Student(first_name = "Lea", last_name = "S", gender = "F")
session.add(student16)
session.commit()

student17 = Student(first_name = "Martin", last_name = "M", gender = "M")
session.add(student17)
session.commit()

student18 = Student(first_name = "Katerina", last_name = "A", gender = "F")
session.add(student18)
session.commit()

student19 = Student(first_name = "Monica", last_name = "M", gender = "F")
session.add(student19)
session.commit()

student20 = Student(first_name = "Lucas", last_name = "S", gender = "M")
session.add(student20)
session.commit()

student21 = Student(first_name = "Eugene", last_name = "C", gender = "M")
session.add(student21)
session.commit()

student22 = Student(first_name = "Corinna", last_name = "V", gender = "F")
session.add(student22)
session.commit()

student23 = Student(first_name = "Sundar", last_name = "R", gender = "M")
session.add(student23)
session.commit()

student24 = Student(first_name = "Patrick", last_name = "G", gender = "M")
session.add(student24)
session.commit()

student25 = Student(first_name = "Serena", last_name = "M", gender = "F")
session.add(student25)
session.commit()

student26 = Student(first_name = "Isabelle", last_name = "C", gender = "F")
session.add(student26)
session.commit()

student27 = Student(first_name = "Abel", last_name = "F", gender = "F")
session.add(student27)
session.commit()

student28 = Student(first_name = "Beatrise", last_name = "S", gender = "F")
session.add(student28)
session.commit()

student29 = Student(first_name = "Oleg", last_name = "A", gender = "M")
session.add(student29)
session.commit()

student30 = Student(first_name = "Anita", last_name = "O", gender = "F")
session.add(student30)
session.commit()

student31 = Student(first_name = "Alvin", last_name = "G", gender = "M")
session.add(student31)
session.commit()

student32 = Student(first_name = "Paula", last_name = "D", gender = "F")
session.add(student32)
session.commit()

student33 = Student(first_name = "Kenya", last_name = "R", gender = "M")
session.add(student33)
session.commit()

student34 = Student(first_name = "Lorena", last_name = "T", gender = "F")
session.add(student34)
session.commit()

student35 = Student(first_name = "Daniel", last_name = "D", gender = "M")
session.add(student35)
session.commit()

student36 = Student(first_name = "Padmini", last_name = "C", gender = "F")
session.add(student36)
session.commit()

student37 = Student(first_name = "Louise", last_name = "D", gender = "F")
session.add(student37)
session.commit()

student38 = Student(first_name = "Mac", last_name = "G", gender = "M")
session.add(student38)
session.commit()

student39 = Student(first_name = "Lucie", last_name = "M", gender = "F")
session.add(student39)
session.commit()

student40 = Student(first_name = "Solomon", last_name = "P", gender = "M")
session.add(student40)
session.commit()

student41 = Student(first_name = "Erwin", last_name = "P", gender = "M")
session.add(student41)
session.commit()

student42 = Student(first_name = "Winona", last_name = "B", gender = "F")
session.add(student42)
session.commit()

student43 = Student(first_name = "Rosa", last_name = "E", gender = "F")
session.add(student43)
session.commit()

student44 = Student(first_name = "Lily", last_name = "K", gender = "F")
session.add(student44)
session.commit()

student45 = Student(first_name = "Rachel", last_name = "S", gender = "F")
session.add(student45)
session.commit()

student46 = Student(first_name = "Doru", last_name = "V", gender = "F")
session.add(student46)
session.commit()

student47 = Student(first_name = "Susie", last_name = "D", gender = "F")
session.add(student47)
session.commit()

student48 = Student(first_name = "Anton", last_name = "M", gender = "M")
session.add(student48)
session.commit()

student49 = Student(first_name = "Amit", last_name = "A", gender = "M")
session.add(student49)
session.commit()

student50 = Student(first_name = "Aseem", last_name = "O", gender = "M")
session.add(student50)
session.commit()

student51 = Student(first_name = "Klemens", last_name = "H", gender = "M")
session.add(student51)
session.commit()

student52 = Student(first_name = "Drita", last_name = "H", gender = "F")
session.add(student52)
session.commit()

student53 = Student(first_name = "Lindsey", last_name = "G", gender = "F")
session.add(student53)
session.commit()

student54 = Student(first_name = "Bianka", last_name = "W", gender = "F")
session.add(student54)
session.commit()

student55 = Student(first_name = "Shirley", last_name = "N", gender = "F")
session.add(student55)
session.commit()

student56 = Student(first_name = "Olympia", last_name = "L", gender = "F")
session.add(student56)
session.commit()

student57 = Student(first_name = "Ranjit", last_name = "F", gender = "M")
session.add(student57)
session.commit()

student58 = Student(first_name = "Mikaela", last_name = "M", gender = "F")
session.add(student58)
session.commit()

student59 = Student(first_name = "Rafeala", last_name = "L", gender = "F")
session.add(student59)
session.commit()

student60 = Student(first_name = "Amos", last_name = "S", gender = "M")
session.add(student60)
session.commit()

student61 = Student(first_name = "Abraham", last_name = "M", gender = "M")
session.add(student61)
session.commit()

student62 = Student(first_name = "Matan", last_name = "L", gender = "M")
session.add(student62)
session.commit()

student63 = Student(first_name = "Anar", last_name = "S", gender = "M")
session.add(student63)
session.commit()

student64 = Student(first_name = "Darnell", last_name = "M", gender = "M")
session.add(student64)
session.commit()

student65 = Student(first_name = "Ariella", last_name = "A", gender = "F")
session.add(student65)
session.commit()

student66 = Student(first_name = "Irene", last_name = "S", gender = "F")
session.add(student66)
session.commit()

student67 = Student(first_name = "Mira", last_name = "A", gender = "F")
session.add(student67)
session.commit()

student68 = Student(first_name = "Fabio", last_name = "P", gender = "M")
session.add(student68)
session.commit()

student69 = Student(first_name = "Roxanne", last_name = "A", gender = "F")
session.add(student69)
session.commit()

student70 = Student(first_name = "Benedict", last_name = "T", gender = "M")
session.add(student70)
session.commit()

stud_1_pref_1 = Preference(first_name1 = "Lily", last_name1 = "K", student_id = 1, gender = "F", student = student1, preference_id = 44)
stud_1_pref_2 = Preference(first_name1 = "Joe", last_name1 = "C", student_id = 1, gender = "M", student = student1, preference_id = 7)
stud_1_pref_3 = Preference(first_name1 = "Irene", last_name1 = "S", student_id = 1, gender = "F", student = student1, preference_id = 66)

session.add(stud_1_pref_1)
session.add(stud_1_pref_2)
session.add(stud_1_pref_3)

stud_2_pref_1 = Preference(first_name1 = "Jack", last_name1 = "R", student_id = 2, gender = "M", student = student2, preference_id = 5)
stud_2_pref_2 = Preference(first_name1 = "Sundar", last_name1 = "R", student_id = 2, gender = "M", student = student2, preference_id = 23)
stud_2_pref_3 = Preference(first_name1 = "Eugene", last_name1 = "C", student_id = 2, gender = "M", student = student2, preference_id = 21)
session.add(stud_2_pref_1)
session.add(stud_2_pref_2)
session.add(stud_2_pref_3)

stud_3_pref_1 = Preference(first_name1 = "Winona", last_name1 = "B", student_id = 3, gender = "F", student = student3, preference_id = 42)
stud_3_pref_2 = Preference(first_name1 = "Olympia", last_name1 = "L", student_id = 3, gender = "F", student = student3, preference_id = 56)
stud_3_pref_3 = Preference(first_name1 = "Samuel", last_name1 = "B", student_id = 3, gender = "M", student = student3, preference_id = 4)
session.add(stud_3_pref_1)
session.add(stud_3_pref_2)
session.add(stud_3_pref_3)

stud_4_pref_1 = Preference(first_name1 = "", last_name1 = "", student_id = 4, gender = "", student = student4)
stud_4_pref_2 = Preference(first_name1 = "", last_name1 = "", student_id = 4, gender = "", student = student4)
stud_4_pref_3 = Preference(first_name1 = "", last_name1 = "", student_id = 4, gender = "", student = student4)

session.add(stud_4_pref_1)
session.add(stud_4_pref_2)
session.add(stud_4_pref_3)

stud_5_pref_1 = Preference(first_name1 = "Sundar", last_name1 = "R", student_id = 5, gender = "M", student = student5, preference_id = 23)
stud_5_pref_2 = Preference(first_name1 = "Alexander", last_name1 = "C", student_id = 5, gender = "M", student = student5, preference_id = 2)
stud_5_pref_3 = Preference(first_name1 = "Ranjit", last_name1 = "F", student_id = 5, gender = "M", student = student5, preference_id = 57)

session.add(stud_5_pref_1)
session.add(stud_5_pref_2)
session.add(stud_5_pref_3)

stud_6_pref_1 = Preference(first_name1 = "Anita", last_name1 = "O", student_id = 6, gender = "F", student = student6, preference_id = 30)
stud_6_pref_2 = Preference(first_name1 = "Samuel", last_name1 = "B", student_id = 6, gender = "M", student = student6, preference_id = 4)
stud_6_pref_3 = Preference(first_name1 = "Lorena", last_name1 = "T", student_id = 6, gender = "F", student = student6, preference_id = 34)

session.add(stud_6_pref_1)
session.add(stud_6_pref_2)
session.add(stud_6_pref_3)

stud_7_pref_1 = Preference(first_name1 = "Amit", last_name1 = "A", student_id = 7, gender = "M", student = student7, preference_id = 49)
stud_7_pref_2 = Preference(first_name1 = "Patrick", last_name1 = "G", student_id = 7, gender = "M", student = student7, preference_id = 24)
stud_7_pref_3 = Preference(first_name1 = "Alvin", last_name1 = "G", student_id = 7, gender = "M", student = student7, preference_id = 31)

session.add(stud_7_pref_1)
session.add(stud_7_pref_2)
session.add(stud_7_pref_3)

stud_8_pref_1 = Preference(first_name1 = "Darnell", last_name1 = "M", student_id = 8, gender = "M", student = student8, preference_id = 64)
stud_8_pref_2 = Preference(first_name1 = "Daniel", last_name1 = "D", student_id = 8, gender = "M", student = student8, preference_id = 35)
stud_8_pref_3 = Preference(first_name1 = "Klemens", last_name1 = "H", student_id = 8, gender = "M", student = student8, preference_id = 51)

session.add(stud_8_pref_1)
session.add(stud_8_pref_2)
session.add(stud_8_pref_3)

stud_9_pref_1 = Preference(first_name1 = "Darnell", last_name1 = "M", student_id = 9, gender = "M", student = student9, preference_id = 64)
stud_9_pref_2 = Preference(first_name1 = "Ranjit", last_name1 = "F", student_id = 9, gender = "M", student = student9, preference_id = 57)
stud_9_pref_3 = Preference(first_name1 = "Lucas", last_name1 = "S", student_id = 9, gender = "M", student = student9, preference_id = 20)

session.add(stud_9_pref_1)
session.add(stud_9_pref_2)
session.add(stud_9_pref_3)

stud_10_pref_1 = Preference(first_name1 = "Anar", last_name1 = "S", student_id = 10, gender = "M", student = student10, preference_id = 63)
stud_10_pref_2 = Preference(first_name1 = "Shirley", last_name1 = "N", student_id = 10, gender = "F", student = student10, preference_id = 55)
stud_10_pref_3 = Preference(first_name1 = "Erwin", last_name1 = "P", student_id = 10, gender = "M", student = student10, preference_id = 41)

session.add(stud_10_pref_1)
session.add(stud_10_pref_2)
session.add(stud_10_pref_3)

stud_11_pref_1 = Preference(first_name1 = "Lea", last_name1 = "S", student_id = 11, gender = "F", student = student11, preference_id = 16)
stud_11_pref_2 = Preference(first_name1 = "Monica", last_name1 = "M", student_id = 11, gender = "F", student = student11, preference_id = 19)
stud_11_pref_3 = Preference(first_name1 = "Joe", last_name1 = "C", student_id = 11, gender = "M", student = student11, preference_id = 7)

session.add(stud_11_pref_1)
session.add(stud_11_pref_2)
session.add(stud_11_pref_3)

stud_12_pref_1 = Preference(first_name1 = "Lea", last_name1 = "S", student_id = 12, gender = "F", student = student12, preference_id = 16)
stud_12_pref_2 = Preference(first_name1 = "Monica", last_name1 = "M", student_id = 12, gender = "F", student = student12, preference_id = 19)
stud_12_pref_3 = Preference(first_name1 = "Padmini", last_name1 = "C", student_id = 12, gender = "F", student = student12, preference_id = 36)

session.add(stud_12_pref_1)
session.add(stud_12_pref_2)
session.add(stud_12_pref_3)

stud_13_pref_1 = Preference(first_name1 = "Anar", last_name1 = "S", student_id = 13, gender = "M", student = student13, preference_id = 63)
stud_13_pref_2 = Preference(first_name1 = "Amit", last_name1 = "A", student_id = 13, gender = "M", student = student13, preference_id = 49)
stud_13_pref_3 = Preference(first_name1 = "Shirley", last_name1 = "N", student_id = 13, gender = "F", student = student13, preference_id = 55)

session.add(stud_13_pref_1)
session.add(stud_13_pref_2)
session.add(stud_13_pref_3)

stud_14_pref_1 = Preference(first_name1 = "Paula", last_name1 = "D", student_id = 14, gender = "F", student = student14, preference_id = 32)
stud_14_pref_2 = Preference(first_name1 = "Rachel", last_name1 = "S", student_id = 14, gender = "F", student = student14, preference_id = 45)
stud_14_pref_3 = Preference(first_name1 = "Ranjit", last_name1 = "F", student_id = 14, gender = "M", student = student14, preference_id = 57)

session.add(stud_14_pref_1)
session.add(stud_14_pref_2)
session.add(stud_14_pref_3)

stud_15_pref_1 = Preference(first_name1 = "Anita", last_name1 = "O", student_id = 15, gender = "F", student = student15, preference_id = 30)
stud_15_pref_2 = Preference(first_name1 = "Lorena", last_name1 = "T", student_id = 15, gender = "F", student = student15, preference_id = 34)
stud_15_pref_3 = Preference(first_name1 = "Drita", last_name1 = "H", student_id = 15, gender = "F", student = student15, preference_id = 53)

session.add(stud_15_pref_1)
session.add(stud_15_pref_2)
session.add(stud_15_pref_3)

stud_16_pref_1 = Preference(first_name1 = "Esther", last_name1 = "J", student_id = 16, gender = "F", student = student16, preference_id = 11)
stud_16_pref_2 = Preference(first_name1 = "Jasmine", last_name1 = "E", student_id = 16, gender = "F", student = student16, preference_id = 13)
stud_16_pref_3 = Preference(first_name1 = "Joe", last_name1 = "C", student_id = 16, gender = "M", student = student16, preference_id = 7)

session.add(stud_16_pref_1)
session.add(stud_16_pref_2)
session.add(stud_16_pref_3)

stud_17_pref_1 = Preference(first_name1 = "Samuel", last_name1 = "B", student_id = 17, gender = "M", student = student17, preference_id = 4)
stud_17_pref_2 = Preference(first_name1 = "Paula", last_name1 = "D", student_id = 17, gender = "F", student = student17, preference_id = 32)
stud_17_pref_3 = Preference(first_name1 = "Anita", last_name1 = "O", student_id = 17, gender = "F", student = student17, preference_id = 30)

session.add(stud_17_pref_1)
session.add(stud_17_pref_2)
session.add(stud_17_pref_3)

stud_18_pref_1 = Preference(first_name1 = "Rafeala", last_name1 = "L", student_id = 18, gender = "F", student = student18, preference_id = 59)
stud_18_pref_2 = Preference(first_name1 = "Amit", last_name1 = "A", student_id = 18, gender = "M", student = student18, preference_id = 49)
stud_18_pref_3 = Preference(first_name1 = "Joe", last_name1 = "C", student_id = 18, gender = "M", student = student18, preference_id = 7)

session.add(stud_18_pref_1)
session.add(stud_18_pref_2)
session.add(stud_18_pref_3)

stud_19_pref_1 = Preference(first_name1 = "Padmini", last_name1 = "C", student_id = 19, gender = "F", student = student19, preference_id = 36)
stud_19_pref_2 = Preference(first_name1 = "Irene", last_name1 = "S", student_id = 19, gender = "F", student = student19, preference_id = 66)
stud_19_pref_3 = Preference(first_name1 = "Rachel", last_name1 = "S", student_id = 19, gender = "F", student = student19, preference_id = 45)

session.add(stud_19_pref_1)
session.add(stud_19_pref_2)
session.add(stud_19_pref_3)

stud_20_pref_1 = Preference(first_name1 = "Benedict", last_name1 = "T", student_id = 20, gender = "M", student = student20, preference_id = 70)
stud_20_pref_2 = Preference(first_name1 = "Matan", last_name1 = "L", student_id = 20, gender = "M", student = student20, preference_id = 62)
stud_20_pref_3 = Preference(first_name1 = "Eugene", last_name1 = "C", student_id = 20, gender = "M", student = student20, preference_id = 21)

session.add(stud_20_pref_1)
session.add(stud_20_pref_2)
session.add(stud_20_pref_3)

stud_21_pref_1 = Preference(first_name1 = "Alexander", last_name1 = "C", student_id = 22, gender = "M", student = student21, preference_id = 2)
stud_21_pref_2 = Preference(first_name1 = "Sundar", last_name1 = "R", student_id = 22, gender = "M", student = student21, preference_id = 23)
stud_21_pref_3 = Preference(first_name1 = "Jack", last_name1 = "R", student_id = 21, gender = "M", student = student21, preference_id = 5)

session.add(stud_21_pref_1)
session.add(stud_21_pref_2)
session.add(stud_21_pref_3)

stud_22_pref_1 = Preference(first_name1 = "", last_name1 = "", student_id = 22, gender = "", student = student22)
stud_22_pref_2 = Preference(first_name1 = "", last_name1 = "", student_id = 22, gender = "", student = student22)
stud_22_pref_3 = Preference(first_name1 = "", last_name1 = "", student_id = 22, gender = "", student = student22)

session.add(stud_22_pref_1)
session.add(stud_22_pref_2)
session.add(stud_22_pref_3)

stud_23_pref_1 = Preference(first_name1 = "Alexander", last_name1 = "C", student_id = 23, gender = "M", student = student23, preference_id = 2)
stud_23_pref_2 = Preference(first_name1 = "Jack", last_name1 = "R", student_id = 23, gender = "M", student = student23, preference_id = 5)
stud_23_pref_3 = Preference(first_name1 = "Eugene", last_name1 = "C", student_id = 23, gender = "M", student = student23, preference_id = 21)

session.add(stud_23_pref_1)
session.add(stud_23_pref_2)
session.add(stud_23_pref_3)

stud_24_pref_1 = Preference(first_name1 = "Amit", last_name1 = "A", student_id = 24, gender = "M", student = student24, preference_id = 49)
stud_24_pref_2 = Preference(first_name1 = "Joe", last_name1 = "C", student_id = 24, gender = "M", student = student24, preference_id = 7)
stud_24_pref_3 = Preference(first_name1 = "Alvin", last_name1 = "G", student_id = 24, gender = "M", student = student24, preference_id = 31)

session.add(stud_24_pref_1)
session.add(stud_24_pref_2)
session.add(stud_24_pref_3)

stud_25_pref_1 = Preference(first_name1 = "Mikaela", last_name1 = "M", student_id = 25, gender = "F", student = student25, preference_id = 58)
stud_25_pref_2 = Preference(first_name1 = "Padmini", last_name1 = "C", student_id = 25, gender = "F", student = student25, preference_id = 36)
stud_25_pref_3 = Preference(first_name1 = "Joe", last_name1 = "C", student_id = 25, gender = "M", student = student25, preference_id = 7)

session.add(stud_25_pref_1)
session.add(stud_25_pref_2)
session.add(stud_25_pref_3)

stud_26_pref_1 = Preference(first_name1 = "Irene", last_name1 = "S", student_id = 26, gender = "F", student = student26, preference_id = 66)
stud_26_pref_2 = Preference(first_name1 = "Beatrise", last_name1 = "S", student_id = 26, gender = "F", student = student26, preference_id = 28)
stud_26_pref_3 = Preference(first_name1 = "Anita", last_name1 = "O", student_id = 26, gender = "F", student = student26, preference_id = 30)

session.add(stud_26_pref_1)
session.add(stud_26_pref_2)
session.add(stud_26_pref_3)

stud_27_pref_1 = Preference(first_name1 = "Sundar", last_name1 = "R", student_id = 27, gender = "M", student = student27, preference_id = 23)
stud_27_pref_2 = Preference(first_name1 = "Klemens", last_name1 = "H", student_id = 27, gender = "M", student = student27, preference_id = 51)
stud_27_pref_3 = Preference(first_name1 = "Joe", last_name1 = "C", student_id = 27, gender = "M", student = student27, preference_id = 7)

session.add(stud_27_pref_1)
session.add(stud_27_pref_2)
session.add(stud_27_pref_3)

stud_28_pref_1 = Preference(first_name1 = "Louise", last_name1 = "D", student_id = 28, gender = "F", student = student28, preference_id = 37)
stud_28_pref_2 = Preference(first_name1 = "Corinna", last_name1 = "V", student_id = 28, gender = "F", student = student28, preference_id = 22)
stud_28_pref_3 = Preference(first_name1 = "Bianka", last_name1 = "W", student_id = 28, gender = "F", student = student28, preference_id = 54)

session.add(stud_28_pref_1)
session.add(stud_28_pref_2)
session.add(stud_28_pref_3)

stud_29_pref_1 = Preference(first_name1 = "Paula", last_name1 = "D", student_id = 29, gender = "F", student = student29, preference_id = 32)
stud_29_pref_2 = Preference(first_name1 = "Zena", last_name1 = "K", student_id = 29, gender = "F", student = student29, preference_id = 14)
stud_29_pref_3 = Preference(first_name1 = "Aseem", last_name1 = "O", student_id = 29, gender = "M", student = student29, preference_id = 50)

session.add(stud_29_pref_1)
session.add(stud_29_pref_2)
session.add(stud_29_pref_3)

stud_30_pref_1 = Preference(first_name1 = "", last_name1 = "", student_id = 30, gender = "", student = student30)
stud_30_pref_2 = Preference(first_name1 = "", last_name1 = "", student_id = 30, gender = "", student = student30)
stud_30_pref_3 = Preference(first_name1 = "", last_name1 = "", student_id = 30, gender = "", student = student30)

session.add(stud_30_pref_1)
session.add(stud_30_pref_2)
session.add(stud_30_pref_3)

stud_31_pref_1 = Preference(first_name1 = "Amos", last_name1 = "S", student_id = 31, gender = "M", student = student31, preference_id = 60)
stud_31_pref_2 = Preference(first_name1 = "Solomon", last_name1 = "P", student_id = 31, gender = "M", student = student31, preference_id = 40)
stud_31_pref_3 = Preference(first_name1 = "Joe", last_name1 = "C", student_id = 31, gender = "M", student = student31, preference_id = 7)

session.add(stud_31_pref_1)
session.add(stud_31_pref_2)
session.add(stud_31_pref_3)

stud_32_pref_1 = Preference(first_name1 = "Zena", last_name1 = "K", student_id = 32, gender = "F", student = student32, preference_id = 14)
stud_32_pref_2 = Preference(first_name1 = "Rachel", last_name1 = "S", student_id = 32, gender = "F", student = student32, preference_id = 45)
stud_32_pref_3 = Preference(first_name1 = "Matan", last_name1 = "L", student_id = 32, gender = "M", student = student32, preference_id = 62)

session.add(stud_32_pref_1)
session.add(stud_32_pref_2)
session.add(stud_32_pref_3)

stud_33_pref_1 = Preference(first_name1 = "Jack", last_name1 = "R", student_id = 33, gender = "M", student = student33, preference_id = 5)
stud_33_pref_2 = Preference(first_name1 = "Roxanne", last_name1 = "A", student_id = 33, gender = "F", student = student33, preference_id = 69)
stud_33_pref_3 = Preference(first_name1 = "Corinna", last_name1 = "V", student_id = 33, gender = "F", student = student33, preference_id = 22)

session.add(stud_33_pref_1)
session.add(stud_33_pref_2)
session.add(stud_33_pref_3)

stud_34_pref_1 = Preference(first_name1 = "Rafeala", last_name1 = "L", student_id = 34, gender = "F", student = student34, preference_id = 59)
stud_34_pref_2 = Preference(first_name1 = "Benedict", last_name1 = "T", student_id = 34, gender = "M", student = student34, preference_id = 70)
stud_34_pref_3 = Preference(first_name1 = "Anita", last_name1 = "O", student_id = 34, gender = "F", student = student34, preference_id = 30)

session.add(stud_34_pref_1)
session.add(stud_34_pref_2)
session.add(stud_34_pref_3)

stud_35_pref_1 = Preference(first_name1 = "Ron", last_name1 = "A", student_id = 35, gender = "M", student = student35, preference_id = 8)
stud_35_pref_2 = Preference(first_name1 = "Amos", last_name1 = "S", student_id = 35, gender = "M", student = student35, preference_id = 60)
stud_35_pref_3 = Preference(first_name1 = "Lucas", last_name1 = "S", student_id = 35, gender = "M", student = student35, preference_id = 20)

session.add(stud_35_pref_1)
session.add(stud_35_pref_2)
session.add(stud_35_pref_3)

stud_36_pref_1 = Preference(first_name1 = "Mikaela", last_name1 = "M", student_id = 36, gender = "F", student = student36, preference_id = 58)
stud_36_pref_2 = Preference(first_name1 = "Winona", last_name1 = "B", student_id = 36, gender = "F", student = student36, preference_id = 42)
stud_36_pref_3 = Preference(first_name1 = "Serena", last_name1 = "M", student_id = 36, gender = "F", student = student36, preference_id = 25)

session.add(stud_36_pref_1)
session.add(stud_36_pref_2)
session.add(stud_36_pref_3)

stud_37_pref_1 = Preference(first_name1 = "Beatrise", last_name1 = "S", student_id = 37, gender = "F", student = student37, preference_id = 28)
stud_37_pref_2 = Preference(first_name1 = "Corinna", last_name1 = "V", student_id = 37, gender = "F", student = student37, preference_id = 22)
stud_37_pref_3 = Preference(first_name1 = "Sundar", last_name1 = "R", student_id = 37, gender = "M", student = student37, preference_id = 23)

session.add(stud_37_pref_1)
session.add(stud_37_pref_2)
session.add(stud_37_pref_3)

stud_38_pref_1 = Preference(first_name1 = "Amos", last_name1 = "S", student_id = 38, gender = "M", student = student38, preference_id = 60)
stud_38_pref_2 = Preference(first_name1 = "Ron", last_name1 = "A", student_id = 38, gender = "M", student = student38, preference_id = 8)
stud_38_pref_3 = Preference(first_name1 = "Abraham", last_name1 = "M", student_id = 38, gender = "M", student = student38, preference_id = 61)

session.add(stud_38_pref_1)
session.add(stud_38_pref_2)
session.add(stud_38_pref_3)

stud_39_pref_1 = Preference(first_name1 = "Winona", last_name1 = "B", student_id = 39, gender = "F", student = student39, preference_id = 42)
stud_39_pref_2 = Preference(first_name1 = "Anita", last_name1 = "O", student_id = 39, gender = "F", student = student39, preference_id = 30)
stud_39_pref_3 = Preference(first_name1 = "Oleg", last_name1 = "A", student_id = 39, gender = "M", student = student39, preference_id = 29)

session.add(stud_39_pref_1)
session.add(stud_39_pref_2)
session.add(stud_39_pref_3)

stud_40_pref_1 = Preference(first_name1 = "Alvin", last_name1 = "G", student_id = 40, gender = "M", student = student40, preference_id = 31)
stud_40_pref_2 = Preference(first_name1 = "Amos", last_name1 = "S", student_id = 40, gender = "M", student = student40, preference_id = 60)
stud_40_pref_3 = Preference(first_name1 = "Katerina", last_name1 = "A", student_id = 40, gender = "F", student = student40, preference_id = 18)

session.add(stud_40_pref_1)
session.add(stud_40_pref_2)
session.add(stud_40_pref_3)

stud_41_pref_1 = Preference(first_name1 = "Jasmine", last_name1 = "E", student_id = 41, gender = "F", student = student41, preference_id = 13)
stud_41_pref_2 = Preference(first_name1 = "Charles", last_name1 = "D", student_id = 41, gender = "M", student = student41, preference_id = 10)
stud_41_pref_3 = Preference(first_name1 = "Anar", last_name1 = "S", student_id = 41, gender = "M", student = student41, preference_id = 63)

session.add(stud_41_pref_1)
session.add(stud_41_pref_2)
session.add(stud_41_pref_3)

stud_42_pref_1 = Preference(first_name1 = "Rafeala", last_name1 = "L", student_id = 42, gender = "F", student = student42, preference_id = 59)
stud_42_pref_2 = Preference(first_name1 = "Lucie", last_name1 = "M", student_id = 42, gender = "F", student = student42, preference_id = 39)
stud_42_pref_3 = Preference(first_name1 = "Silvia", last_name1 = "G", student_id = 42, gender = "F", student = student42, preference_id = 12)

session.add(stud_42_pref_1)
session.add(stud_42_pref_2)
session.add(stud_42_pref_3)

stud_43_pref_1 = Preference(first_name1 = "Olympia", last_name1 = "L", student_id = 43, gender = "F", student = student43, preference_id = 56)
stud_43_pref_2 = Preference(first_name1 = "Roxanne", last_name1 = "A", student_id = 43, gender = "F", student = student43, preference_id = 69)
stud_43_pref_3 = Preference(first_name1 = "Shirley", last_name1 = "N", student_id = 43, gender = "F", student = student43, preference_id = 55)

session.add(stud_43_pref_1)
session.add(stud_43_pref_2)
session.add(stud_43_pref_3)

stud_44_pref_1 = Preference(first_name1 = "Samantha", last_name1 = "A", student_id = 44, gender = "F", student = student44, preference_id = 1)
stud_44_pref_2 = Preference(first_name1 = "Joe", last_name1 = "C", student_id = 44, gender = "M", student = student44, preference_id = 7)
stud_44_pref_3 = Preference(first_name1 = "Irene", last_name1 = "S", student_id = 44, gender = "F", student = student44, preference_id = 66)

session.add(stud_44_pref_1)
session.add(stud_44_pref_2)
session.add(stud_44_pref_3)

stud_45_pref_1 = Preference(first_name1 = "Paula", last_name1 = "D", student_id = 45, gender = "F", student = student45, preference_id = 32)
stud_45_pref_2 = Preference(first_name1 = "Zena", last_name1 = "K", student_id = 45, gender = "F", student = student45, preference_id = 14)
stud_45_pref_3 = Preference(first_name1 = "Aseem", last_name1 = "O", student_id = 45, gender = "M", student = student45, preference_id = 50)

session.add(stud_45_pref_1)
session.add(stud_45_pref_2)
session.add(stud_45_pref_3)

stud_46_pref_1 = Preference(first_name1 = "Amit", last_name1 = "A", student_id = 46, gender = "M", student = student46, preference_id = 49)
stud_46_pref_2 = Preference(first_name1 = "Corinna", last_name1 = "V", student_id = 46, gender = "F", student = student46, preference_id = 22)
stud_46_pref_3 = Preference(first_name1 = "Sundar", last_name1 = "R", student_id = 46, gender = "M", student = student46, preference_id = 23)

session.add(stud_46_pref_1)
session.add(stud_46_pref_2)
session.add(stud_46_pref_3)

stud_47_pref_1 = Preference(first_name1 = "Mira", last_name1 = "A", student_id = 47, gender = "F", student = student47, preference_id = 67)
stud_47_pref_2 = Preference(first_name1 = "Mikaela", last_name1 = "M", student_id = 47, gender = "F", student = student47, preference_id = 58)
stud_47_pref_3 = Preference(first_name1 = "Joe", last_name1 = "C", student_id = 47, gender = "M", student = student47, preference_id = 7)

session.add(stud_47_pref_1)
session.add(stud_47_pref_2)
session.add(stud_47_pref_3)

stud_48_pref_1 = Preference(first_name1 = "Amit", last_name1 = "A", student_id = 48, gender = "M", student = student48, preference_id = 49)
stud_48_pref_2 = Preference(first_name1 = "Sundar", last_name1 = "R", student_id = 48, gender = "M", student = student48, preference_id = 23)
stud_48_pref_3 = Preference(first_name1 = "Ranjit", last_name1 = "F", student_id = 48, gender = "M", student = student48, preference_id = 57)

session.add(stud_48_pref_1)
session.add(stud_48_pref_2)
session.add(stud_48_pref_3)

stud_49_pref_1 = Preference(first_name1 = "Joe", last_name1 = "C", student_id = 49, gender = "M", student = student49, preference_id = 7)
stud_49_pref_2 = Preference(first_name1 = "Patrick", last_name1 = "G", student_id = 49, gender = "M", student = student49, preference_id = 24)
stud_49_pref_3 = Preference(first_name1 = "Doru", last_name1 = "V", student_id = 49, gender = "F", student = student49, preference_id = 46)

session.add(stud_49_pref_1)
session.add(stud_49_pref_2)
session.add(stud_49_pref_3)

stud_50_pref_1 = Preference(first_name1 = "Alexander", last_name1 = "C", student_id = 50, gender = "M", student = student50, preference_id = 2)
stud_50_pref_2 = Preference(first_name1 = "Sundar", last_name1 = "R", student_id = 50, gender = "M", student = student50, preference_id = 23)
stud_50_pref_3 = Preference(first_name1 = "Jack", last_name1 = "R", student_id = 50, gender = "M", student = student50, preference_id = 5)

session.add(stud_50_pref_1)
session.add(stud_50_pref_2)
session.add(stud_50_pref_3)

stud_51_pref_1 = Preference(first_name1 = "Joe", last_name1 = "C", student_id = 51, gender = "M", student = student51, preference_id = 7)
stud_51_pref_2 = Preference(first_name1 = "Susie", last_name1 = "D", student_id = 51, gender = "F", student = student51, preference_id = 47)
stud_51_pref_3 = Preference(first_name1 = "Aseem", last_name1 = "O", student_id = 51, gender = "M", student = student51, preference_id = 50)

session.add(stud_51_pref_1)
session.add(stud_51_pref_2)
session.add(stud_51_pref_3)

stud_52_pref_1 = Preference(first_name1 = "Lorena", last_name1 = "T", student_id = 52, gender = "F", student = student52, preference_id = 34)
stud_52_pref_2 = Preference(first_name1 = "Lexi", last_name1 = "L", student_id = 52, gender = "F", student = student52, preference_id = 6)
stud_52_pref_3 = Preference(first_name1 = "Sundar", last_name1 = "R", student_id = 52, gender = "M", student = student52, preference_id = 23)

session.add(stud_52_pref_1)
session.add(stud_52_pref_2)
session.add(stud_52_pref_3)

stud_53_pref_1 = Preference(first_name1 = "", last_name1 = "", student_id = 53, gender = "", student = student53)
stud_53_pref_2 = Preference(first_name1 = "", last_name1 = "", student_id = 53, gender = "", student = student53)
stud_53_pref_3 = Preference(first_name1 = "", last_name1 = "", student_id = 53, gender = "", student = student53)

session.add(stud_53_pref_1)
session.add(stud_53_pref_2)
session.add(stud_53_pref_3)

stud_54_pref_1 = Preference(first_name1 = "Olympia", last_name1 = "L", student_id = 54, gender = "F", student = student54, preference_id = 56)
stud_54_pref_2 = Preference(first_name1 = "Rosa", last_name1 = "E", student_id = 54, gender = "F", student = student54, preference_id = 43)
stud_54_pref_3 = Preference(first_name1 = "Louise", last_name1 = "D", student_id = 54, gender = "F", student = student54, preference_id = 37)

session.add(stud_54_pref_1)
session.add(stud_54_pref_2)
session.add(stud_54_pref_3)

stud_55_pref_1 = Preference(first_name1 = "Roxanne", last_name1 = "A", student_id = 55, gender = "F", student = student55, preference_id = 69)
stud_55_pref_2 = Preference(first_name1 = "Jasmine", last_name1 = "E", student_id = 55, gender = "F", student = student55, preference_id = 13)
stud_55_pref_3 = Preference(first_name1 = "Erwin", last_name1 = "P", student_id = 55, gender = "M", student = student55, preference_id = 41)

session.add(stud_55_pref_1)
session.add(stud_55_pref_2)
session.add(stud_55_pref_3)

stud_56_pref_1 = Preference(first_name1 = "Roxanne", last_name1 = "A", student_id = 56, gender = "F", student = student56, preference_id = 69)
stud_56_pref_2 = Preference(first_name1 = "Shirley", last_name1 = "N", student_id = 56, gender = "F", student = student56, preference_id = 55)
stud_56_pref_3 = Preference(first_name1 = "Winona", last_name1 = "B", student_id = 56, gender = "F", student = student56, preference_id = 42)

session.add(stud_56_pref_1)
session.add(stud_56_pref_2)
session.add(stud_56_pref_3)

stud_57_pref_1 = Preference(first_name1 = "Rafeala", last_name1 = "L", student_id = 57, gender = "F", student = student57, preference_id = 59)
stud_57_pref_2 = Preference(first_name1 = "Zena", last_name1 = "K", student_id = 57, gender = "F", student = student57, preference_id = 14)
stud_57_pref_3 = Preference(first_name1 = "Kate", last_name1 = "S", student_id = 57, gender = "F", student = student57, preference_id = 3)

session.add(stud_57_pref_1)
session.add(stud_57_pref_2)
session.add(stud_57_pref_3)

stud_58_pref_1 = Preference(first_name1 = "Serena", last_name1 = "M", student_id = 58, gender = "F", student = student58, preference_id = 25)
stud_58_pref_2 = Preference(first_name1 = "Joe", last_name1 = "C", student_id = 58, gender = "M", student = student58, preference_id = 7)
stud_58_pref_3 = Preference(first_name1 = "Alvin", last_name1 = "G", student_id = 58, gender = "M", student = student58, preference_id = 31)

session.add(stud_58_pref_1)
session.add(stud_58_pref_2)
session.add(stud_58_pref_3)

stud_59_pref_1 = Preference(first_name1 = "Katerina", last_name1 = "A", student_id = 59, gender = "F", student = student59, preference_id = 18)
stud_59_pref_2 = Preference(first_name1 = "Amit", last_name1 = "A", student_id = 59, gender = "M", student = student59, preference_id = 49)
stud_59_pref_3 = Preference(first_name1 = "Joe", last_name1 = "C", student_id = 59, gender = "M", student = student59, preference_id = 7)

session.add(stud_59_pref_1)
session.add(stud_59_pref_2)
session.add(stud_59_pref_3)

stud_60_pref_1 = Preference(first_name1 = "Solomon", last_name1 = "P", student_id = 60, gender = "M", student = student60, preference_id = 40)
stud_60_pref_2 = Preference(first_name1 = "Alvin", last_name1 = "G", student_id = 60, gender = "M", student = student60, preference_id = 31)
stud_60_pref_3 = Preference(first_name1 = "Ariella", last_name1 = "A", student_id = 60, gender = "F", student = student60, preference_id = 65)

session.add(stud_60_pref_1)
session.add(stud_60_pref_2)
session.add(stud_60_pref_3)

stud_61_pref_1 = Preference(first_name1 = "Ranjit", last_name1 = "F", student_id = 61, gender = "M", student = student61, preference_id = 57)
stud_61_pref_2 = Preference(first_name1 = "Anton", last_name1 = "M", student_id = 61, gender = "M", student = student61, preference_id = 48)
stud_61_pref_3 = Preference(first_name1 = "Ron", last_name1 = "A", student_id = 61, gender = "M", student = student61, preference_id = 8)

session.add(stud_61_pref_1)
session.add(stud_61_pref_2)
session.add(stud_61_pref_3)

stud_62_pref_1 = Preference(first_name1 = "Lucas", last_name1 = "S", student_id = 62, gender = "M", student = student62, preference_id = 20)
stud_62_pref_2 = Preference(first_name1 = "Paula", last_name1 = "D", student_id = 62, gender = "F", student = student62, preference_id = 32)
stud_62_pref_3 = Preference(first_name1 = "Benedict", last_name1 = "T", student_id = 62, gender = "M", student = student62, preference_id = 70)

session.add(stud_62_pref_1)
session.add(stud_62_pref_2)
session.add(stud_62_pref_3)

stud_63_pref_1 = Preference(first_name1 = "Jasmine", last_name1 = "E", student_id = 63, gender = "F", student = student63, preference_id = 13)
stud_63_pref_2 = Preference(first_name1 = "Erwin", last_name1 = "P", student_id = 63, gender = "M", student = student63, preference_id = 41)
stud_63_pref_3 = Preference(first_name1 = "Charles", last_name1 = "D", student_id = 63, gender = "M", student = student63, preference_id = 10)

session.add(stud_63_pref_1)
session.add(stud_63_pref_2)
session.add(stud_63_pref_3)

stud_64_pref_1 = Preference(first_name1 = "", last_name1 = "", student_id = 64, gender = "", student = student64)
stud_64_pref_2 = Preference(first_name1 = "", last_name1 = "", student_id = 64, gender = "", student = student64)
stud_64_pref_3 = Preference(first_name1 = "", last_name1 = "", student_id = 64, gender = "", student = student64)

session.add(stud_64_pref_1)
session.add(stud_64_pref_2)
session.add(stud_64_pref_3)

stud_65_pref_1 = Preference(first_name1 = "", last_name1 = "", student_id = 65, gender = "", student = student65)
stud_65_pref_2 = Preference(first_name1 = "", last_name1 = "", student_id = 65, gender = "", student = student65)
stud_65_pref_3 = Preference(first_name1 = "", last_name1 = "", student_id = 65, gender = "", student = student65)

session.add(stud_65_pref_1)
session.add(stud_65_pref_2)
session.add(stud_65_pref_3)

stud_66_pref_1 = Preference(first_name1 = "", last_name1 = "", student_id = 66, gender = "", student = student66)
stud_66_pref_2 = Preference(first_name1 = "", last_name1 = "", student_id = 66, gender = "", student = student66)
stud_66_pref_3 = Preference(first_name1 = "", last_name1 = "", student_id = 66, gender = "", student = student66)

session.add(stud_66_pref_1)
session.add(stud_66_pref_2)
session.add(stud_66_pref_3)

stud_67_pref_1 = Preference(first_name1 = "", last_name1 = "", student_id = 67, gender = "", student = student67)
stud_67_pref_2 = Preference(first_name1 = "", last_name1 = "", student_id = 67, gender = "", student = student67)
stud_67_pref_3 = Preference(first_name1 = "", last_name1 = "", student_id = 67, gender = "", student = student67)

session.add(stud_67_pref_1)
session.add(stud_67_pref_2)
session.add(stud_67_pref_3)

stud_68_pref_1 = Preference(first_name1 = "", last_name1 = "", student_id = 68, gender = "", student = student68)
stud_68_pref_2 = Preference(first_name1 = "", last_name1 = "", student_id = 68, gender = "", student = student68)
stud_68_pref_3 = Preference(first_name1 = "", last_name1 = "", student_id = 68, gender = "", student = student68)

session.add(stud_68_pref_1)
session.add(stud_68_pref_2)
session.add(stud_68_pref_3)

stud_69_pref_1 = Preference(first_name1 = "", last_name1 = "", student_id = 69, gender = "", student = student69)
stud_69_pref_2 = Preference(first_name1 = "", last_name1 = "", student_id = 69, gender = "", student = student69)
stud_69_pref_3 = Preference(first_name1 = "", last_name1 = "", student_id = 69, gender = "", student = student69)

session.add(stud_69_pref_1)
session.add(stud_69_pref_2)
session.add(stud_69_pref_3)

stud_70_pref_1 = Preference(first_name1 = "Lucas", last_name1 = "S", student_id = 70, gender = "M", student = student70, preference_id = 20)
stud_70_pref_2 = Preference(first_name1 = "Eugene", last_name1 = "C", student_id = 70, gender = "M", student = student70, preference_id = 21)
stud_70_pref_3 = Preference(first_name1 = "Matan", last_name1 = "L", student_id = 70, gender = "M", student = student70, preference_id = 62)

session.add(stud_70_pref_1)
session.add(stud_70_pref_2)
session.add(stud_70_pref_3)

session.commit()
