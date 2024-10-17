class Typed:
    def __init__(self,typ):
        self.typ = typ
        
    def __set_name__(self, owner, name):
        self.name = name
        
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if not isinstance(value,self.typ):
            raise TypeError(f"Oczekiwano wartości typu: {self.typ}")
        instance.__dict__[self.name] = value
        
class Person:
    name = Typed(str)
    age = Typed(int)
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
