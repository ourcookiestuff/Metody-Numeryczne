import numpy as np
import matplotlib.pyplot as plt


# Definiowanie funkcji odwzorowania logistycznego
def logistic_map(r, x):
    return r * x * (1 - x)


def linspace(start, stop, num):
    step = (stop - start) / (num - 1)
    return [start + step * i for i in range(num)]


# Wartości parametru r
r_values = linspace(2, 4, 1000)  # Przedział wartości r od 2 do 4, 1000 punktów
iterations = 1000  # Liczba iteracji dla każdej wartości r
last = 100  # Ilość ostatnich punktów, które zostaną wyświetlone

# Przechowywanie danych dla diagramu rozgałęzienia
x_values = []  # Lista wartości x
r_output = []  # Lista odpowiadających im wartości r

# Obliczanie diagramu rozgałęzienia
for r in r_values:
    x = 0.1  # Początkowa wartość x
    for i in range(iterations):
        x = logistic_map(r, x)
        # Zapisywanie tylko ostatnich wartości, aby wyświetlić atraktor
        if i >= (iterations - last):
            x_values.append(x)
            r_output.append(r)

# Rysowanie diagramu rozgałęzienia
plt.figure(figsize=(10, 7))
plt.plot(r_output, x_values, ',k', alpha=.25)
plt.title("Odwzorowanie logistyczne")
plt.xlabel("r")
plt.ylabel("X")
plt.show()
