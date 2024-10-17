from desc1 import Person

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
