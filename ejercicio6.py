import sys
#Se establecen los valores
valor_hora = 2000
multa = 5000
total = 0
#Se solicita el número de horas que se usó el parqueadero
horas = int(input("Ingrese el número de horas que usó: "))
#Se verifica el positivo del número
if horas <= 0:
    print("No se permiten números menores a 1")
    sys.exit()
if horas > 5:
    total = horas * valor_hora
    total += multa
    mensaje = "Multa aplicada"
else:
    total = horas * valor_hora
    mensaje = "Multa no aplicada"
print("El total a pagar es: ", total)
print(mensaje)