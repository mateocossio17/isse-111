
def es_primo(n):
    for i  in range ( 2 , n):
         if (n % i == 0   ):
              return False
    return True     
def main ():
    n = 0
    while (n!=-1):
        n= int (input("Escribe un numero, si quieres salir escribe -1 : "))
        if (n==-1):
            print("Fin")
        if(es_primo(n)):
            print(str(n)+" es primo ")
        else:
            print(str(n)+" no es primo ") 
main()

        

     

