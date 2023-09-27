#!/usr/bin/python3

from collections.abc import Callable
import numpy as np

def needleman_wunsch(a: list, b: list, M: Callable[[str, str], float], e: float) -> list:

    A = len(a) + 1
    B = len(b) + 1

    D = np.ones((A, B)) * -np.infty
    p = np.ones((A, B, 2), dtype = int) * (-1)

    for i in range(1, A):
        D[i, 0] = -e * i

    for j in range(1, B):
        D[0, j] = -e * j

    for i in range(1, A):
        for j in range(1, B):

            if D[i, j] < D[i - 1, j] - e:
                D[i, j] = D[i - 1, j] - e
                p[i, j] = (i - 1, j)

            if D[i, j] < D[i, j - 1] - e:
                D[i, j] = D[i, j - 1] - e
                p[i, j] = (i, j - 1)
            
            if D[i, j] < D[i - 1, j - 1] + M(a[i], b[j]):
                D[i, j] = D[i - 1, j - 1] + M(a[i], b[j])
                p[i, j] = (i - 1, j - 1)

    v = np.array([len(a), len(b)]) 
    P = []

    while not (v == [0, 0]).all():
        P.append((p[v[0], v[1]], v))
        v = p[v[0], v[1]]

    return P

def needleman_wunsch_matrix(a: list, b: list, M: Callable[[str, str], float], e: float) -> np.array:

    A = len(a) + 1
    B = len(b) + 1

    D = np.zeros((A, B))

    for i in range(1, A):
        D[i, 0] = D[i - 1, 0] - e
    
    for j in range(1, B):
        D[0, j] = D[0, j - 1] - e

    for i in range(1, A):
        for j in range(1, B):

            D[i, j] = max(D[i - 1, j - 1] + M(a[i - 1], b[j - 1]), D[i - 1, j] - e, D[i, j - 1] - e)


    return D

def smith_waterman_matrix(a: list, b: list, M: Callable[[str, str], float], e: float) -> np.array:

    A = len(a) + 1
    B = len(b) + 1

    D = np.zeros((A, B))

    for i in range(1, A):
        for j in range(1, B):

            D[i, j] = max(D[i - 1, j - 1] + M(a[i - 1], b[j - 1]), D[i - 1, j] - e, D[i, j - 1] - e, 0)

    return D
