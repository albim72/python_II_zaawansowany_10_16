import threading
import time

# Tworzymy semafor, który pozwala na równoczesny dostęp maksymalnie 2 wątkom
semafor = threading.Semaphore(2)

def dostep_do_uslugi(watek_id):
    print(f"Wątek {watek_id} czeka na dostęp do usługi")
    with semafor:
        print(f"Wątek {watek_id} uzyskał dostęp do usługi")
        time.sleep(2)  # Symulujemy czas działania usługi
        print(f"Wątek {watek_id} kończy korzystanie z usługi")

# Tworzenie i uruchamianie 5 wątków
watki = []
for i in range(5):
    watek = threading.Thread(target=dostep_do_uslugi, args=(i,))
    watki.append(watek)
    watek.start()

# Oczekiwanie na zakończenie wszystkich wątków
for watek in watki:
    watek.join()
