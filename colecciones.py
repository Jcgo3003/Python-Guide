# ------------------------------- Colecciones (Arrays)---------------------------------
# Hay 4 tipos de colecciones en Python 

# Lista 	Coleccion ordenada y modificable, Permite miembros duplicados.
print('\n----- Lista -----')
l = [1, 2 , 3 , 4, 5]
print(l)		# >> [1, 2, 3, 4, 5]


print(l[1])		# >> 2 		ACCEDER a un elemento
print(l[-1])	# >> 5		ACCEDER al ultimo elemento

# Edit DESTRUCTIVO
l[1] = 9		# >> [1, 9, 3, 4, 5]	MODIFICAR un elemento

l.pop()			# >> [1, 9, 3, 4]		ELIMINAR el ulitimo elemento ||>> RETURN  elemento eliminado
l.remove(9)		# >> [1, 9, 3]			ELIMINAR un elemento en especifico||>> RETURN None o ValueError
print(l)		# >> [1, 3, 4]		

l.append(10)	# >> [1, 3, 4, 10]		AGREGAR un elemento ||>> RETURN None
l.insert(2, 20) # >> [1, 9, 20, 4, 10]	AGREGAR un elemento en lugar especifico ||>> RETURN None

l.extend([30,40])# >> [1, 9, 20, 3, 10, 30, 40] 	CONCATENAR con otra lista||>> RETURN None

l.reverse()		# >> [40, 30, 10, 4, 20, 3, 1]	||>> RETURN la lista REACOMODADA la de atras hacia adelante
l.sort()		# >> [1, 3, 4, 10, 20, 30, 40]	||>> RETURN la lista REACOMODADA la forma alfabetica

# No destructivo
l + [50, 60]	# >> [1, 9, 20, 3, 10, 30, 40, 50, 60] 	CONCATENA temporalmente(l permanecera sin cambios).
sorted(l)		# >> [1, 3, 9, 10, 20, 30, 40] 	||>> RETURN la lista reacomodada de forma alfabetica
len(l)			# >> 7							||>> RETURN tamano de la lista


l = list(range(2,11))	# >> [2, 3, 4, 5, 6, 7, 8, 9, 10] CREANDO una lista
print(l[0::2])	# >> [2, 4, 6, 8, 10]			||>> RETURN l pero cortada 


# Tuple 	Coleccion ordenada e inmodificable, Permite miembros duplicados.
print('\n----- Tuple -----') 
t = (1, 2 , 3 , 4, 5)
print(t)		# >> (1, 2, 3, 4, 5)
print(t[1])		# >> 2 		ACCEDER a un elemento
print(t[-1])	# >> 5 		ACCEDER a un elemento
# t[0] = 1  	# >> error!	Inmodificable!

t2 =(10, 15) + t	
t2				# >> (1, 2, 3, 4, 5, 10, 15) 	CONCATENA temporalmente(t permanecera sin cambios).
sorted(t2)		# >> [1, 2, 3, 4, 5, 10, 15] 	RETURN lista reacomodada de forma alfanumerica
len(t)			# >> 5							RETURN tamano del Tuple


t = tuple(range(5))	# CREANDO una tuple range 
print(t)			# >> (0, 1, 2, 3, 4)	RETURN l pero cortada 



# Set		Coleccion desordenada, inmodificable y sin index, No perminte miembros duplicados.
print('\n----- Set -----')
s = {1, 2 , 3}		# Declarando un set

print(s.add(4))		# AGREGA un elemento, RETURN None , add() toma solo un paramentro.
print(s)			# >> {1, 2, 3, 4}



# Diccionario Coleccion Ordenada y modificable, No permite miembros duplicados.
print('\n----- Diccionario -----')
d = {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5}
print(d)				# {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4, 'cinco': 5}

print(d['uno'])			# >> 1			ACCEDIENDO
print(d.items())		# >> dict_items([('uno', 1), ('dos', 2), ('tres', 3), ('cuatro', 4), ('cinco', 5)])
print(d.keys())			# >> dict_keys(['uno', 'dos', 'tres', 'cuatro', 'cinco'])
print(d.values())		# >> dict_values([1, 2, 3, 4, 5])

print('\n- get -')
r = d.get(10, "Bla")	# >> Bla	RETURN el valor del elemento buscado, si no existe RETURN el valor definido
print(r)



