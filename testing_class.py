#Testing a class l
from test_programs.survey import AnonymousSurvey

# # Define a question, and make a survey.
# question = "What language did you first learn to speak?" 
# my_survey = AnonymousSurvey(question)

# # Show the question, and store responses to the question. my_survey.show_question() 
# print("Enter 'q' at any time to quit.\n") 
# while True:
# 	response = input("Language: ") 
# 	if response == 'q':
# 		break 
# 	my_survey.store_response(response)

# # Show the survey results.
# print("\nThank you to everyone who participated in the survey!") 
# my_survey.show_results()

print('Creando el test')
import unittest 						# importando unittest

class TestAnonymousSurvey(unittest.TestCase):
	"""Tests for the class AnonymousSurvey"""
	
	def test_store_single_response1(self):
		"""Test that a single response is stored properly.""" 	 
		question = "What language did you first learn to speak?"  # Pregunta para la instancia
		my_survey = AnonymousSurvey(question)			  # Creando una instancia my_survey	  
		my_survey.store_response('English') 			  # Guardando una respuesta
		self.assertIn('English', my_survey.responses)	  # Comprobando la respuesta

	
	def test_store_three_responses1(self):
		"""Test that three individual responses are stored properly.""" 
		question = "What language did you first learn to speak?" # Pregunta
		my_survey = AnonymousSurvey(question)			  	# Creando una instancia
		responses = ['English', 'Spanish', 'Mandarin']		# Respuestas
		for response in responses:				
			my_survey.store_response(response)		  		# Agregando 3 respuestas

		for response in responses: 				 # Comprobando cada respuesta
			self.assertIn(response, my_survey.responses)	  #


# - - - - - - - Alternativa utilizando setup en los test RECOMENDADO - - - - - - - - - - - - - -
# Para evitar declarar en cada test unittest independientemente

	def setUp(self):		# Creando un setup para utilizarlo en todos los test
		""" Create a survey and a set of responses for use in all test methods. """ 
		question = "What language did you first learn to speak?"   	# Pregunta
		self.my_survey = AnonymousSurvey(question)		   	 		# Instancia
		self.responses = ['English', 'Spanish', 'Mandarin']       	# Respuestas


	def test_store_single_response2(self):			  	
		"""Test that a single response is stored properly.""" 	
		self.my_survey.store_response(self.responses[0]) 		# Agregando todo desde el setup
		self.assertIn(self.responses[0], self.my_survey.responses) 
		

	def test_store_three_responses2(self):
		"""Test that three individual responses are stored properly.""" 
		for response in self.responses:				# Agregando las respuestas
			self.my_survey.store_response(response) 	# una a una
		for response in self.responses:				# Poniendo a prueba el metodo
			self.assertIn(response, self.my_survey.responses)	
 

if __name__ == '__main__':
	unittest.main()

# _helperMethod_  - Con solo una _ indica utilización del método de ayuda
