luvut = []
while True:
    luku = float(input("Anna luku: "))

    if luku == "":
        break

    luvut.append(luku)

    if luvut:
        print(f"Pienin luku: {min(luvut)}")
        print(f"Suurin luku: {max(luvut)}")



