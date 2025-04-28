def nombre_funcion():
    print("salida de fincion ")

def nombre_funcion2():
    print("funcion 22")

def funcion_retorno():
    return 123
def obtener_edad():
    edad= int(input("indique su edad "))
    if (edad > 0):
        return edad
    else:
        return ("error ")
    
def calcular_descuento_producto():
    precio_original = 100
    descuento = 20 
    precio_decuento= (precio_original* descuento)/100 
    precio_final=precio_original - precio_decuento
    return precio_final 
def calcular_descuento_producto_mejorado (precio_original , descuento ):
    precio_descuento = (precio_original* descuento)/100
    precio_final= precio_original - precio_descuento
    return precio_final
def calcular_descuento_profucto_mejorado_2(precio_original , descuento ):
    return precio_original -(precio_original- descuento )/100

    
#salida a consola 
precio_original = int (input ("ingrese el precio del producto : "))
descuento = int (input("ingrese el descuento : "))





#1 edad minima para votar 
def edad_minima_votar():
    print("la edad es 18 anios ")
#solicitar el mayor de dos numeros 
def mayor_dos_num(numA , numB ):
    if(numA==numB): "IGUALES"
    if (numA>numB):
        return numA
    if(numB>numA):
        return numB


#consola 
edad_minima_votar()
var_numA=int(input("ingrese el numero a : "))
var_numB = int(input("ingrese el numero b : "))
var_num_mayor= mayor_dos_num(var_numA ,var_numB )
print(var_num_mayor)



# algoritmo baseree
def recorrer_digitos(num):
    while(num>0 ):
        dig= num %10 
        print(dig)
        num = num //10

#par impar de los dig 
def par_impar_dig(num)

