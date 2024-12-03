import random
import numpy as np
import matplotlib.pyplot as plt

def func(x1, x2):
    return np.sin(x1 * 0.05) + np.sin(x2 * 0.05) + 0.4 * np.sin(x1 * 0.15) * np.sin(x2 * 0.15)

def mu_lambda(mu, lambd, turniej_rozmiar, mutacja_poziom, iteracje_liczba, zadane_iteracje):
    pula_r = [[random.uniform(0, 100) for _ in range(2)] for _ in range(mu)]
    kopie_r = []
    kopie_p = []

    for i in range(iteracje_liczba):
        fosobnik = [func(x1, x2) for x1, x2 in pula_r]
        pula_p = []

        for _ in range(lambd):
            oss_turniej = random.sample(pula_r, turniej_rozmiar)
            os_n = max(oss_turniej, key=lambda osobnik: func(*osobnik))
            mutacja = [
                os_n[0] + random.uniform(-mutacja_poziom, mutacja_poziom),
                os_n[1] + random.uniform(-mutacja_poziom, mutacja_poziom)
            ]
            mutacja = [max(0, min(100, gen)) for gen in mutacja]
            pula_p.append(mutacja)

        fpotomny = [func(xp1, xp2) for xp1, xp2 in pula_p]
        pula_rp = pula_r + pula_p
        frp = fosobnik + fpotomny
        najlepsze_id = np.argsort(frp)[-mu:]
        pula_r = [pula_rp[i] for i in najlepsze_id]

        if i + 1 in zadane_iteracje:
            kopie_r.append(pula_r.copy())
            kopie_p.append(pula_p.copy())

    return kopie_r, kopie_p

