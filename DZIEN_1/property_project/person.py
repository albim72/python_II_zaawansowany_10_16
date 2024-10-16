from datetime import datetime,time

class Person:
    def __init__(self,name,year,city):
        self._name = name
        self._year = year
        self.city = city
        self._desc = "uczestnik konkursu"
        self.howmany = 9

    def __repr__(self):
        return f"osoba: {self._name}, rok urodzenia: {self._year}, miasto: {self.city}"
