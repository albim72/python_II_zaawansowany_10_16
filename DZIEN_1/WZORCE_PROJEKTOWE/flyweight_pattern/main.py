if __name__ == "__main__":
    army = Army()

    # Dodajemy postacie do armii
    army.add_character("Knight", "Sword", 10, 20)
    army.add_character("Knight", "Sword", 15, 25)
    army.add_character("Archer", "Bow", 50, 60)
    army.add_character("Archer", "Bow", 55, 65)
    army.add_character("Mage", "Staff", 30, 40)

    # Renderowanie armii
    army.render_army()
