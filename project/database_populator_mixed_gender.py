from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Student, engine, Preference

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

student1 = Student(first_name = "Tej", last_name = "", gender = "M")
stud_1_pref_1 = Preference(first_name1 = "Patrick", last_name1 = "", student_id = 1, gender = "F")
stud_1_pref_2 = Preference(first_name1 = "Bob", last_name1 = "", student_id = 1, gender = "M")
stud_1_pref_3 = Preference(first_name1 = "Curry", last_name1 = "", student_id = 1, gender = "F")
stud_1_pref_4 = Preference(first_name1 = "Reggie", last_name1 = "", student_id = 1, gender = "M")

session.add(student1)
session.add(stud_1_pref_1)
session.add(stud_1_pref_2)
session.add(stud_1_pref_3)
session.add(stud_1_pref_4)

session.commit()

student2 = Student(first_name = "Jack", last_name = "", gender = "F")
stud_2_pref_1 = Preference(first_name1 = "Manny", last_name1 = "", student_id = 2, gender = "F")
stud_2_pref_2 = Preference(first_name1 = "Bob", last_name1 = "", student_id = 2, gender = "M")
stud_2_pref_3 = Preference(first_name1 = "Fred", last_name1 = "", student_id = 2, gender = "M")
stud_2_pref_4 = Preference(first_name1 = "Patrick", last_name1 = "", student_id = 2, gender = "F")

session.add(student2)
session.add(stud_2_pref_1)
session.add(stud_2_pref_2)
session.add(stud_2_pref_3)
session.add(stud_2_pref_4)

session.commit()

student3 = Student(first_name = "Fred", last_name = "", gender = "M")
stud_3_pref_1 = Preference(first_name1 = "Patrick", last_name1 = "", student_id = 3, gender = "F")
stud_3_pref_2 = Preference(first_name1 = "Bob", last_name1 = "", student_id = 3, gender = "M")
stud_3_pref_3 = Preference(first_name1 = "Jack", last_name1 = "", student_id = 3, gender = "F")
stud_3_pref_4 = Preference(first_name1 = "Fisher", last_name1 = "", student_id = 3, gender = "M")

session.add(student3)
session.add(stud_3_pref_1)
session.add(stud_3_pref_2)
session.add(stud_3_pref_3)
session.add(stud_3_pref_4)

session.commit()

student4 = Student(first_name = "Bob", last_name = "", gender = "M")
stud_4_pref_1 = Preference(first_name1 = "Fred", last_name1 = "", student_id = 4, gender = "M")
stud_4_pref_2 = Preference(first_name1 = "Jack", last_name1 = "", student_id = 4, gender = "F")
stud_4_pref_3 = Preference(first_name1 = "Magic", last_name1 = "", student_id = 4, gender = "M")
stud_4_pref_4 = Preference(first_name1 = "Rambus", last_name1 = "", student_id = 4, gender = "M")

session.add(student4)
session.add(stud_4_pref_1)
session.add(stud_4_pref_2)
session.add(stud_4_pref_3)
session.add(stud_4_pref_4)

session.commit()

student5 = Student(first_name = "Frank", last_name = "", gender = "F")
stud_5_pref_1 = Preference(first_name1 = "Bob", last_name1 = "", student_id = 5, gender = "M")
stud_5_pref_2 = Preference(first_name1 = "Manny", last_name1 = "", student_id = 5, gender = "F")
stud_5_pref_3 = Preference(first_name1 = "Worthy", last_name1 = "", student_id = 5, gender = "M")
stud_5_pref_4 = Preference(first_name1 = "Byron", last_name1 = "", student_id = 5, gender = "F")

session.add(student5)
session.add(stud_5_pref_1)
session.add(stud_5_pref_2)
session.add(stud_5_pref_3)
session.add(stud_5_pref_4)

session.commit()

student6 = Student(first_name = "Manny", last_name = "", gender = "F")
stud_6_pref_1 = Preference(first_name1 = "James", last_name1 = "", student_id = 6, gender = "M")
stud_6_pref_2 = Preference(first_name1 = "Frank", last_name1 = "", student_id = 6, gender = "F")
stud_6_pref_3 = Preference(first_name1 = "Shaq", last_name1 = "", student_id = 6, gender = "F")
stud_6_pref_4 = Preference(first_name1 = "Horry", last_name1 = "", student_id = 6, gender = "F")

session.add(student6)
session.add(stud_6_pref_1)
session.add(stud_6_pref_2)
session.add(stud_6_pref_3)
session.add(stud_6_pref_4)

