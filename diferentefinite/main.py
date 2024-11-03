import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

c, d = 0, 1
n = 10
h = (d - c) / n

# Crearea matricei A și a vectorului b
A = np.zeros((n+1, n+1))
b = np.zeros(n+1)

# Condiții la limită
b[0] = 0  # u(0) = 0
b[n] = 1  # u(1) = 1

# Completarea matricei A și vectorului b
A[0, 0] = 1  # Stabilirea condiției la limită u(0) = 0
A[n, n] = 1  # Stabilirea condiției la limită u(1) = 1

for i in range(1, n):
    xi = c + i * h
    A[i, i-1] = 1 - h/2 * xi      # Coeficient pentru u'(xi) folosind diferența centrală
    A[i, i] = -2 - h**2 * 2       # Coeficient pentru u(xi)
    A[i, i+1] = 1 + h/2 * xi      # Coeficient pentru u'(xi) folosind diferența centrală
    b[i] = h**2 * np.exp(xi)      # Termen sursă e^x, scalat cu h^2

# Rezolvarea sistemului liniar
try:
    U = np.linalg.solve(A, b)
except np.linalg.LinAlgError:
    print("Matricea este singulara, nu se poate gasi o solutie unica.")

# Punctele x pe grilă
x_points = np.linspace(c, d, n+1)

# Crearea graficului
plt.figure(figsize=(8, 5))
plt.plot(x_points, U, 'o-', label='Aproximatia numerica U')
plt.title('Solutia numerica a ecuatiei diferentiale')
plt.xlabel('x')
plt.ylabel('u(x)')
plt.legend()
plt.grid(True)
plt.show()
