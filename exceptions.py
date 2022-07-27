# Exceptions
print('- Exceptions -')

def div(x, y):
	try: 					 	# Intentando ejecutar codigo código
		division = (x/y)		

	except ZeroDivisionError:	# En caso de error - ZeroDivizionError 
		print("No puedes dividir entre 0") # Se ejecutara el siguiente codigo

	except FileNotFoundError:	# En caso de FileNotFoundError etc
	       pass					# PERMITE reaccionar silenciosamente a los errores ignorándolos, sin traceback

	else:						# Si todo sale bien
		 print(x/y)

div(5, 0)
div(5, 1)

# Raise Exceptions
print('\n- Raise exceptions - ')
n = 9
if n > 10:
	raise Exception('Bla bla bla bla bla')

# >> Exception: Bla bla bla bla bla


# Referencia
# https://realpython.com/python-exceptions/

