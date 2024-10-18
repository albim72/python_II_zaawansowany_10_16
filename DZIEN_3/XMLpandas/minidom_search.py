import pandas as pd
from xml.dom import minidom

# Funkcja do odczytu pliku XML i konwersji na DataFrame
def read_xml_to_dataframe(file_path):
    # Parsowanie pliku XML
    doc = minidom.parse(file_path)
    
    # Znalezienie wszystkich elementów 'person'
    persons = doc.getElementsByTagName('person')
    
    # Lista do przechowywania danych
    data = []
    
    # Iteracja przez elementy 'person'
    for person in persons:
        name = person.getElementsByTagName('name')[0].firstChild.nodeValue
        age = person.getElementsByTagName('age')[0].firstChild.nodeValue
        city = person.getElementsByTagName('city')[0].firstChild.nodeValue
        
        # Dodawanie danych do listy
        data.append({'name': name, 'age': age, 'city': city})
    
    # Tworzenie DataFrame z zebranych danych
    df = pd.DataFrame(data)
    
    return df

# Użycie funkcji do wczytania danych
df = read_xml_to_dataframe('data.xml')
print(df)
