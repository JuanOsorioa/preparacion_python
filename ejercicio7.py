menu = 12000
bebida = 3000

print("El menú vale", menu)

ver_bebida = input("¿Desea incluir bebida? Seleccione S o N: ").lower()

if ver_bebida == "s":
    total = menu + bebida
else:
    total = menu

IVA = total * 8 / 100
total += IVA

print("El total a pagar + IVA es de:", total)
