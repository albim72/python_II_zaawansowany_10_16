# Product: Klasa Kawa
class Kawa:
    def __init__(self):
        self.rodzaj = None
        self.mleko = False
        self.rodzaj_mleka = None
        self.syrop = None
        self.cukier = 1
        self.rozmiar = 'mała'

    def __str__(self):
        return (f"Kawa: {self.rodzaj}, Rozmiar: {self.rozmiar}, Mleko: {self.mleko if not self.rodzaj_mleka else self.rodzaj_mleka}, "
                f"Syrop: {self.syrop if self.syrop else 'brak'}, Cukier: {self.cukier} łyżeczki")

    def oblicz_cene(self):
        cena = 5  # bazowa cena kawy
        if self.rozmiar == 'duża':
            cena += 2
        if self.mleko or self.rodzaj_mleka:
            cena += 1
        if self.syrop:
            cena += 1
        if self.cukier > 1:
            cena += 0.5 * (self.cukier - 1)  # każdy kolejny cukier kosztuje dodatkowo
        return round(cena, 2)


# Builder: Abstrakcyjny interfejs budowniczego
class Builder:
    def set_rodzaj(self, rodzaj):
        pass

    def set_mleko(self, mleko):
        pass

    def set_rodzaj_mleka(self, rodzaj_mleka):
        pass

    def set_syrop(self, syrop):
        pass

    def set_cukier(self, cukier):
        pass

    def set_rozmiar(self, rozmiar):
        pass

    def get_kawa(self):
        pass


# ConcreteBuilder: Konkretny budowniczy
class KawaBuilder(Builder):
    def __init__(self):
        self.kawa = Kawa()

    def set_rodzaj(self, rodzaj):
        self.kawa.rodzaj = rodzaj

    def set_mleko(self, mleko):
        self.kawa.mleko = mleko

    def set_rodzaj_mleka(self, rodzaj_mleka):
        self.kawa.rodzaj_mleka = rodzaj_mleka

    def set_syrop(self, syrop):
        self.kawa.syrop = syrop

    def set_cukier(self, cukier):
        self.kawa.cukier = cukier

    def set_rozmiar(self, rozmiar):
        self.kawa.rozmiar = rozmiar

    def get_kawa(self):
        return self.kawa


# Director: Klasa odpowiedzialna za koordynację procesu budowania
class Director:
    def __init__(self, builder):
        self.builder = builder

    def make_espresso(self):
        self.builder.set_rodzaj("Espresso")
        self.builder.set_rozmiar("mała")
        self.builder.set_mleko(False)

    def make_latte(self):
        self.builder.set_rodzaj("Latte")
        self.builder.set_rozmiar("duża")
        self.builder.set_mleko(True)
        self.builder.set_syrop("waniliowy")
        self.builder.set_cukier(2)

    def make_cappuccino(self):
        self.builder.set_rodzaj("Cappuccino")
        self.builder.set_rozmiar("średnia")
        self.builder.set_rodzaj_mleka("migdałowe")
        self.builder.set_cukier(3)

    def get_kawa(self):
        return self.builder.get_kawa()


# Przykład użycia
if __name__ == "__main__":
    # Budowanie espresso
    espresso_builder = KawaBuilder()
    director = Director(espresso_builder)
    director.make_espresso()
    kawa1 = director.get_kawa()
    print(kawa1)
    print(f"Cena: {kawa1.oblicz_cene()} zł\n")

    # Budowanie latte
    latte_builder = KawaBuilder()
    director = Director(latte_builder)
    director.make_latte()
    kawa2 = director.get_kawa()
    print(kawa2)
    print(f"Cena: {kawa2.oblicz_cene()} zł\n")

    # Budowanie cappuccino
    cappuccino_builder = KawaBuilder()
    director = Director(cappuccino_builder)
    director.make_cappuccino()
    kawa3 = director.get_kawa()
    print(kawa3)
    print(f"Cena: {kawa3.oblicz_cene()} zł\n")
