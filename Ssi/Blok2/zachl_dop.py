import math
import numpy as np


def euklides(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def manhattan(a, b):
    return np.abs(a[0] - b[0]) + np.abs(a[1] - b[1])


def czebyszew(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


def miara_niepodobienstwa(BA, BB, odl):
    miara = 0
    for i in range(BA.shape[0]):
        for j in range(BA.shape[1]):
            if BA[i][j] == 1:
                odl_min = np.inf
                for k in range(BB.shape[0]):
                    for l in range(BB.shape[1]):
                        if BB[k][l] == 1:
                            if odl == 'euk':
                                odl_akt = euklides((i, j), (k, l))
                            elif odl == 'man':
                                odl_akt = manhattan((i, j), (k, l))
                            elif odl == 'cze':
                                odl_akt = czebyszew((i, j), (k, l))
                            odl_min = min(odl_min, odl_akt)
                miara += odl_min
    return miara


def miara_niepodobienstwa_obustronnego(miara_a, miara_b):
    return -(miara_a + miara_b)


znaki_wz1 = np.array([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 0, 1], [0, 0, 0, 1], [0, 0, 0, 1]])
znaki_wz2 = np.array([[0, 1, 1, 1], [1, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]])
znaki_wz3 = np.array([[1, 1, 1, 0], [0, 0, 0, 1], [1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 0]])

znaki_tst1 = np.array([[0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]])
znaki_tst2 = np.array([[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1]])
znaki_tst3 = np.array([[1, 1, 1, 1], [0, 0, 0, 1], [0, 0, 1, 0], [1, 1, 0, 0], [1, 1, 1, 1]])


