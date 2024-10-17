from desc1 import Person
from desc2 import MClass

#przykład desc1
print("przykład desc1")
try:
    p = Person("Jan",56)
    print(p.name)
    print(p.age)

    p.age = "szesnaście"
    print(p.age)
except TypeError as te:
    print(te)

#przykład desc2
print("przykład desc2")
try:
    ob = MClass()
    print(ob.constant)
    ob.constant = 900
except AttributeError as ae:
    print(ae)
