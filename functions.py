# ----------------------------------- Functions --------------------------------------------------------
# - Es un bloque de código que solo se ejecuta cuando se le llama. 
# - Puede pasar datos(parámetros)
# - Puede devolver datos como resultado.


# - Declarar -
print('\n- Declarar -')
def ejemplo(): 				# DECLARAR una funcion
	print('Hello')			# DECLARAR lo que regresara

ejemplo()					# >> Hello 		INVOCANDO una funcion

# - Procesando Argumentos -
print('\n- Argumentos -')
def ejemplo(x):  	  		# PASAR una variable
	return x*x	  			# Funcion temporal, se utiliza en maquetacion

print(ejemplo(2))			# >> 4		 	PRINT el resultado de una funcion

# Pasando argumentos a funciones
print('\n- Positional Arguments -') # Basados en el orden en que los argumentos son pasados.
def ejemplo(name, country): 	# # Y sus variables deben utilizarse en ese orden, si no la function no funciona adecuadamente
	print(f'Name: {name} Country: {country}')

ejemplo('Juan', 'MX')			# >> Name: Juan Country: MX
ejemplo('Mx', 'Juan')			# >> Name: Mx Country: Juan

# Keyword arguments
print('\n- Keyword arguments -') 	# En un nombre-valor que se pasa a una function, no importa el orden
ejemplo(country= 'Mx', name= 'Juan')	# >> Name: Juan Country: Mx


# Default values 
print('\n- Default values -')   # Valores que se agregan como valores por defecto, los valores default deben ir al final de la function.
def ejemplo(name, country= 'Mx'):
	print(f'Name: {name} Country: {country}')

ejemplo('Juan')					# >> Name: Juan Country: Mx		Si el segundo argumento no es proporcionado 
ejemplo('Juan', 'Fr')			# >> Name: Juan Country: Fr		se ejecuta la funcion con el argumento Default

# - Procesando Miltiples Argumentos -
print('\n- Multiples Argumentos -') 	# Procesando multiples argumentos con el unpacking operator (*).
def ejemplo(*args):			# DECLARAR una funcion que recibe multiples Paramentros(*)
	# args.pop()			# 'tuple' object has no attribute 'pop'
	print(args)				# Los paramentros recibidos se guardan un un tuple(*args).
			          		
ejemplo(1,2,3,4,5)			# >> (1, 2, 3, 4, 5)	

# lista como argumento
print('\n- lista como argumento -') 	# Procesando un lista como argumento
def ejemplo(a, b, c):		# Con Unpacking operator (*) tambien es posible pasar una lista como arguemnto
    print(a + b + c)		# Esta funcion procesa un numero especifico de argumentos

l = [1, 2, 3]				# ES IMPORTANTE	que el # de elementos en la lista sea igual al # argumentos tomados
ejemplo(*l)					# >> 6

print('\n- Multiples listas -') # Con * es posible procesar multiples listas
def ejemplo(*args):
    result = 0
    for x in args:
        result += x
    return result

l2 = [4, 5]					
l3 = [6, 7, 8]				

print(ejemplo(*l, *l2, *l3))# Es posible procesar multiples listas

print('\n- Combinando args. posicionales y arbirtrarios')
def ejemplo(x, *args):   	# Combinando argumentos posicionares y arbitrarios.
	print(x)				
	print(args)

ejemplo(5, 4, 3, 2, 1)		# >> 5				Cada valor es idependiente
							# >> (4, 3, 2, 1)		
# - Procesando diccionarios
print('\n- Diccionarios') 		# PROCESAR diccionarios con **kwargs
def ejemplo(**kwargs):   		# De esta manera los argumentos que se reciban se empaquetaran en diccionarios(genéricamente se le conoce como **gwrgs).
	for x, y in kwargs.items():
		print(f'Key {x} Value {y}') 


ejemplo(b="Python", c="Is", d="Great", e="!") # >> Key b Value Python
												#  Key c Value Is

print(f'-\n- Pasando un diccionario entero -')
d = {'a': 1, 'b': 2 ,'c': 3}	# Se puede procesar el diccionario completo utilizando **
ejemplo(**d)					# >> Key a Value 1
								# 	 Key b Value 2

# - Procesando Diferentes tipos de argumentos
print('\n- Procesando Diferentes tipos de argumentos -') 	# PROCESAR diccionarios con **kwargs
def ejemplo(*args, **kwargs):							# Se pueden procesar todos los tipos de argumentos al mismo tiempo
	print(f'args {args}')
	for x, y in kwargs.items():
		print(f'Key {x} Value {y}')     	# Es IMPORTANTE que me * y ** estes escritos en ese orden
		print('helo')
	# print(f'a {a} b args')


ejemplo(*l, **d)					# >> args (1, 2, 3)
									#	 Key a Value 1	...

# Despues de intentar con multiples opciones 
# ejemplo( a, *args, **kwargs)		No se puede procesar mas alla de args, porque args mete a kwargs como otro dato mas
#									Y hace que se pierda **kwargs	- Aunque no lanza ningun error 
# ejemplo(1234, *l, *d) 			# Si solo agregas * solo se pasaran las keys y los values no

# ejemplo(10, [1,2,3], {'a': 1, 'b': 2, 'c': 3})					