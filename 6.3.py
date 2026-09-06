def gallonat_litroiksi(gallonaa):
    return gallonaa * 3.785


while True:
    gallonat = float(input("Anna gallonamäärä: "))

    if gallonat < 0:
        break

    litrat = gallonat_litroiksi(gallonat)
    print(f"{litrat:.3f} litraa")