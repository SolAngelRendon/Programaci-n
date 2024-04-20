#Octavo Problema. Escribe un programa en Python paraverificar si un diciconario esta vacio o no.

Dic_1={
    "Angel":12,
    "Sol":4,
    "Jaime":6,
    "Cesar":17
}

Dic_2={}

Diccionarios=[Dic_1,Dic_2]

for i in range(0,len(Diccionarios)):
    if len(Diccionarios[i]) == 0:
        print(f"El diccionario {i+1} esta vacio")
    else:
        print(f"El diccionario {i+1} no esta vacio")
