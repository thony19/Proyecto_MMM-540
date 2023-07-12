import numpy as np
import pandas as pd

# Cargar matriz de estilos ideales desde Excel
basedatos = 'EstilosInteligencias.xlsx'
celdasinteligencias = 'CL2:FM9'
inteligenciasideales = pd.read_excel(basedatos, sheet_name=4, header=None, usecols="CL:FM", skiprows=1, nrows=8).values

# Graficar estilos ideales
[S_Sokal, S_Jaccard, D2_S, D2_J] = socal_jaccard(inteligenciasideales)
[R, vaps, percent, acum] = coorp3c(D2_S)
R = R[:, :3]
grid()

# Calcular puntos ideales para un solo punto
basedatos = 'EstilosInteligencias.xlsx'
celdasinteligenciasp = 'B2:CC2'
estup = pd.read_excel(basedatos, sheet_name=6, header=None, usecols="B:CC", skiprows=1, nrows=1).values

X = inteligenciasideales
x = estup
[m, n] = x.shape
rr = np.zeros((m, 3))
for i in range(m):
    yt = puntos_idealesi(X, x[i, :])
    rr[i, :] = yt[:3]
rr

# Calcular puntos ideales para cada estudiante
basedatos = 'EstilosInteligencias.xlsx'
celdasinteligencias1360 = 'CE2:FF1361'
estui1360 = pd.read_excel(basedatos, sheet_name=3, header=None, usecols="CE:FF", skiprows=1, nrows=1360).values

X = inteligenciasideales
x = estui1360
[m, n] = x.shape
r = np.zeros((m, 3))
for i in range(m):
    yt = puntos_ideales(X, x[i, :])
    r[i, :] = yt[:3]
r

# Calcular normas euclidianas
[p, q] = r.shape
[n, m] = R[:, :3].shape
normat = np.zeros((p, n))
for j in range(p):
    for i in range(n):
        normat[j, i] = np.linalg.norm(R[i, :] - r[j, :])
normat
grid()
