import sqlite3
import sys

RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

from prettytable import PrettyTable


sys.stdout.write(RED)


def student(con, sql) :
    try :
        print("Choose your next action :")
        print("1. Enroll to Course")
        print("2. View information about Student")
        print("3. Drop all courses which choosen")
        print("4. Drop one course")
        print("5. My courses")
        print("6. Grades")
        x = int(input("Type here: "))
        if x == 1 :
            id = input("Enter your STUDENT_ID: ")
            con.execute("SELECT * FROM COURSE;")
            record = con.fetchall()
            t = PrettyTable(['Course code', 'Course name', 'Course ETC'])
            for list in record :
                t.add_row(list)
            print(t)
            code = int(input("Enter your choosen COURSE CODE: "))
            ins = "INSERT INTO ENROLL(STUDENT_ID, COURSE_CODE) VALUES(" + str(id) + ", " + str(code) + ");"
            con.execute(ins)
            sql.commit()
            print("Course successfully added")
        elif x == 2 :
            id = int(input("Type student ID: "))
            con.execute("SELECT * FROM STUDENT WHERE STUDENT_ID = " + str(id))
            student = con.fetchall()
            t = PrettyTable([])
            t.add_row(["Student's name: ", str(student[0][1])])
            t.add_row(["Student's surname: ", str(student[0][2])])
            t.add_row(["Student's gender: ", str(student[0][3])])
            t.add_row(["Student's birthday: ", str(student[0][4])])
            t.add_row(["Student's address: ", str(student[0][5])])
            t.add_row(["Student's phone: ", str(student[0][6])])
            t.add_row(["Student's email: ", str(student[0][7])])
            t.add_row(["Student's country: ", str(student[0][8])])
            t.add_row(["Student's nationality: ", str(student[0][9])])
            t.add_row(["Status: ", str(student[0][10])])
            t.add_row(["Student's graduate school: ", str(student[0][11])])
            t.add_row(["Grant type: ", str(student[0][12])])
            t.add_row(["Entry exam score: ", str(student[0][13])])
            t.add_row(["English level: ", str(student[0][14])])
            t.add_row(["Turkish level: ", str(student[0][15])])
            con.execute("SELECT FACULTY_NAME FROM STUDENT, FACULTY, SPECIALITY WHERE STUDENT_ID = " + str(student[0][16]) + " AND SPECIALITY.FACULTY_ID = FACULTY.FACULTY_ID AND SPECIALITY.SPECIALITY_ID = STUDENT.SPECIALITY_ID"
                        )
            t.add_row(["Student's faculty: ", con.fetchone()[0]])
            print(t)
        elif x == 3 :
            id = int(input("Type your ID for drop all courses: "))
            con.execute("DELETE FROM ENROLL WHERE STUDENT_ID = " + str(id) + ";")
            sql.commit()
            print("Succesfully dropped")
        elif x == 4 :
            id = int(input("Type your Id for drop course: "))
            code = int(input("Type your COURSE_CODE for drop this course: "))
            com = "DELETE FROM ENROLL WHERE STUDENT_ID = " + str(id) + " AND COURSE_CODE = " + str(code) + ";"
            con.execute(com)
            sql.commit()
            com = "DELETE FROM GRADES WHERE STUDENT_ID = " + str(id) + " AND COURSE_CODE = " + str(code) + ";"
            con.execute(com)
            sql.commit()
            print("Successfully dropped!")
        elif x == 5 :
            id = int(input("Type your ID for see your Enrolled course: "))
            code = "SELECT * FROM ENROLL WHERE STUDENT_ID = " + str(id) + ";"
            con.execute(code)
            record = con.fetchall()
            if len(record) == 0 :
                print("\nYou didn't choose a course yet!")
                return
            t = PrettyTable(['Course Code', 'Course Name', 'Course Credits', 'Price'])
            sum = 0
            sum_etc = 0
            for r in record :
                course_code = r[2]
                s = ("SELECT COURSE_NAME FROM COURSE WHERE COURSE_CODE = " + str(course_code) + ";")
                con.execute(s)
                d = con.fetchall()
                s = "SELECT COURSE_ETC FROM COURSE WHERE COURSE_CODE = " + str(course_code) + ";"
                con.execute(s)
                etc = con.fetchall()
                t.add_row([course_code, d[0][0], etc[0][0], str(int(etc[0][0] * 22000))])
                sum += int(etc[0][0]) * 22000
                sum_etc += int(etc[0][0])
            t.add_row(['', '', sum_etc, sum])
            print(t)
        else :
            id = input("Type your ID for see your grades: ")
            code = "SELECT COURSE_NAME, LETTER_GRADE FROM COURSE, GRADES WHERE GRADES.STUDENT_ID = " + str(id) + " AND COURSE.COURSE_CODE = GRADES.COURSE_CODE"
            con.execute(code)
            record = con.fetchall()
            t = PrettyTable(['Code name', 'Letter ID'])
            for list in record :
                t.add_row(list)
            print(t)
    except sqliteConnection as error :
        print("Error code", error)


