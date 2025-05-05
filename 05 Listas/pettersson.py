""" 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
range.

list = list(range(0,102, 4))

print(list)"""

""" 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
indexing con números negativos!

list = [1,2,3,4,5]

print(list[-1])
"""

""" 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
ejemplo: []

list = []

list.append("Hola")
list.append("Chau")
list.append("Mundo")

print(list)
"""

""" 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"] 

animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"
animales[-1] = "oso"

print(animales)
"""

""" 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza

# Creamos la lista con los numeros
numero = [8,15,3,22,7]

# Esto elimina el numero mas grande de la lista
numero.remove(max(numero))

# Y imprimimos la lista modificada
print(numero) """

""" 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
pantalla los dos primeros. 

numero = list(range(10,35,5))

print(numero[0])
print(numero[-1])
"""

""" 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
cualesquiera. 

autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "hilux"
autos[2] = "sandero"

print(autos)"""

""" 8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
directamente. Imprimir la lista resultante por pantalla. 

dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)
"""

""" 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
diferentes clientes:


compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]

compras[2].append("jugo")
compras[1][1] = 'tallarines'
compras[0].remove("pan")

print(compras) """

""" 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]


print(lista_anidada[0],
lista_anidada[1],
lista_anidada[2][0],
lista_anidada[2][1],
lista_anidada[2][2],
lista_anidada[3]), """
