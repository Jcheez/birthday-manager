import calendar


class Birthday:

    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year

    def __str__(self):
        return f"({self.__day},{self.__month},{self.__year})"

    def getDay(self):
        """
        Function to get the day of the birthday.

        @Return
        --> integer
        """
        return self.__day

    def getMonth(self):
        """
        Function to get the month of the birthday.

        @Return
        --> Integer
        """
        return self.__month

    def getYear(self):
        """
        Function to get the year of the birthday.

        @Return
        --> integer
        """
        return self.__year

    def formatMonth(self):
        """
        Function to get the month of the birthday in string.

        @Return
        --> String
        """
        return calendar.month_name[self.__month]
