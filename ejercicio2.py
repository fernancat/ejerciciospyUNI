nombreCompleto = input("Ingresa tu nombre completo: ")

print(nombreCompleto.lower())
print(nombreCompleto.upper())


palabras = nombreCompleto.split(" ")

for i in palabras:
    print(i.capitalize(), end=" ")