def add(con, sql) :
    try :
        s_name = input("Type your name: ")
        s_surname = input("Type your surname: ")
        s_gender = input("Type your gender(male / female): ")
        s_birthday = input("Type your birthday: ")
        s_address = input("Type your address: ")
        s_phone = input("Type your phone: ")
        s_email = input("Type your email: ")
        s_country = input("Type your country: ")
        s_nationality = input("Type your nationality: ")
        s_status = input("Type your status (studying, graduated): ")
        s_graduate_school = input("Type your graduate school: ")
        turkish_level = 'A1'
        if s_graduate_school.__contains__('KTL') or s_graduate_school.__contains__("BIL") :
            turkish_level = 'B1'
        s_grant_type = input("Type your grant type: ")
        s_entry_exam_score = int(input("Type your entry exam score: "))
        s_english_lvl = input("Type your english level: ")
        specialist_id = int(input("Type your SPECIALITY_ID: "))
        s_advisor = input("Type your advisor's name: ")
        degree = input("Type your degree: ")
        s_gpa = float(input("Type your GPA: "))
        s_balance = int(input("Type your balance: "))
        club_id = int(input("Type your CLUB_ID: "))
        code = "INSERT INTO STUDENT(S_NAME, S_SURNAME, S_GENDER, S_BIRTHDAY, S_ADDRESS, S_PHONE, S_EMAIL, S_COUNTRY, S_NATIONALITY, STATUS, GRADUATE_SCHOOL, GRANT_TYPE, ENTRY_EXAM_SCORE, ENGLISH_LVL, TURKISH_LVL, SPECIALITY_ID, ADVISOR, DEGREE, GPA, BALANCE, CLUB_ID) VALUES("
        code += "'" + str(s_name) + "', "
        code += "'" + str(s_surname) + "', "
        code += "'" + str(s_gender) + "', "
        code += "'" + str(s_birthday) + "', "
        code += "'" + str(s_address) + "', "
        code += "'" + str(s_phone) + "', "
        code += "'" + str(s_email) + "', "
        code += "'" + str(s_country) + "', "
        code += "'" + str(s_nationality) + "', "
        code += "'" + str(s_status) + "', "
        code += "'" + str(s_graduate_school) + "', "
        code += "'" + str(s_grant_type) + "', "
        code += str(s_entry_exam_score) + ", "
        code += "'" + str(s_english_lvl) + "', "
        code += "'" + str(turkish_level) + "', "
        code += str(specialist_id) + ", "
        code += "'" + str(s_advisor) + "', "
        code += "'" + str(degree) + "', "
        code += str(s_gpa) + ", "
        code += str(s_balance) + ", "
        code += str(club_id)
        code += ");"
        con.execute(code)
        sql.commit()
        print("Congrats, succsessfully added!")
    except sqliteConnection as error :
        print("Error code", error)


