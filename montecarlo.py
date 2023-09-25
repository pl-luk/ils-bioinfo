#!/usr/bin/python3
import numpy as np
import numpy.random as random

# Kreisgleichung für Kreis mit Radius 1
isInCircle = lambda x, y: x ** 2 + y ** 2 <= 1

# Aufgabe R1 a) 
def R1_a(N: int) -> float:

    # Sampeln von x und y aus einem Quadrat von -1 bis 1
    xs = random.uniform(-1, 1, N)
    ys = random.uniform(-1, 1, N)

    # Berechnen wieviele der Punkte im Kreis liegen
    K = np.sum(isInCircle(xs, ys))

    # Berechnen von pi vol(Q) = 4 => pi = K / N * 4
    return (K * 4) / N

# Aufgabe R1 b)
def R1_b(N: int) -> float:

    # Sampeln von x und y aus einem Quadrat von 0 bis 1
    xs = random.uniform(0, 1, N)
    ys = random.uniform(0, 1, N)

    # Berechnen wieviele der Punkte im (Viertel) Kreis liegen
    K = np.sum(isInCircle(xs, ys))

    return (K * 4) / N
