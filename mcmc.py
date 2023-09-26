#!/usr/bin/python3

import numpy as np
import numpy.random as random
from collections.abc import Callable

# template funktion, sodass wir nur flip Kriterium übergeben müssen
def packe_template(a: np.array, c: np.array, b: float, iter: int,
                   flip: Callable[[float, float], [bool]]) -> np.array:

    X = np.zeros(len(a), dtype = '?')
    score = 0

    for _ in range(iter):

        j = random.randint(0, len(a))

        Y = X.copy()
        Y[j] = ~Y[j]

        new_score = np.sum(c * Y)
 
        if np.sum(a * Y) <= b and flip(score, new_score):
            X = Y
            score = new_score

    return X

packe = lambda a, c, b, iter: packe_template(a, c, b, iter,
                                             lambda o, n: True)

packe_compare = lambda a, c, b, iter: packe_template(a, c, b, iter,
                                                     lambda o, n: n > o)

packe_mc = lambda a, c, b, iter: packe_template(a, c, b, iter,
                                                lambda o, n: (n > o) or random.choice([0, 1]))

packe_var = lambda a, c, b, iter: packe_template(a, c, b, iter,
                                                 lambda o, n: (n > o) or np.round(random.uniform(0, 1 + n / o)))

# Erweiterter random Walk von 1 ... 50
def next_step(old: int) -> int:

    if old == 1:
        return random.choice([1, 2])
    elif old > 1 and old < 50:
        return random.choice([old - 1, old + 1])
    elif old == 50:
        return random.choice([49, 50])
    else:
        return None


def metropolis_hastings(I: int) -> np.array:

    X = np.linspace(-np.pi / 2, np.pi / 2, 50 + 1)
    pi = np.cos(X)
    pi /= np.sum(pi)

    s = np.zeros(I, dtype = int)
    s[0] = random.randint(1, 51)

    for i in range(1, I - 1):

        t = next_step(s[i - 1])

        # P(t, s[i - 1]) und P(s[i - 1], t) kann auch hier vollständig weggelassen
        # werden, da P(...) in unserem Fall immer 1/2 zurückgibt. Das 1/2 kürzt sich
        alpha = min(pi[t] / pi[s[i - 1]], 1)
        x = random.uniform()
        if x <= alpha:
            s[i] = t
    
        else:
            s[i] = s[i - 1]

    return s
