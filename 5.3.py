luku = int(input("Anna kokonaisluku: "))

if luku <= 1:
    alkuluku = False
else:
    alkuluku = True
    for i in range(2, int(luku**0.5) + 1):
        if luku % i == 0:
            alkuluku = False
            break

if alkuluku:
    print(f"Luku {luku} on alkuluku.")
else:
    print(f"Luku {luku} ei ole alkuluku.")