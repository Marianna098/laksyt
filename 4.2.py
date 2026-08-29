while True:
    tuuma = float(input("Anna tuumat"))

    if tuuma < 0:
        break
sentit = tuuma * 2.54

print(f"{tuuma} tuumaa = {sentit} cm")