print("""
Escribe tu numero de telefono como en el siguiente fromato: prefijo-número-extension, por ejemplo  +34-913724710-56 (separalo por guiones) """)
      
numeroTelefono = input(": ")

numeroTelefono = numeroTelefono.split("-")

print(f"numero de telefono sin prefijo ni extension: {numeroTelefono[1]} ")