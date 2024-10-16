class Character:
    def __init__(self, character_type, weapon):
        self.character_type = character_type
        self.weapon = weapon
    
    def render(self, position_x, position_y):
        # Wyświetla informacje o postaci oraz jej pozycję
        print(f"{self.character_type} with {self.weapon} at position ({position_x}, {position_y})")
