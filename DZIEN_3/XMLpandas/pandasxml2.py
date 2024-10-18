import pandas as pd
import xml.etree.ElementTree as ET

# Parsowanie pliku XML
tree = ET.parse('dane.xml')
root = tree.getroot()

# Tworzenie listy słowników, wybierając tylko konkretne pola
data = []
for person in root.findall('person'):
    name = person.find('name').text
    city = person.find('city').text
    data.append({'name': name, 'city': city})

# Tworzenie DataFrame z wybranych pól
df = pd.DataFrame(data)

print(df)
