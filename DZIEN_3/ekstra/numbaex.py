import numpy as np
from numba import jit

# Dekorujemy funkcjê za pomoc¹ JIT
@jit(nopython=True)
def numba_sum(n):
    s = 0
    for i in range(n):
        s += i
    return s

print(numba_sum(1000000))
