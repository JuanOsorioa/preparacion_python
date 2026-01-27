#Precios
bebes = 0
pequenos = 5000
grandes = 8000
adulto_mayor = 4000
tarifa = None
#Verificación de edad
edad = int(input("Por favor ingrese la edad: "))
#Identificación de tarifa según edad
if edad < 0:
    tarifa = "ERROR"
elif edad >= 60:
    tarifa = adulto_mayor
elif edad >= 12 and edad <= 59:
    tarifa = grandes
elif edad >= 5 and edad <= 11:
    tarifa = pequenos
else:
    tarifa = bebes
#Muestra resultados
print("La tarifa es: ", tarifa)


