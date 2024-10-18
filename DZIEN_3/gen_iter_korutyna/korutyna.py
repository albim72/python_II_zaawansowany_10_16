def my_coroutine():
    print("Korutyna została uruchomiona")
    while True: # Add a while loop to continuously receive values
        received = yield
        print(f"Otrzymano: {received}")

# Użycie:
coro = my_coroutine()
next(coro)  # Inicjalizacja korutyny
coro.send("Dane dla korutyny")  # Wysyłanie wartości do korutyny
