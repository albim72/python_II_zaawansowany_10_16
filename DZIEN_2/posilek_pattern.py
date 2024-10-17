# Metaklasa do kontroli kategorii składników
class SkładnikiMeta(type):
    dozwolone_kategorie = ['białko', 'węglowodany', 'tłuszcze']

    def __new__(cls, name, bases, attrs):
        # Sprawdza, czy kategoria składnika jest dozwolona, 
        # ale tylko jeśli atrybut 'kategoria' jest zdefiniowany
        # This change ensures that the check for 'kategoria' only happens 
        # if the attribute is actually defined in the class.
        if 'kategoria' in attrs and attrs.get('kategoria') not in cls.dozwolone_kategorie:
            raise ValueError(f"Kategoria {attrs.get('kategoria')} nie jest dozwolona.")
        return super().__new__(cls, name, bases, attrs)

# Klasa abstrakcyjna składnika
class Składnik(metaclass=SkładnikiMeta):
    def __init__(self, nazwa, kalorie, tłuszcz, białko, węglowodany):
        self.nazwa = nazwa
        self.kalorie = kalorie
        self.tłuszcz = tłuszcz
        self.białko = białko
        self.węglowodany = węglowodany

    def __str__(self):
        return f"{self.nazwa}: {self.kalorie} kcal, {self.tłuszcz}g tłuszczu, {self.białko}g białka, {self.węglowodany}g węglowodanów."


# Fabryka abstrakcyjna do komponowania posiłków
class PosiłekFactory:
    def dodaj_składnik(self, składnik):
        raise NotImplementedError

    def oblicz_wartości_odżywcze(self):
        raise NotImplementedError

# Klasy składników
class Białko(Składnik):
    kategoria = 'białko'

class Węglowodany(Składnik):
    kategoria = 'węglowodany'

class Tłuszcze(Składnik):
    kategoria = 'tłuszcze'

# Fabryka posiłków (konkretny posiłek)
class Śniadanie(PosiłekFactory):
    def __init__(self):
        self.składniki = []

    def dodaj_składnik(self, składnik):
        self.składniki.append(składnik)

    def oblicz_wartości_odżywcze(self):
        kalorie = sum([składnik.kalorie for składnik in self.składniki])
        tłuszcz = sum([składnik.tłuszcz for składnik in self.składniki])
        białko = sum([składnik.białko for składnik in self.składniki])
        węglowodany = sum([składnik.węglowodany for składnik in self.składniki])
        return {
            "kalorie": kalorie,
            "tłuszcz": tłuszcz,
            "białko": białko,
            "węglowodany": węglowodany
        }

# Fabryka dla innych posiłków
class Obiad(PosiłekFactory):
    def __init__(self):
        self.składniki = []

    def dodaj_składnik(self, składnik):
        self.składniki.append(składnik)

    def oblicz_wartości_odżywcze(self):
        kalorie = sum([składnik.kalorie for składnik in self.składniki])
        tłuszcz = sum([składnik.tłuszcz for składnik in self.składniki])
        białko = sum([składnik.białko for składnik in self.składniki])
        węglowodany = sum([składnik.węglowodany for składnik in self.składniki])
        return {
            "kalorie": kalorie,
            "tłuszcz": tłuszcz,
            "białko": białko,
            "węglowodany": węglowodany
        }

# Testowanie systemu
def komponuj_posiłek():
    # Tworzymy składniki
    jajko = Białko(nazwa="Jajko", kalorie=155, tłuszcz=11, białko=13, węglowodany=1.1)
    chleb = Węglowodany(nazwa="Chleb", kalorie=265, tłuszcz=3.2, białko=9, węglowodany=49)
    masło = Tłuszcze(nazwa="Masło", kalorie=717, tłuszcz=81, białko=0.9, węglowodany=0.1)

    # Komponujemy śniadanie
    śniadanie = Śniadanie()
    śniadanie.dodaj_składnik(jajko)
    śniadanie.dodaj_składnik(chleb)
    śniadanie.dodaj_składnik(masło)

    # Wyświetlamy składniki
    print("Składniki śniadania:")
    for składnik in śniadanie.składniki:
        print(składnik)

    # Obliczamy wartości odżywcze
    wartości = śniadanie.oblicz_wartości_odżywcze()
    print("\nWartości odżywcze śniadania:")
    print(f"Kalorie: {wartości['kalorie']} kcal")
    print(f"Tłuszcz: {wartości['tłuszcz']}g")
    print(f"Białko: {wartości['białko']}g")
    print(f"Węglowodany: {wartości['węglowodany']}g")

# Uruchamiamy komponowanie posiłku
komponuj_posiłek()
