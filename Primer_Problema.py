#Primer Problema. Escribe un programa en Python para multiplicar todos los elementos de un diccionario. 

Diccionario={
    "Angel":8,
    "Sol":4,
    "Jaime":10,
    "Cesar":5
}

def llave_indice(Diccionario,indice):
    lista_Diccionario=list(Diccionario)
    return(lista_Diccionario[indice])
    
def multiplicacion_diccionario(Diccionario,Numero):
    for i in range(0,len(Diccionario)):
        x=(Diccionario[llave_indice(Diccionario,i)]*Numero)
        Diccionario[llave_indice(Diccionario,i)]=x
    return(Diccionario)

print(multiplicacion_diccionario(Diccionario,4))