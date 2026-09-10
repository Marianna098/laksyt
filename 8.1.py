import sqlite3

icao = input("Anna lentoaseman ICAO-koodi: ")

yhteys = sqlite3.connect("lentokentat.db")
kursori = yhteys.cursor()

sql = """
SELECT name, municipality
FROM airport
WHERE ident = ?
"""

kursori.execute(sql, (icao,))
tulos = kursori.fetchone()

if tulos:
    print(f"Lentokenttä: {tulos[0]}")
    print(f"Sijaintikunta: {tulos[1]}")
else:
    print("ICAO-koodia vastaavaa lentokenttää ei löytynyt.")

yhteys.close()