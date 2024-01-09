import requests

from dateSheet import getDateSheet
from loginAction import loginAction
from perInfo import getPerInfo
from seatingPlan import getSeatingPlan
from examMarks import getExamMarks
from examGrades import getExamGrades
from cgpa import getCgpa

# Main Menu

def mainMenu():
    mainMenu = """\nOptions
    \t1. DateSheet
    \t2. Seating Plan
    \t3. Marks
    \t4. Personal Info (Beta Testing)
    \t5. Grades
    \t6. CGPA
    \t7. Exit"""

    print(mainMenu)

    while True:
        print("\nChoose An Option: ", end="")
        option = int(input())

        if option == 1:
            print("\nGetting DateSheet...\n")
            try:
                getDateSheet(session)
            except:
                print("Something went wrong. Please try again later.")
        elif option == 2:
            print("\nGetting Seating Plan...\n")
            try:
                getSeatingPlan(session)
            except:
                print("Something went wrong. Please try again later.")
        elif option == 3:
            print("\nGetting Marks...\n")
            getExamMarks(session)
        elif option == 4:
            print("\nGetting Personal Info...\n")
            getPerInfo(session)
        elif option == 5:
            print("\nGetting Grades...\n")
            getExamGrades(session)
        elif option == 6:
            print("\nGetting CGPA...\n")
            getCgpa(session)        
        elif option == 7:
            print("\nExitting Program...\n")
            break

while True:

    session = requests.Session()

    enrolNum = input("Enter Roll Number: ")
    passWd = input("Enter Password/PIN: ")

    session, logSuccess = loginAction(enrolNum, passWd, session)

    if logSuccess == 1:
        print("\nLogin Successful !")
        mainMenu()
        break
    elif logSuccess == 0:
        print("\nInvalid Password !\n")
        session.cookies.clear()
    else:
        print("\nSomething Went Wrong !\n")
        session.cookies.clear()

