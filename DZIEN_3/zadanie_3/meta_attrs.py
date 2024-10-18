class RequiredAttributesMetaclass(type):
    # Lista atrybutów, które muszą być obecne w każdej klasie pochodnej
    required_attributes = ['name', 'execute']

    def __new__(cls, name, bases, dct):
        # Sprawdzamy, czy wszystkie wymagane atrybuty są obecne, pomijając klasę bazową
        if name != 'BaseCommand':  # Added this condition to skip checks for BaseCommand
            for attr in cls.required_attributes:
                if attr not in dct:
                    raise TypeError(f"Class '{name}' must implement attribute '{attr}'")

        return super().__new__(cls, name, bases, dct)


# Przykładowa klasa bazowa używająca metaklasy
class BaseCommand(metaclass=RequiredAttributesMetaclass):
    pass


# Klasa poprawnie implementująca wymagane atrybuty
class MyCommand(BaseCommand):
    name = "MyCommand"

    def execute(self):
        print(f"{self.name} is executed")


# Klasa, która nie implementuje wymaganych atrybutów - zgłosi błąd
class IncompleteCommand(BaseCommand):
    pass


# Przykładowe użycie
print("prawidłowe użycie")
cmd = MyCommand()
cmd.execute()
