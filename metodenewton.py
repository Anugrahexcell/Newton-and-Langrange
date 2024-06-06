import numpy as np
import matplotlib.pyplot as plt

def divided_differences(x, y):
    """
    Menghitung tabel divided differences.
    
    Parameter:
    x (list): daftar koordinat x
    y (list): daftar koordinat y
    
    Mengembalikan:
    numpy.ndarray: tabel divided differences
    """
    n = len(y)
    coef = np.zeros([n, n])
    coef[:,0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
    
    return coef

def newton_interpolation(x, y, x_interp):
    """
    Melakukan interpolasi Newton.
    
    Parameter:
    x (list): daftar koordinat x
    y (list): daftar koordinat y
    x_interp (float): nilai x untuk diinterpolasi
    
    Mengembalikan:
    float: nilai y yang diinterpolasi
    """
    coef = divided_differences(x, y)[0, :]
    n = len(x) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x_interp - x[n - k]) * p
    return p

# Data yang diberikan
x_titik = [5, 10, 15, 20, 25, 30, 35, 40]
y_titik = [40, 30, 25, 40, 18, 20, 22, 15]

# Menginterpolasi nilai antara 5 dan 40
x_nilai = np.linspace(5, 40, 100)
y_nilai = [newton_interpolation(x_titik, y_titik, x) for x in x_nilai]

# Memplot titik data dan hasil interpolasi
plt.plot(x_titik, y_titik, 'ro', label='Titik Data')
plt.plot(x_nilai, y_nilai, 'b-', label='Interpolasi Newton')
plt.xlabel('Tegangan, x (kg/mm^2)')
plt.ylabel('Waktu patah, y (jam)')
plt.title('Interpolasi Polinom Newton')
plt.legend()
plt.grid(True)
plt.show()