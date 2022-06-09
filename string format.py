# String formating
print('String formating')
# The format() method allows you format string in any way you want.
# Syntax: template.format(p1, p1, .... , k1=v1, k2=v2)

# format() usa su argumento para sustituir el valor de cada código de formato. Por ejemplo:
print('Sam has {0} red balls and {1} yellow balls'.format(12, 31))
print('Numero {uno} Numero {dos} Numero {0}'.format(3, uno = 1, dos = 2))
# -> Numero 1 Numero 2 Numero 3

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
