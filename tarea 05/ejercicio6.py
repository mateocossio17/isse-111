meta_usuario=int(input("introduce tu meta de ahorros:"))
ahorro = 5
punto_inicio=5 
cantidad_dias = 1
while (ahorro < meta_usuario):
    ahorro = ahorro *2
    cantidad_dias= cantidad_dias + 1
print ("tu meta se alcanzara en ",cantidad_dias," dias.")