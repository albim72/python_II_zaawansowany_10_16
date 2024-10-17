import datetime

class Greeting:
    def __call__(self, hour=None):
        if hour is None:
            hour = datetime.datetime.now().hour

        if 5<=hour<12:
            return "Dzień dobry"
        elif 12<= hour < 18:
            return "Miłego popołudnia!"
        elif 18<=hour<22:
            return "Dobry wieczór"
        else:
            return "Dobranoc!"

greet = Greeting()

print(greet)
print(greet())

print(greet(10))
print(greet(17))
print(greet(19))
print(greet(23))
print(greet(2))
