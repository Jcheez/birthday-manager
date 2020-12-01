from Birthday import Birthday
from Person import Person


class FileController:

    def __init__(self):
        self.__fileName = 'Birthdays.txt'

    def addPerson(self, personName, day, month, year):
        birthday = Birthday(day, month, year)
        person = Person(personName, birthday)
        file = open(self.__fileName, "a")
        file.write(person.__str__() + "\n")
        file.close()
        return f"{personName} successfully added"

    def removePerson(self, personName):
        found = False
        with open(self.__fileName, "r") as f:
            lines = f.readlines()
        with open(self.__fileName, "w") as f:
            for line in lines:
                if personName != self.formatString(line)[0]:
                    f.write(line)
                elif found:
                    f.write(line)
                else:
                    found = True
            f.close()
        if found:
            return f"{personName} successfully removed"
        else:
            return f"{personName} not found"

    def formatString(self, line):
        formatted = line.strip('\n').strip(" (").strip(")").split(",(")
        name = formatted[0]
        birthday = []
        for data in formatted[1].split(","):
            birthday.append(int(data))
        return (name, tuple(birthday))

    def viewNames(self):
        count = 0
        file = open(self.__fileName, "r")
        for line in file.readlines():
            print(self.formatString(line)[0])
            count += 1

        print(f"There are {count} names stored")
