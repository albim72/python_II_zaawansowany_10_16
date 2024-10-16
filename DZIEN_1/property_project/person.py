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

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,new_name):
        self._name = new_name

    @property
    def age(self):
        value = datetime.now().year - self._year
        age_ = value + self.howmany
        return value, age_

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self,times):
        newyear, month = times
        self._year = newyear + month/12

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self,newcity):
        self._city = newcity

    @property
    def policz(self):
        return 5*self._x

    @policz.setter
    def policz(self,x):
        self._x = x








