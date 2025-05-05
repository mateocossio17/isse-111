anterior= 0 
lista =[]
for i in range (1,5):
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
        
for l in range(1,4):
    print("Corrida "+str(l))
    z =l
    for j in range(z , 4 ):
        print ("("+str(lista[l-1])+","+str(lista[j])+")")
