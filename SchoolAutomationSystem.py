#School Automation System 

students = [] #include students informations
teachers = [] #include teachers informations
login = None  

def title(value): # used this function with print for something like basics interfaces
    return "*"*20+" "+value+" "+20*"*"

def condition(text): # used this function for automatize our conditions or functions messages
    return "[condition] "+text

def MainMenu(): # Here is the Main Menu function which is calling other funtions with their conditions
    while True:
        print(title("MAIN MENU"))
        print("1) Student Registration")
        print("2) Teacher Registration")
        print("3) Student Login")
        print("4) Teacher Login")
        print("5) Exit")

        operation = input("Options: ")
        if operation == "1":
            studentRegister()
        elif operation == "2":
            teacherRegister()
        elif operation == "3":
            studentLogin()
        elif operation == "4":
            teacherLogin()
        elif operation == "5":
            break
        else:
            print("Please enter valid options..")

def studentRegister(): # Here is the Student Registration function which is saving student informations in student dictionary. That dictionary is saving in "students" list for saving each students.
    print(title("STUDENT REGISTRATION"))

    student = {}
    student['username']     = input("Username: ")
    student["password"]     = input("Password: ")
    student["name"]         = input("Name: ")
    student["surname"]      = input("Surname: ")
    student["school"]       = input("School: ")
    student["department"]   = input("Department: ")
    student["lectures"]     = []

    students.append(student)
    print(condition("Student Registered!"))

def teacherRegister(): # Here is the Teacher Registration function which is saving teacher informations in teacher dictionary. That dictionary is saving in "teachers" list for saving each teachers.
    print(title("TEACHER REGISTRATION"))

    teacher = {}
    teacher["username"] = input("Username: ")
    teacher["password"] = input("password: ")
    teachers.append(teacher)
    print(condition("Teacher Registered"))

def studentLogin(): # Here is the Student Login function which is controlling inputs username&password in students list if these infos equal calling studentMenu function, if its not try again student login.
    print(title("STUDENT LOGIN"))

    username = input("Username: ")
    password = input("Password: ")

    loginSucceed = False

    for student in students:
        if student['username'] == username and student["password"] == password:
            loginSucceed = True
            studentMenu(student)

    if not loginSucceed:
        print(condition("Incorrect username or password"))
        studentLogin()

def studentMenu(login):  # Here is the Student Menu function which is calling other funtions with their conditions

    while True:
        print(title("STUDENT MENU"))
        print("Welcome, "+login['name']+" "+login['surname'])
        print("1) Lectures")
        print("2) Grades")
        print("3) Addition Lecture")
        print("4) Drop Lecture")
        print("5) Exit")

        operation = input("Options: ")
        if operation == "1":
            Lectures(login)
        elif operation == "2":
            Grades(login)
        elif operation == "3":
            addLecture(login)
        elif operation == "4":
            removeLecture(login)
        elif operation == "5":
            break
        else:
            print("Please enter valid options")

def Lectures(login): # That function shows that student which lessons taken in the system. 
    print("Enroll lectures: ")
    for lecture in login["lectures"]:
        print("- "+lecture["Lecture Name"])

def Grades(login): # That function shows that each lecture grades. Logged students can see only their grades.
    print("Grades: ")
    for lecture in login["lectures"]:
        if lecture["not"] != None:
            print("- "+lecture["Lecture Name"]+" --> "+lecture["not"])
        else:
            print("- "+lecture["Lecture Name"]+" grade can not enter for this lecture ")

def addLecture(login): # That function provide, students can add their lectures
    lecture = input("lecture? ")
    login["lectures"].append({"Lecture Name": lecture, "not": None})

def removeLecture(login): # That function provide, students can delete their lectures 
    print("Remove lecture: ")
    lectureNo = 1
    for lecture in login["lectures"]:
        print(str(lectureNo)+") " + lecture["Lecture Name"])
        lectureNo+=1
    choose = input("Choose: ")
    del login["lectures"][int(choose)-1]


def teacherMenu(login): # Here is the Teacher Menu function which is calling other funtions with their conditions
        print(title("TEACHER MENU"))
        print("1) Students")
        print("2) Add new student")
        print("3) Remove student")
        print("4) Update lecture grades")
        print("5) Exit")

        operation = input("Options: ")
        if operation == "1":
            studentListe(login)
        elif operation == "2":
            studentAdd(login)
        elif operation == "3":
            studentDelete(login)
        elif operation == "4":
            UpdateGrades(login)
        elif operation == "5":
            break
        else:
            print("Please enter valid select! ")

def studentListe(login): # Teachers can see registered students list 
    print("Students:")
    for student in students:
        print(student["name"]+" "+student["surname"])

def studentAdd(login): # Teachers can add student in students list
    student = {}
    student['username'] = input("Username: ")
    student["password"] = input("Password: ")
    student["name"] = input("Name: ")
    student["surname"] = input("Surname: ")
    student["school"] = input("School: ")
    student["department"] = input("Department: ")
    student["lectures"] = []

    students.append(student)
    print(condition("Student Registered"))

def studentDelete(login): # Teachers can delete students in student list 
    print("Enter remove student name: ")
    studentNo = 1
    for student in students:
        print(str(studentNo) + ") " + student["name"])
        studentNo+= 1
    choose = input("Choose: ")
    del students[int(choose) - 1]

def UpdateGrades(login): # Teachers can update or add new grade for students lectures
    print("Select Student: ")
    studentNo = 1
    for student in students:
        print(str(studentNo) + ") " + student["name"])
        studentNo += 1
    choose = input("Choice: ")
    student = students[int(choose) - 1]

    print(student["name"]+" "+student["surname"]+" update grades: ")
    for lecture in student["lectures"]:
        oldGrade = 0
        if lecture["not"] != None:
            oldGrade = lecture["not"]
        print(lecture["Lecture Name"]+": "+str(oldGrade))
        newGrade = input("New Grade: ")
        if newGrade != "0":
            lecture["not"] = newGrade

def teacherLogin(): # Here is the Teacher Login function which is controlling inputs username&password in teachers list if these infos equal calling teacherMenu function, if its not try again teacher login.
    print(title("TEACHER LOGIN"))

    username = input("Username: ")
    password = input("password: ")

    loginSucceed = False

    for teacher in teachers:
        if teacher['username'] == username and teacher["password"] == password:
            loginSucceed = True
            teacherMenu(teacher)

    if not loginSucceed:
        print(condition("Username or password invalid!"))
        teacherLogin()
    else:
        MainMenu()

MainMenu()