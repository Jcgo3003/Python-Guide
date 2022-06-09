# -------------------- Tuple --------------------
print('----------- Tuple -----------')
# Coleccion ordenada de datos de cualquier tipo, inmutable(No se puede modificar).

# - Asignar -
print('\n- Crear Tuple -')
t = ('uno', 2, [3, 4], 5 )	# CREAR un tuple con multiples elementos
print(t)					# ('uno', 2, [3, 4], 5)
#t = (3, )					# Si solo contiene un elemento debe llevar  ' , '  al final, si no Python no lo reconoce
#print(t)					# >> ('uno', 2, [3, 4], 5)

# - Acceder -
print('\n- Acceder elementos -')
t[0] 			# ACCESAR al PRIMER elemento del tuple
print(t[0])		# >> 'uno' 
tuple[-1] 		# ACCESAR el ULTIMO elemento del tuple(penultimo [-2] ect...)
print(t[-1])	# >> 5

# ----- Metodos --------
print('\n--- Metodos ---')
t = (2, 0, 0, 4, 0, 2, 5, 0)
print(len(t))		# >> 8  RETURN INT TAMANO del tuple.
print(t.count(2))	# >> 2  RETURN CUENTA el numero de veces que aparece un elemento
print(t.index(0))	# >> 1  RETURN INDICE de su primera aparicion, ValueError si no esta en el tuple
print(t.index(0, 3, 5)) # >> 4  Opciones: element - start (optional) - end (optional)

# - Contat elemenst -
print('\n- Concat - ')

t += (10, 11) 		# CONCATENAR dos listas con + 
print(t)			# >> ['uno', 'dos', 2, [3, 4], 5, 7, 8, 9, 10, 11]

t1 = (1, 2, 3)		
t2 = (4, 5, 6)
merged = (*t1, *t2) # MEZCLAR dos listas con Asterisk Operators *
print(merged)		# >> (1, 2, 3, 4, 5, 6)


# - Slice/Cortar con slice notation-
print('\nSlice/Cortar Slice Notation')
t = (0, 1, 2, 3, 4)
print(t[1:4]) 		# >> (1, 2, 3)  CREA un subtuple del tuple original. [index inicio: index final(no incluido)] 
print(t[:3])		# >> (0, 1, 2)  x deja vacio se toma como inicio del tuple(que es diferente de 0) 
print(t[4:1])		# >> ()         x siempre debe ser mayor que y() 
print(t[2:])		# >> (2, 3, 4)  y se deja vacio se toma el elemento final(que es diferente de -1) 
print(t[2:-1])		# >> (2, 3) 	Si  se agrega -1 para llegar al final del tuple el ultimo elemento queda excluido
print(t[0:: 2]) 	# >> (0, 2, 4)  OBTENER un sutuple pero en saltos de 2 elementos
for x in t[1:4]: 	# RECORRER en loop en un intervalo definido(o cualquier otro intervalo).
	print(x, end = ' ')	# >> 1 2 3 
#						Tip: El ultimo elemento obtenido del tuple es con Slice notacion y - 1
#							y - x es el tamano del tuple(En indices negativos se debe obtener el valor absoluto x-y )
#		Indice negativo
print("\n\nIndice negativo") #   [-5, -4, -3, -2, -1] - Comienzan por el ultimo elemento(-1), es otra manera de ver el index
print(t[-4])		# >> 1  
print(t[-2:])		# >> (3, 4)  	OBTENER los dos últimos elementos del tuple.
print(t[:-2])		# >> (0, 1, 2)  OBTENER todos los elementos excepto los ultimos dos
print(t[-4:-1]) 	# >> (1, 2, 3) 	OBTENER un subtuple - es lo mismo que [1:4] 
print(t[::-1])      # >> (4, 3, 2, 1, 0)  OBTENER todos los elementos pero invertidos con Step negativo
print(t[-2:1:-1])	# >> (3, 2) 	OBTENER los elementos desde el elemento indice -2 hasta elemento indice 1

# - Copiar -	
print('\n- Copiar -')	
t_Nueva = t 				# CREA una copia independiente.
print(f'{t_Nueva} {t}') 	# >> Nueva (0, 1, 2, 3, 4)  Original (0, 1, 2, 3, 4).
t = ('uno', 'dos', 'tres')	# Ambas son independientes(a diferencia de las listas que se referencian).
print(f'{t_Nueva} {t}\n') 	# >> Nueva (0, 1, 2, 3, 4)  Original (0, 1, 2, 3, 4)

t_Nueva = t[:] 				# CREAR una copia de un tuple.
print(f'{t_Nueva} {t}') 	# >> Nueva ('uno', 'dos', 'tres')  Original ('uno', 'dos', 'tres')
t = (3, 2, 1)				# t_Nueva es independiente de t.
print(f'{t_Nueva} {t}') 	# >> Nueva ('uno', 'dos', 'tres') Original (1, 2, 3) 

print(t)
print(sorted(t)) 			# RETURN lista organizada en orden alf. o numerico(opciones reverse=True)
							# >> [1, 2, 3] - solo organiza un tipo a la vez not supported between instances of 'int' and 'str'

#t_Nueva = t.copy() 		# NO EXISTE metodo copy /AttributeError: 'tuple' object has no attribute 'copy' 

# Transform a list
print("\n- Tranformation -")
l = [0, 1, 2, 3, 4, 5]		# TRANSFORMAR utilisando tuple function
t = tuple(l)				# Lista a tuple
print(f'lista {l} to  {t}')	# >> lista [0, 1, 2, 3, 4, 5] to  (0, 1, 2, 3, 4, 5)
s = {'uno', 'dos', 'tres'}	# 
t = tuple(s)				# Set a tuple
print(f'Set {s} to  {t}')	# >> Set {'tres', 'dos', 'uno'} to ('tres', 'dos', 'uno')
str = 'abc'					#
t = tuple(str)				# String to tuple
print(f'Str {str} to  {t}')	# >> Str abc to  ('a', 'b', 'c')

# Range
print('\n- Range -')			
t = tuple(range(10))		# CREAR un tuple a partir de un rango.
print(t)					# >> (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
t = tuple(range(0,6)) 		# CREAR tuple de números rango 0 al 5.
print(t)					# >> (0, 1, 2, 3, 4, 5)
t_Par = tuple(range(2,11,2)) # CREAR tuple de números primos del 1 al 10.
print(t_Par)				# >> (2, 4, 6, 8, 10)

#- Boolean -
print('\n- Boolean -')
print(bool(t))				# >> True RETURN True o False
t = ()						# Si tuple no tiene elementos sera RETURN False
print(bool(t))				# >> False

