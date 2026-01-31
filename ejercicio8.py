#Se preparan las variables
tecnica = float(input("Ingrese la nota técnica (De 0.0 a 5.0 solamente): "))
logica = float(input("Ingrese la nota lógica (De 0.0 a 5.0 solamente): "))
nota_final = None
estado = None
#Se valida que las notas estén dentro del rango permitido
if 0.0 <= tecnica <= 5.0 and 0.0 <= logica <= 5.0 :
    nota_final = (tecnica * 0.7) + (logica * 0.3)
    if nota_final >= 3:
        estado = "APROBADO"
    elif nota_final >= 2 and nota_final < 3:
        estado = "REVISION"
    else:
        estado = "REPROBADO"
    print("Su nota final es: ", nota_final, "Y su estado es: ", estado)
else:
    print("Las notas están fuera de los rangos para evaluar")

