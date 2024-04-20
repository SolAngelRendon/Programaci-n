#Decimoquinto Problema. Escribe un programa en Python para convertir un diciconario en una lista de listas.
#Diccionario original:

Dic_Original={
    1:"rojo",
    2:"azul",
    3:"negro",
    4:"blanco",
    5:"negro"
}

def llave_indice(Diccionario,indice):
    lista_Diccionario=list(Diccionario)
    return(lista_Diccionario[indice])

L1=[]

for i in range(0,len(Dic_Original)):
    lista2=[llave_indice(Dic_Original,i),Dic_Original[llave_indice(Dic_Original,i)]]
    L1.append(lista2)
    
print(L1)
    
