# Herencias 
print('Herencias')
# - Cuando creas una clase hijo, la clase padre debe aparecer antes que el hijo
# - Permite definir una clase que hereda todos los métodos y propiedades de otra clase.
# - Por convecion al Padre superclass y al hijo subclass.

# - Classe padre -
print('\n- Classe padre -')
class Padre:
	""" Init metodo"""
	def __init__(self, var1, var2):
		self.private = 10
		self.var1 = var1
		self.var2 = var2

	def metodo_Padre(self):
		""" Mostrando el valor privado """
		print(f"Metodo Padre")

	def valor_privado(self):
		""" Mostrando el valor privado """
		print(f"Valor privado {self.private}")

	def multi(self):
		""" Multiplicando las variables """ 
		print(f'Multi {self.var1 *  self.var2}')

arbol = Padre(2, 5)		# CREANDO una instancia

print(arbol.var1)		# >> 2 		ACCESANDO valores dentro de la instancia
print(arbol.var2)		# >> 5 		ACCESANDO valores dentro de la instancia

arbol.metodo_Padre()	# >> Metodo Padre 	ACCESANDO a los metodos
arbol.multi()			# >> Multi 10 		ACCESANDO a los metodos


print(arbol)			# >> <__main__.Padre object at 0x1016cef70> 	MOSTRANDO informacion sobre la intancia
print(Padre.__bases__)	# >> ((<class 'object'>,)	MOSTRANDO la clase padre

# - Classe hijo -
print('\n- Classe hijo -')
class Hijo(Padre):		# ** EL nombre de la clase padre tiene que estar como parametro 
	pass				# pass - Valor nulo

semilla = Hijo(7, 9)	# CREA un intancia de la clase Hijo

print(semilla.var1)		# >> 7 		ACCESANDO valores de la instancia
print(semilla.var2)		# >> 9 		ACCESANDO valores de la instancia
semilla.metodo_Padre()  # >> Metodo Padre 	ACCESANDO metodos del padre

print(Hijo.__bases__)	# >> (<class '__main__.Padre'>,)	MOSTRANDO la clase padre


# - Metodo __init__ Propio -
print('\n- Metodo __init__ Propio -')
class Hijo(Padre):							# 
	def __init__(self, var3, var4, var5):	# __init__ remplaza el metodo __init__ de la Clase Padre
		self.private_Hijo = 15
		self.var3 = var3
		self.var4 = var4
		self.var5 = var5

semilla = Hijo(1, 2, 3)	# CREANDO un instancia de la clase hijo

print(semilla.var5)		# >> 3     	ACCESANDO valores de la instancia
print(semilla.var3)		# >> 1 		ACCESANDO valores de la instancia
semilla.metodo_Padre()  # >> Metodo Padre 	ACCESANDO metodos del padre

# semilla.multi()         >> AttributeError: 'Hijo' object has no attribute 'var1' 		Al remplazar el metodo __init__    
#print(semilla.var1)      >> AttributeError: 'Hijo' object has no attribute 'var1' 		todos los metodos que dependen de init
# semilla.valor_privado() >> AttributeError: 'Hijo' object has no attribute 'private' 	se ven afectados


# Super clase
print('\n- Super Class -')
class Hijo(Padre):		# El nombre de la clase padre tiene que estar entre paréntesis 
	def __init__(self, var3, var4, var5):	# El metodo init toma los valores para crear una instancia "Padre".
		super().__init__(var3, var4)		# AGREGANDO super().__init__ se agregan los  datos y metodos de Padre de nuevo
		super().multi()						# AGREGAR mas metodos no tiene sentido porque solo se rescribio __init__
		self.private_Hijo = 15
		self.var3 = var3
		self.var4 = var4
		self.var5 = var5

	def multi_hijo(self):			# DEFINIENDO un metodo propio 
		print(f'Multi hijo {self.var1 * self.var2 * self.var3 * self.var4 * self.var5}')


semilla = Hijo(1, 2, 3)	# CONTROL total sobre los datos y metodoo de las clases Padre e hijo
print(semilla.var1)		# >> 1 		ACCESANDO valores dentro de la instancia(Padre)
print(semilla.var2)		# >> 2 		ACCESANDO valores dentro de la instancia(Padre)
print(semilla.var3)		# >> 1 		ACCESANDO valores dentro de la instancia(Hijo)
print(semilla.var4)		# >> 2 		ACCESANDO valores dentro de la instancia(Hijo)
print(semilla.var5)		# >> 3     	ACCESANDO valores dentro de la instancia(Hijo)
print(semilla.private)	# >> 10     ACCESANDO valores dentro de la instancia(Padre)
print(semilla.private_Hijo)	# >> 15     ACCESANDO valores dentro de la instancia(Hijo)
semilla.metodo_Padre()	# >> Metodo Padre  			(Padre)
semilla.valor_privado() # >> Valor privado 10 		(Padre)
semilla.multi()			# >> Multi 2 				(Padre)
semilla.multi_hijo()	# >> Multi hijo 12			(Hijo)




	# 	super().__init__(self.var1, self.var2)		# Super permite llamar un metodo de la funcion padre(aqui llama al metodo init)
	# 	super().multi(self.var1, self.var2)			  
	# 	self.privado_hijo = 10		# Definiendo atributo hijo.

	# 	self.attributo_tercero = Tercera() # Creando una tercera instancia con la clase Tercera, y asignándola 
	# 	self.attributo_tercero
	
	# def metodo_hijo(self):			# Definiendo métodos propios
 # 		"""Definiendo un metodo propio"""
 # 		print(f"El valor de la variable del hijo es {self.privado_hijo}")
		

