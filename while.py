# ---------------------------------------- while --------------------------------
# while loop podemos ejecutar un conjunto de declaraciones siempre que una condición sea verdadera
#


i = 0
while(i <= 5):		# while loop te permite correr un programa hasta que una 
	if(i == 3):	
		i += 1
		continue 		# Continue - Permite agregar excepciones en un loop, El codigo regresa al comienzo del loop
	
	print(f'i {i}')		   
	i += 1

	if(i == 5):
		print('- End -')
		break 			# Rermite detener un while o for
else:
	print("It won't get execute") # Este else no se ejecutara porque utilice break statement


i = 0
while(i <= 5):
	print(f'i {i}')
	i += 1 		
else:							# Permite ejecutar un bloque de código una vez cuando la condición ya no es verdadera
	print('- else statement -')	# else stament no se ejecutara si se utiliza break statement
	

# Nota: recuerda incrementar i, o de lo contrario el ciclo continuará para siempre. 

