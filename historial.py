# Mi primer Hola mundo
print("Hola mundo, espero que esten bien")

# VARIABLES
fruta = "pera"
print(fruta)

numero = 15
print(numero)


# ==========================================================
# EJERCICIO
# Crea un programa que te salude, 
# creando dos variables, una con tu nombre 
# y otra con tu edad y mostrando el resultado en la pantalla
# ==========================================================

# Crear dos variables: nombre, edad
# Saludar mostrando el resultado en pantalla

nombre = "Hellen"
edad = "20"
print("Hola " + nombre + " tienes " + edad)
#-----------------------------------------------------------


# Tipos de datos
caracter = "T" # char
caracters = "Hola munda" # string
entero = 32 # int
decimal = 28.5 # float
booleanoEncendido = True # boolean
booleanoApagado = False # boolean

# Operaciones entre tipos de datos
operacion_1 = 3 + 2
print(operacion_1)

operacion_2 = "3" + "2"
print(operacion_2)



#==========================================================================
# EJERCICIO
# Crea un programa que imprima las notas que un estudiante lleva actualmente en un curso.
# En tarea 1 obtuvo 12, en tarea 2 obtuvo 8, en tarea 3 obtuvo 15, en examen 1 obtuvo 20
#==========================================================================

tarea_1 = 12
tarea_2 = 8
tarea_3 = 15
examen_1 = 20
nota_actual = tarea_1 + tarea_2 + tarea_3 + examen_1
print(nota_actual)
#-----------------------------------------------------------


# Interaccion con el usuario
nombre = input("Ingresa tu nombre: ")
print("Hola " + nombre + " bienvenido a mi programa.")



# Conversiones entre tipos de datos
nombre = "Grisel"
edad = 21
edad_2 = str(edad)
print("Hola " + nombre + " tienes " + edad_2)

# Tipos de conversiones
numero = "32"
print(type(numero)) # Esta instrucción imprime el tipo de la variable "número"
#---------------------
conversion = int(numero) # int() convierte lo que se encuentra dentro de sus parentesis a un entero
print(type(conversion)) # Esta instrucción imprime el tipo de la variable "conversion"
print(conversion) # Esta instrucción imprime el valor de la variable "conversion"
#--------------------
conversion_decimal = float(numero) # float() convierte lo que se encuentra dentro de sus parentesis a un decimal
print(type(conversion_decimal)) # Esta instrucción imprime el tipo de la variable "conversion_decimal"
print(conversion_decimal) # Esta instrucción imprime el valor de la variable "conversion_decimal"

#=======================================================================
# EJERCICIO
# Un banco da 5% de interes anual y se necesita saber el valor que se recibira en ese tiempo.
# Se debe de solicitar al usuario que ingrese el dinero que piensa depositar al banco,
# convertirlo en decimal, 
# opear el deposito por el interes del banco,
# convertir el valor a una cadena de caracteres
# Mostrar un mensaje que diga: El dinero que recibiras despues de este tiempo es de: RESULTADO <--- Mostrar aqui el resultado de la operacion
#=======================================================================

# DATOS
# Crear una variable que almacene un input solicitando monto de deposito
# Convertir ese input a decimal
# Operar el ingreso con el interes del banco 0.05
# Convertir el resultado de la operacion en cadena de caracteres
# Mostrar un mensaje final

# ESTA PARTE ES DE ANALISIS DEL PROBLEMA
# El analisis de un posible ingreso de datos de 100 y el proceso para operar

# montodeposito       deposito                    interes    
#     "100"    ---->    100.0  ----> 100.0 *0.05 =   5 

# total            resultado
# 105.0     ---->  "105.0"

#   SOLUCION
monto_deposito = input("Ingrese el monto que va a depositar: ")
deposito = float(monto_deposito)
interes = deposito * 0.05
total = deposito + interes
resultado = str(total)
print("El dinero que recibiras despues de este tiempo es de: " + resultado)
#-----------------------------------------------------------



# Agregar texto sin necesidad de hacer conversion de tipo de dato
nombre = "Merari"
edad = 22
print(f"Hola {nombre} tienes {edad} años")


