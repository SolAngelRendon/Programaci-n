#Decimocuarto Problema. Escribe un programa en Python para acceder al elemento de la clave de un diccionario por indice. Salida esperada: fisica matematicas quimica

Diccionario={
    'Fisica': 5, 
    'Matematicas': 13,
    "Quimica":22,
    "Lengua":87,
    "Historia":44
}

def llave_indice(Diccionario,indice):
    lista_dic=list(Diccionario)
    return(lista_dic[indice])
    
print(llave_indice(Diccionario,0),llave_indice(Diccionario,1),llave_indice(Diccionario,2))