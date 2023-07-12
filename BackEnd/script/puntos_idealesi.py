import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from socal_jaccard import socal_jaccard
from coorp3c import coorp3c

def puntos_idealesi(X, x):
    n, p = X.shape

    a = np.matmul(X, x)
    d = np.matmul((np.ones((n, p)) - X), (np.ones((1, p)) - x))
    s = (a + d) / p
    d = 2 * (np.ones((n, 1)) - s)
    st = np.transpose(s)
    dt = np.transpose(d)

    S_Sokal, S_Jaccard, D2_S, D2_J = socal_jaccard(X)
    Y, vaps, percent, acum = coorp3c(D2_S)
    B = np.matmul(Y, np.transpose(Y))
    b = np.diag(B)
    Lambda = np.diag(vaps[:p])
    y = 1/2 * np.matmul(np.linalg.inv(Lambda), np.matmul(np.transpose(Y), (b - d)))
    yt = np.transpose(y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot([yt[0]], [yt[1]], [yt[2]], '.r', markersize=12)

    ax.set_xlabel('Primera coordenada principal')
    ax.set_ylabel('Segunda coordenada principal')
    ax.set_zlabel('Tercera coordenada principal')
    ax.grid()

    plt.show()

    return yt
