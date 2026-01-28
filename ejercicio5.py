#Se importa sys para poder detener el programa cuando sea necesario
import sys
#Se establecen los valores y descuentos
total = 0
libro = 25000
quince_porciento = libro * 15 / 100
codigo = "LIBRO10"
codigo_usuario = None
#Se verifica si es estudiante y si el descuento aplica
print("Bienvenido a la libreria El Saber. El libro seleccionado cuesta 25000")
verficacion_estudiante = str(input("¿Usted es estudiante? Escriba si o no: ")).lower()
# Si no aplica se muestra el total y se interrumpe la ejecución del programa
if verficacion_estudiante != "si":
    total += libro
    print("El total a pagar es: ", total)
# Si es estudiante se valida el posible código de descuento
else:
    print("Descuento del ""15%"" por ser estudiante aplicado")
    total += libro
    total -= quince_porciento
    verificacion_codigo = str(input("¿Usted tiene código de descuento? Escriba si o no: ")).lower()
    if verificacion_codigo == "si":
# Se verifica el código de descuento
        codigo_usuario = str(input("Ingrese el código de descuento: "))
        if codigo_usuario == codigo:
            print("Descuento del ""10%"" aplicado")
            diez_porciento = total * 10 / 100
            total -= diez_porciento
            print("El total a pagar es: ", total)
            sys.exit()
        else:
            print("CÓDIGO INVALIDO")
            print("El total a pagar es: ", total)
            sys.exit()
    else:
        print("El total a pagar es: ", total)






