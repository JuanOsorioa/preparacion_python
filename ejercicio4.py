import sys
#Precios
precio_chocolate = 4000
precio_vainilla = 3500
precio_topping = 1000
# Verificación sabor
total = 0
verificacion = str(input("Por favor ingrese el sabor: "))
if verificacion != "chocolate" and verificacion != "vainilla":
    sys.exit("Sabor no disponible")
elif verificacion == "chocolate":
    total = precio_chocolate
else:
    total = precio_vainilla
# Selección Topping
verificacion_topping = str(input("¿Desea añadir topping?: "))
if verificacion_topping == "si":
    total += precio_topping
if total > 0:
    print("El total a pagar es: ", total)





