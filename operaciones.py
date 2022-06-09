# ---------- Operaciones Validas en Python ----------
print('Suma')
print(1+1)			# >> 2 			+	Suma	

print('Substraccion')
print(1-1)			# >> 0			- Substraccion

print('Multiplicacion')
print(2*2)			# >> 4			* Multiplicacion

print('Division')
print(4/2)			# >> 2.0		/ Division

print('Division Entera floor')		# Division entera, redondea HACIA ABAJO al entero más cercano.
print(5//2) 	  					# >> 2				a // b	

print('Division Entera ceil')		# Division entera, redondea HACIA Arriva al entero más cercano.
print(-1 *(-5//2)) 	  				# >> 3		  -1 * (-a // b)			

print('Exponente')
print(2**3) 		# >> 8			Exponente

					
# Otro tipo de operadores
print('\n- Otro tipo de operadores -')
l = [1, 2, 3, 4, 5]
print(*l)				# >> 1 2 3 4 5 		UNPACKING de una lista con Asterisk Operators

a, *b, c = l
print(f'{a} {b} {c}')	# >> 1 [2, 3, 4] 5	UNPACKING e asignandola


