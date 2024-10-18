import cProfile

def test_function():
    total = 0
    for i in range(1, 10000):
        total += i ** 2
    return total

cProfile.run('test_function()')
