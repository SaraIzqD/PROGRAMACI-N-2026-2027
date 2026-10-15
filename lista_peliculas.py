# Lista de películas: cada película es una tupla (título, duración)
peliculas = [
    ("Shrek", 90),
    ("Toy Story", 81),
    ("Buscando a Nemo", 100)
]

# 1. Mostrar los tipos de estructuras
print(type(peliculas))      #<class 'list'>
print(type(peliculas[0]))   #<class 'tuple'>

# 2. Recorrer la lista y mostrar cada película
print("\nPeliculas iniciales: ")
for pelicula in peliculas:
    print("Titulo: ", pelicula[0], "-Duracion: ", pelicula[1], "minutos")

# 3. Añadir una película con append()
peliculas.append(("Los increibles", 115))

# 4. Mostrar todas las películas para comprobar que se ha añadido
print("\nPeliculas actualizadas: ")
for pelicula in peliculas:
    print("Titulo: ", pelicula[0], "-Duracion: ", pelicula[1], "minutos")

# 5. Intentar cambiar la duración de Shrek
peliculas[0] = ("Shrek", 95)
print("No se puede cambiar la duracion de la pelicula de Shrek porque es una tupla")
