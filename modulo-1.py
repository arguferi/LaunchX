#primer ejercicio solo imprimir

print('Hola desde la consola')

#segundo ejercicio usar variables

sum = 1 + 2 # 3
product = sum * 2
print(product)

# Declaramos la variable
distancia_a_alfa_centauri = 4.367
# Descubrimos su tipo de dato
print(type(distancia_a_alfa_centauri))

# Importamos la biblioteca 
from datetime import date

# Obtenemos la fecha de hoy
date.today()

# Mostramos la fecha en la consola
print(date.today())

print("Today's date is: " + str(date.today()))

print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)

#esta calc de abajo me lo toma como string y no como numero

print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(first_number + second_number)

#modificado

print(int(first_number) + int(second_number))