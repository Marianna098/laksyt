biologinen_sukupuolen = input("Anna biologisen sukupuolen: ")
hemoglobiiniarvo = int(input("Anna hemoglobiiniarvon: "))

if biologinen_sukupuolen == "Nainen":
    if hemoglobiiniarvo < 117:
        print("Hemoglobiiniarvo alhainen")
    elif hemoglobiiniarvo <= 175:
        print("Hemoglobiiniarvo normaali")
    elif hemoglobiiniarvo > 175:
        print("Hemoglobiiniarvo korkea")

if biologinen_sukupuolen == "Mies":
    if hemoglobiiniarvo < 134:
        print("Hemoglobiiniarvo alhainen")
    elif hemoglobiiniarvo <= 195:
        print("Hemoglobiiniarvo normaali")
    elif hemoglobiiniarvo > 195:
        print("Hemoglobiiniarvo korkea")
