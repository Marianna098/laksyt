kaupungit = []

print("Anna viiden kaupungin nimi:")

for i in range(5):
    kaupunki = input(f"Kaupunki {i + 1}: ")
    kaupungit.append(kaupunki)

print("\nSyöttämäsi kaupungit:")

for kaupunki in kaupungit:
    print(kaupunki)