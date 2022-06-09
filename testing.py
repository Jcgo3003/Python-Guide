# ----------------------- Testing ----------------------- 
print('- Testing -')
# - Unit Tests and Test Cases - Tipos de test
# - Unit test - Prueba unitaria
# - Test Cases - Casos de prueba -  Varios test unitarios

print('- Unit Tests and Test Cases -')
import unittest 											# Importando unittest
from test_programs.name_function import get_formatted_name	# importa la funcion a probar


class NamesTestCase(unittest.TestCase):			# Creando la Classe que hará todos los Test unitarios, es necesario agregar 
				# 	IMPORTANTE				 	unittest.TestCase para heredar funciones

	"""Tests for 'name_function.py'."""			
	def test_first_last_name(self):				# Nombre del metodo o unit test
		"""Do names like 'Janis Joplin' work?"""
		formatted_name = get_formatted_name('janis','joplin')	# Llamando a una función con unas variables controladas y asignadolo a una variable
		self.assertEqual(formatted_name, 'Janis Joplin')		# Utilizando assertEqual para comparar la salida de la función con resultado esperado

	def test_first_last_middle_name(self):			# Siempre tieneque empezar con Test, para que corra en automatico
		"""Do names like 'Wolfgang Amadeus Mozart' work?""" 
		
		formatted_name = get_formatted_name( 'wolfgang', 'mozart', 'amadeus') 
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')					 			    

if __name__ == '__main__': 
	unittest.main()


# Assert Methods/Métodos de afirmación disponibles en el módulo unittest

# Method					Use
# assertEqual(a, b) 		Verify that a == b
# assertNotEqual(a, b) a		Verify that a != b
# ssertTrue(x) 			Verify that x is True
# assertFalse(x) 			Verify that x is False
# assertIn(item, list) 		Verify that item is in list
# assertNotIn(item, list)		Verify that item is not in list
