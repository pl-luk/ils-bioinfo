#!/usr/bin/python3

import casino_template
import numpy as np
from numpy import random

def faculty(n: int) -> int:
    return 1 if n == 0 else n * faculty(n - 1)

def werfe(N: int) -> np.array:
        
    res = np.zeros(N, dtype = int)
    p = casino_template.p2.copy()

    for i in range(N):

        zst = random.choice([0, 1], p = p)
        res[i] = random.choice(np.arange(1, 7), p = casino_template.E2[zst])
        p = casino_template.P2[zst]

    return res

# shifted als dient als switch, sodass nur im ersten rekursionsschritt geschifted wird
def alpha_t(t: int, E: np.array, P: np.array, p: np.array, o: np.array, shifted: bool = False):
   
    # shifte t und o auf 0-basiert => algorithmus aus dem Skript kann verwendet werden
    if not shifted:
        t = t - 1
        o = o - 1
    
    return p * E[:, o[t]] if t == 0 else (alpha_t(t - 1, E, P, p, o, shifted | 1) @ P) * E[:, o[t]]

