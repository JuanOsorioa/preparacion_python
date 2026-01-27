# Primero establezco los datos conocidos
descuento_mas_cincuenta = 20
descuento_mas_veinte = 10
precio_unidad = 300
# Luego Solicito la información al cliente
unidades = int(input("Ingrese la cantidad de panes a comprar: "))
# Despues se hace el calculo total
total = precio_unidad * unidades
# Se aplican los descuentos según corresponde
if unidades < 0:
    total = "CANTIDAD INVALIDA"
elif unidades > 50: 
    total = total - total * descuento_mas_cincuenta / 100
elif unidades > 20: 
    total = total - total * descuento_mas_veinte / 100
 # Se imprime
print(total)

 