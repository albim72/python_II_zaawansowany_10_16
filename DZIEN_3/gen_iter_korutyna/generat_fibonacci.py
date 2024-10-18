import math

# Funkcja sprawdzająca, czy liczba jest liczbą pierwszą
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Generator liczb Fibonacciego z opcjonalnym filtrowaniem liczb pierwszych
def fibonacci_generator(prime_only=False):
    a, b = 0, 1
    while True:
        if prime_only:
            if is_prime(b):
                yield b
        else:
            yield b
        a, b = b, a + b

# Użycie:
# 1. Standardowy generator liczb Fibonacciego
fib_gen = fibonacci_generator()

print("Pierwsze 10 liczb Fibonacciego:")
for _ in range(10):
    print(next(fib_gen), end=", ")

print("\n\nPierwsze 10 liczb pierwszych z ciągu Fibonacciego:")
# 2. Generator liczb pierwszych w ciągu Fibonacciego
prime_fib_gen = fibonacci_generator(prime_only=True)

for _ in range(10):
    print(next(prime_fib_gen), end=", ")
