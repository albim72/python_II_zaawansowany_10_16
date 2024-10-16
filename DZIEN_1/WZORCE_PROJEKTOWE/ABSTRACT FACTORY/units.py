from abc import ABC, abstractmethod

# Interfejs samochodu
class Car(ABC):
    @abstractmethod
    def description(self) -> str:
        pass

# Interfejs silnika
class Engine(ABC):
    @abstractmethod
    def start(self) -> str:
        pass

# Interfejs baterii
class Battery(ABC):
    @abstractmethod
    def charge(self) -> str:
        pass
