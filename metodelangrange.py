import numpy as np
import matplotlib.pyplot as plt

def interpolasi_lagrange(x_titik, y_titik, x):
    """
    Melakukan interpolasi Lagrange.
    
    Parameter:
    x_titik (list): daftar koordinat x
    y_titik (list): daftar koordinat y
    x (float): nilai x untuk diinterpolasi
    
    Mengembalikan:
    float: nilai y yang diinterpolasi
    """
    total = 0
    n = len(x_titik)
    for i in range(n):
        xi, yi = x_titik[i], y_titik[i]
        
        def L(i, x):
            term = 1
            for j in range(n):
                if i != j:
                    term *= (x - x_titik[j]) / (xi - x_titik[j])
            return term
        
        total += yi * L(i, x)
    
    return total

# Data yang diberikan
x_titik = [5, 10, 15, 20, 25, 30, 35, 40]
y_titik = [40, 30, 25, 40, 18, 20, 22, 15]

# Menginterpolasi nilai antara 5 dan 40
x_nilai = np.linspace(5, 40, 100)
y_nilai = [interpolasi_lagrange(x_titik, y_titik, x) for x in x_nilai]

# Memplot titik data dan hasil interpolasi
plt.plot(x_titik, y_titik, 'ro', label='Titik Data')
plt.plot(x_nilai, y_nilai, 'b-', label='Interpolasi Lagrange')
plt.xlabel('Tegangan, x (kg/mm^2)')
plt.ylabel('Waktu patah, y (jam)')
plt.title('Interpolasi Polinom Lagrange')
plt.legend()
plt.grid(True)
plt.show()