import math
from random import random, choice
import numpy as np
import matplotlib.pyplot as plt
import csv


def euklides(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def dbscan(data, MinPts, Eps):
    probka = choice(data)
    sasiadujace = []
    wewnetrzne = []
    brzegowe = []
    zewnetrzne = []
    for punkt in data:
        if euklides(probka, punkt) <= Eps:
            sasiadujace.append(punkt)
            if len(sasiadujace) > MinPts:
                wewnetrzne.append(sasiadujace)
    return wewnetrzne



with open('szumoida.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile, delimiter=','))

data = np.array(data, dtype=float)
Eps = 10
MinPts = 3
ds = np.array(dbscan(data, MinPts, Eps))
print(ds)

plt.scatter(data[:, 0], data[:, 1])
plt.scatter(ds[:, 0], ds[:, 1], color='red')
plt.xlim(-20, 120)
plt.ylim(-60, 60)
plt.show()





