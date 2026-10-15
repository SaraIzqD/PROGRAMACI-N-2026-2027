talleres = [
    ("Fotografía", ["Ana", "Luis"],
     {"aula": 12, "plazas": 4},
     {"cámara", "tarjeta de memoria"}),

    ("Robótica", ["Marta"],
     {"aula": 15, "plazas": 3},
     {"portátil", "cable USB"}),

    ("Pintura", [],
     {"aula": 8, "plazas": 5},
     {"pinceles", "acuarelas", "papel"})
]

while True:
    print("\n1. Mostrar talleres")
    print("2. Inscribir alumno")
    print("3. Cancelar inscripción")
    print("4. Cambiar aula")
    print("5. Añadir material")
    print("6. Terminar")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        for t in talleres:
            print("\nTaller:", t[0])
            print("Aula:", t[2]["aula"])
            print("Alumnos:", t[1])
            print("Plazas libres:", t[2]["plazas"] - len(t[1]))
            print("Materiales:", t[3])

    elif opcion == "2":
        nombre = input("Taller: ")
        alumno = input("Alumno: ")

        for t in talleres:
            if t[0].lower() == nombre.lower():
                if len(t[1]) < t[2]["plazas"]:
                    if alumno not in t[1]:
                        t[1].append(alumno)
                        print("Alumno inscrito")
                    else:
                        print("El alumno ya está inscrito")
                else:
                    print("No hay plazas libres")
                break
        else:
            print("Taller no encontrado")

    elif opcion == "3":
        nombre = input("Taller: ")
        alumno = input("Alumno: ")

        for t in talleres:
            if t[0].lower() == nombre.lower():
                if alumno in t[1]:
                    t[1].remove(alumno)
                    print("Inscripción cancelada")
                else:
                    print("El alumno no está inscrito")
                break
        else:
            print("Taller no encontrado")

    elif opcion == "4":
        nombre = input("Taller: ")
        aula = int(input("Nueva aula: "))

        for t in talleres:
            if t[0].lower() == nombre.lower():
                t[2]["aula"] = aula
                print("Aula cambiada")
                break
        else:
            print("Taller no encontrado")

    elif opcion == "5":
        nombre = input("Taller: ")
        material = input("Material: ")

        for t in talleres:
            if t[0].lower() == nombre.lower():
                if material not in t[3]:
                    t[3].add(material)
                    print("Material añadido")
                else:
                    print("El material ya existe")
                break
        else:
            print("Taller no encontrado")

    elif opcion == "6":
        print("Programa terminado")
        break

    else:
        print("Opción incorrecta")