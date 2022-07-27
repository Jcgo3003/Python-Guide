# --------------------------- Print ----------------------------

print('Algo', end = ' ')	# IMPRIMIR sin salto de linea('end' sustituye \n por ' ')
print()						# IMPRIMIR un salto de linea
print(" x " * 5)			# IMPRIMIR una linea x veces



dict = {'A':1, 'B':2}		# >> 
print(*dict)				# >> A B
print(*['hello', 'world']) 	# >> hello world IMPRIMIR sin informacion sin [], (), {}
print(*('hello', 'world')) 	# >> hello world IMPRIMIR sin 
print(*{'hello', 'world'}) 	# >> hello world IMPRIMIR sin 


# !r -  calls the repr of the value supplied.
# !s (str), !a (ascii) just to ease compatibility with the str.format alternative, you don't need to use them with f-strings.

bla = 12
print(f'Something {bla!r}')


