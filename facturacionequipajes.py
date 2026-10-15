numero_equipajes = int(input("Introduzca el numero de equipajes que se van a facturar: "))
coste_total = 0

for i in range (numero_equipajes, 0, -1):
    peso_equipaje = float(input("Introduzca el peso del equipaje: "))
    if peso_equipaje <= 10:
        print("Se considera equipaje de mano y es gratuito")
        coste = 0

    elif 10 < peso_equipaje <= 20:
        print("Debe facturarse y cuesta 20 euros")
        coste = 20

    else:
        coste = 20 + (peso_equipaje-20) * 5


    coste_total = coste_total + coste

    print("El precio total del equipaje es: ", coste_total, "euros")



