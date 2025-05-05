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
aterior= 0 
lista2 =[]
for i in range (1,6):
    print(str(i))
    if (i ==1) : 
        n=  int (input("Escribe un numero: "))
        lista2.append(n)
        anterior = n
    else:
        n= int (input("introduxca un valor numerico:"))
        lista2.append(n)
        while (anterior == n):
            print ("no se puede repetir")
            n= int(input("introduzca otro valor "))
            lista2.append(n)
        anterior = n
suma1=0
suma2=0 
for i in range (0,4):
    suma1=suma1 + lista[i]
    suma2= suma2 + lista2[i]
if(suma1>suma2):
    print("el equipo 1 gano")
elif(suma2>suma1):
    print("el equipo 2 gano")
else:
    print("los equipos empataron")