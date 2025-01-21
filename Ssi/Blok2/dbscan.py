import math
from random import random, choice
import numpy as np
import matplotlib.pyplot as plt
import csv


def euklides(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def dbscan(data, MinPts, Eps):
    wewnetrzne = []
    brzegowe = []
    zewnetrzne = []

    for punkt in data:
        sasiedzi = [p for p in data if euklides(punkt, p) <= Eps]
        if len(sasiedzi) > MinPts:
            wewnetrzne.append(punkt)
        elif any(euklides(punkt, s) <= Eps for s in wewnetrzne) and len(sasiedzi) > 0:
            brzegowe.append(punkt)
        else:
            zewnetrzne.append(punkt)
    return wewnetrzne, brzegowe, zewnetrzne


with open('szumoida.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile, delimiter=','))

data = np.array(data, dtype=float)
Eps = 10
MinPts = 3
wewnetrzne, brzegowe, zewnetrzne = dbscan(data, MinPts, Eps)

wewnetrzne_x, wewnetrzne_y = zip(*wewnetrzne) if wewnetrzne else ([], [])
brzegowe_x, brzegowe_y = zip(*brzegowe) if brzegowe else ([], [])
zewnetrzne_x, zewnetrzne_y = zip(*zewnetrzne) if zewnetrzne else ([], [])


plt.scatter(wewnetrzne_x, wewnetrzne_y, color='green', label='Wewnętrzne')
plt.scatter(brzegowe_x, brzegowe_y, color='red', label='Brzegowe')
plt.scatter(zewnetrzne_x, zewnetrzne_y, color='blue', label='Zewnętrzne')

plt.xlim(-20, 120)
plt.ylim(-60, 60)
plt.legend()
plt.show()



