# import random

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), 
# en orden creciente, mostrando un número por línea

""" for i in range(0, 101):
    print("Numero: ", i)
"""

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

""" numero = int(input("Ingresa un numero: "))
contador = 0 

while numero != 0:  
    numero = numero // 10 
    contador += 1

print("La cantidad de digitos es: " ,contador)    
 """

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.


""" numero_1 = int(input("Ingresa el numero 1: "))
numero_2 = int(input("Ingresa el numero 2: "))

min_valor = min(numero_1, numero_2)
may_valor = max(numero_1, numero_2)

total = 0

for i in range(min_valor + 1, may_valor):
    total = total + i

print(total)        
 """

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

""" total = 0  # Acumulador para la suma total

while True:
    numero = int(input("Ingresa un número (0 para terminar): "))

    if numero == 0:
        break  # Sale del bucle cuando se ingresa 0
    
    total += numero  # Suma el número al total
    print(f"Suma parcial: {total}")

print(f"La suma total es: {total}")
print("Fin del programa") """


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número

""" intentos = 0
numero_correcto = random.randint(0 , 10)

print("Adivina el número entre 0 y 9!")

while True:
    numero = int(input("Ingresa un numero: "))
    
    if numero == numero_correcto:
        break
    
    print("Lo siento no es el numero correcto")
    intentos += 1


print("Felicidades lo lograste!!")
print("Numero de intentos: ", intentos)
 """

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente

""" for numero in range(100, -1, -1): 
    if numero % 2 == 0:           
        print(numero)

 """

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario 

""" numero = int(input("ingresa un numero par: "))

if numero % 2 != 0:
    print("El numero tiene que ser par")
else: 
    suma = 0
    for i in range(numero + 1):
        suma += i
    
print(suma) """

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

""" min_numero = 0

cantidad_par = 0
cantidad_impar = 0

cantidad_neg = 0
cantidad_pos = 0

while min_numero < 100:
    numero = int(input("Ingresa un numero: "))
    
    if numero < 0:
        cantidad_neg+=1

    if numero > 0:
        cantidad_pos+=1

    # Validar si es par o impar
    if numero % 2 == 0:
        cantidad_par+=1
        
    elif numero % 2 == 1:
        cantidad_impar+=1
    
    min_numero +=1
        

print("Cantidad de pares: ", cantidad_par)
print("Cantidad de impares: ", cantidad_impar)
print("Cantidad de positivos: ", cantidad_pos)
print("Cantidad de negativo: ", cantidad_neg) """

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

""" suma_total = 0.0  # Usamos float para precisión en divisiones
contador = 0

while contador < 100:
    numero = float(input(f"Ingrese el número {contador + 1}/100: "))  # Convertimos a float
    suma_total += numero
    contador += 1

media = suma_total / 100
print(f"\nLa media de los 100 números es: {media:.2f}")  # :.2f redondea a 2 decimales
 """

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.


""" numero = int(input("Ingresa un número: "))
es_negativo = numero < 0
numero = abs(numero)  # Trabajamos con positivo
invertido = 0

while numero > 0:
    ultimo_digito = numero % 10
    invertido = (invertido * 10) + ultimo_digito
    numero = numero // 10

if es_negativo:
    invertido = -invertido

print("Número invertido:", invertido) """
