class LazyLoader:
    def __init__(self):
        self._expensive_module = None

    @property
    def expensive_module(self):
        if self._expensive_module is None:
            print("Ładuję moduł...")
            import time
            self._expensive_module = time  # Import odbywa się tutaj
        return self._expensive_module


# Tworzymy instancję LazyLoader
loader = LazyLoader()

# Moduł time nie jest jeszcze zaimportowany
print("Moduł jeszcze nie zaimportowany.")

# Pierwszy raz używamy time, następuje lazy loading
print(loader.expensive_module.time())
