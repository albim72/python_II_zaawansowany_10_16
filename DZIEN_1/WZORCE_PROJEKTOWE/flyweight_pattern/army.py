class Army:
    def __init__(self):
        self.characters = []

    def add_character(self, character_type, weapon, position_x, position_y):
        # Uzyskujemy obiekt postaci z fabryki pyłków
        character = CharacterFactory.get_character(character_type, weapon)
        # Dodajemy postać do armii z jej specyficznymi danymi
        self.characters.append((character, position_x, position_y))

    def render_army(self):
        # Wyświetla wszystkie postaci w armii
        for character, pos_x, pos_y in self.characters:
            character.render(pos_x, pos_y)
