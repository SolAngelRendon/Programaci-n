prod = { "id" : 1, "Nombre" : "Sacapuntas", "Precio" : 3, "Cantidad" : 20 }
L1 = [prod]

def agregar(id, Nombre, Precio, Cantidad) :
    prod_2 = {"id" : id, "Nombre" : Nombre, "Precio" : Precio, "Cantidad" : Cantidad }
    L1.append(prod_2)
    print(L1)
    
print("La lista nueva es :", L1)