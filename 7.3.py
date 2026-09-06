lentoasemat = {}
while True:
    print("1 - Syötä uusi lentoasema")
    print("2 - Hae lentoasema")
    print("3 - Lopeta")
    valinta = input("Valitse toiminto: ")

    if valinta == "1":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi

    elif valinta == "2":
        icao = input("Anna ICAO-koodi: ")
        if icao in lentoasemat:
            print(lentoasemat[icao])
        else:
            print("Lentoasemaa ei löydy.")

    elif valinta == "3":
        break