session.commit()

student7 = Student(first_name = "Jonathan", last_name = "", gender = "M")
stud_7_pref_1 = Preference(first_name1 = "Fred", last_name1 = "", student_id = 7, gender = "M")
stud_7_pref_2 = Preference(first_name1 = "Frank", last_name1 = "", student_id = 7, gender = "F")
stud_7_pref_3 = Preference(first_name1 = "Jack", last_name1 = "", student_id = 7, gender = "F")
stud_7_pref_4 = Preference(first_name1 = "Shaq", last_name1 = "", student_id = 7, gender = "F")

session.add(student7)
session.add(stud_7_pref_1)
session.add(stud_7_pref_2)
session.add(stud_7_pref_3)
session.add(stud_7_pref_4)

session.commit()

student8 = Student(first_name = "Magic", last_name = "", gender = "M")
stud_8_pref_1 = Preference(first_name1 = "Patrick", last_name1 = "", student_id = 8, gender = "F")
stud_8_pref_2 = Preference(first_name1 = "Shaq", last_name1 = "", student_id = 8, gender = "F")
stud_8_pref_3 = Preference(first_name1 = "Kareem", last_name1 = "", student_id = 8, gender = "M")
stud_8_pref_4 = Preference(first_name1 = "James", last_name1 = "", student_id = 8, gender = "M")

session.add(student8)
session.add(stud_8_pref_1)
session.add(stud_8_pref_2)
session.add(stud_8_pref_3)
session.add(stud_8_pref_4)

session.commit()

student9 = Student(first_name = "Jordan", last_name = "", gender = "F")
stud_9_pref_1 = Preference(first_name1 = "Magic", last_name1 = "", student_id = 9, gender = "M")
stud_9_pref_2 = Preference(first_name1 = "Jerry", last_name1 = "", student_id = 9, gender = "M")
stud_9_pref_3 = Preference(first_name1 = "Nev", last_name1 = "", student_id = 9, gender = "M")
stud_9_pref_4 = Preference(first_name1 = "Joe", last_name1 = "", student_id = 9, gender = "F")

session.add(student9)
session.add(stud_9_pref_1)
session.add(stud_9_pref_2)
session.add(stud_9_pref_3)
session.add(stud_9_pref_4)

session.commit()

student10 = Student(first_name = "Cooper", last_name = "", gender = "M")
stud_10_pref_1 = Preference(first_name1 = "Rambus", last_name1 = "", student_id = 10, gender = "M")
stud_10_pref_2 = Preference(first_name1 = "Moe", last_name1 = "", student_id = 10, gender = "F")
stud_10_pref_3 = Preference(first_name1 = "Kobe", last_name1 = "", student_id = 10, gender = "F")
stud_10_pref_4 = Preference(first_name1 = "Curry", last_name1 = "", student_id = 10, gender = "F")

session.add(student10)
session.add(stud_10_pref_1)
session.add(stud_10_pref_2)
session.add(stud_10_pref_3)
session.add(stud_10_pref_4)

session.commit()

student11 = Student(first_name = "Patrick", last_name = "", gender = "F")
stud_11_pref_1 = Preference(first_name1 = "Bob", last_name1 = "", student_id = 11, gender = "M")
stud_11_pref_2 = Preference(first_name1 = "Frank", last_name1 = "", student_id = 11, gender = "F")
stud_11_pref_3 = Preference(first_name1 = "Jordan", last_name1 = "", student_id = 11, gender = "F")
stud_11_pref_4 = Preference(first_name1 = "Moe", last_name1 = "", student_id = 11, gender = "F")

session.add(student11)
session.add(stud_11_pref_1)
session.add(stud_11_pref_2)
session.add(stud_11_pref_3)
session.add(stud_11_pref_4)

session.commit()

student12 = Student(first_name = "Rambus", last_name = "", gender = "M")
stud_12_pref_1 = Preference(first_name1 = "Gasol", last_name1 = "", student_id = 12, gender = "F")
stud_12_pref_2 = Preference(first_name1 = "Jack", last_name1 = "", student_id = 12, gender = "F")
stud_12_pref_3 = Preference(first_name1 = "Fisher", last_name1 = "", student_id = 12, gender = "M")
stud_12_pref_4 = Preference(first_name1 = "Bob", last_name1 = "", student_id = 12, gender = "M")

session.add(student12)
session.add(stud_12_pref_1)
session.add(stud_12_pref_2)
session.add(stud_12_pref_3)
session.add(stud_12_pref_4)

