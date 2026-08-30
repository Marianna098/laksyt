import random
maara = int(input("Anna arpakuutioiden lukumäärä: "))
summa = 0

for i in range(maara):
    luku = random.randint(1, 6)
    summa += luku

print(f"Silmälukujen summa: {summa}")
