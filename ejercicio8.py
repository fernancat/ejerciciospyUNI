producto = input("Ingrese el nombre del producto: ")
precio = round(float(input("Ingrese el precio del producto: ")),2) 

v = str(precio).split(".")


print(f" Los euros de  {producto} son: {v[0]}, y su numero de centimos es: {v[1]}")