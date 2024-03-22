from mudulos.miModulo import *

# Multiples vairables


x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
"""Illegal variable names: 
2myvar = "John"
my-var = "John"
my var = "John"
"""


""" QUINTA CLASE 
 fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
"""

#       Output Varibles


x = "Python is awesome"
print(x)


x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


# variables globales


x = "awesome"

# Funciones 4 clase


def myfunc():
    print("Python is " + x)


myfunc()

"""

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

"""


"""
 En este ejemplo, la función type() devuelve la clase 'str', 
 lo que significa que la variable "x" contiene un string.

"""

x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))


"""

Puede haber ocasiones en las que desee especificar un tipo en una variable. Esto se puede hacer con casting. Python es un lenguaje orientado a objetos y, como tal, utiliza clases para definir tipos de datos, incluidos sus tipos primitivos.

Por lo tanto, la conversión en Python se realiza mediante funciones constructoras:

int(): construye un número entero a partir de un literal entero, un literal flotante (eliminando todos los decimales) o un literal de cadena (siempre que la cadena represente un número entero).
float(): construye un número flotante a partir de un literal entero, un literal flotante o un literal de cadena (siempre que la cadena represente un flotante o un número entero)
str(): construye una cadena a partir de una amplia variedad de tipos de datos, incluidas cadenas, literales enteros y literales flotantes.


"""

a = 1
b = "hola"
c = 20.8


x = int(1)   # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
# z = float("3")   # z will be 3.0
w = float("4.2")  # w will be 4.2

x = str("s1")  # x will be 's1'
y = str(2)    # y will be '2'
# z = str(3.0)  # z will be '3.0'


tipo1 = type(a)

tipo2 = type(b)

tipo3 = type(c)

tipo4 = type(z)

print(tipo1)
print(tipo2)
print(tipo3)
print(tipo4)


"""
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y

"""


# Python Comparison Operators

"""

==	    Equal       	            x == y	
!=	    Not equal	                x != y	
>	    Greater than            	x > y	
<	    Less than	                x < y	
>=	    Greater than or equal to	x >= y	
<=	    Less than or equal to	    x <= y

"""


"""
¿Qué es un módulo?
Considere que un módulo es lo mismo que una biblioteca de códigos.

Un archivo que contiene un conjunto de funciones que desea incluir en su aplicación.
"""
