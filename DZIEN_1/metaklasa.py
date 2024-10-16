class MojaMeta(type):
    def __new__(cls,clsnames,superclasses,attrs):
        print(f" ______________ {cls.__class__.__name__} __________________")
        print(f"nazwa klasy: {clsnames}")
        print(f"klasy dziedziczone: {superclasses}")
        print(f"słownik atrybutów klas: {attrs}")
        return type.__new__(cls,clsnames,superclasses,attrs)

    def jedynka(cls):
        return 1

class S:
    pass

class F:
    pass

class Specjalna(S,metaclass=MojaMeta):
    pass

class B(Specjalna):
    pass

class C(F,B):
    @property
    def info(self):
        print("abc...")

# cf = C()
# print(cf.jedynka())

cg = C
print(cg.jedynka())
