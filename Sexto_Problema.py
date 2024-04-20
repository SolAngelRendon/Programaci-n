#Sexto Problema. Escribe un programa en Python para obtener un diccionario a partir de los campos de un objeto. 

class Videojuego:
    def __init__(self, nombre, marca, color, genero):
        self.nombre = nombre
        self.marca = marca
        self.color = color
        self.genero = genero


Juego = Videojuego("SmashBros", "Nintendo", "Rojo","Entretenimiento")

Diccionario = vars(Juego)

print(Diccionario)