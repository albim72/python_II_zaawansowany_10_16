def prime_generator():
    """Generator zwracający kolejne liczby pierwsze."""
    primes = []  # Lista przechowująca wszystkie znalezione liczby pierwsze
    num = 2  # Zaczynamy od 2, pierwszej liczby pierwszej

    while True:
        is_prime = True
        # Sprawdzamy, czy num jest liczbą pierwszą
        for prime in primes:
            if prime * prime > num:
                break  # Optymalizacja: wystarczy sprawdzać do pierwiastka z num
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)  # Dodajemy liczbę do listy liczb pierwszych
            yield num  # Zwracamy liczbę pierwszą
        num += 1  # Przechodzimy do kolejnej liczby
# Generujemy pierwsze 10 liczb pierwszych:
prime_gen = prime_generator()
for _ in range(10):
    print(next(prime_gen))
