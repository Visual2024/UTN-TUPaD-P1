# Ejercicio 1
# Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

print("Hola Mundo!")

# Ejercicio 2
""" Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
realizar la impresión por pantalla. """

nombre = str(input("Ingresa tu nombre: "))

print(f"Hola{nombre}!")


# Ejercicio 3
""" Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
la impresión por pantalla.
 """

nombre = str(input("Ingresa tu nombre: "))
apellido = str(input("Ingresa tu apellido: "))
edad = int(input("Ingresa tu edad: "))
residencia = str(input("Ingresa tu residencia: "))

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Ejercicio 4

""" Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
su perímetro.
"""

radio = float(input("Ingrese el radio de un circulo: "))
pi = 3.14

area = pi * radio * radio
perimetro = 2 * pi * radio


print(f"Este es el area del circulo: {area}")
print(f"Este es el perimetro del circulo: {perimetro}")


# Ejercicio 5
""" Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
cuántas horas equivale.
"""

segundos = int(input("Ingrese una cantidad de segundos: "))
 
horas = segundos / 3600

print(f"{segundos} segundos equivalen a {horas} horas")

# Ejercicio 6
""" Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
multiplicar de dicho número.
"""

numero = int(input("Ingrese un numero: "))

print(numero * 1)
print(numero * 2)
print(numero * 3)
print(numero * 4)
print(numero * 5)
print(numero * 6)
print(numero * 7)
print(numero * 8)
print(numero * 9)
print(numero * 10)


# Ejercicio 7
""" Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
 """

print("Ingrese dos numeros distinto de cero")

numero_1 = int(input("Ingrese el primer numero: "))
numero_2 = int(input("Ingrese el segundo numero: "))

print(numero_1 + numero_2)
print(numero_1 - numero_2)
print(numero_1 * numero_2)
print(numero_1 / numero_2)


# Ejercicio: Cálculo del Índice de Masa Corporal (IMC)
""" 
Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
de masa corporal (IMC).
"""

altura = float(input("Ingrese su altura en metros (ej: 1.75): "))  # Convertir a metros
peso = float(input("Ingrese su peso en kg: "))

IMC = peso / (altura ** 2)  # Fórmula correcta

print(f"Su índice de masa corporal (IMC) es: {IMC:.2f}")

""" Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
 """

temperatura_celsius = float(input("Ingrese la temparatura en grados Celsius: "))

temperatura_fahrenheit = (9 / 5 ) * temperatura_celsius + 32

print(f"{temperatura_celsius}°C equivalen a {temperatura_fahrenheit:.2f}°F")

""" Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
dichos números. """

numero__1 = int(input("ingresa el primer numero: "))
numero__2 = int(input("ingresa el segundo numero: "))
numero__3 = int(input("ingresa el tercero numero: "))

promedio = (numero__1 + numero__2 + numero__3) / 3

print(promedio)