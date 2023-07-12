import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def coorp3c(D):
    n, _ = D.shape
    H = np.eye(n) - np.ones((n, n)) / n
    B = -H @ D @ H / 2
    L, T = np.linalg.eig(B)
    m = np.min(L)
    epsilon = 1e-6
    if np.abs(m) < epsilon:
        D1 = non2euclid(D)
        B = -H @ D1 @ H / 2
        L, T = np.linalg.eig(B)

    vaps = np.diag(L)
    j = 1
    while vaps[j] > epsilon:
        T1 = T[:, :j]
        X = T1 @ np.sqrt(vaps[:j, :j])
        j = min(j + 1, n)

    percent = vaps / np.sum(vaps) * 100
    acum = np.zeros(n)
    for i in range(n):
        acum[i] = np.sum(percent[:i+1])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c='blue', marker='*', s=15)

    for i in range(n):
        ax.text(X[i, 0], X[i, 1], X[i, 2], str(i+1))

    ax.set_xlabel('Primera coordenada principal', fontsize=10)
    ax.set_ylabel('Segunda coordenada principal', fontsize=10)
    ax.set_zlabel('Tercera coordenada principal', fontsize=10)
    ax.set_title('Porcentaje de variabilidad explicada: {}%'.format(acum[2]), fontsize=12)

    plt.grid()
    plt.show()

    return X, vaps, percent, acum
