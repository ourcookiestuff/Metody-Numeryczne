import numpy as np
import matplotlib.pyplot as plt

# Parametry
N = 1000
h = 0.01

# Inicjalizacja macierzy A i wektora prawej strony b
A = np.zeros((N + 1, N + 1))
b = np.zeros(N + 1)

# Warunki brzegowe
A[0, 0] = 1
A[N, N] = 1

# Wypełnienie macierzy A dla równania różniczkowego
for i in range(1, N):
    A[i, i-1] = 1/h**2
    A[i, i] = -2/h**2 + 1
    A[i, i+1] = 1/h**2

# Wektor b
b[0] = 1  # warunek brzegowy dla y_0

# Algorytm Thomasa (eliminacja w przód)
A_copy = A.copy()
b_copy = b.copy()

for i in range(1, N + 1):
    m = A_copy[i, i-1] / A_copy[i-1, i-1]
    A_copy[i] -= m * A_copy[i-1]
    b_copy[i] -= m * b_copy[i-1]

# Algorytm Thomasa (substytucja wstecz)
y = np.zeros(N + 1)
y[N] = b_copy[N] / A_copy[N, N]

for i in range(N-1, -1, -1):
    y[i] = (b_copy[i] - A_copy[i, i+1] * y[i+1]) / A_copy[i, i]

# Wykres
plt.figure(figsize=(10, 6))
plt.plot(np.arange(0, (N + 1) * h, h), y, label="Solution y_n")
plt.title("Algorytm Thomasa")
plt.xlabel("nh")
plt.ylabel("y_n")
plt.legend()
plt.grid(True)
plt.show()
