import matplotlib.pyplot as plt
import math
import random
import numpy as np


def median(lista):
    return sorted(lista)[len(lista) // 2] if len(lista) % 2 == 1 else (sorted(lista)[len(lista) // 2 - 1] + sorted(lista)[len(lista) // 2]) / 2

def euklides(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def manhattan(a, b):
    return abs(a[0] - b[0])

def k_srednia(m, iters, miara, checkpoints=[4, 10]):
    probki = list(zip(x1, x2))
    V = random.sample(probki, m)
    checkpoints_data = {}

    for ite in range(iters):
        grupy = [[] for _ in range(m)]
        for s in probki:
            if miara == 'euk':
                odleglosc = [euklides(s, x) for x in V]
            elif miara == 'man':
                odleglosc = [manhattan(s, x) for x in V]
            u = odleglosc.index(min(odleglosc))
            grupy[u].append(s)

        nowe_V = []
        for j in range(m):
            xgr = grupy[j]
            if xgr:
                srednia = tuple(sum(i[k] for i in xgr) / len(xgr) for k in range(len(xgr[0])))
                nowe_V.append(srednia)
            else:
                nowe_V.append(V[j])

        if V == nowe_V and ite >= 10:
            print(f'Algorytm zakończył się po {ite + 1} iteracjach')
            break

        V = nowe_V

        if ite + 1 in checkpoints:
            checkpoints_data[ite + 1] = (list(V), grupy)

    return V, grupy, checkpoints_data

def k_mediana(m, iters, miara, checkpoints=[4, 10]):
    probki = list(zip(x1, x2))
    V = random.sample(probki, m)
    checkpoints_data = {}

    for ite in range(iters):
        grupy = [[] for _ in range(m)]
        for s in probki:
            if miara == 'euk':
                odleglosc = [euklides(s, x) for x in V]
            elif miara == 'man':
                odleglosc = [manhattan(s, x) for x in V]
            u = odleglosc.index(min(odleglosc))
            grupy[u].append(s)

        nowe_V = []
        for j in range(m):
            xgr = grupy[j]
            if xgr:
                mediana_x1 = median([i[0] for i in xgr])
                mediana_x2 = median([i[1] for i in xgr])
                nowe_V.append((mediana_x1, mediana_x2))
            else:
                nowe_V.append(V[j])

        if V == nowe_V and ite >= 10:
            print(f'Algorytm zakończył się po {ite + 1} iteracjach')
            break

        V = nowe_V

        if ite + 1 in checkpoints:
            checkpoints_data[ite + 1] = (list(V), grupy)

    return V, grupy, checkpoints_data


def analiza_grup(grupy):
    raport = []
    for idx, grupa in enumerate(grupy):
        if grupa:
            x1_min = min(p[0] for p in grupa)
            x1_max = max(p[0] for p in grupa)
            x2_min = min(p[1] for p in grupa)
            x2_max = max(p[1] for p in grupa)
            raport.append({
                "grupa": idx + 1,
                "liczba_prob": len(grupa),
                "x1_min": x1_min,
                "x1_max": x1_max,
                "x2_min": x2_min,
                "x2_max": x2_max
            })
        else:
            raport.append({
                "grupa": idx + 1,
                "liczba_prob": 0,
                "x1_min": None,
                "x1_max": None,
                "x2_min": None,
                "x2_max": None
            })
    return raport


def rysuj_wykres(srodki, grupy, tytul, iteracja):
    colors = ['green', 'blue', 'orange', 'yellow', 'pink', 'purple']
    plt.figure(figsize=(8, 6))
    
    for idx, grupa in enumerate(grupy):
        if grupa:
            grupa_x = [p[0] for p in grupa]
            grupa_y = [p[1] for p in grupa]
            plt.scatter(grupa_x, grupa_y, color=colors[idx % len(colors)], label=f'Grupa {idx + 1}')
    
    srodek_x = [c[0] for c in srodki]
    srodek_y = [c[1] for c in srodki]
    plt.scatter(srodek_x, srodek_y, color='red', marker='o', s=100, label='Środki')
    
    plt.title(f'{tytul} - Iteracja {iteracja}')
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.legend()
    plt.grid(True)
    plt.show()


file_path = 'dane'
x1 = []
x2 = []

with open(file_path, 'r') as file:
    for line in file:
        line = line.strip()
        values = line.split(';')
        if len(values) == 2:
            x1.append(float(values[0]))
            x2.append(float(values[1]))