session.commit()

student13 = Student(first_name = "Fisher", last_name = "", gender = "M")
stud_13_pref_1 = Preference(first_name1 = "Wilt", last_name1 = "", student_id = 13, gender = "F")
stud_13_pref_2 = Preference(first_name1 = "Manny", last_name1 = "", student_id = 13, gender = "F")
stud_13_pref_3 = Preference(first_name1 = "Tej", last_name1 = "", student_id = 13, gender = "M")
stud_13_pref_4 = Preference(first_name1 = "Jack", last_name1 = "", student_id = 13, gender = "F")

session.add(student13)
session.add(stud_13_pref_1)
session.add(stud_13_pref_2)
session.add(stud_13_pref_3)
session.add(stud_13_pref_4)

session.commit()

student14 = Student(first_name = "Wilt", last_name = "", gender = "F")
stud_14_pref_1 = Preference(first_name1 = "Rambus", last_name1 = "", student_id = 14, gender = "M")
stud_14_pref_2 = Preference(first_name1 = "Tej", last_name1 = "", student_id = 14, gender = "M")
stud_14_pref_3 = Preference(first_name1 = "Fred", last_name1 = "", student_id = 14, gender = "M")
stud_14_pref_4 = Preference(first_name1 = "Durant", last_name1 = "", student_id = 14, gender = "F")

session.add(student14)
session.add(stud_14_pref_1)
session.add(stud_14_pref_2)
session.add(stud_14_pref_3)
session.add(stud_14_pref_4)

session.commit()

student15 = Student(first_name = "Kareem", last_name = "", gender = "M")
stud_15_pref_1 = Preference(first_name1 = "Wilt", last_name1 = "", student_id = 15, gender = "F")
stud_15_pref_2 = Preference(first_name1 = "Fisher", last_name1 = "", student_id = 15, gender = "M")
stud_15_pref_3 = Preference(first_name1 = "Tej", last_name1 = "", student_id = 15, gender = "M")
stud_15_pref_4 = Preference(first_name1 = "Manny", last_name1 = "", student_id = 15, gender = "F")

session.add(student15)
session.add(stud_15_pref_1)
session.add(stud_15_pref_2)
session.add(stud_15_pref_3)
session.add(stud_15_pref_4)

session.commit()

student16 = Student(first_name = "Kobe", last_name = "", gender = "F")
stud_16_pref_1 = Preference(first_name1 = "Jack", last_name1 = "", student_id = 16, gender = "F")
stud_16_pref_2 = Preference(first_name1 = "Fred", last_name1 = "", student_id = 16, gender = "M")
stud_16_pref_3 = Preference(first_name1 = "Reggie", last_name1 = "", student_id = 16, gender = "M")
stud_16_pref_4 = Preference(first_name1 = "Tej", last_name1 = "", student_id = 16, gender = "M")

session.add(student16)
session.add(stud_16_pref_1)
session.add(stud_16_pref_2)
session.add(stud_16_pref_3)
session.add(stud_16_pref_4)

session.commit()

student17 = Student(first_name = "Shaq", last_name = "", gender = "F")
stud_17_pref_1 = Preference(first_name1 = "Frank", last_name1 = "", student_id = 17, gender = "F")
stud_17_pref_2 = Preference(first_name1 = "Fred", last_name1 = "", student_id = 17, gender = "M")
stud_17_pref_3 = Preference(first_name1 = "Curry", last_name1 = "", student_id = 17, gender = "F")
stud_17_pref_4 = Preference(first_name1 = "Gasol", last_name1 = "", student_id = 17, gender = "F")

session.add(student17)
session.add(stud_17_pref_1)
session.add(stud_17_pref_2)
session.add(stud_17_pref_3)
session.add(stud_17_pref_4)

session.commit()

student18 = Student(first_name = "Lebron", last_name = "", gender = "F")
stud_18_pref_1 = Preference(first_name1 = "Kareem", last_name1 = "", student_id = 18, gender = "M")
stud_18_pref_2 = Preference(first_name1 = "Joe", last_name1 = "", student_id = 18, gender = "F")
stud_18_pref_3 = Preference(first_name1 = "Manny", last_name1 = "", student_id = 18, gender = "F")
stud_18_pref_4 = Preference(first_name1 = "Frank", last_name1 = "", student_id = 18, gender = "F")

session.add(student18)
session.add(stud_18_pref_1)
session.add(stud_18_pref_2)
session.add(stud_18_pref_3)
session.add(stud_18_pref_4)

