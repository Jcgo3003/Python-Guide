# ----------------------------------- Boolean Expressions -----------------------------------

print(True + 1 + False)

# Sumando True
lines="""\ He took his vorpal sword in hand;  			
	Long time the manxome foe he sought
	So rested he by the Tumtum tree
		And stood awhile in thought.
		""".splitlines()								# Texto 

print(sum("the" in line.lower() for line in lines))		# Suma total de True 
	

print('\n- AND -')
# --------- AND --------- 	# Es verdadero solo si ambos son verdaderos
# A	B	A and B 			# Si el primero es Falso es segundo ni siquiera es evaluado
# ----------------------- 	#
# True	True	True
# False	True	False
# True	False	False
# False	False	False

# Ejemplo
def example_AND(x):				# AND se comporta un como 'return' 
	print(f"Este es {x}")		# La siguiente linea de codigo es ignorada
	return x

True and example_AND(True)		# >> Este es True
True and example_AND(False)		# >> Este es False
False and example_AND(True)		# >>			Como el primer paramentro es falso el segundo
False and example_AND(False)	# >>			Ni si quiera es valuado, Es un shot-circuit

print('\n- OR -')
# --------- OR ----------	# Es verdadero a menos que ambas entradas sean False
#	A	B   	A or 		# Si el primer argumento es True no hay necesidad de evaluar el segundo
# True	True	True
# False	True	True
# True	False	True
# False	False	False

# Ejemplo
def example_OR():
	print("print_and_true called")
	return True

True or example_OR()		# >> Si el primer argumento es True no hay necesidad de evaluar el segundo
False or example_OR()		# >> print_and_true called


print('\n- is -')		  	# VERIFICA por la identidad de un objeto
x, y = [], []				# Solo va evaluar True si se esta refiriendo al mismo objeto
print(x is y)				# >> False
print(x is x)				# >> True
print(x is not x)			# >> False
print(x is not y)			# >> True

print('\n- in -')			# VERIFICA la existencia de un miembro, Un objeto puede definir lo que considera miembros.
print(1 in x) 				# >> False
x.append(1)					# La mayoría de las secuencias, como las listas, consideran que sus elementos son miembros
print(1 in x)				# >> True  		 	
print('h' in 'hello')		# >> True 			Tambien funciona en Strings, tanto para chars
print('hello' in 'hello world') # >> True  		Como para substrings
print('mundo' in 'hello world')	# >> False

print('\n- Chains -') 		# Se pueden crear cadenas de comparaciones
print(1 < 3 < 5)			# >> True 		Con comparadores de direccion
print(1 < 4 < 2)			# >> False		
print(1 == True)			# >> True 		Con el signo de comparacion
print(1 != True)			# >> False
print(1 < 2 and 2 < 4)		# >> True 		Con Condiciones logicas
print(3 < 1 < '1')			# >> False 		TIP: puede ser  utilizado como corto circuito
							# 3 < '1' 		Hubiese arrojado error

print('\n- Numbers as booleans -')	# El valor de numeros evaluados en booleanos
print(bool(5))				# >> True 		Sera True siempre que sean diferentes de 0.
print(bool(0))				# >> False
print(bool(-5))				# >> True
print(bool(1.5))			# >> True
print(bool(-1.5)) 			# >> True 		Esto incluye a numeros tipo flotante

print('\n- Otros tipos de datos -') # En general, los objetos que tienen len seran falsos si len es 0
print(bool([]))				# >> False
print(bool([1, 2]))			# >> True

print('\n- Mas alla -')		# Si no tienen metodo len, en general tenderan a ser Truthy
def func():
	pass
print(bool(func))			# >> True 



