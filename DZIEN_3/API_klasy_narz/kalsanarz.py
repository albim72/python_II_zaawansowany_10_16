class StringUtils:
    @staticmethod
    def to_uppercase(text: str) -> str:
        """Konwertuje ciąg na wielkie litery."""
        return text.upper()

    @staticmethod
    def reverse_string(text: str) -> str:
        """Odwraca kolejność znaków w ciągu."""
        return text[::-1]

    @staticmethod
    def is_palindrome(text: str) -> bool:
        """Sprawdza, czy dany ciąg jest palindromem."""
        return text == text[::-1]


# Przykłady użycia:
print(StringUtils.to_uppercase("python"))  # Output: PYTHON
print(StringUtils.reverse_string("python"))  # Output: nohtyp
print(StringUtils.is_palindrome("madam"))  # Output: True