session.commit()

student19 = Student(first_name = "Curry", last_name = "", gender = "F")
stud_19_pref_1 = Preference(first_name1 = "Byron", last_name1 = "", student_id = 19, gender = "F")
stud_19_pref_2 = Preference(first_name1 = "Jordan", last_name1 = "", student_id = 19, gender = "F")
stud_19_pref_3 = Preference(first_name1 = "Worthy", last_name1 = "", student_id = 19, gender = "M")
stud_19_pref_4 = Preference(first_name1 = "Fred", last_name1 = "", student_id = 19, gender = "M")

session.add(student19)
session.add(stud_19_pref_1)
session.add(stud_19_pref_2)
session.add(stud_19_pref_3)
session.add(stud_19_pref_4)

session.commit()

student20 = Student(first_name = "Reggie", last_name = "", gender = "M")
stud_20_pref_1 = Preference(first_name1 = "Magic", last_name1 = "", student_id = 20, gender = "M")
stud_20_pref_2 = Preference(first_name1 = "Cooper", last_name1 = "", student_id = 20, gender = "M")
stud_20_pref_3 = Preference(first_name1 = "Rambus", last_name1 = "", student_id = 20, gender = "M")
stud_20_pref_4 = Preference(first_name1 = "Jordan", last_name1 = "", student_id = 20, gender = "F")

session.add(student20)
session.add(stud_20_pref_1)
session.add(stud_20_pref_2)
session.add(stud_20_pref_3)
session.add(stud_20_pref_4)

session.commit()

student21 = Student(first_name = "Worthy", last_name = "", gender = "M")
stud_21_pref_1 = Preference(first_name1 = "Jonathan", last_name1 = "", student_id = 21, gender = "M")
stud_21_pref_2 = Preference(first_name1 = "Tej", last_name1 = "", student_id = 21, gender = "M")
stud_21_pref_3 = Preference(first_name1 = "Fisher", last_name1 = "", student_id = 21, gender = "M")
stud_21_pref_4 = Preference(first_name1 = "Jerry", last_name1 = "", student_id = 21, gender = "M")

session.add(student21)
session.add(stud_21_pref_1)
session.add(stud_21_pref_2)
session.add(stud_21_pref_3)
session.add(stud_21_pref_4)

session.commit()

student22 = Student(first_name = "Moe", last_name = "", gender = "F")
stud_22_pref_1 = Preference(first_name1 = "Jonathan", last_name1 = "", student_id = 22, gender = "M")
stud_22_pref_2 = Preference(first_name1 = "Tej", last_name1 = "", student_id = 22, gender = "M")
stud_22_pref_3 = Preference(first_name1 = "Cooper", last_name1 = "", student_id = 22, gender = "M")
stud_22_pref_4 = Preference(first_name1 = "Magic", last_name1 = "", student_id = 22, gender = "M")

session.add(student22)
session.add(stud_22_pref_1)
session.add(stud_22_pref_2)
session.add(stud_22_pref_3)
session.add(stud_22_pref_4)

session.commit()

student23 = Student(first_name = "Jerry", last_name = "", gender = "M")
stud_23_pref_1 = Preference(first_name1 = "Jonathan", last_name1 = "", student_id = 23, gender = "M")
stud_23_pref_2 = Preference(first_name1 = "Lebron", last_name1 = "", student_id = 23, gender = "F")
stud_23_pref_3 = Preference(first_name1 = "Jordan", last_name1 = "", student_id = 23, gender = "F")
stud_23_pref_4 = Preference(first_name1 = "Kobe", last_name1 = "", student_id = 23, gender = "F")

session.add(student23)
session.add(stud_23_pref_1)
session.add(stud_23_pref_2)
session.add(stud_23_pref_3)
session.add(stud_23_pref_4)

session.commit()

student24 = Student(first_name = "Joe", last_name = "", gender = "F")
stud_24_pref_1 = Preference(first_name1 = "Frank", last_name1 = "", student_id = 24, gender = "F")
stud_24_pref_2 = Preference(first_name1 = "Jonathan", last_name1 = "", student_id = 24, gender = "M")
stud_24_pref_3 = Preference(first_name1 = "Wilt", last_name1 = "", student_id = 24, gender = "F")
stud_24_pref_4 = Preference(first_name1 = "Cooper", last_name1 = "", student_id = 24, gender = "M")

session.add(student24)
session.add(stud_24_pref_1)
session.add(stud_24_pref_2)
session.add(stud_24_pref_3)
session.add(stud_24_pref_4)

