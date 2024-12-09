import math

# Globalna zmienna do zliczania operacji
operations_count = 0


def add_operation(operation_type, count=1):
    global operations_count
    # Zdefiniowanie kosztów operacji na podstawie wymagań
    costs = {
        'arithmetic': 1.0,
        'function_call': 1.0,  # Wywołanie funkcji
        'math_function_call': 30.0,  # Wywołanie funkcji matematycznej
        'logical': 1.0,  # Operacja logiczna
        'bitwise': 0.5,  # Operacja bitowa
        'assignment': 0.5,  # Operator przypisania
        'compound_assignment': 1.0,  # Operatory +=, -= itd.
        'printing': 50.0,  # Wyświetlanie wyników
        'script_parsing': 50.0  # Parsowanie linii skryptu
    }
    operations_count += costs[operation_type] * count


def f(x, N):
    global operations_count
    # Zaczynamy od zliczania operacji parsowania i przypisania
    add_operation('script_parsing')
    add_operation('assignment')

    result = 0.0  # Inicjalizacja sumy szeregu
    x_pow = x ** 4  # Obliczenie x do potęgi 4
    add_operation('arithmetic', 3)
    add_operation('assignment',2)

    sin_x_pow = math.sin(x_pow)
    cos_x_pow = math.cos(x_pow)
    add_operation('math_function_call', 2)
    add_operation('assignment', 2)

    sin_nx = 0.0
    cos_nx = 1.0  # cos(0) = 1
    add_operation('assignment', 2)

    exp_minus_1 = math.exp(-1)
    exp_minus_4 = math.exp(-4)
    add_operation('math_function_call', 2)  # Dla exp(-1) i exp(-4)
    add_operation('assignment', 2)  # Dla przypisania do exp_minus_1 i exp_minus_4

    current_exp_n = 1.0  # e^0
    current_exp_4n = 1.0  # e^0
    add_operation('assignment', 2)  # Dla przypisania do current_exp_n i current_exp_4n

    for n in range(N):  # Pętla sumująca wyrazy szeregu
        add_operation('script_parsing')

        # Obliczanie wartości exp(-n) i exp(-4n)
        if n > 0:
            sin_nx, cos_nx = sin_nx * cos_x_pow + cos_nx * sin_x_pow, cos_nx * cos_x_pow - sin_nx * sin_x_pow
            add_operation('arithmetic', 6)
            add_operation('assignment', 4)

            current_exp_n *= exp_minus_1
            current_exp_4n *= exp_minus_4
            add_operation('arithmetic', 2)
            add_operation('assignment', 2)

        # Obliczenie pojedynczego wyrazu szeregu
        term = sin_nx ** 2 * current_exp_n + cos_nx ** 2 * current_exp_4n
        add_operation('arithmetic', 5)
        add_operation('assignment')

        result += term
        add_operation('arithmetic')  # Dla dodawania term do result
        add_operation('assignment')  # Dla przypisania do result

    return result


def corrected_calculate_with_precision(x, N):
    global operations_count
    add_operation('script_parsing')  # Parsowanie definicji funkcji
    operations_count = 0  # Resetowanie licznika operacji
    add_operation('script_parsing')  # Parsowanie przypisania
    add_operation('assignment')

    # Obliczamy wynik
    result = f(x, N)
    add_operation('function_call')  # Wywołanie funkcji f
    add_operation('assignment')

    return result, operations_count


# Ustawienie wartości N na 20
N = 20
add_operation('assignment')

# Obliczenie funkcji
corrected_result = f(1, N)
add_operation('assignment')
add_operation('function_call')  # Dla wywołania f(x, N)

# Wyświetlenie wyniku
print(f"Wynik: {corrected_result:.10g}")
print(f"Liczba operacji: {operations_count}")
