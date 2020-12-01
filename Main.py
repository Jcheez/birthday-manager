from FileController import FileController
from Birthday import Birthday
from Person import Person


class Main:
    file = FileController()

    @staticmethod
    def opening():
        print("Welcome to the Birthday Manager")
        print("Type help to see a full list of commands")
        print("© Jcheez")
        print("")
        print("Below are the people who are currently stored")
        Main.file.viewNames()

    @staticmethod
    def addPerson():
        print("Adding a new person to the manager...")
        name = input("Name of the person: ")
        day = input("Day of Birthdate: ")
        month = input("Month of Birthdate: ")
        year = input("Year of Birthdate: ")
        try:
            day = int(day)
            month = int(month)
            year = int(year)
        except:
            print("Sudden termination")
            print("Reason: non numbers entered into day, month or year.")
            print("Please try again")
            print("")
            raise TypeError()

        print(Main.file.addPerson(name, day, month, year))

    @staticmethod
    def help():
        print("help --> See a full list of commands available")
        print("add  --> Add a person's birthday to the manager")
        print("q    --> Quit the application")


default = True
firstOpen = True

while default:
    if firstOpen:
        Main.opening()
        firstOpen = False
    command = input("What would you like to access? ")

    if command == "help":
        Main.help()
    elif command == "b":
        try:
            Main.addPerson()
        except TypeError:
            Main.addPerson()
    elif command == "q":
        default = False
        print("See you again")
    else:
        print("Command not found. Please try again")
