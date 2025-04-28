#ejercicio 1
edad = 17

if edad >= 18:
  print("Puedes votar")
else:
  print("No puedes votar")
#ejercicio2 
numero1 = 8
numero2 =5 

if numero1 > numero2:
  print(f"El número mayor es {numero1}")
elif numero2 > numero1:
  print(f"El número mayor es {numero2}")
else:
  print("Ambos números son iguales")


# 3 
muestra = 81
if muestra <80 and muestra >95:
  print("calidad aceptable")

  

else: print ("calidad excelente ")
   
#ejercicio 
peso = 18  
if peso >= 5 : 
  print("ligero")
elif peso < 5 and peso >20: 
  print("medio")
elif peso >20 :
  print("pesado") 

#ejercicio 5 
anios = 8
salario = 1000
if anios < 5 and anios >= 10  :
  print(salario * 0.10)
elif anios > 10 : 
  print(salario * 0.20)
# ejercicio 6
numero_1 = 15
numero_2 = 30 
if(numero_1 and numero2 %3==0) and (numero_1 and numero2 %5==0):
  print("si son cosos")
 


  

  
  

#formulas de ingenieria 
x= 2 
y= 2
z= (x*x + y *y/ y + x )
print(z)
# identificador de triangulos 
lado_1 = 5
lado_2 = 10 
lado_3 = 5
if lado_1 == lado_2 and lado_2 == lado_3 :
  print ("felicidades , tu triandulo es equilatero")
elif lado_1 != lado_2 and lado_2 == lado_3 :
  print('felicidades tienes un triangulo isoceles ')
elif lado_1 == lado_3 and lado_2 != lado_1 : 
  print ('felicidades es isoceles ')
elif lado_1 != lado_2 and lado_2 != lado_3 and lado_1 != lado_3 :
  print ("es un triangulo escaleno")

#comprobador de año bisiesto 
año = 2100
if (año % 4 == 0 and año %100 != 0 ) or año % 400 == 0 :
    print('el  es bisiesto')
else:
  print("el año no es bisciesto bb")


#calculo costos de envio 