def staff(con, sql) :
    try :
        print("Choose your next action")
        print("1. View information about Staff")
        print("2. Set Grade to Student")
        x = int(input("Type here: "))

        if x == 1 :
            id = int(input("Type staff id: "))
            con.execute("SELECT * FROM STAFF WHERE STAFF_ID = " + str(id) + ";")
            rec = con.fetchall()
            t = PrettyTable([])
            t.add_row(["Staff's name: ", str(rec[0][1])])
            t.add_row(["Staff's surname: ",  str(rec[0][2])])
            t.add_row(["Staff's gender: ", str(rec[0][3])])
            t.add_row(["Staff's email: ", str(rec[0][4])])
            t.add_row(["Staff's campus_block: ", str(rec[0][5])])
            t.add_row(["Staff's room: ", str(rec[0][6])])
            t.add_row(["Staff's course code: ", str(rec[0][7])])
            print(t)
        else :
            id = input("Type your id: ")
            code = "SELECT COURSE_NAME, S_NAME, S_SURNAME, LETTER_GRADE FROM COURSE, STAFF, ENROLL, STUDENT, GRADES WHERE STAFF_ID = " + str(id) + " AND STAFF.COURSE_CODE = COURSE.COURSE_CODE AND ENROLL.COURSE_CODE = COURSE.COURSE_CODE AND ENROLL.STUDENT_ID = STUDENT.STUDENT_ID AND GRADES.STUDENT_ID = STUDENT.STUDENT_ID  AND GRADES.COURSE_CODE = ENROLL.COURSE_CODE"
            con.execute(code)
            rec = con.fetchall()
            t = PrettyTable(['Course name', 'Student name', 'Student surname', 'Letter Grade'])
            for list in rec :
                t.add_row(list)
            print(t)
            while True :
                print("1. Set grade to student")
                print("2. Go back")
                x = int(input("Type your choice here: "))
                if x == 2 :
                    break
                id = int(input("Type student's id: "))
                grade = input("Student's grade: ")
                code = "UPDATE GRADES SET LETTER_GRADE = '" + str(grade) + "' WHERE STUDENT_ID = " + str(id) + ";"

                con.execute(code)
                sql.commit();
    except sqliteConnection as error :
        print("Error code", error)


def add2(con, sql) :
    try :
        st_name = input("Type your name: ")
        st_surname = input("Type your surname: ")
        st_gender = input("Type your gender: ")
        st_email = input("Type your email: ")
        st_block = input("Type your block: ")
        st_room = input("Type your room: ")
        st_course = input("Type your COURSE_CODE which your instruct: ")
        code = "INSERT INTO STAFF(STAFF_NAME, STAFF_SURNAME, GENDER, EMAIL, CAMPUS_BLOCK, BLOCK_ROOM, COURSE_CODE) VALUES("
        code += "'" + str(st_name) + "', "
        code += "'" + str(st_surname) + "', "
        code += "'" + str(st_gender) + "', "
        code += "'" + str(st_email) + "', "
        code += "'" + str(st_block) + "', "
        code += str(st_room) + ", "
        code += str(st_course) + ")"
        con.execute(code)
        sql.commit()
    except sqliteConnection as error:
        print("Error code", error)


try :
    sqliteConnection = sqlite3.connect('/home/alisher/Рабочий стол/codehandler/project_dbms/PROJECT_0')
    cursor = sqliteConnection.cursor()
    print("Hello, Welcome to Database of SDU university!")
    while True :
        print()
        print("Type number of your choice")
        print("1. Student") # ready
        print("2. Staff") # ready
        print("3. Add new Student") # ready
        print("4. Add new Staff") # ready
        x = int(input("Type here: "))
        if x == 1 :
            student(cursor, sqliteConnection)
        elif x == 2 :
            staff(cursor, sqliteConnection)
        elif x == 3 :
            add(cursor, sqliteConnection)
        else :
            add2(cursor, sqliteConnection)

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")