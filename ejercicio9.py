fecha = input("Escribe la fecha de tu nacimiento en este formato:dd/mm/aaaa:  ")

fecha = fecha.split("/")

print(f" El dia de tu nacimiento es: {fecha[0]} , Dia: {fecha[1]}, Año: {fecha[2]}")