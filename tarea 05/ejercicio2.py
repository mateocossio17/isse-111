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
numero_a_buscar= int(input("numero a buscar : "))
anterior = lista[0]
no_encontrado = True
for i in range(0,4):
    if (numero_a_buscar==lista[i] ):
        print("El numero esta en la lista, en la posicion "+ str(i+1))
        no_encontrado = False
        break
if (no_encontrado): print("Numero "+str(numero_a_buscar)+" no se encuentra en la lista")