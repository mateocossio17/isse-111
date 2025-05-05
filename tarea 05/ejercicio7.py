numero=int(input("introduce tu numero: "))
palabra= str(numero)

nuevo =''
lista = []
i =0
for letra in palabra:
   lista.append(letra)
   i=i+1

for j in range (i-1,-1,-1):
   nuevo =nuevo+lista[j]
   
numero_volcado = int(nuevo)
if (numero_volcado == numero):
   print("El numero ",numero, " es palindromo")
else:
   print("El numero ",numero, " NO es palindromo")