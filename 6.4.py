def laske_summa(luvut):
    summa = 0

    for luku in luvut:
        summa += luku

    return summa
luvut = [2, 5, 7, 10]

summa = laske_summa(luvut)

print("Lukujen summa on:", summa)