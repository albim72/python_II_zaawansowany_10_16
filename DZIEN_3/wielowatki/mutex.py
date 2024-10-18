import threading

# Wspólny zasób
licznik = 0
licznik_lock = threading.Lock()

def zwieksz_licznik():
    global licznik
    for _ in range(100000):
        # Blokowanie dostępu do wspólnego zasobu
        with licznik_lock:
            licznik += 1

# Tworzenie wątków
watek1 = threading.Thread(target=zwieksz_licznik)
watek2 = threading.Thread(target=zwieksz_licznik)

# Startowanie wątków
watek1.start()
watek2.start()

# Oczekiwanie na zakończenie wątków
watek1.join()
watek2.join()

print(f"Finalna wartość licznika: {licznik}")
