import numpy as np


# Metoda potęgowa
def power_method(B, tol, max_iter=1000):
    n = B.shape[0]
    x = np.random.rand(n)
    x = x / np.linalg.norm(x)
    lambda_last = 0
    for i in range(max_iter):
        y = B @ x
        x = y / np.linalg.norm(y)
        lambda_new = x @ (B @ x)
        if np.abs(lambda_new - lambda_last) < tol:
            return lambda_new, x
        lambda_last = lambda_new
    return lambda_last, x


# Deflacja
def deflate(B, eigenvalue, eigenvector):
    return B - eigenvalue * np.outer(eigenvector, eigenvector)


# Metoda iteracyjna QR
def gram_schmidt_qr(B):
    n, m = B.shape
    Q = np.zeros((n, m))
    R = np.zeros((m, m))

    for k in range(m):
        Q[:, k] = B[:, k]
        for i in range(k):
            R[i, k] = np.dot(Q[:, i], B[:, k])
            Q[:, k] -= R[i, k] * Q[:, i]
        R[k, k] = np.linalg.norm(Q[:, k])
        Q[:, k] /= R[k, k]

    return Q, R


def qr_iteration(B, tol, max_iter=1000):
    n = B.shape[0]
    B_k = B.copy()
    for i in range(max_iter):
        Q_k, R_k = gram_schmidt_qr(B_k)
        B_k = R_k @ Q_k

        if np.allclose(np.diag(B_k), np.sort(np.diag(B_k))[::-1], atol=tol):
            return np.diag(B_k)

    return np.diag(B_k)


# Metoda Rayleigha
def rayleigh_quotient_iteration(B, tol, max_iter=1000, num_eigenvalues=3, precision=8):
    n = len(B)
    eigenvalues = []

    for _ in range(num_eigenvalues):
        b = np.random.rand(n)
        b = b / np.linalg.norm(b)
        prev_eigenvalue = 0

        for _ in range(max_iter):
            try:
                # Obliczenie kwocjentu Rayleigha
                Ab = np.dot(B, b)
                eigenvalue = np.dot(b, Ab) / np.dot(b, b)

                if np.abs(eigenvalue - prev_eigenvalue) < tol:
                    eigenvalues.append(np.round(eigenvalue, precision))
                    break

                prev_eigenvalue = eigenvalue
                # Rozwiązanie układu równań dla nowego wektora
                b = Ab / np.linalg.norm(Ab)
            except np.linalg.LinAlgError:
                print("Problem z obliczeniami numerycznymi.")
                break

        B = B - eigenvalue * np.outer(b, b) / np.dot(b, b)

    return eigenvalues


# Macierz A
A = np.array([[1, 2, 3], [2, 4, 5], [3, 5, -1]])

# Tolerancja
tolerance = 1e-8

# Metoda potęgowa z deflacją
eigenvalues_power = []
B_deflated_power = A.copy()
for _ in range(A.shape[0]):
    eigenvalue_power, eigenvector_power = power_method(B_deflated_power, tolerance)
    eigenvalues_power.append(eigenvalue_power)
    B_deflated_power = deflate(B_deflated_power, eigenvalue_power, eigenvector_power)

# Metoda iteracyjna QR
eigenvalues_qr = qr_iteration(A, tolerance)

A_copy_for_rayleigh = np.copy(A)
eigenvalues_rayleigh = rayleigh_quotient_iteration(A_copy_for_rayleigh, tolerance)

print("Metoda potęgowa - wartości własne:", eigenvalues_power)
print("Metoda iteracyjna QR - wartości własne:", eigenvalues_qr)
print("Metoda Rayleigha - wartości własne:", eigenvalues_rayleigh)
