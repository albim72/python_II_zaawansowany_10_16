from xml.dom.minidom import Document

# Tworzenie nowego dokumentu XML
def create_xml_file(file_path):
    # Tworzenie obiektu dokumentu
    doc = Document()

    # Tworzenie elementu głównego
    root = doc.createElement('data')
    doc.appendChild(root)

    # Lista danych do dodania
    people = [
        {'name': 'John', 'age': '30', 'city': 'New York'},
        {'name': 'Alice', 'age': '25', 'city': 'Los Angeles'},
        {'name': 'Bob', 'age': '35', 'city': 'Chicago'}
    ]

    # Iteracja przez listę ludzi
    for person in people:
        person_element = doc.createElement('person')
        
        name_element = doc.createElement('name')
        name_element.appendChild(doc.createTextNode(person['name']))
        person_element.appendChild(name_element)

        age_element = doc.createElement('age')
        age_element.appendChild(doc.createTextNode(person['age']))
        person_element.appendChild(age_element)

        city_element = doc.createElement('city')
        city_element.appendChild(doc.createTextNode(person['city']))
        person_element.appendChild(city_element)

        root.appendChild(person_element)

    # Zapis do pliku XML
    with open(file_path, 'w') as file:
        file.write(doc.toprettyxml(indent='  '))

# Użycie funkcji do tworzenia pliku XML
create_xml_file('new_data.xml')
print("Plik XML został utworzony jako 'new_data.xml'.")
