#Solicitud de datos
precio_unidad = 2000
unidades = int(input("Ingrese el número de unidades: "))
#Sumatoria
total = unidades * precio_unidad
#Descuentos y valor de envio
des_treinta = total * 15 / 100
des_diez = total * 5 / 100
envio = 5000
#Evaluación de condiciones
if unidades >= 30:
    total -= des_treinta
    print("Descuento del 15","%"," aplicado")
elif unidades >= 10:
    total -= des_diez
    print("Descuento del ","5%"," aplicado")
if total < 50000:
    total += envio
    print("Precio del envío incluido")
print("El total a pagar es de: $", total, " pesos")



