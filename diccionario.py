arqueros = {
    1:"Pedro Gallese",
    2:"Carlos Cáceda"
}

# print(productos)

# delanteros = {
#     9:"Jugador 09",
#     10:"Jugador 10",
#     11:"Jugador 11",
#     14:"Jugador 14",
#     18:"Jugador 18"
# }

usuarios = {
    "user01": "u001",
    "clave01": "@123456",
    "user02": "u002",
    "clave02": "@123456"
}
# print(arqueros)
# print(delanteros)
# print(usuarios)

# productos = {
#     1:"Laptop Lenovo",
#     2:"Mouse Logitech",
#     3:"Impresora Epson",
#     4:"Tarjeta de Sonido EVO 4"
# }

# ## Metodos items() -> Lista los elementos de un diccionario
# print(productos)
# for p in productos.items():
#      print(p)

#len() cuenta los elementos de un diccionario
# c = len(productos)
# print(c)

# print(len(arqueros))
# print(len(delanteros))

# Keys() Listado de las claves del diccionario
# print(productos.keys())
# for p in productos.keys():
#     print(p)

# print(arqueros.keys())
# for var in arqueros.keys():
#     print(var)

#values() devuelve los valores de un diccionario
# print(productos.values())
# for p in productos.values():
#     print(p)

# print(arqueros.values())
# for var in delanteros.values():
#     print(var)
productos = {
    1:"Laptop Lenovo",
    2:"Mouse Logitech",
    3:"Impresora Epson",
    4:"Tarjeta de Sonido EVO 4"
}
delanteros = {
    9:"Jugador 09",
    10:"Jugador 10",
    11:"Jugador 11",
    14:"Jugador 14",
    18:"Jugador 18"
}
for p in productos.values():
     print(p)

# Agregar un nuevo Item
# productos[5] = "Audifonos EVO"
# print(productos)
# for p in productos.values():
#     print(p)

# pop() Eliminaba un registro del dicconario
# e = productos.pop(2)
# print(e)
# print(productos)

# arqueros[3] = "Juan Perez"
# print(arqueros)

# print(arqueros.pop(1))
# print(arqueros)

# copy() Copiar contenido en un diccionario
# prod2 = productos.copy()
# print(prod2)

# dict2 = arqueros.copy()
# print(arqueros)
# print(dict2)

# delanteros = arqueros.copy()
# print(delanteros)

# clear() Limpia un diccionario
# prod2.clear()
# print(prod2)

# dict2.clear()
# print(dict2)

# print(arqueros.update(delanteros))

# d = {
#         1: "uno", 
#         2: "tres"
#     }
# d1 = {
#         1: 1,
#         2: "dos",
#         3: 15.30
#     }

# # # # updates the value of key 2
# d.update(d1)
# print(d)
# print(d1)

# get() Muestra el valor del diccionario desde su key
print(productos.get(1))
print(productos.get(4))

# print(delanteros.get(11))