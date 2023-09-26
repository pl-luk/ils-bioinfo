#!/usr/bin/python3
import numpy as np

# Ersetze jeden Buchstaben mit nummer im dict (seq ohne \n)
num_mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
seq2num = lambda seq: [num_mapping[i] for i in list(seq)]

def probability_matrix(seqs: list) -> np.array:

    prob_matrix = np.zeros(shape = (4, 4))
    ln = 0

    # prob_matrix enthält die Anzahl der jeweiligen Tupel
    # in ln wird jeweils die Anzahl der Tupel in seq gespeichert
    for seq in seqs:
        
        num = seq2num(seq)

        for i in range(len(num) - 1):
            prob_matrix[num[i]][num[i + 1]] += 1

    # Summe der einzelnen Zeilen
    gsmt = np.sum(prob_matrix, axis = 1)

    # Teilen der einzelnen Zeilen durch die einzelnen Elemente aus gsmt
    return (prob_matrix.transpose() / gsmt).transpose()

def score(seq: str, p_plus: np.array, p_minus: np.array) -> float:

    num = seq2num(seq)
    s = 0

    for i in range(2, len(num)):

        s += np.log(p_plus[num[i - 1]][num[i]]) 
        s -= np.log(p_minus[num[i - 1]][num[i]])

    return s / (len(num) - 1)

# Funktion die den score vom mctest auswertet
def score_test():

    with open("mcplus.txt", "r") as f:
        t_plus = f.read().splitlines()

    with open("mcminus.txt", "r") as f:
        t_minus = f.read().splitlines()

    with open("mctest.txt", "r") as f:
        t_test = f.read().splitlines()

    p_plus = probability_matrix(t_plus)
    p_minus = probability_matrix(t_minus)
    
    for i in range(len(t_test)):
        sc = score(t_test[i], p_plus, p_minus)

        if sc < 0:
            print(i + 1)

