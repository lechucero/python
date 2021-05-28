# Metodo count()
## Busca un elemento en una tupla y retorna el 
## número de veces que se repita
# t = (0, 1, 2, 3, 2, 4, 5, 2, 2)
# print(t.count(2))
# print(t.count(5))
# a = ('manuel','oscar','manuel')
# print(a.count('manuel'))

# tupla = ('Curso', 15, True, 150.20, 150.20, False, 'Alumno')
# print(tupla.count('Alumno'))  #Imprime 1

# # Metodo index()
# ## Busca el elemento en una tupla y retorna el 
# # ## número indice
# t = (0, 1, 2, 3, 2, "Z", 4, 5, 2, 2)
#print(t.index("Z"))

# # Unpack
# ## Se puede asiganr los valores de una tupla a variables
# t = ("manzana", "pera", "naranja", "uva")
# (s1, s2, s3, s4) = t

# # # #Imprimimos el elemento ceo 0
# print(t[2])   # Imprime manzana
# # # # Imprimimos la variable s1
# print(s3)

# # Actualización
# ## Los elementos de las tuplas no pueden ser actulizados
# # ## a diferencia de las listas que si se puede
# profesor = ("Yosip", "Urquizo", "Gómez")
# #profesor[1] = "Morales"  # Genera un error al ejecutar

# # ## Pero si podemos concatenar una tupla con otra
# direccion = ("Victor Larco", "Trujillo")
# datos_del_profesor = profesor + direccion
# print(datos_del_profesor)

# # Operaciones
# ## Las tuplas responden a los signos + y *
# ## + significa concatenacion
# # ## * significa repeticion
a = (1, 2, 3, 4, 5, 6, 7, 8)
b = (4, 5, 6)

# longitud = len(a + b)
# print(longitud)   # 3

# concatenar = a + b
# print(concatenar)   # 1,2,3,4,5,6

# afiliacion = 7 in a
# print(afiliacion)   # True

# # #iteraccion
for xy in (a+b):print(xy, end='')
