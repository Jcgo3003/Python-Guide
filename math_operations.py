# ------------------------------- Math --------------------------------
print("---------- Math -----------")

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]	# Lista
t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) 	# tuple
s = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}	# set

#- Metodos Built-in -
print('\n- Built-in -')
print(min(l)) 			# OBTENER el numero mas pequeño.
print(max(t)) 			# OBTENER el numero mas grande.
print(sum(s)) 			# OBTENER la suma de una lista.

# modulo % 	El operador modulo te muestra el resto de lo que quedo de una division
print('\n- Modulo -')
print(5 % 3)			# >> 2
print(6 % 3) 			# >> 0
print(6 % 7)			# >> 1

# Operaciones entre tipos distitos
print('\n- Operaciones entre distintos tipos -') # NO SE PARA QUE SIRVE O SI QUIERA COMO FUNCIONA!!!!!!!!! 
print([-1, 3][True])		# >> 3
print([3, -1][True])		# >> -1 	
# print([True][3, -1])		# >> TypeError: list indices must be integers or slices, not tuple
print()
print([-1, 3][False])		# >> -1
print([3, -1][False])		# >> 3 	

print('\n- round -')
print(round(3.1415, 2)) 	# OBTENER un numero redondeado a un numero de decimales dado
print(f'{3.1415:.3f}') 		# OBTENER un numero redondeado a un numero de decimales dado con %.f

# - Metodos Math -
print('\n- Metodos Math -')
import math				# Importando modulo
print('\n- Truncar -')
print(math.trunc(99.123))	# >> 99 	TRUNCA un INT(Elimina los decimales)
print(math.pi)				# >> 3.141592653589793  Numero Pi

print('\n- prod -')     # Producto de todos los elemento detro de un objeto iterable
print(math.prod([1,2,3,4])) # -> 24

print('\n- Dist. Euclidiana -')
l1 = [1, 3]
l2 = [2, 4]
print(math.dist(l1, l2))# >> 1.4142 ... 	Encuentra la distancia euclidiana(incluso en 3D)  	> Python 3.8

# El máximo común divisor o mcd
# una expresión matemática para encontrar el número más alto que puede dividir dos numeros

print('\n- Maximo común divisor -')
print(math.gcd(18, 30))			# -> 6




