import numpy as np
import matplotlib.pyplot as plt

def derivative_1(x, h, f):
    return (f(x + h) - f(x)) / h

def derivative_2(x, h, f):
    return (f(x + h) - f(x - h)) / (2 * h)

def derivative_3(x, h, f):
    return ((-f(x + 2 * h) + 8 * f(x + h) - 8 * f(x - h) + f(x - 2 * h)) / (12 * h))

def absolute_error(f1, f2, x):
    return np.abs(f1(x) - f2(x))

def find_optimal_h(x, f, D_f):
    h_values = np.logspace(-16, 0, num=1000, endpoint=False)
    errors_1 = []
    errors_2 = []
    errors_3 = []

    for h in h_values:
        error_1 = absolute_error(lambda k: derivative_1(k, h, f), D_f, x)
        error_2 = absolute_error(lambda k: derivative_2(k, h, f), D_f, x)
        error_3 = absolute_error(lambda k: derivative_3(k, h, f), D_f, x)

        errors_1.append(error_1)
        errors_2.append(error_2)
        errors_3.append(error_3)

    min_error_1 = np.min(errors_1)
    min_error_2 = np.min(errors_2)
    min_error_3 = np.min(errors_3)

    optimal_h_1 = h_values[np.argmin(errors_1)]
    optimal_h_2 = h_values[np.argmin(errors_2)]
    optimal_h_3 = h_values[np.argmin(errors_3)]

    return {
        'x': x,
        'optimal_h_1': optimal_h_1,
        'min_error_1': min_error_1,
        'optimal_h_2': optimal_h_2,
        'min_error_2': min_error_2,
        'optimal_h_3': optimal_h_3,
        'min_error_3': min_error_3,
    }

def plot_error(x, optimal_values):
    for values in optimal_values:
        x = values['x']
        optimal_h_1 = values['optimal_h_1']
        min_error_1 = values['min_error_1']
        optimal_h_2 = values['optimal_h_2']
        min_error_2 = values['min_error_2']
        optimal_h_3 = values['optimal_h_3']
        min_error_3 = values['min_error_3']

        print(f"Metoda 1 dla x={x}: Optymalne h = {optimal_h_1}, Minimalny błąd = {min_error_1}")
        print(f"Metoda 2 dla x={x}: Optymalne h = {optimal_h_2}, Minimalny błąd = {min_error_2}")
        print(f"Metoda 3 dla x={x}: Optymalne h = {optimal_h_3}, Minimalny błąd = {min_error_3}")

        h_values = np.logspace(-16, 0, num=1000, endpoint=False)
        errors_1 = []
        errors_2 = []
        errors_3 = []

        for h in h_values:
            error_1 = absolute_error(lambda k: derivative_1(k, h, np.sin), np.cos, x)
            error_2 = absolute_error(lambda k: derivative_2(k, h, np.sin), np.cos, x)
            error_3 = absolute_error(lambda k: derivative_3(k, h, np.sin), np.cos, x)

            errors_1.append(error_1)
            errors_2.append(error_2)
            errors_3.append(error_3)

        plt.title(f"Błąd metod dyskretyzacji dla x = {x}")
        plt.xscale('log')
        plt.yscale('log')
        plt.plot(h_values, errors_1, label=f"Metoda 1")
        plt.plot(h_values, errors_2, label=f"Metoda 2")
        plt.plot(h_values, errors_3, label=f"Metoda 3")
        plt.grid()
        plt.xlabel('log h')
        plt.ylabel(f"log E(x) dla {x = }")
        plt.legend()
        plt.savefig(f"wykres_N2_{x}.pdf")
        plt.show()

def main():
    x_values = [np.float64(1), np.pi / 2]

    optimal_values = [find_optimal_h(x, f=np.sin, D_f=np.cos) for x in x_values]

    plot_error(x_values, optimal_values)

if __name__ == "__main__":
    main()
