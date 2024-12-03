import random
import numpy as np
import matplotlib.pyplot as plt


def main():
    x = random.uniform(0, 100)
    y = np.sin(x / 10.0) * np.sin(x / 200.0)
    rozrzut = 10
    wsp_przyrostu = 1.1
    l_iteracji = 100
    y_wszystkie = []
    x_wszystkie = []

    for i in range(l_iteracji):
        xpot = x + random.uniform(-rozrzut, rozrzut)
        if xpot < 0:
            xpot = 0
        elif xpot > 100:
            xpot = 100
        ypot = np.sin(xpot / 10.0) * np.sin(xpot / 200.0)
        if ypot >= y:
            x = xpot
            y = ypot
            rozrzut *= wsp_przyrostu
        elif ypot < y:
            rozrzut /= wsp_przyrostu
        print(f'Nr: {i}, rozrzut: {rozrzut}, x: {x}, y: {y}')
        y_wszystkie.append(y)
        x_wszystkie.append(x)

    zakres_x = np.linspace(0, 100, 100)
    zakres_y = np.sin(zakres_x / 10.0) * np.sin(zakres_x / 200.0)
    plt.plot(zakres_x, zakres_y)
    plt.scatter(x_wszystkie, y_wszystkie, color='red')
    plt.show()


def zad1():
    x = random.uniform(0, 100)
    y = np.sin(x / 10.0) * np.sin(x / 200.0)
    rozrzut = 10
    wsp_przyrostu = 1.1
    l_iteracji = 100
    y_wszystkie = []
    x_wszystkie = []

    for i in range(l_iteracji):
        xpot = x + random.uniform(-rozrzut, rozrzut)
        if xpot < 0:
            xpot = 0
        elif xpot > 100:
            xpot = 100
        ypot = np.sin(xpot / 10.0) * np.sin(xpot / 200.0)
        if ypot >= y:
            x = xpot
            y = ypot
            rozrzut *= wsp_przyrostu
        elif ypot < y:
            rozrzut /= wsp_przyrostu
        if i == 0 or i == 5 or i == 10 or i == 15:
            print(f'Nr: {i}, x: {x}, y: {y}')
            y_wszystkie.append(y)
            x_wszystkie.append(x)

    zakres_x = np.linspace(0, 100, 100)
    zakres_y = np.sin(zakres_x / 10.0) * np.sin(zakres_x / 200.0)
    plt.plot(zakres_x, zakres_y)
    plt.scatter(x_wszystkie, y_wszystkie, color='red')
    plt.show()

def zad2():
    x = random.uniform(0, 100)
    y = np.sin(x / 10.0) * np.sin(x / 200.0)
    rozrzut = 10
    wsp_przyrostu = 1.1
    l_iteracji = 100
    y_wszystkie = []
    x_wszystkie = []

    for i in range(l_iteracji):
        xpot = x + random.uniform(-rozrzut, rozrzut)
        if xpot < 0:
            xpot = 0
        elif xpot > 100:
            xpot = 100
        ypot = np.sin(xpot / 10.0) * np.sin(xpot / 200.0)
        if ypot >= y:
            x = xpot
            y = ypot
            rozrzut *= wsp_przyrostu
        elif ypot < y:
            rozrzut /= wsp_przyrostu
        if i <= 20:
            print(f'Nr: {i}, rozrzut: {rozrzut}, y: {y}')
            y_wszystkie.append(y)
            x_wszystkie.append(x)

    zakres_x = np.linspace(0, 100, 100)
    zakres_y = np.sin(zakres_x / 10.0) * np.sin(zakres_x / 200.0)
    plt.plot(zakres_x, zakres_y)
    plt.scatter(x_wszystkie, y_wszystkie, color='red')
    plt.show()


def zad3():
    x = random.uniform(15, 35)
    y = np.sin(x / 10.0) * np.sin(x / 200.0)
    rozrzut = 5
    wsp_przyrostu = 1.1
    l_iteracji = 100
    y_wszystkie = []
    x_wszystkie = []

    for i in range(l_iteracji):
        xpot = x + random.uniform(-rozrzut, rozrzut)
        if xpot < 0:
            xpot = 0
        elif xpot > 100:
            xpot = 100
        ypot = np.sin(xpot / 10.0) * np.sin(xpot / 200.0)
        if ypot >= y:
            x = xpot
            y = ypot
            rozrzut *= wsp_przyrostu
        elif ypot < y:
            rozrzut /= wsp_przyrostu
        if i <= 20:
            print(f'Nr: {i}, x: {x}, y: {y}')
            y_wszystkie.append(y)
            x_wszystkie.append(x)

    zakres_x = np.linspace(0, 100, 100)
    zakres_y = np.sin(zakres_x / 10.0) * np.sin(zakres_x / 200.0)
    plt.plot(zakres_x, zakres_y)
    plt.scatter(x_wszystkie, y_wszystkie, color='red')
    plt.show()


main()