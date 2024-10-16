class CharacterFactory:
    _characters = {}

    @staticmethod
    def get_character(character_type, weapon):
        # Sprawdza, czy istnieje już obiekt postaci o zadanym typie
        key = (character_type, weapon)
        if key not in CharacterFactory._characters:
            # Jeśli nie istnieje, twórz nowy i dodaj do fabryki
            CharacterFactory._characters[key] = Character(character_type, weapon)
        return CharacterFactory._characters[key]
