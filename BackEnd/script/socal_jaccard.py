import numpy as np

def socal_jaccard(X):
    n, p = X.shape
    J = np.ones((n, p))
    a = np.dot(X, X.T)
    d = np.dot((J - X), (J - X).T)

    S_Sokal = (a + d) / p
    S_Jaccard = a / (p * np.ones((n, n)) - d)

    J = np.ones((n, n))

    D2_S = 2 * (J - S_Sokal)
    D2_J = 1 * (J - S_Jaccard)

    return S_Sokal, S_Jaccard, D2_S, D2_J


# X = np.array([
#     [1, 1, 0, 0, 1, 1],
#     [1, 1, 1, 0, 0, 1],
#     [1, 0, 0, 1, 0, 1],
#     [1, 0, 0, 1, 0, 1],
#     [1, 0, 0, 0, 1, 1],
#     [0, 0, 0, 0, 1, 0]
# ])

# S_Sokal, S_Jaccard, D2_S, D2_J = socal_jaccard(X)

# print("S_Sokal:", S_Sokal)
# print("S_Jaccard:", S_Jaccard)
# print("D2_S:", D2_S)
# print("D2_J:", D2_J)
