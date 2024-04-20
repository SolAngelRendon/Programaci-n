#Segundo Problema. Escribe un programa en Python para eliminar una clave de un diciconario. 

Diccionario={
    "Angel":4,
    "Sol":8,
    "Jaime":5,
    "Cesar":3
}

x=input("La clave a eliminar: ")
del Diccionario[x]
print(Diccionario)