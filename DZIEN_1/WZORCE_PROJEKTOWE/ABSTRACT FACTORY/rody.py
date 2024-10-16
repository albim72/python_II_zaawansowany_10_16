# Jednostki dla rodu Stark
class StarkWarrior(Unit):
    def attack(self):
        return "Stark Warrior attacks with a sword!"

class StarkMage(Unit):
    def attack(self):
        return "Stark Mage casts a winter spell!"

# Jednostki dla rodu Lannister
class LannisterWarrior(Unit):
    def attack(self):
        return "Lannister Warrior attacks with a spear!"

class LannisterMage(Unit):
    def attack(self):
        return "Lannister Mage casts a fire spell!"

# Jednostki dla rodu Targaryen
class TargaryenWarrior(Unit):
    def attack(self):
        return "Targaryen Warrior attacks with a dragon!"

class TargaryenMage(Unit):
    def attack(self):
        return "Targaryen Mage breathes fire!"
