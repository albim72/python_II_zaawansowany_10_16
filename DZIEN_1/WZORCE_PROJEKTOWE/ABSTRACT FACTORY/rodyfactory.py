# Fabryka jednostek dla rodu Stark
class StarkFactory(UnitFactory):
    def create_warrior(self) -> Unit:
        return StarkWarrior()
    
    def create_mage(self) -> Unit:
        return StarkMage()

# Fabryka jednostek dla rodu Lannister
class LannisterFactory(UnitFactory):
    def create_warrior(self) -> Unit:
        return LannisterWarrior()
    
    def create_mage(self) -> Unit:
        return LannisterMage()

# Fabryka jednostek dla rodu Targaryen
class TargaryenFactory(UnitFactory):
    def create_warrior(self) -> Unit:
        return TargaryenWarrior()
    
    def create_mage(self) -> Unit:
        return TargaryenMage()
