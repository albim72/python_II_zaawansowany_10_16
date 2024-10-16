from abc import ABC, abstractmethod

# Interfejs jednostki
class Unit(ABC):
    @abstractmethod
    def attack(self):
        pass

# Interfejs fabryki jednostek
class UnitFactory(ABC):
    @abstractmethod
    def create_warrior(self) -> Unit:
        pass
    
    @abstractmethod
    def create_mage(self) -> Unit:
        pass
