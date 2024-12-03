import random
import numpy as np
import matplotlib.pyplot as plt

def _plus_1(x,y,rozrzut, wsp_przyrostu, l_iteracji, x_wszystkie, y_wszystkie):
    for i in range(l_iteracji):
        xpot = x + random.uniform(-rozrzut, rozrzut)
        if xpot < 0:
            xpot = 0
        elif xpot > 100:
            xpot = 100
        ypot = np.sin(xpot/10.0)*np.sin(xpot/200.0)
        if ypot >= y:
            x = xpot
            y = ypot
            rozrzut *= wsp_przyrostu
        elif ypot<y:
            rozrzut /= wsp_przyrostu
        print(f'Nr: {i}, rozrzut: {rozrzut}, x: {x}, y: {y}')
        y_wszystkie.append(y)
        x_wszystkie.append(x)
    return x_wszystkie, y_wszystkie


