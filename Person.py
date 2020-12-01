from Birthday import Birthday


class Person:

    def __init__(self, name, birthday):
        self.__name = name
        self.__birthday = birthday

    def __str__(self):
        return f"({self.__name},{self.__birthday})"

    def toString(self):
        return f"{self.__name}'s birthday is on {self.__birthday.getDay()} {self.__birthday.formatMonth()} {self.__birthday.getYear()}"
