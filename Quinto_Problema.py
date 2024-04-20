#Quinto Problema. Escreibe un programa en Python para obtener los valores maximos y minimos de un diccionario.

Diccionario={
    "Angel":10,
    "Sol":30,
    "Jaime":15,
    "Cesar":20
}

def llave_indice(Diccionario,indice):
    lista_Diccionario=list(Diccionario)
    return(lista_Diccionario[indice])


def valores_max_y_min(Diccionario):
    L1=[]
    for i in range(0,len(Diccionario)):
        L1.append(Diccionario[llave_indice(Diccionario,i)])

    for j in range(0,len(L1)):
        if L1[j] == min(L1):
            print(llave_indice(Diccionario,j),":", Diccionario[llave_indice(Diccionario,j)])
        elif L1[j] == max(L1):
            print(llave_indice(Diccionario,j),":", Diccionario[llave_indice(Diccionario,j)])

valores_max_y_min(Diccionario)