import numpy as np
import matplotlib.pyplot as plt

def conv(a):
    a[a == 0] = -1


def hopfield_uczenie(waga, wyjscie):
    conv(wyjscie)
    wyjscie = wyjscie.flatten()
    n = len(wyjscie)
    for i in range(waga.shape[0]):
        for j in range(waga.shape[1]):
            if i != j:
                waga[i][j] += (1/n) * wyjscie[i] * wyjscie[j]
            if i == j:
                waga[i][j] = 0
    return waga


def hopfield_rozpoznanie(waga, wyjscie):
    conv(wyjscie)
    wyjscie = wyjscie.flatten()
    for i in range(waga.shape[0]):
        suma = 0
        for j in range(waga.shape[1]):
            suma += wyjscie[j] * waga[i][j]
        wyjscie[i] = 1 if suma > 0 else -1
    return wyjscie.reshape((5, 5))


waga = np.zeros((25, 25))
znak_wz1 = np.array([[1, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0]])
znak_wz2 = np.array([[1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]])
znak_wz3 = np.array([[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]])

znak_tst1 = np.array([[0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0]])
znak_tst2 = np.array([[1, 1, 0, 0, 1], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0], [0, 1, 0, 1, 0], [1, 1, 0, 0, 1]])
znak_tst3 = np.array([[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]])
znak_tst4 = np.array([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 0, 1, 1, 1], [1, 0, 1, 1, 1], [1, 0, 1, 1, 1]])

wzory = [znak_wz1, znak_wz2, znak_wz3]
for wzor in wzory:
    waga = hopfield_uczenie(waga, wzor)

ts = hopfield_rozpoznanie(waga, znak_tst1)
ts2 = hopfield_rozpoznanie(waga, znak_tst2)
ts3 = hopfield_rozpoznanie(waga, znak_tst3)
ts4 = hopfield_rozpoznanie(waga, znak_tst4)

