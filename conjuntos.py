# a = {2, 4, 6, 8}
# print(a)
# a1 = set({2, 4, 6, 8})
# print(a1)

# b = {"casa", "A", 2, True, 10.50}
# print(b)

# # # # Conjuntos Vacios
# c = set()
# print(c)

# # Definimos conjuntos nuevos
# d = set([1, 2, 3, 4, 5])
# e = set('Hola')
# e1 = {'Hola'}
# f = {'A', 2, 3.5, (1,2)}
# print(d)
# print(e)
# print(e1)
# print(f)

# ##  Métodos add
# frutas = {'mango','pera','manzana'}
# frutas.add('fresa')
# print(frutas)

# ## Metodo discard Elimina un elemento si esta presente
# frutas = {'mango','pera','manzana'}
# frutas.discard('pera')
# print(frutas)

# ## Metodo remove Elimina un elemento, pero si no 
# ## lo encuentra lanza un error
# frutas = {'mango','pera','manzana'}
# frutas.remove('papaya')
# print(frutas)

# ## Metodo pop retorna un elemento en forma aleatoria
# frutas = {'mango','pera','manzana'}
# print(frutas.pop())
# print(frutas)

# ## Metodo clear Elimina los elementos de un conjunto
# frutas = {'mango','pera','manzana', 'uva'}
# print(frutas)
# frutas.clear()
# print(frutas)

## Metodo update Añadir elementos lista, tupla, string o conjunto
# frutas1 = {'mango','pera','manzana', 'uva'}
# frutas2 = {'mandarina','naranja','papaya','mango'}
# frutas1.update(frutas2)
# print(frutas1)

# ## Metodo len - obtiene la cantidad de elementos de un conjunto
# frutas = {'mango','pera','manzana', 'uva'}
# print(len(frutas))

## Operador in - para saber si un elemento esta contenido en un conjunto
# frutas = {'mango','pera','manzana', 'uva'}
# print('manzana' in frutas)
# print('melocoton' in frutas)

#### OPERACIONES SOBRE CONJUNTOS
# a = {1,2,3,4}
# b = {5,6,7,8,9}
# print(a | b)
# print(a.union(b))  # Tambien se puede usar union

# ## Interseccion de conjuntos
# a = {1,2,3,4}
# b = {5,2,7,4,9}
# print(a & b)
# print(a.intersection(b))

## diferencia de conjuntos
# a = {1,2,3,4,10,11,12}
# b = {5,2,7,4,9}
# print(b - a)
# print(a.difference(b))

## Diferencia simetrica de conjuntos
# a = {1,2,3,4}      # 2, 4
# b = {5,2,7,4,9}
# print(a ^ b)
# print(a.symmetric_difference(b))

## Inclusion de conjuntos
# a = {1,2,3,4,5,6,7,8,9}
# b = {5,2,7,4,9}
# print('a es subconjunto de b',a <= b)
# print('b es subconjunto de a',a >= b)

# ## Conjuntos disjuntos
a = {1,2,3,4}
b = {5,2,9,4,8}
print('a y b son disjuntos',a.isdisjoint(b))

c = {1,3,5,7,9}
d = {2,4,6,8}
print('c y d son disjuntos',c.isdisjoint(d))


