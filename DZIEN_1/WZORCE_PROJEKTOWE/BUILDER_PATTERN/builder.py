from abc import ABC, abstractmethod

class Builder(ABC):
    @property
    @abstractmethod
    def product(self):
        pass
    
    @abstractmethod
    def produce_part_a(self):
        pass

    @abstractmethod
    def produce_part_b(self):
        pass

    @abstractmethod
    def produce_part_c(self):
        pass
