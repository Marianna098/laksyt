leiviskät = int(input("Anna leiviskät: "))
naulat = int(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

grammat = leiviskät * 20 * 32 * 13.3
grammat = grammat + naulat * 32 * 13.3
grammat = grammat + luodit * 13.3

kilot = int(grammat / 1000)
grammat = grammat - kilot * 1000

print("Massa nykymittojen mukaan:")
print(kilot, "kilogrammaa ja", grammat, "grammaa.")
