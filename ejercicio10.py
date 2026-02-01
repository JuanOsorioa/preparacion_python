#Solicitud de datos
edad = int(input("Ingrese su edad: "))
documento = str(input("¿Tiene documento? S o N: ")).lower()
#Validación de ingreso
if edad >= 18:
    if documento == "s":
        print("ENTRADA PERMITIDA")
    else:
        print("DEBE PRESENTAR DOCUMENTO")
else:
    print("ENTRADA DENEGADA")