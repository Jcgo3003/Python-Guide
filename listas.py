# ---------- Listas ----------
print('----------- Listas -----------')
# Coleccion ordenada de elementos, mutable
# - Asignar -
print('\n- Crear lista -')
lista = ['uno', 2, [3, 4], 5 ]	# CREAR una lista con multiples elementos
print(lista)					# >> ['uno', 2, [3, 4], 5]

# - Acceder -
print('\n- Acceder elementos -')
lista[0] 			# ACCESAR al PRIMER elemento de la lista
print(lista[0])		# >> 'uno' 
lista[-1] 			# ACCESAR el ULTIMO elemento de la lista(penultimo [-2] ect...)
print(lista[-1])	# >> 5

# - Edicion de elementos (siempre es destructiva).
# - Agregar elementos -
print('\n- Agregar elementos -')
lista.append(10) 	# AGREGANDO elementos al ULTIMO lugar en la lista, RETURN None
print(lista)	    # >> ['uno', 2, [3, 4], 5, 10] - 10 ha sido agregado

lista.insert(1, "dos") # INSERTANDO elementos en un sitio en especifico, RETURN None
print(lista)		# >> ['uno', 'dos', 2, [3, 4], 5, 10] - 'dos' ha sido agreadado

lista[-1] = 7		# ASIGNAR un nuevo elemento 
print(lista)		# >> 

# - Contat elemenst -
print('\n- Concat - ')
lista.extend([8, 9]) 	# CONCATENAR dos listas con metodo extend
print(lista)			# >> ['uno', 'dos', 2, [3, 4], 5, 7, 8, 9]
lista += [10, 11] 	# CONCATENAR dos listas con + 
print(lista)		# >> ['uno', 'dos', 2, [3, 4], 5, 7, 8, 9, 10, 11]

l1 = [1, 2, 3]		
l2 = [4, 5, 6]
merged = [*l1, *l2] # MEZCLAR dos listas con Asterisk Operators *
print(merged)		# >> [1, 2, 3, 4, 5, 6]


lista = ['uno', 'dos', 2, [3, 4], 5, 8]

# - Eliminar -
print("\n- Eliminar -")# ELIMINAR el ultimo elemento de una lista, RETURN Elemento eliminando
print(lista.pop())	# >> 8 		RETURN el elemento eliminado
print(lista)		# >> ['uno', 'dos', 2, [3, 4], 5] - 8 ha sido eliminado

lista.pop(1)		# ELIMINAR un elemento especifico dado su index
print(lista)		# >> ['uno', 2, [3, 4], 5] - 'dos' ha sido eliminado

lista.remove('uno') # REMOVER un elemento en especifico por su nombre, RETURN None
print(lista)		# >> [2, [3, 4], 5] 	- 'uno' ha sido eliminado 

del lista[1] 		# ELIMINA un elemento por indice, RETURN Invalid sintaxis
print(lista)		# >> [2, 5]				- [3, 4] ha sido eliminado
del lista[:]		# ELIMINA todos los elementos de una lista con slice notation.
print(lista)		# >> []					- Todos los elementos eliminados


del lista			# ELIMINA por completo la lista.
#print(lista)		# >> NameError: name 'lista' is not defined

#lista.clear()		# ELIMINA todos los elementos de la lista

# ----- Metodos --------
print('\n--- Metodos ---')
lista = [2, 3, 1, 4, 0] 
print(len(lista))		# RETURN eltamano de la lista en un int
# lista = ['b', 'c', 'a']

print(lista.count(2))	# >> 1			RETURN numero de veces que aparece un elemento
print(lista.index(2))	# >> 1			RETURN numero de indice en el que aparece un elemento

# - Destructivo -
print('\n- Destructivos -')
lista.reverse() 		# CAMBIA el orden de una lista, el ultimo primero el primero ultimo, RETURN None
print(lista)			# >> [5, [3, 4], 2, 'uno']  - ['a', 'c', 'b']
lista.sort() 			# ORGANIZA una lista en orden alf. o numerico(opciones reverse=True), RETURN None
print(lista)			# >> [1, 2, 3, 4, 5] - solo organiza un tipo a la vez not supported between instances of 'int' and 'str'

# - Slide assignament - 
print('\nSlide Assignament')	# ASSIGNAR valores en un rango en particular de una lista
print(lista)
lista[:2] = [6, 7, 8]			# ASSIGNAR valores que sustituyan los valores en un rango indice 0 - 2
print(lista)					# >> [6, 7, 8, 2, 3, 4]
lista[3:] = [9, 10]		        # ASSIGNAR valores que sustituyan los valores desde rango indice 2 hasta el final
print(lista)					# >> [6, 7, 8, 9, 10] 
lista[::2] = [3,2,1]    		# REMPLAZAR cada 2 elementos con elementos de otra lista
print(lista)					# >> [3, 7, 2, 9, 1] - IMPORTANTE La lista que pasa a ser 
#								assignada debe tener la misma cantidad de elementos a sustituir.
lista[::-2] = [3,2,1]			# NEGATIVE step para que la lista que va a remplazar sea ordenada del ultimo elmento al primero
print(lista)					# >> [1, 7, 2, 9, 3] 

