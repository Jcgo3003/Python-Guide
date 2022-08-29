# Herencias 
print('Herencias')
# - Cuando creas una clase hijo, la clase padre debe aparecer antes que el hijo
# - Permite definir una clase que hereda todos los métodos y propiedades de otra clase.
# - Por convecion al Padre superclass y al hijo subclass.

# - Classe padre -
print('\n- Classe padre -')
class Person:
	"""A Class to describe a person """
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber

	def printPerson(self):
		print(f'Name: {self.lastName} {self.firstName}')
		print(f'ID: {self.idNumber}') 

uno = Person('Gomez', 'Juan', 1234) # CREANDO una instancia
first = uno.firstName	# ACCESANDO valores dentro de la instancia
last = uno.lastName
uno.printPerson()		# >> Name: Juan Gomez ID: 1234
print(first, last)		# >> Gomez Juan  	| ACCESANDO un metodo


# - Classe hijo -     # Classe hijo hereda todos los paramentros y metodos del Padre
class Student(Person):# ** EL nombre de la clase padre tiene que estar como parametro 
	pass			  # pass - Valor nulo

stu_uno = Student('Ramirez', 'Jose', 12324)
first = stu_uno.firstName	# ACCESANDO valores 
last = stu_uno.lastName
id = stu_uno.idNumber
print(first, last, id)		# >> Ramirez Jose 12324
stu_uno.printPerson()		# >> ACCESANDO metodos del padre

# Re-writing and keeping parent's Inherintence 
print("\nRe-writing and keeping parent's Inherintence")
print("Bringing back parent's __init__ Method")
class Student_ext(Person):
	def __init__(self,  firstName, lastName, idNumber, scores): # __init__() own function, child class will no longer inherit the parent's __init__() function
		Person.__init__(self, firstName, lastName, idNumber) # To keep parent's __init__ function, you need to call it.
		self.scores = scores		

stu_uno = Student_ext('Ramirez', 'Jose', 12324, 10)
first = stu_uno.firstName
last = stu_uno.lastName
id = stu_uno.idNumber
sco = stu_uno.scores
print(first, last, id, sco)# >> Ramirez Jose 12324 10
stu_uno.printPerson()	# >> Name: Jose Ramirez ID: 12324

print("Super() Function")
class Student_ext(Person):
	def __init__(self,  firstName, lastName, idNumber, scores): # __init__() own function, child class will no longer inherit the parent's __init__() function
		super().__init__(firstName, lastName, idNumber) # To keep parent's __init__ function, you need to call it.
		self.scores = scores		

stu_uno = Student_ext('Ramirez', 'Jose', 12324, 10)
first = stu_uno.firstName
last = stu_uno.lastName
id = stu_uno.idNumber
sco = stu_uno.scores
print(first, last, id, sco)# >> Ramirez Jose 12324 10
stu_uno.printPerson()	# >> Name: Jose Ramirez ID: 12324
