edad = int(input("¿Cuántos años tienes?: "))
altura = int(input("¿Cuánto mides (en centímetros)?: "))
acompañado = input("¿Vas acompañado (sí o no)?")
if altura <120:
   print("Lo sentimos, no puede subir a la atracción")
elif edad >=12:
   print("Puedes subir a la atracción")
elif acompañado == "sí":
   print("Puede subir a la atracción yendo acompañado")
else:
   print("No puedes subir")