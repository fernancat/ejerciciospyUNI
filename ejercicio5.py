frase = input("Ingresa una frase: ")

#print(frase[::-1])
count = len(frase) -1

for i in range(0, count +1):
    print(frase[count], end=" ")
    count-=1

