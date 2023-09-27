#!/usr/bin/python3

import numpy as np

def viterbi_backtrace(E: np.array, P: np.array, p: list, o: list) -> (np.float64, np.array):

    V = np.zeros((len(P), len(o)))
    b = np.zeros((len(P), len(o)), dtype = np.int32)

    T = len(o)

    V[:, 0] = np.log(p) + np.log(E[:, o[0]])

    for t in range(1, T):
        for x in range(len(P)):

            search = np.log(P[:, x]) + V[:, t - 1]

            V[:, t] = np.log(E[:, o[t]]) + search.max()
            b[:, t] = search.argmax()

    hidden = np.zeros(T, dtype = np.int32)
    hidden[-1] = V[:, -1].argmax()

    for t in range(T - 1, 0, -1):
        hidden[t - 1] = b[hidden[t], t]

    return V[:, -1].max(), hidden

# 1. Samplen einer Matrix mit beliebigen Werten
# 2. Teilen jeder Zeile durch die entsprechende Zeilensumme
def prob_matrix(n: int, m: int) -> np.array:
    prob = np.uniform(size = (n, m))
    return prob / prob.sum(axis = 1)[:, np.newaxis]
