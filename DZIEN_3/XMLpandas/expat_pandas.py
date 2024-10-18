import pandas as pd
import xml.parsers.expat

# Lista do przechowywania danych
data = []

# Funkcje do obsługi zdarzeń parsera
def start_element(name, attrs):
    global current_element
    current_element = {}

def end_element(name):
    if name == 'person':
        data.append(current_element)

def char_data(data_char):
    if current_element is not None:
        if 'name' not in current_element:
            current_element['name'] = data_char
        elif 'age' not in current_element:
            current_element['age'] = data_char
        elif 'city' not in current_element:
            current_element['city'] = data_char

# Inicjalizacja parsera
parser = xml.parsers.expat.ParserCreate()
parser.StartElementHandler = start_element
parser.EndElementHandler = end_element
parser.CharacterDataHandler = char_data

# Wczytanie pliku XML
with open('data.xml', 'r') as file:
    xml_data = file.read()
    parser.Parse(xml_data)

# Tworzenie DataFrame z zebranych danych
df = pd.DataFrame(data)

# Wyświetlanie DataFrame
print(df)
