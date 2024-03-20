# Introducción a la programación.
## webinar_18-03-2024

## Código utilizado en clase

### Mi primer Hola Mundo
```python
# Mi primer Hola mundo
print("Hola mundo, espero que esten bien")
```

### Variables
NOMBRE = VALOR

A diferencia de otros lenguajes, en python no es necesario colocar el tipo de dato.

Solo se pueden usar letras (sin tildes), numeros, o guion bajo para definir el nombre de una variable. Se debe de iniciar con letra, seguido de cualquier letra, numero o guion bajo.

Como buena práctica el nombre debe ser coherente con el valor que se piensa colocar. Ejemplo:
```python
fruta = "pera" # Variable "fruta" y su valor es "pera"
print(fruta) # Esta instrucción imprime el valor de la variable fruta

numero = 15 # Variable "numero" y su valor es 15
print(numero) # Esta instrucción imprime el valor de la variable numero
```

### Ejercicio práctico
Crea un programa que te salude, creando dos variables, una con tu nombre y otra con tu edad y mostrando el resultado en la pantalla
```python
nombre = "Hellen"
edad = "20"
print("Hola " + nombre + " tienes " + edad)
```

### Tipos de datos
```python
caracter = "T" # char --> Un solo caracter entre comillas simples o comillas dobles
caracteres = "Hola munda" # string --> Cadena de caracteres entre comillas simples o comillas dobles
entero = 32 # int --> Numero entero
decimal = 28.5 # float --> Numero decimal
booleanoEncendido = True # boolean --> Valor booleano (como un foco con corriente), en este caso encendido (True)
booleanoApagado = False # boolean --> Valor booleano (como un foco con corriente), en este caso apagado (False)
```

### Operaciones entre tipos de datos
Se pueden realizar operaciones entre tipos de datos numéricos o de texto, el resultado es distinto

#### Operacion con numeros
Cuando las operaciones son numéricas, se realiza como una operacion matemática
```python
operacion_1 = 3 + 2 # Se realiza la operacion de 3 + 2 y se almacena en la variable "operacion_1"
print(operacion_1) # Se imprime el valor de la variable "operacion_1", es decir 5.
```

#### Operacion con texto
Cuando las operaciones son de texto, se realiza una unión (concatenación) de los textos
```python
operacion_2 = "3" + "2" # Se realiza la unión de "3" + "2" y se almacena en la variable "operacion_2"
print(operacion_2) # Se imprime el valor de la variable "operacion_2", es decir 32.
```

### Ejercicio práctico
Crea un programa que imprima las notas que un estudiante lleva actualmente en un curso.
En la tarea 1 obtuvo 12 puntos, en la tarea 2 obtuvo 8 puntos, en la tarea 3 obtuvo 15 puntos, en el examen 1 obtuvo 20 puntos.
#### Solución 1
```python
# Creamos una variable por cada nota que el estudiante ha sacado
tarea_1 = 12
tarea_2 = 8
tarea_3 = 15
examen_1 = 20
# Se suman las notas
nota_actual = tarea_1 + tarea_2 + tarea_3 + examen_1
print(nota_actual) # Se imprime el valor de la variable "nota_actual", es decir 55.
```
#### Solución 2
```python
# Otra solución más práctica, es hacer la operación directamente en la instrucción "print()"
print(12+8+15+20) # Se imprime el valor de las operaciones dentro de los paréntesis de la instrucción "print()", y el resultado es el mismo.
```

### Interacción con el usuario
Una forma de obtener datos desde afuera de nuestro programa, es decir, datos que se solicitan al usuario que lo utilice, es con la instrucción "input()"
```python
nombre = input("Ingresa tu nombre: ") # Se solicita al usuario que ingrese un nombre y se almacena en la variable "nombre"
print("Hola " + nombre + " bienvenido a mi programa.") # Se imprime un mensaje con el nombre que el usuario ingresó
```

### Conversión entre tipos de datos
En muchas ocasiones, necesitamos convertir un tipo de dato hacia otro tipo de dato, por lo que es necesario realizarle una conversion, entre los datos anteriormente mencionados podemos mencionar:
```python
str() # Convierte lo que se encuentra dentro de los parentésis, a tipo string (cadena de caracteres)
int() # Convierte lo que se encuentra dentro de los parentésis, a tipo int (número entero)
float() # Convierte lo que se encuentra dentro de los parentésis, a tipo float (número decimal)
```
Por ejemplo:
```python
nombre = "Grisel"
edad = 21
edad_2 = str(edad) # str(edad) Convierte en string (cadena de texto) el valor de la variable "edad"
print("Hola " + nombre + " tienes " + edad_2)

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
```

### Ejercicio práctico
Un banco otorga 5% (0.05) de interes anual y se necesita crear un programa que obtenga el valor que se recibirá en ese tiempo.
- Se debe de solicitar al usuario que ingrese el dinero que piensa depositar al banco,
- Ese valor se debe de convertir en decimal,
- Opear el deposito por el interes del banco,
- Convertir el valor a una cadena de caracteres y
- Mostrar un mensaje que diga: El dinero que recibiras despues de este tiempo es de: RESULTADO <--- Mostrar aqui el resultado de la operacion

SOLUCION:
A veces los problemas se ven complejos, entonces lo que necesitamos es descomponer todo el problema en problemas más pequeños, ya que esto permitirá resolver mucho más rápido los problemas que nos presenten.

Antes de programar la solución, haremos un análisis al problema. Supongamos que el usuario ingrese 100, el programa debería de retornar 105, ya que son los 100 del usuario, más el interés que ha generado en el banco.
- Monto del deposito = "100" (es lo que suponemos).
Ya que el valor que se recibe con la instrucción "input()" es un string (cadena de caracteres), es necesario convertir ese valor a tipo de dato numérico, por lo que le realizamos una conversión
- Conversion a tipo numérico (puede ser entero o decimal). Ahora conversion = 100.0
Luego necesitamos obtener el interés que se genera en el banco, por lo que ya que tenemos la conversión solo la operamos
- Obtener el interés multiplicando la conversión por el porcentaje de interés (0.05). Interes = conversion * 0.05
Ahora necesitamos sumar los dos valores, el monto que se depositó, más el interés del banco
- Total será igual a la conversión más el interés que se ganó en el banco.
Se imprime el mensaje con el resultado final.

Ya que establecimos el problema en problemas más pequeños, realizamos nuestro programa:
```python
#   "100" <-- Suponemos que vale "100"
monto_deposito = input("Ingrese el monto que va a depositar: ") # Suponemos que la variable "monto_deposito" vale "100" ya que la instrucción "input()" obtiene un string (cadena de caracteres)

# 100.0 <-- Ahora, con la operación de abajo, ya tiene un valor decimal 
deposito = float(monto_deposito) # Se convierte la variable "monto_deposito" a decimal

# 5.0   =  100.0   * 0.05 <-- La operación devuelve el interés
interes = deposito * 0.05

# 105.0 = 100.0  +   5.0 <-- Se obtiene el valor total
total = deposito + interes

resultado = str(total) <-- Necesitamos convertir el total de nuevo a una cadena de caracteres

print("El dinero que recibiras despues de este tiempo es de: " + resultado) # Se imprime el mensaje con la unión del resultado final
```
