#Mensajes
cuatro_o_mas_dias = "¡Excelente disciplina! + gana 1 punto de energía"
dos_o_tres_dias = "Bien, pero puedes dar más"
cero_o_un_dia = "No aflojes, tú puedes mejorar"
mensaje = None
#Puntos
puntos = 0
#Verificación días (bucle infinito)
while True:
    verificacion = int(input("Ingresa el número de días que entrenaste esta semana: "))
    #Evaluación
    if verificacion > 3:
        mensaje = cuatro_o_mas_dias
        puntos += 1
    elif verificacion >= 2 and verificacion <= 3:
        mensaje = dos_o_tres_dias
    else:
        mensaje = cero_o_un_dia
    #Muestra resultados
    print(mensaje)
    print("Puntos de energía: ", puntos)