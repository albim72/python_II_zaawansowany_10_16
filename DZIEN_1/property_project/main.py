from person import Person

p = Person("Jacek",1976,"Lublin")
print(p)
print(p.name)
p.name = "Jarek"
print(p.name)

print(p.age)
print(f"wiek ososby: {p.age[0]} lat")
print(f"wiek osoby za {p.howmany} lat - {p.age[1]} lat")

print(p.year)

p.year = 1970,7
print(p.year)

print(p.city)
