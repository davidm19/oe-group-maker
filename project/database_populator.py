from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Student, engine, Preference

engine = create_engine('sqlite:///database.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

student1 = Student(first_name = "Tej", last_name = "")
stud_1_pref_1 = Preference(first_name1 = "Patrick", last_name1 = "", student_id = 1)
stud_1_pref_2 = Preference(first_name1 = "Bob", last_name1 = "", student_id = 1)
stud_1_pref_3 = Preference(first_name1 = "Curry", last_name1 = "", student_id = 1)
stud_1_pref_4 = Preference(first_name1 = "Reggie", last_name1 = "", student_id = 1)

session.add(student1)
session.add(stud_1_pref_1)
session.add(stud_1_pref_2)
session.add(stud_1_pref_3)
session.add(stud_1_pref_4)

session.commit()

student2 = Student(first_name = "Jack", last_name = "")
stud_2_pref_1 = Preference(first_name1 = "Manny", last_name1 = "", student_id = 2)
stud_2_pref_2 = Preference(first_name1 = "Bob", last_name1 = "", student_id = 2)
stud_2_pref_3 = Preference(first_name1 = "Fred", last_name1 = "", student_id = 2)
stud_2_pref_4 = Preference(first_name1 = "Patrick", last_name1 = "", student_id = 2)

session.add(student2)
session.add(stud_2_pref_1)
session.add(stud_2_pref_2)
session.add(stud_2_pref_3)
session.add(stud_2_pref_4)

session.commit()

student3 = Student(first_name = "Fred", last_name = "")
stud_3_pref_1 = Preference(first_name1 = "Patrick", last_name1 = "", student_id = 3)
stud_3_pref_2 = Preference(first_name1 = "Bob", last_name1 = "", student_id = 3)
stud_3_pref_3 = Preference(first_name1 = "Jack", last_name1 = "", student_id = 3)
stud_3_pref_4 = Preference(first_name1 = "Fisher", last_name1 = "", student_id = 3)

session.add(student3)
session.add(stud_3_pref_1)
session.add(stud_3_pref_2)
session.add(stud_3_pref_3)
session.add(stud_3_pref_4)

session.commit()

student4 = Student(first_name = "Bob", last_name = "")
stud_4_pref_1 = Preference(first_name1 = "Fred", last_name1 = "", student_id = 4)
stud_4_pref_2 = Preference(first_name1 = "Jack", last_name1 = "", student_id = 4)
stud_4_pref_3 = Preference(first_name1 = "Magic", last_name1 = "", student_id = 4)
stud_4_pref_4 = Preference(first_name1 = "Rambus", last_name1 = "", student_id = 4)

session.add(student4)
session.add(stud_4_pref_1)
session.add(stud_4_pref_2)
session.add(stud_4_pref_3)
session.add(stud_4_pref_4)

session.commit()

student5 = Student(first_name = "Frank", last_name = "")
stud_5_pref_1 = Preference(first_name1 = "Bob", last_name1 = "", student_id = 5)
stud_5_pref_2 = Preference(first_name1 = "Manny", last_name1 = "", student_id = 5)
stud_5_pref_3 = Preference(first_name1 = "Worthy", last_name1 = "", student_id = 5)
stud_5_pref_4 = Preference(first_name1 = "Byron", last_name1 = "", student_id = 5)

session.add(student5)
session.add(stud_5_pref_1)
session.add(stud_5_pref_2)
session.add(stud_5_pref_3)
session.add(stud_5_pref_4)

session.commit()

student6 = Student(first_name = "Manny", last_name = "")
stud_6_pref_1 = Preference(first_name1 = "James", last_name1 = "", student_id = 6)
stud_6_pref_2 = Preference(first_name1 = "Frank", last_name1 = "", student_id = 6)
stud_6_pref_3 = Preference(first_name1 = "Shaq", last_name1 = "", student_id = 6)
stud_6_pref_4 = Preference(first_name1 = "Horry", last_name1 = "", student_id = 6)

session.add(student6)
session.add(stud_6_pref_1)
session.add(stud_6_pref_2)
session.add(stud_6_pref_3)
session.add(stud_6_pref_4)

session.commit()

student7 = Student(first_name = "Jonathan", last_name = "")
stud_7_pref_1 = Preference(first_name1 = "Fred", last_name1 = "", student_id = 7)
stud_7_pref_2 = Preference(first_name1 = "Frank", last_name1 = "", student_id = 7)
stud_7_pref_3 = Preference(first_name1 = "Jack", last_name1 = "", student_id = 7)
stud_7_pref_4 = Preference(first_name1 = "Shaq", last_name1 = "", student_id = 7)

session.add(student7)
session.add(stud_7_pref_1)
session.add(stud_7_pref_2)
session.add(stud_7_pref_3)
session.add(stud_7_pref_4)

session.commit()

student8 = Student(first_name = "Magic", last_name = "")
stud_8_pref_1 = Preference(first_name1 = "Patrick", last_name1 = "", student_id = 8)
stud_8_pref_2 = Preference(first_name1 = "Shaq", last_name1 = "", student_id = 8)
stud_8_pref_3 = Preference(first_name1 = "Kareem", last_name1 = "", student_id = 8)
stud_8_pref_4 = Preference(first_name1 = "James", last_name1 = "", student_id = 8)

session.add(student8)
session.add(stud_8_pref_1)
session.add(stud_8_pref_2)
session.add(stud_8_pref_3)
session.add(stud_8_pref_4)

session.commit()

student9 = Student(first_name = "Jordan", last_name = "")
stud_9_pref_1 = Preference(first_name1 = "Magic", last_name1 = "", student_id = 9)
stud_9_pref_2 = Preference(first_name1 = "Jerry", last_name1 = "", student_id = 9)
stud_9_pref_3 = Preference(first_name1 = "Nev", last_name1 = "", student_id = 9)
stud_9_pref_4 = Preference(first_name1 = "Joe", last_name1 = "", student_id = 9)

session.add(student9)
session.add(stud_9_pref_1)
session.add(stud_9_pref_2)
session.add(stud_9_pref_3)
session.add(stud_9_pref_4)

session.commit()

student10 = Student(first_name = "Cooper", last_name = "")
stud_10_pref_1 = Preference(first_name1 = "Rambus", last_name1 = "", student_id = 10)
stud_10_pref_2 = Preference(first_name1 = "Moe", last_name1 = "", student_id = 10)
stud_10_pref_3 = Preference(first_name1 = "Kobe", last_name1 = "", student_id = 10)
stud_10_pref_4 = Preference(first_name1 = "Curry", last_name1 = "", student_id = 10)

session.add(student10)
session.add(stud_10_pref_1)
session.add(stud_10_pref_2)
session.add(stud_10_pref_3)
session.add(stud_10_pref_4)

session.commit()

student11 = Student(first_name = "Patrick", last_name = "")
stud_11_pref_1 = Preference(first_name1 = "Bob", last_name1 = "", student_id = 11)
stud_11_pref_2 = Preference(first_name1 = "Frank", last_name1 = "", student_id = 11)
stud_11_pref_3 = Preference(first_name1 = "Jordan", last_name1 = "", student_id = 11)
stud_11_pref_4 = Preference(first_name1 = "Moe", last_name1 = "", student_id = 11)

#I AM CHANGING BOB AND JACK IN THE FOURTH PREFERENCE SLOT ACCORDING TO THE SPREADHSHEET. WILL CORRECT WHEN SHEET IS CORRECTED

session.add(student11)
session.add(stud_11_pref_1)
session.add(stud_11_pref_2)
session.add(stud_11_pref_3)
session.add(stud_11_pref_4)

session.commit()

student12 = Student(first_name = "Rambus", last_name = "")
stud_12_pref_1 = Preference(first_name1 = "Gasol", last_name1 = "", student_id = 12)
stud_12_pref_2 = Preference(first_name1 = "Jack", last_name1 = "", student_id = 12)
stud_12_pref_3 = Preference(first_name1 = "Fisher", last_name1 = "", student_id = 12)
stud_12_pref_4 = Preference(first_name1 = "Bob", last_name1 = "", student_id = 12)

session.add(student12)
session.add(stud_12_pref_1)
session.add(stud_12_pref_2)
session.add(stud_12_pref_3)
session.add(stud_12_pref_4)

session.commit()

student13 = Student(first_name = "Fisher", last_name = "")
stud_13_pref_1 = Preference(first_name1 = "Wilt", last_name1 = "", student_id = 13)
stud_13_pref_2 = Preference(first_name1 = "Manny", last_name1 = "", student_id = 13)
stud_13_pref_3 = Preference(first_name1 = "Tej", last_name1 = "", student_id = 13)
stud_13_pref_4 = Preference(first_name1 = "Jack", last_name1 = "", student_id = 13)

session.add(student13)
session.add(stud_13_pref_1)
session.add(stud_13_pref_2)
session.add(stud_13_pref_3)
session.add(stud_13_pref_4)

session.commit()

student14 = Student(first_name = "Wilt", last_name = "")
stud_14_pref_1 = Preference(first_name1 = "Rambus", last_name1 = "", student_id = 14)
stud_14_pref_2 = Preference(first_name1 = "Tej", last_name1 = "", student_id = 14)
stud_14_pref_3 = Preference(first_name1 = "Fred", last_name1 = "", student_id = 14)
stud_14_pref_4 = Preference(first_name1 = "Durant", last_name1 = "", student_id = 14)

session.add(student14)
session.add(stud_14_pref_1)
session.add(stud_14_pref_2)
session.add(stud_14_pref_3)
session.add(stud_14_pref_4)

session.commit()

student15 = Student(first_name = "Kareem", last_name = "")
stud_15_pref_1 = Preference(first_name1 = "Wilt", last_name1 = "", student_id = 15)
stud_15_pref_2 = Preference(first_name1 = "Fisher", last_name1 = "", student_id = 15)
stud_15_pref_3 = Preference(first_name1 = "Tej", last_name1 = "", student_id = 15)
stud_15_pref_4 = Preference(first_name1 = "Manny", last_name1 = "", student_id = 15)

session.add(student15)
session.add(stud_15_pref_1)
session.add(stud_15_pref_2)
session.add(stud_15_pref_3)
session.add(stud_15_pref_4)

session.commit()

student16 = Student(first_name = "Kobe", last_name = "")
stud_16_pref_1 = Preference(first_name1 = "Jack", last_name1 = "", student_id = 16)
stud_16_pref_2 = Preference(first_name1 = "Fred", last_name1 = "", student_id = 16)
stud_16_pref_3 = Preference(first_name1 = "Reggie", last_name1 = "", student_id = 16)
stud_16_pref_4 = Preference(first_name1 = "Tej", last_name1 = "", student_id = 16)

session.add(student16)
session.add(stud_16_pref_1)
session.add(stud_16_pref_2)
session.add(stud_16_pref_3)
session.add(stud_16_pref_4)

session.commit()

student17 = Student(first_name = "Shaq", last_name = "")
stud_17_pref_1 = Preference(first_name1 = "Frank", last_name1 = "", student_id = 17)
stud_17_pref_2 = Preference(first_name1 = "Fred", last_name1 = "", student_id = 17)
stud_17_pref_3 = Preference(first_name1 = "Curry", last_name1 = "", student_id = 17)
stud_17_pref_4 = Preference(first_name1 = "Gasol", last_name1 = "", student_id = 17)

session.add(student17)
session.add(stud_17_pref_1)
session.add(stud_17_pref_2)
session.add(stud_17_pref_3)
session.add(stud_17_pref_4)

session.commit()

student18 = Student(first_name = "Lebron", last_name = "")
stud_18_pref_1 = Preference(first_name1 = "Kareem", last_name1 = "", student_id = 18)
stud_18_pref_2 = Preference(first_name1 = "Joe", last_name1 = "", student_id = 18)
stud_18_pref_3 = Preference(first_name1 = "Manny", last_name1 = "", student_id = 18)
stud_18_pref_4 = Preference(first_name1 = "Frank", last_name1 = "", student_id = 18)

session.add(student18)
session.add(stud_18_pref_1)
session.add(stud_18_pref_2)
session.add(stud_18_pref_3)
session.add(stud_18_pref_4)

session.commit()

student19 = Student(first_name = "Curry", last_name = "")
stud_19_pref_1 = Preference(first_name1 = "Byron", last_name1 = "", student_id = 19)
stud_19_pref_2 = Preference(first_name1 = "Jordan", last_name1 = "", student_id = 19)
stud_19_pref_3 = Preference(first_name1 = "Worthy", last_name1 = "", student_id = 19)
stud_19_pref_4 = Preference(first_name1 = "Fred", last_name1 = "", student_id = 19)

session.add(student19)
session.add(stud_19_pref_1)
session.add(stud_19_pref_2)
session.add(stud_19_pref_3)
session.add(stud_19_pref_4)

session.commit()

student20 = Student(first_name = "Reggie", last_name = "")
stud_20_pref_1 = Preference(first_name1 = "Magic", last_name1 = "", student_id = 20)
stud_20_pref_2 = Preference(first_name1 = "Cooper", last_name1 = "", student_id = 20)
stud_20_pref_3 = Preference(first_name1 = "Rambus", last_name1 = "", student_id = 20)
stud_20_pref_4 = Preference(first_name1 = "Jordan", last_name1 = "", student_id = 20)

session.add(student20)
session.add(stud_20_pref_1)
session.add(stud_20_pref_2)
session.add(stud_20_pref_3)
session.add(stud_20_pref_4)

session.commit()

student21 = Student(first_name = "Worthy", last_name = "")
stud_21_pref_1 = Preference(first_name1 = "Jonathan", last_name1 = "", student_id = 21)
stud_21_pref_2 = Preference(first_name1 = "Tej", last_name1 = "", student_id = 21)
stud_21_pref_3 = Preference(first_name1 = "Fisher", last_name1 = "", student_id = 21)
stud_21_pref_4 = Preference(first_name1 = "Jerry", last_name1 = "", student_id = 21)

session.add(student21)
session.add(stud_21_pref_1)
session.add(stud_21_pref_2)
session.add(stud_21_pref_3)
session.add(stud_21_pref_4)

session.commit()

student22 = Student(first_name = "Moe", last_name = "")
stud_22_pref_1 = Preference(first_name1 = "Jonathan", last_name1 = "", student_id = 22)
stud_22_pref_2 = Preference(first_name1 = "Tej", last_name1 = "", student_id = 22)
stud_22_pref_3 = Preference(first_name1 = "Cooper", last_name1 = "", student_id = 22)
stud_22_pref_4 = Preference(first_name1 = "Magic", last_name1 = "", student_id = 22)

session.add(student22)
session.add(stud_22_pref_1)
session.add(stud_22_pref_2)
session.add(stud_22_pref_3)
session.add(stud_22_pref_4)

session.commit()

student23 = Student(first_name = "Jerry", last_name = "")
stud_23_pref_1 = Preference(first_name1 = "Jonathan", last_name1 = "", student_id = 23)
stud_23_pref_2 = Preference(first_name1 = "Lebron", last_name1 = "", student_id = 23)
stud_23_pref_3 = Preference(first_name1 = "Jordan", last_name1 = "", student_id = 23)
stud_23_pref_4 = Preference(first_name1 = "Kobe", last_name1 = "", student_id = 23)

session.add(student23)
session.add(stud_23_pref_1)
session.add(stud_23_pref_2)
session.add(stud_23_pref_3)
session.add(stud_23_pref_4)

session.commit()

student24 = Student(first_name = "Joe", last_name = "")
stud_24_pref_1 = Preference(first_name1 = "Frank", last_name1 = "", student_id = 24)
stud_24_pref_2 = Preference(first_name1 = "Jonathan", last_name1 = "", student_id = 24)
stud_24_pref_3 = Preference(first_name1 = "Wilt", last_name1 = "", student_id = 24)
stud_24_pref_4 = Preference(first_name1 = "Cooper", last_name1 = "", student_id = 24)

session.add(student24)
session.add(stud_24_pref_1)
session.add(stud_24_pref_2)
session.add(stud_24_pref_3)
session.add(stud_24_pref_4)

session.commit()

student25 = Student(first_name = "Nev", last_name = "")
stud_25_pref_1 = Preference(first_name1 = "Tej", last_name1 = "", student_id = 25)
stud_25_pref_2 = Preference(first_name1 = "Jonathan", last_name1 = "", student_id = 25)
stud_25_pref_3 = Preference(first_name1 = "Reggie", last_name1 = "", student_id = 25)
stud_25_pref_4 = Preference(first_name1 = "Kareem", last_name1 = "", student_id = 25)

session.add(student25)
session.add(stud_25_pref_1)
session.add(stud_25_pref_2)
session.add(stud_25_pref_3)
session.add(stud_25_pref_4)

session.commit()

student26 = Student(first_name = "James", last_name = "")
stud_26_pref_1 = Preference(first_name1 = "Fred", last_name1 = "", student_id = 26)
stud_26_pref_2 = Preference(first_name1 = "Tej", last_name1 = "", student_id = 26)
stud_26_pref_3 = Preference(first_name1 = "Kobe", last_name1 = "", student_id = 26)
stud_26_pref_4 = Preference(first_name1 = "Jonathan", last_name1 = "", student_id = 26)

session.add(student26)
session.add(stud_26_pref_1)
session.add(stud_26_pref_2)
session.add(stud_26_pref_3)
session.add(stud_26_pref_4)

session.commit()

student27 = Student(first_name = "Byron", last_name = "")
stud_27_pref_1 = Preference(first_name1 = "Horry", last_name1 = "", student_id = 27)
stud_27_pref_2 = Preference(first_name1 = "Manny", last_name1 = "", student_id = 27)
stud_27_pref_3 = Preference(first_name1 = "Jack", last_name1 = "", student_id = 27)
stud_27_pref_4 = Preference(first_name1 = "Worthy", last_name1 = "", student_id = 27)

session.add(student27)
session.add(stud_27_pref_1)
session.add(stud_27_pref_2)
session.add(stud_27_pref_3)
session.add(stud_27_pref_4)

session.commit()

student28 = Student(first_name = "Horry", last_name = "")
stud_28_pref_1 = Preference(first_name1 = "Lebron", last_name1 = "", student_id = 28)
stud_28_pref_2 = Preference(first_name1 = "Bob", last_name1 = "", student_id = 28)
stud_28_pref_3 = Preference(first_name1 = "Jack", last_name1 = "", student_id = 28)
stud_28_pref_4 = Preference(first_name1 = "Wilt", last_name1 = "", student_id = 28)

session.add(student28)
session.add(stud_28_pref_1)
session.add(stud_28_pref_2)
session.add(stud_28_pref_3)
session.add(stud_28_pref_4)

session.commit()

student29 = Student(first_name = "Gasol", last_name = "")
stud_29_pref_1 = Preference(first_name1 = "Cooper", last_name1 = "", student_id = 29)
stud_29_pref_2 = Preference(first_name1 = "Frank", last_name1 = "", student_id = 29)
stud_29_pref_3 = Preference(first_name1 = "Jack", last_name1 = "", student_id = 29)
stud_29_pref_4 = Preference(first_name1 = "Nev", last_name1 = "", student_id = 29)

session.add(student29)
session.add(stud_29_pref_1)
session.add(stud_29_pref_2)
session.add(stud_29_pref_3)
session.add(stud_29_pref_4)

session.commit()

student30 = Student(first_name = "Durant", last_name = "")
stud_30_pref_1 = Preference(first_name1 = "Fred", last_name1 = "", student_id = 30)
stud_30_pref_2 = Preference(first_name1 = "Tej", last_name1 = "", student_id = 30)
stud_30_pref_3 = Preference(first_name1 = "Magic", last_name1 = "", student_id = 30)
stud_30_pref_4 = Preference(first_name1 = "Lebron", last_name1 = "", student_id = 30)

session.add(student30)
session.add(stud_30_pref_1)
session.add(stud_30_pref_2)
session.add(stud_30_pref_3)
session.add(stud_30_pref_4)

session.commit()
