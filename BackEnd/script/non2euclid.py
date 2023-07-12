import numpy as np

def non2euclid(D):
    n, _ = D.shape
    H = np.eye(n) - np.ones((n, n)) / n
    T, lambda_vals = np.linalg.eig(-H @ D @ H / 2)
    m = np.min(np.diag(lambda_vals))
    D1 = D - 2 * m * np.ones((n, n)) + 2 * m * np.eye(n)
    return D1
