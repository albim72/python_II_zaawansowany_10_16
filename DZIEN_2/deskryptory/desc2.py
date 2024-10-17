class ReadOnly:
    def __init__(self,value):
        self.value = value
        
    def __get__(self, instance, owner):
        return self.value
    
    def __set__(self, instance, value):
        raise AttributeError("To jest tylko do ODCZYTU!")
    
class MClass:
    constant = ReadOnly(45)
