import numpy as np


# Równanie charakterystyczne macierzy A
def char_eq(lam):
    return -lam ** 3 + 12 * lam ** 2 - 46 * lam + 56


# Implementacja metody bisekcji
def bisection_method(f, a, b, tol=1e-8):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("Funkcja musi mieć przeciwne znaki na końcach przedziału")

    iterations = 0
    while (b - a) / 2 > tol:
        iterations += 1
        c = (a + b) / 2
        fc = f(c)
        if fc == 0 or (b - a) / 2 < tol:
            break
        if np.sign(fc) == np.sign(fa):
            a = c
            fa = fc
        else:
            b = c
            fb = fc
    return (a + b) / 2, iterations


# Implementacja metody reguła falsi
def false_position_method(f, a, b, tol=1e-8):
    fa, fb = f(a), f(b)
    if fa * fb > 0:
        raise ValueError("Funkcja musi mieć przeciwne znaki na końcach przedziału")

    iterations = 0
    c = a
    for _ in range(100):
        iterations += 1
        c_old = c
        c = b - fb * (b - a) / (fb - fa)
        fc = f(c)
        if abs(c - c_old) < tol:
            break
        if np.sign(fc) == np.sign(fa):
            a = c
            fa = fc
        else:
            b = c
            fb = fc
    return c, iterations


# Implementacja metody siecznych
def secant_method(f, a, b, tol=1e-8):
    fa, fb = f(a), f(b)
    iterations = 0
    while abs(b - a) > tol:
        iterations += 1
        c = b - fb * (b - a) / (fb - fa)
        a, b = b, c
        fa, fb = fb, f(b)
    return b, iterations


# Znajdowanie przedziałów, w których funkcja zmienia znak
lambda_range = np.linspace(1, 6, 1000)  # Zdefiniowanie zakresu wartości lambda do sprawdzenia
values = np.array([char_eq(lam) for lam in lambda_range])  # Obliczenie wartości równania charakterystycznego

sign_change_intervals = []  # Znajdowanie przedziałów, w których funkcja zmienia znak
for i in range(len(lambda_range) - 1):
    if values[i] * values[i + 1] < 0:
        sign_change_intervals.append((lambda_range[i], lambda_range[i + 1]))

# Wypisywanie znalezionych przedziałów
print("Znalezione przedziały, w których funkcja zmienia znak:")
for interval in sign_change_intervals:
    print(interval)

# Zastosowanie wszystkich trzech metod do znalezienia pierwiastków i porównanie liczby iteracji
print("\nWyniki:")
for i, interval in enumerate(sign_change_intervals):
    a, b = interval
    # Zastosowanie metody bisekcji
    root_bisect, iter_bisect = bisection_method(char_eq, a, b)
    # Zastosowanie metody reguła falsi
    root_false_pos, iter_false_pos = false_position_method(char_eq, a, b)
    # Zastosowanie metody siecznych
    root_secant, iter_secant = secant_method(char_eq, a, b)

    # Wypisywanie wyników dla każdego przedziału
    print(f"\nPrzedział: {interval}")
    print(f"Metoda bisekcji:    korzeń = {root_bisect:.8f}, liczba iteracji = {iter_bisect}")
    print(f"Metoda reguła falsi: korzeń = {root_false_pos:.8f}, liczba iteracji = {iter_false_pos}")
    print(f"Metoda siecznych:    korzeń = {root_secant:.8f}, liczba iteracji = {iter_secant}")
