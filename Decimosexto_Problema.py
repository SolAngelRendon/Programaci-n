#Decimosexto Problema. Escribeun programa en Python para filtrar numeros pares de un diccionario de valores.
#Diccionario Original:
    
Dic_1= {
    'V': [1, 4, 6, 10], 
    'VI': [1, 4, 12], 
    'VII': [1, 3, 8]
}

Dic_2={
    'V': [1, 3, 5], 
    'VI': [1, 5], 
    'VII': [2, 7, 9]
}

def llave_indice(Diccionario,indice):
    lista_Diccionario=list(Diccionario)
    return(lista_Diccionario[indice])

def filtrar_pares(Diccionario):
    for i in range(0,len(Diccionario)):
        y=llave_indice(Diccionario,i)
        x=Diccionario[y]
        L1=[]
        for j in range(0,len(x)):
            if not x[j]%2==1:
                L1.append(x[j])
        Diccionario[str(y)]=L1
    return (Diccionario)

print(filtrar_pares(Dic_1))
print(filtrar_pares(Dic_2))