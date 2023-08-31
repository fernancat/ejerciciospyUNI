l = []
cadena = ""
num =int(input("Numero de productos que lleva: "))

for i in range (1, num+1):
   p = input(f"Ingrese el producto {i}: ")
   l.append(p)
   cadena+= p + " " + "\n"

print("Producto que contiene en la sesta: " + cadena)    