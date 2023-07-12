import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Graficar líneas entre estilos y punto ideal
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot([R[0, 0], r[0]], [R[0, 1], r[1]], [R[0, 2], r[2]], 'r--')
ax.plot([R[1, 0], r[0]], [R[1, 1], r[1]], [R[1, 2], r[2]], 'r--')
ax.plot([R[2, 0], r[0]], [R[2, 1], r[1]], [R[2, 2], r[2]], 'r--')
ax.plot([R[3, 0], r[0]], [R[3, 1], r[1]], [R[3, 2], r[2]], 'r--')
ax.plot([R[4, 0], r[0]], [R[4, 1], r[1]], [R[4, 2], r[2]], 'r--')
ax.plot([R[5, 0], r[0]], [R[5, 1], r[1]], [R[5, 2], r[2]], 'r--')
ax.plot([R[6, 0], r[0]], [R[6, 1], r[1]], [R[6, 2], r[2]], 'r--')
ax.plot([R[7, 0], r[0]], [R[7, 1], r[1]], [R[7, 2], r[2]], 'r--')

# Graficar líneas entre estilos y puntos ideales generales
ax.plot([R[0, 0], rr[0]], [R[0, 1], rr[1]], [R[0, 2], rr[2]], 'r--')
ax.plot([R[1, 0], rr[0]], [R[1, 1], rr[1]], [R[1, 2], rr[2]], 'r--')
ax.plot([R[2, 0], rr[0]], [R[2, 1], rr[1]], [R[2, 2], rr[2]], 'r--')
ax.plot([R[3, 0], rr[0]], [R[3, 1], rr[1]], [R[3, 2], rr[2]], 'r--')
ax.plot([R[4, 0], rr[0]], [R[4, 1], rr[1]], [R[4, 2], rr[2]], 'r--')
ax.plot([R[5, 0], rr[0]], [R[5, 1], rr[1]], [R[5, 2], rr[2]], 'r--')
ax.plot([R[6, 0], rr[0]], [R[6, 1], rr[1]], [R[6, 2], rr[2]], 'r--')
ax.plot([R[7, 0], rr[0]], [R[7, 1], rr[1]], [R[7, 2], rr[2]], 'r--')

# Graficar mapa entre estilos
ax.plot([R[0, 0], R[1, 0]], [R[0, 1], R[1, 1]], [R[0, 2], R[1, 2]], 'k-')
ax.plot([R[0, 0], R[2, 0]], [R[0, 1], R[2, 1]], [R[0, 2], R[2, 2]], 'k-')
ax.plot([R[0, 0], R[3, 0]], [R[0, 1], R[3, 1]], [R[0, 2], R[3, 2]], 'k-')
ax.plot([R[2, 0], R[1, 0]], [R[2, 1], R[1, 1]], [R[2, 2], R[1, 2]], 'k-')
ax.plot([R[3, 0], R[1, 0]], [R[3, 1], R[1, 1]], [R[3, 2], R[1, 2]], 'k-')
ax.plot([R[3, 0], R[2, 0]], [R[3, 1], R[2, 1]], [R[3, 2], R[2, 2]], 'k-')

# Graficar líneas entre estilos
ax.plot([R[0, 0], R[1, 0]], [R[0, 1], R[1, 1]], [R[0, 2], R[1, 2]], 'r--')
ax.plot([R[0, 0], R[2, 0]], [R[0, 1], R[2, 1]], [R[0, 2], R[2, 2]], 'r--')
ax.plot([R[0, 0], R[3, 0]], [R[0, 1], R[3, 1]], [R[0, 2], R[3, 2]], 'r--')
ax.plot([R[1, 0], R[2, 0]], [R[1, 1], R[2, 1]], [R[1, 2], R[2, 2]], 'r--')
ax.plot([R[1, 0], R[3, 0]], [R[1, 1], R[3, 1]], [R[1, 2], R[3, 2]], 'r--')
ax.plot([R[2, 0], R[3, 0]], [R[2, 1], R[3, 1]], [R[2, 2], R[3, 2]], 'r--')

plt.show()
