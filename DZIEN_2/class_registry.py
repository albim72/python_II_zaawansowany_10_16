class ClassRegistry(type):
    registry = {}

    def __new__(cls,name,bases,attrs):
        new_class = super().__new__(cls,name,bases,attrs)
        cls.registry[name] = new_class
        return new_class

    @classmethod
    def get_registrated_classes(cls):
        return cls.registry

    @classmethod
    def get_bases_classes(cls):
        return cls.__bases__


class BaseClass(metaclass=ClassRegistry):
    pass

class FirstClass(BaseClass):
    pass

class SecondClass(BaseClass):
    pass

class ThirdClass(BaseClass):
    pass

class Empty(metaclass=ClassRegistry):
    pass

print(f'wynik działania metaklasy ClassRegistry:\n{ClassRegistry.get_registrated_classes()}')
print(f'przodkowie klasy:\n{ClassRegistry.get_bases_classes()}')

# f = FirstClass()
# print(f.get_bases_classes())


