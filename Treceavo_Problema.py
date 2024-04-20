#Treceavo Problema. Escribe un programa en Pyhton para obtener la profundidad de un dicionario. 

diccionario={"x":{"y":8,"z":{"k":{"w":12}}}}

def deep(diccionario):
    if isinstance(diccionario, dict):
        return 1+(max(map(deep, diccionario.values())) if diccionario else 0)
    return 0
        
print(deep(diccionario))