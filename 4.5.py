yritykset = 0
while yritykset < 5:
    kayttunnus = input("Anna kayttäjätunnus: ")
    salasana = int(input("Anna salasana: "))

    if kayttunnus == "Marianna" and salasana == "12345":
        print("Terveutloa!")
        break

    yritykset += 1

else:
    print("Pääsy evätty")