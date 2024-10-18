import pandas as pd
import xml.etree.ElementTree as ET

# Parsowanie pliku XML
tree = ET.parse('dane.xml')
root = tree.getroot()

# Tworzenie listy słowników, aby konwertować dane do DataFrame
data = []
for person in root.findall('person'):
    name = person.find('name').text
    age = int(person.find('age').text)  # Konwersja na int
    city = person.find('city').text
    data.append({'name': name, 'age': age, 'city': city})

# Tworzenie DataFrame
df = pd.DataFrame(data)

# Filtrowanie danych, np. age > 30
filtered_df = df[df['age'] > 30]

print(filtered_df)
