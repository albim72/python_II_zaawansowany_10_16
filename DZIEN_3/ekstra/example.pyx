# Deklarujemy typy zmiennych dla szybszego dzia�ania
def cython_sum(int n):
    cdef int i
    cdef double s = 0
    for i in range(n):
        s += i
    return s
