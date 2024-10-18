import pandas as pd
import xml.etree.ElementTree as ET

# Tworzenie DataFrame z miastami i mieszkańcami
data = {'city': ['New York', 'New York', 'Los Angeles', 'Chicago', 'Chicago'],
        'name': ['John', 'Sarah', 'Alice', 'Bob', 'Charlie'],
        'age': [30, 28, 25, 35, 40]}
df = pd.DataFrame(data)

# Tworzenie głównego elementu XML
root = ET.Element('cities')

# Iteracja przez unikalne miasta
for city_name, city_group in df.groupby('city'):
    city = ET.SubElement(root, 'city', attrib={'name': city_name})
    
    # Dodanie mieszkańców do danego miasta
    for i, row in city_group.iterrows():
        person = ET.SubElement(city, 'person')
        name = ET.SubElement(person, 'name')
        name.text = row['name']
        age = ET.SubElement(person, 'age')
        age.text = str(row['age'])

# Zapis do pliku XML
tree = ET.ElementTree(root)
with open('output2.xml', 'wb') as file:
    tree.write(file)

print("Plik XML został utworzony jako 'output2.xml'.")
