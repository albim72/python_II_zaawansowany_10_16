import pandas as pd
import xml.etree.ElementTree as ET

# Tworzenie prostego DataFrame
data = {'name': ['John', 'Alice', 'Bob'],
        'age': [30, 25, 35],
        'city': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Tworzenie głównego elementu XML
root = ET.Element('data')

# Iteracja przez DataFrame i tworzenie struktury XML
for i, row in df.iterrows():
    person = ET.SubElement(root, 'person')
    name = ET.SubElement(person, 'name')
    name.text = row['name']
    age = ET.SubElement(person, 'age')
    age.text = str(row['age'])
    city = ET.SubElement(person, 'city')
    city.text = row['city']

# Zapis do pliku XML
tree = ET.ElementTree(root)
with open('output1.xml', 'wb') as file:
    tree.write(file)

print("Plik XML został utworzony jako 'output1.xml'.")
