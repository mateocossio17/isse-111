anterior= 0 
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
suma=0
for i in range(0,5):
    if(lista[i]%2==0):
        suma = suma + lista[i]
print("la suma de los pares es: ",suma)
