aterior= 0 
lista =[]
for i in range (1,6):
    print(str(i))
    if (i ==1) : 
        n=  int (input("Escribe un numero: "))
        lista.append(n)
        anterior = n
    else:
        n= int (input("introduxca un valor numerico:"))
        lista.append(n)
        while (anterior == n):
            print ("no se puede repetir")
            n= int(input("introduzca otro valor "))
            lista.append(n)
        anterior = n
mayor=lista[0]
mayor2= lista[0]
indicemayor=0
for i in range(0,5):
    if (lista[i]>mayor ):
        indicemayor=i
        mayor=lista[i]   
if (indicemayor == 0): mayor2 =lista[1]
for i in range (0,5):
    if (i != indicemayor and lista[i]> mayor2):
        mayor2=lista[i]
producto = mayor2 * mayor 
print("el producto mayor es: ",producto) 