import numpy as np

# Matrizen fuer die beiden HMM Modellierungsvarianten des Casinobeispiels 
P1 = np.zeros((12,12))
P1[0:6,0:6]  = .95/6 # die oberen Schranken sind nicht enthalten 
P1[0:6,6:11] = 0.05/10
P1[0:6,11:12] = 0.05/2
P1[6:12,0:6] = .1/6
P1[6:12,6:11] = 0.9/10
P1[6:12,11:12] = 0.9/2

assert P1[0,:].sum() == 1.0 # check der ersten Zeile

E1 = np.zeros((12,6))
for i in range(12):
  E1[i,i % 6] = 1

# laut Skript ist der Startwert jeweils der erste Wert  
p1 = np.zeros(12)
p1[0] = 1   
 
P2 = np.array([[.95, 0.05],[0.1, 0.9]])  

E2 = np.zeros((2,6))
E2[0,:] = 1/6.
E2[1,0:5] = 1/10.
E2[1,5] = 1/2.

p2 = np.array([1,0]) 

