# String formating
print('String formating')
# Used for rendering messages in user interfaces and command-line utilities, writing data to files and sockets.
# Formatting is the process of combining predefined text with data values
# Three different methods 
# - C - style method
# - str.format method
# - Interpolated format strings | f-strings

# C-Style - Metodo inspirado en C printf
# text template is provided on the left side in a format string
# values to insert are provided as a single value or tuple of multiple values on the right side of the format operato
# Format specifiers (%d,  %s, %x, %f, etc) as placeholders 
# Other options: control over decimal places, padding, fill, and alignment.
# Incoveneces:
# - if you change the type or order of data get errors due to type conversion incompatibility
# - Hard to read
# - if you want to use the same value multiple times, you have to repeat it in the right side tuple
# - If using diccionaries each key must be specified at least twice

# ------ C - Style ------
print('--- C-style ---')
name = 'Juan'
number = 3.1416
# You can't change the values
print('Hello %s | lucky number %f' % (name, number )) # >> Hello Juan | lucky number 3.141600
print('Hello %s | lucky number %.2f' % (name, number )) # >> Hello Juan | lucky number 3.14   - El numero solo imprime 2 decimales

# Hard to read!!!!
l = [('Quesadilla', 3.5),('Tacos', 5), ('Pizza slice', 1)]
for i,(name, price) in enumerate(l):
	print('#%d  %-10s  %.1f' % (i+1, name, price))

#1  Quesadilla  3.5
#2  Tacos       5.0
#3  Pizza slice  1.0

# You need to write multiple times the same value
name = 'Juan'
print("Hello my name is %s, %s it's a cool name" % (name, name)) # Hello my name is Juan, Juan it's a cool name
# >> I'm Juan, I live in mx, my number is 1234

# Using a dicctionary make thing's even more complicated
print("I'm %(name)s, I live in %(country)s, my number is %(num)d" % {'num': 1234 , 'country': 'mx','name': 'Juan' })

menu = {'soup': 'lentil',     
		'oyster': 'kumamoto',     
		'special': 'schnitzel', } 

template = ('Today\'s soup is %(soup)s, '
			'buy one get two %(oyster)s oysters, '             
			'and our special entrée is %(special)s.') 

print(template % menu)
# >> Today's soup is lentil, buy one get two kumamoto oysters, and our special entrée is schnitzel.

print('Transformaciones  ')
b = 0b1111
h = 0xA
print('bin to dec %d | hex to dec %d' % (b, h)) # -> Binary is 15, hex is 10

# Escape
print('%d%%' % 10)		# >> 10%

# ------ str.format ------
# - Dificil de leer
print('\n--- str.format ---')
# - placeholders {}. 
# - Dos Maneras de implementar

# 1 - Llamando metodo con 2 argumentos(value, 'formato salida')
pi = 3.1416
formated = format(pi, ',.2f')
print(formated) 		# -> 3.14

# Format tiene muchas opciones de formato
hola = 'Hola Mundo'
formated = format(hola, '^20')
print(formated)				# >>         Hola Mundo     
# print('|{centro} |'.format('Hola Mundo', '^20s'))

# 2 - Directamente en el string
# format() usa su argumento para sustituir el valor de cada código de formato. Por ejemplo:
print('Sam has {0} red balls and {1} yellow balls'.format(12, 31))
# -> Sam has 12 red balls and 31 yellow balls

# Format permite nombra variables y sus valores, ademas de especificar su index
print('Numero {uno} Numero {dos} Numero {0}'.format(3, uno = 1, dos = 2))
# -> Numero 1 Numero 2 Numero 3

# Agregando 'format specifiers'
print('{:^10} {:.2f}'.format('Hola', 3.1416)) # >>    hola   3.14


# Escape {}
print('{{ {0} }}'.format('something'))      # >> { Something }


# Format specifiers
# Padding
# ^10 - Centrado en 10 espacio    #    bla   bla 
# <10 - 10 Espacio a la Derecha   # bla         bla
# >10 - 10 Espacio a la izquierda #         bla bla

# Format codes	
print('\n- Format codes -')
# d	for integers
# f	for floating point numbers
# b	for binary numbers
# o	for octal numbers
# x	for octal hexadecimal numbers
# s	for string
# e	for floating point in exponent format


import math
print(math.pi)						# -> 3.141592653589793		Pi
print('{:.2f}'.format(math.pi))		# -> 3.142              format
print(f'{3.1416:.3f}')				# -> 3.142 				f string

#		10 para ancho , 3 dígitos de precisión y float
print("Floating point {0:10.3f}".format(math.pi)) # -> Floating point      3.142
# -> Floating point      3.142

#	indice 0	3 dígitos de precisión, float,  indice 1 int
print("Floating point pi = {0:.3f}, with {1:d} digit precision".format(math.pi, 3))
# -> Floating point pi = 3.142, with 3 digit precision

#		indice 0 int				indice 1 3 dígitos de precisión, float, 
print(" {0:d} digit precision, Floating point pi = {1:.3f}".format(3, math.pi))
# -> 3 digit precision, Floating point pi = 3.142


# Transformaciones con format
print('\n- Transformaciones -')
print("12 to bin {0:b} 	to oct {1:o} to hex {2:x}".format(10, 10, 10))
# -> 12 to bin 1010 to oct 12 to hex a

print("12 to bin {0:b} {1:5s} to oct {2:o} {3:5s} to hex {4:x}".format(10, '$', 10, '$', 10))
# -> 12 to bin 1010 $     to oct 12 $     to hex a

# Diccionarios
print('\n- Diccionarios -')
d = {
'peces' : 4,
'perros' : 6
}

print("Juan tiene {peces} peces y {perros} perros".format(**d))

# Legacy
print('\n- Legacy -') # 		% En vez de {}
print("%d camisas cuestan = %.2f" % (12, 150.87612))

 