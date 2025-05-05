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
        anterior = n
anterior = lista[0]
ascendiente = True
descendiente = True
for i in range (0,5):
    if (lista[i]<anterior):
        ascendiente = False
        break
    else:
        anterior = lista [i]
anterior = lista[0]
for i in range (0 , 5):
    if (lista[i]>anterior):
        descendiente =False
        break
    anterior = lista[i]
if (descendiente==False and ascendiente==False):
    print("es de orden ramdon ")
elif(ascendiente == True):
    print("es ascendiente")
elif(descendiente==True):
    print("es descendiente")