# ----------------------------------------------------------- Classes ------------------------------------------------------------
# - Una clase son las instrucciones para crear una instancia, son celdas vacías que representan a una instancia(sujeto).
print('- Classes -')
class Tu_clase:						# CREANDO la clase, por convencion se declara primera letra en Mayúscula.
	"""Description de la clase en doctrina""" # Docstring con information sobre la clase.

	def __init__(self, valor1, valor2): # CREANDO un metodo(funcion), __init__ y self son obligatorios
		"""Mas descripciones"""
		self.var1 = valor1        	# Declarando variables, las variables que se pueden accesar 
		self.var2 = valor2         # A travez de las intancias(el sujeto que describe la clase) se llaman atributos.
	
	def mostrar_variable_1(self):	# CREANDO un método, este metodo no requiere variable adicionales
		"""Mas info"""	       		# Por lo que solo se agrega self
		print(f"{self.var1} Esta es la variable 1") # ACCESANDO a informacion ya declarada en la clase. 
	
	def mostrar_variable_2(self):	
		"""Aun mas info"""
		print(f"{self.var2} Esta es la variable 2")


print('\n- Creando una instancia -')# - Creando una instancias -
mi_instancia = Tu_clase("var uno", 2) # CREA una instancia, utilizando el metodo __init__, asigna a var1 y var2

print(mi_instancia.var1)			# >> var uno 		ACCESAR los datos de la instancia
print(mi_instancia.var2) 			# >> 2
mi_instancia.var2 = 100				# MODIFICAR las variables 
print(mi_instancia.var2)			# >> 100

mi_instancia.mostrar_variable_1() 	# >> var uno Esta es la variable 1		LLAMA al metodo(función) dentro de la instancia.
mi_instancia.mostrar_variable_2() 	# >> 100 Esta es la variable 2			LLAMA al metodo(función) dentro de la instancia.


print('\n- Modificando los atributos por defecto') 	# Modificando attributos por defecto 
class tu_classe:

	def __init__(self, uno, dos):
		self.uno = uno 
		self.dos = dos 		
		self.por_defecto =  1		# Declarando una variable con un valor por defecto

	def update_por_defecto(self, valor): # CREANDO un metodo para actualizar el valor

			"""Set the odometer reading to the given value.""" 	  
			self.por_defecto = valor




tu_instancia = tu_classe(1, 2) 		# Creando instancia

tu_instancia.por_defecto = 10 		# Modificando el parametro directamente

tu_instancia.update_por_defecto(100) # MODIFICANDO un paramentro con un metodo interno
print(tu_instancia.por_defecto)
	

print('\n- Modificando variables a traves de metodos -')# Ejemplos de modificaciones a travez de métodos 
class Car:
	def __init__(self):
		self.odometer_reading = 0

	def update_odometer(self, mileage):       # Podemos crear hacer que el metodo No permita modificar el valor si el valor es menor
		""" Set the odometer reading to the given value.  
	Reject the change if it attempts to roll the odometer back. """          
		if mileage > self.odometer_reading:	# Como en el ejemplo del kilometrage.
			self.odometer_reading = mileage 
		else:
			print("You can't roll back an odometer!")



	def increment_odometer(self, miles):		# Incrementando valores con un metodo
		"""Add the given amount to the odometer reading.""" 
		self.odometer_reading += miles

nuevo_coche = Car()
print(nuevo_coche.odometer_reading)			#
nuevo_coche.update_odometer(20)				# MODIFICANDO la variable atraves de un metodo
print(nuevo_coche.odometer_reading)			# >> 20
nuevo_coche.update_odometer(10)				# >> You can't roll back an odometer!		MODIFICANDO la variable atraves de un metodo
print(nuevo_coche.odometer_reading)			# >> 20




