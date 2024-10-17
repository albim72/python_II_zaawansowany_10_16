class MetaAddder(type):
    def __new__(cls,name,bases,attrs):
        attrs['print_class_name'] = lambda self:print(f'jestem klasą: {self.__class__.__name__}')
        attrs['class_name'] = property(lambda self:self.__class__.__qualname__)
        return super().__new__(cls,name,bases,attrs)

class MojaKlasa(metaclass=MetaAddder):
    @property
    def class_name(self):
        return 7634563

class Druga(MojaKlasa):
    @property
    def class_name(self):
        return True

obj1 = MojaKlasa()
obj1.print_class_name()

# MojaKlasa.print_class_name()
print(obj1.class_name)

print("______________________________________")

obj2 = Druga()
obj2.print_class_name()
print(obj2.class_name)