# - No Destructivos -
print('\n- No Destructivos -')
rtn = sorted(lista) 	# RETURN una lista organizada en orden alf. o numerico(opciones reverse=True)
print(rtn)				# >> [1, 2, 3, 4, 5] - solo organiza un tipo a la vez not supported between instances of 'int' and 'str'

lista = [0, 1, 2, 3, 4]
# - Slice/Cortar con slice notation-
print('\nSlice/Cortar')
print(lista[1:4]) 		# >> [1, 2, 3] Obtener una copia sublista de una lista. [index inicio: index final(no incluido)] 
print(lista[4:1])		# >> [] x siempre debe ser mayor que y() 
print(lista[:3])		# >> [0, 1, 2] x deja vacio se toma como inicio de lista(que es diferente de 0) 
print(lista[2:])		# >> [2, 3, 4] y se deja vacio se toma final de lista(que es diferente de -1) 
print(lista[2:-1])		# >> [2, 3] Si se agrega -1 para llegar al final de la lista el ultimo elemento queda excluido
print(lista[0:: 2]) 	# >> [0, 2, 4] OBTENER una sublista pero en saltos de 2 elementos
for x in lista[1:4]: 	# RECORRER en loop en un intervalo definido(o cualquier otro intervalo).
	print(x, end = ' ')	# >> 1 2 3 
#						Tip: El ultimo elemento de la sublista es y - 1
#							y - x es el tamano de la lista(En indices negativos se debe obtener el valor absoluto x-y )
#		Indice negativo
print("\n\nIndice negativo") #   [-5, -4, -3, -2, -1] - Comienzan por el ultimo elemento(-1), es otra manera de ver el index
print(lista[-4])		# >> 1 
print(lista[-2:])		# >> [3, 4] - OBTENER los dos últimos elementos de la lista.
print(lista[:-2])		# >> [0, 1, 2] - OBTENER todos los elementos excepto los ultimos dos
print(lista[-4:-1]) 	# >> [1, 2, 3] - OBTENER una sublista - es lo mismo que [1:4] 
print(lista[::-1])      # >> [4, 3, 2, 1, 0] - OBTENER todos los elementos pero INVERTIR con Step negativo
print(lista[-2:1:-1])	# >> [3, 2] - OBETENER los elementos desde el elemento indice -2 hasta elemento indice 1

# - Copiar -	
print('\n- Copiar -')	# Para crear una copia se debe utilizar uno de Metodos para copiar 
lista_Nueva = lista 	# De otra manera solo creara un Puntero/Referencia.
print(f'{lista_Nueva} {lista}') # >> Nueva [0, 1, 2, 3, 4]  Original [0, 1, 2, 3, 4]
lista_Nueva.pop()		# Lo que le ocurra a lista_Nueva tambien le ocurrira a lista		
print(f'{lista_Nueva} {lista}') # >> Nueva [0, 1, 2, 3]     Original [0, 1, 2, 3]


lista_Nueva = lista[:] 				# CREAR una copia de una lista, con Slice notation
print(f'{lista_Nueva} {lista}') 	# >> Nueva [0, 1, 2, 3]  Original [0, 1, 2, 3]
lista_Nueva.pop()					# lista_Nueva es independiente de lista.
print(f'{lista_Nueva} {lista}') 	# >> Nueva [0, 1, 2]     Original [0, 1, 2, 3]

lista = [5, 6, 7, 8]
lista_Nueva = lista.copy()			# CREAR una copia de una lista, Copy function.
print(f'{lista_Nueva} {lista}') 	# >> Nueva [5, 6, 7, 8]  Original [5, 6, 7, 8]
lista_Nueva.pop()					# lista_Nueva es independiente de lista.
print(f'{lista_Nueva} {lista}') 	# >> Nueva [5, 6, 7]     Original [5, 6, 7, 8]

# Transform a list
print("\n- Tranformation -")
t = (0, 1, 2, 3, 4, 5)			# TRANSFORMAR utilisando list function
lista = list(t)					# Tuple to list
print(f'Tuple {t} to {lista}')	# >> Tuple (0, 1, 2, 3, 4, 5) to [0, 1, 2, 3, 4, 5]
s = {'uno', 'dos', 'tres'}		#	 
lista = list(s)					# Set a list
print(f'Set {s} to {lista}')	# >> Set {'tres', 'dos', 'uno'} to ['tres', 'dos', 'uno']
str = 'abc'						#
lista = list(str)				# String to list
print(f'Str {str} to  {lista}')	# >> Str abc to  ['a', 'b', 'c']

# - Crear listas -
print('\n- Range -')
lista = list(range(10)) 		# CREAR una lista de números rango 0 al 5.
print(lista)					# >> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista = list(range(3, 10))      # CREAR una lista de numeros rango 3 al 9
print(lista)					# >> [3, 4, 5, 6, 7, 8, 9]
lista_Par = list(range(2,11,2)) # CREAR una lista de números primos del 1 al 10.
print(lista_Par)				# >> [2, 4, 6, 8, 10]

#- Boolean -
print('\n- Boolean -')
print(bool(lista)) 					# RETURN True o False
lista = []							# Si la lista no tiene elementos sera RETURN False
print(bool(lista))					# >> False


