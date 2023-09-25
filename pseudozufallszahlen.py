#!/usr/bin/python3
import numpy as np
import numpy.random as random


# 1. Ziehen aus [0, 1)
# 2. Multiplizieren mit N => Skaliert das Intervall auf [0, N)
# 3. Runden auf die nächsthöhere ganze Zahl => liefert natürliche Zahl aus {1, ..., N}
def R2_1(N: int, size: int = 1):
    return np.ceil(random.uniform(0, 1, size) * N).astype(int)

# 1. Ziehen aus [0, 1)
# 2. Aufsummieren der Vorgänger der W'keiten also aus p = [.25, .5, .25] wird [.25, .75, 1]
# 3. Die "Nummer" des Teilintervalls liefert die Zufallszahl
def pk_dist(p: list) -> int:

    # Wenn die Gesamtw'keiten von p nicht gleich 1 müssen wir abbrechen
    if np.sum(p) != 1:
        return None

    x = random.uniform(0, 1)
    p = np.array([np.sum(p[:i + 1]) for i in range(len(p))])

    return np.sum(x > p) + 1

def minst(size: int, seed: int) -> list:

    a = 48721
    c = 0
    n = 2 ** 31 - 1

    nums = [seed]

    for i in range(size):
        nums.append((a * nums[i] + c) % n)

    # Abschneiden des ersten Wertes, da dieser sonst immer dem Seed entspricht
    return nums[1:]

def cos_distr():

    cos_pdf = lambda x: np.cos(x) / 2

    while True:
    
        y = random.uniform(-np.pi / 2, np.pi / 2)
        u = random.uniform(0, 1)

        if u * np.pi / 2 * 1 / np.pi <= cos_pdf(y):
            return y[0]
