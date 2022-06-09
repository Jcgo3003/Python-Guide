# -------------------------------------------- import ----------------------------------------------------------
# - importar funciones de otros programas(módulos)
# - Se debe colocar al comienzo del archivo 
# - modulo.nombre_funcion() - Para llamar a las funciones IMPORTADAS GLOBALMENTE CON IMPORT 
# - importar un módulo carga el contenido y crea el namespace que contiene el contenido.
# - El namespace del mudulo esta implementado como un diccionario (math.__dict__["pi"])

# - Import -
print('- Import -')		
from test_programs import def_test  		# IMPORTAR un modulo completo(con todas sus funciones). 

def_test.one()			# >> Function one 	Se invoca primero el modulo y despues la funcion

# - Importar funciones independientes -
print('\n- Importar funciones independientes -')
from test_programs.def_test import two, three	 # IMPORTAR una funcion en especifico(o varias)

two()					# >> Function Two		Se invoca derectamente la funcion			
three()					# >> Funciton Three		esto coloca a las funciones en el global namespace

# Importar todas las funciones
print('\n- Importar todas las funciones  -') 
from test_programs.def_test import *	# IMPORTAR todas las funciones de un modulo

one()					# >> Function One 		Se invoca la funcion directamente
two() 					# >> Function Two		
three()					# >> Function Three

# - Importar modulos bajo un alias
print('\n- Importar modulos bajo un alias -')
from test_programs import def_test as test 	# IMPORTAR modulos completos bajo un alias

test.one()					# >> Function One 	Se invoca un modulo bajo un alias y despues la funcion

# - Importar funciones bajo un alias
print('\n- Importar funciones bajo un alias -')
from test_programs.def_test import one as uno # Se pueden importar módulos con alias
uno()						# >> Function One	Se invoca la funcion bajo su nuevo alias.

# - Printing informacion -
print('\n- Lista de contenidos')
import math
dir()						# MUESTRA lo que hay en el  global namespace.
print(dir())				# '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__',

dir(math)					# LISTA los contenidos de un modulo
print(dir(math))			# >> ['__doc__', '__file__', '__loader__', '__name__', '__package__',

print(math.__dict__['pi'])	# >> 3.141592653589793				Muestra el valor de llave del namespace