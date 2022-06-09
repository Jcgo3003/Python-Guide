# --------------------------- Print ----------------------------

print('Algo', end = ' ')	# IMPRIMIR sin salto de linea('end' sustituye \n por ' ')
print()						# IMPRIMIR un salto de linea
print(" x " * 5)			# IMPRIMIR una linea x veces



dict = {'A':1, 'B':2}		# >> 
print(*dict)				# >> A B
print(*['hello', 'world']) 	# >> hello world IMPRIMIR sin informacion sin [], (), {}
print(*('hello', 'world')) 	# >> hello world IMPRIMIR sin 
print(*{'hello', 'world'}) 	# >> hello world IMPRIMIR sin 


