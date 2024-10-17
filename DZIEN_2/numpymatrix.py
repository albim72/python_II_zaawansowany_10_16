import numpy as np

#macierz współczynników A
A = np.array([[2,3,1],
              [4,1,2],
              [3,2,4]])
#wektor wyników
B = np.array([1,2,3])

#rozwiązanie układu równań za pomocą funkcji algebraicznej linalg.solve

x = np.linalg.solve(A,B)

print(f"Rozwiązanie układu równań (x,y,z): {x}")

#weryfikacja: mnożenie macierzy A i wektora x powinno dac B
B_check  = np.dot(A,x)
print(f"Weryfikacja (A*x): {B_check}")
