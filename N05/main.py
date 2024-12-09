import numpy as np
import matplotlib.pyplot as plt

# parametry
N = 1000
h = 0.01


def calculate_y(N, h):
    y = np.zeros(N + 1)
    # wyliczanie w sposób jawny
    y[0] = 1
    y[1] = 4 / (6 - h**2)

    for n in range(2, N + 1):
        y[n] = (2 - h**2) * y[n - 1] - y[n - 2]

    return y


y = calculate_y(N, h)

# rysowanie rozwiązania
plt.figure(figsize=(10, 6))
plt.plot(np.arange(0, (N + 1) * h, h), y, label="Solution y_n")
plt.title("Jawnie")
plt.xlabel("nh")
plt.ylabel("y_n")
plt.legend()
plt.grid(True)
plt.show()
