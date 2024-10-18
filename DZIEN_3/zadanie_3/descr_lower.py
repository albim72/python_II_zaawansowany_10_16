class LowercaseString:
    def __init__(self, name):
        self.name = name
        self._value = ""

    def __get__(self, instance, owner):
        print(f"Getting '{self.name}': '{self._value}'")
        return self._value

    def __set__(self, instance, value):
        print(f"Setting '{self.name}' to '{value}' (converted to lowercase)")
        self._value = value.lower()

    def __delete__(self, instance):
        print(f"Deleting '{self.name}'")
        self._value = ""

class User:
    username = LowercaseString("username")

# Przykładowe użycie
user = User()
user.username = "JohnDoe"  # Ustawianie wartości
print(user.username)         # Pobieranie wartości
del user.username            # Usuwanie wartości
print(user.username)         # Pobieranie wartości