session.commit()

student25 = Student(first_name = "Nev", last_name = "", gender = "M")
stud_25_pref_1 = Preference(first_name1 = "Tej", last_name1 = "", student_id = 25, gender = "M")
stud_25_pref_2 = Preference(first_name1 = "Jonathan", last_name1 = "", student_id = 25, gender = "M")
stud_25_pref_3 = Preference(first_name1 = "Reggie", last_name1 = "", student_id = 25, gender = "M")
stud_25_pref_4 = Preference(first_name1 = "Kareem", last_name1 = "", student_id = 25, gender = "M")

session.add(student25)
session.add(stud_25_pref_1)
session.add(stud_25_pref_2)
session.add(stud_25_pref_3)
session.add(stud_25_pref_4)

session.commit()

student26 = Student(first_name = "James", last_name = "", gender = "M")
stud_26_pref_1 = Preference(first_name1 = "Fred", last_name1 = "", student_id = 26, gender = "M")
stud_26_pref_2 = Preference(first_name1 = "Tej", last_name1 = "", student_id = 26, gender = "M")
stud_26_pref_3 = Preference(first_name1 = "Kobe", last_name1 = "", student_id = 26, gender = "F")
stud_26_pref_4 = Preference(first_name1 = "Jonathan", last_name1 = "", student_id = 26, gender = "M")

session.add(student26)
session.add(stud_26_pref_1)
session.add(stud_26_pref_2)
session.add(stud_26_pref_3)
session.add(stud_26_pref_4)

session.commit()

student27 = Student(first_name = "Byron", last_name = "", gender = "F")
stud_27_pref_1 = Preference(first_name1 = "Horry", last_name1 = "", student_id = 27, gender = "F")
stud_27_pref_2 = Preference(first_name1 = "Manny", last_name1 = "", student_id = 27, gender = "F")
stud_27_pref_3 = Preference(first_name1 = "Jack", last_name1 = "", student_id = 27, gender = "F")
stud_27_pref_4 = Preference(first_name1 = "Worthy", last_name1 = "", student_id = 27, gender = "M")

session.add(student27)
session.add(stud_27_pref_1)
session.add(stud_27_pref_2)
session.add(stud_27_pref_3)
session.add(stud_27_pref_4)

session.commit()

student28 = Student(first_name = "Horry", last_name = "", gender = "F")
stud_28_pref_1 = Preference(first_name1 = "Lebron", last_name1 = "", student_id = 28, gender = "F")
stud_28_pref_2 = Preference(first_name1 = "Bob", last_name1 = "", student_id = 28, gender = "M")
stud_28_pref_3 = Preference(first_name1 = "Jack", last_name1 = "", student_id = 28, gender = "F")
stud_28_pref_4 = Preference(first_name1 = "Wilt", last_name1 = "", student_id = 28, gender = "F")

session.add(student28)
session.add(stud_28_pref_1)
session.add(stud_28_pref_2)
session.add(stud_28_pref_3)
session.add(stud_28_pref_4)

session.commit()

student29 = Student(first_name = "Gasol", last_name = "", gender = "F")
stud_29_pref_1 = Preference(first_name1 = "Cooper", last_name1 = "", student_id = 29, gender = "M")
stud_29_pref_2 = Preference(first_name1 = "Frank", last_name1 = "", student_id = 29, gender = "F")
stud_29_pref_3 = Preference(first_name1 = "Jack", last_name1 = "", student_id = 29, gender = "F")
stud_29_pref_4 = Preference(first_name1 = "Nev", last_name1 = "", student_id = 29, gender = "M")

session.add(student29)
session.add(stud_29_pref_1)
session.add(stud_29_pref_2)
session.add(stud_29_pref_3)
session.add(stud_29_pref_4)

session.commit()

student30 = Student(first_name = "Durant", last_name = "", gender = "F")
stud_30_pref_1 = Preference(first_name1 = "Fred", last_name1 = "", student_id = 30, gender = "M")
stud_30_pref_2 = Preference(first_name1 = "Tej", last_name1 = "", student_id = 30, gender = "M")
stud_30_pref_3 = Preference(first_name1 = "Magic", last_name1 = "", student_id = 30, gender = "M")
stud_30_pref_4 = Preference(first_name1 = "Lebron", last_name1 = "", student_id = 30, gender = "F")

session.add(student30)
session.add(stud_30_pref_1)
session.add(stud_30_pref_2)
session.add(stud_30_pref_3)
session.add(stud_30_pref_4)

session.commit()
