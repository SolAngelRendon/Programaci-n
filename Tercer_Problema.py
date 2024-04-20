#Tercer Problema. Escribe un programa en Python para convertir dos listas en un diccionario.

L1=["lapiz","sacapuntas","borrador"]
L2=["mochila","libreta","estuchera"]

Diccionario={}

for i in range(0, len(L1)):
    Diccionario[str(L2[i])]=str(L1[i])
    
print(Diccionario)
