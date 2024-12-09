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
A[N, N] = -2
A[N, N - 1] = 1

# Wypełnienie macierzy A dla równania różniczkowego
for i in range(1, N):
    A[i, i-1] = 1
    A[i, i] = -2 + h**2
    A[i, i+1] = 1

# Wektor b
b[0] = 1
b[N] = -1

# Algorytm Thomasa (eliminacja w przód)
N = len(b) - 1

A_copy = np.copy(np.diag(A, k = -1))
b_copy = np.copy(np.diag(A, k = 0))
c_copy = np.copy(np.diag(A ,k = 1))

for i in range(1, N + 1):
    m = A_copy[i-1] / b_copy[i-1]
    b_copy[i] = b_copy[i] - m * c_copy[i - 1]
    b[i] = b[i] - m * b[i - 1]

# Algorytm Thomasa (substytucja wstecz)
y = np.zeros(N + 1)
y[N] = b[N] / b_copy[N]

for i in range(N-1, -1, -1):
    y[i] = (b[i] - c_copy[i] * y[i + 1]) / b_copy[i]

# Wykres
plt.figure(figsize=(10, 6))
plt.plot(np.arange(0, (N + 1) * h, h), y, label="Solution y_n")
plt.title("Wykres wartości wektora y")
plt.xlabel("nh")
plt.ylabel("y_n")
plt.legend()
plt.grid(True)
plt.show()
