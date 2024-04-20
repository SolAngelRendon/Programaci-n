#Noveno Problema. Decimo Problema. Onceavo Problema. Escribe un programa en Python para extraer una lista de valores de una lista dada de diccionarios.
#Diccionario original:

Dic_original=[{'Matematicas': 90, 'ciencia': 92}, {'matematicas': 89, 'ciencia': 94}, {'Matematicas': 92, 'ciencia': 88}]

def llave_indice(Diccionario,indice):
    lista_Diccionario=list(Diccionario)
    return(lista_Diccionario[indice])

def lista_values(Diccionario, asignatura):
    L1=[]
    for i in range(0,len(Diccionario)):
        for x in range(0,len(Diccionario[i])):
            y=llave_indice(Diccionario[i],x)
            if y.lower() == asignatura.lower():
                L1.append(Diccionario[i][y])
    return L1
    L1=[]
    
print("La lista de matematicas es :",lista_values(Dic_original, "Matematicas"))
print("La lista de ciencias es :",lista_values(Dic_original, "ciencia"))
