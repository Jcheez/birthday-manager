from FileController import FileController
from Birthday import Birthday
from Person import Person
from datetime import datetime
import calendar


class Main:
    file = FileController()

    @staticmethod
    def opening():
        print("verson 1.0")
        print("Welcome to the Birthday Manager")
        print("Type help to see a full list of commands")
        print("© Jcheez")
        print("")

    @staticmethod
    def errorMessage(reason):
        print("")
        print("Sudden termination")
        print(reason)
        print("Please try again")
        print("")

    @staticmethod
    def addPerson():
        """
        How this method works.

        1. Get the details of the person and birthdate
        2. Check that name is not blank and birthday are all numbers
        3. Gives a confirmation that data has been added.

        """
        print("")
        print("Adding a new person to the manager...")
        print("")
        name = input("Name of the person: ")
        day = input("Day of Birthdate: ")
        month = input("Month of Birthdate: ")
        year = input("Year of Birthdate: ")
        if name == "":
            Main.errorMessage("Reason: Name field cannot be blank.")
            raise Exception()
        try:
            day = int(day)
            month = int(month)
            year = int(year)
        except:
            Main.errorMessage(
                "Reason: non numbers entered into day, month or year.")
            raise ValueError()

        print(Main.file.addPerson(name, day, month, year))
        print("")

    @staticmethod
    def help():
        print("")
        print("help        --> See a full list of commands available")
        print("add         --> Add a person's birthday to the manager")
        print("remove      --> Remove a person's birthday from the manager")
        print("view all    --> View all the birthdays stored in the manager")
        print("filter      --> View all the birthdays filtered by a particular month")
        print("this month  --> View all birthdays that occur in the next month")
        print("quit        --> Quit the application")
        print("")

    @staticmethod
    def removePerson():
        print("")
        print("Remove a person from the manager...")
        name = input("Name of the person: ")
        if name == "":
            Main.errorMessage("Reason: Name field cannot be blank.")
            raise Exception()

        print(Main.file.removePerson(name))
        print("")

    @staticmethod
    def viewAllBirthdays():
        print("")
        print("Showing all birthdays...")
        print("")
        Main.file.viewNames()
        print("")

    @staticmethod
    def filterBirthdays():
        print("")
        print("Fitering birthdays...")
        month = input("Month which you will like to filter: ")
        print("")
        Main.file.filterBirthdays(month)
        print("")

    @staticmethod
    def filterNextMonthBirthdays():
        print("")
        print("Fitering this month's birthdays...")
        month_current = datetime.today().month
        print("")
        Main.file.filterBirthdays(calendar.month_name[month_current])
        print("")


default = True
firstOpen = True

while default:
    if firstOpen:
        Main.opening()
        firstOpen = False
    command = input("What would you like to access? ")

    if command == "help":
        Main.help()
    elif command == "add":
        run = True
        while run:
            try:
                Main.addPerson()
            except:
                pass
            else:
                run = False
    elif command == "remove":
        run = True
        while run:
            try:
                Main.removePerson()
            except:
                pass
            else:
                run = False
    elif command == "view all":
        Main.viewAllBirthdays()
    elif command == "filter":
        Main.filterBirthdays()
    elif command == "this month":
        Main.filterNextMonthBirthdays()
    elif command == "quit":
        default = False
        print("See you again")
    else:
        print("Command not found. Please try again")
