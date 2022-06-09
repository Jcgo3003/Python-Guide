# --------------------------------- Diccionarios --------------------------------------
print('- Diccionaries -')
# - Estructura de datos ordenada(Python > 3.7)
# - Guarda datos en forma de key-llave / valor/value
# - Duplicates Not Allowed!!!

# - Declarando -
print('\n-Declarando -') 	
dic = {}  				# Creando un diccionario vacío
print(dic)				# >> 

# Assignado valores 
print('\n- Assignando -')
dic["uno"] = 1 			# ASSIGNAR un valor nuevo.
print(dic)				# >> 
dic["uno"] = 2  		# RE-ASSIGNAR valores nuevos a elementos existentes.
print(dic)				# >> 

print('\n- Accesando -')
dic["uno"]			 	# ACCESAR un elemento.		
print(dic['uno'])		# >>

# Agregando elementos
print('\n- Agregando elementos -')
dic["dos"] = 2 			# Creando nuevas llaves y valores
print(dic)				# >>

# Eliminando elementos
print('\n- Eliminando elementos -')
del dic["uno"] 	# ELIMINANDO un elemento.
print(dic)

del dic     		 	# ELIMINANDO un dic completo
#print(dic)				# >> name 'dic' is not defined

# - Metodos - 
print('\n- Metodos -')
dic = {					# DICCIONARIO en multiples lineas.
	"uno": 1,
	"dos": 2,
	"tres": 3 }

# items	Regresa un objeto compuesto por una lista de tuples key-value
print('\n- items -')
print(dic.items())					# dict_items([('uno', 1), ('dos', 2), ('tres', 3)])
# NO se puede acceder al objeto como si fuera una lista dic.items()[] no funciona

# - Ejem
for key, value in dic.items(): 		# EXPLORAR un Diccionario 
	print(f"K:{key} V:{value}")	    # >> K:uno V:1 
									# >> K:dos V:2

# keys Regresa un objeto con lo valores de las llaves/keys
print('\n- keys -')
print(dic.keys())					# >> dict_keys(['uno', 'dos', 'tres'])

for name in dic.keys(): 		  	# MUESTRA las llaves del diccionario.
	print(name)          			# >> uno
									# >> dos

for llave in dic:					# Aunque por DEFAULT al iterar en un dic. RETURN keys/llaves	
	print(llave)					# >> uno
									# >> dos
# - Values -
print('\n- Values -')
dic.values() 						# RETURN una lista de los valores un diccionario.
print(dic.values())					# >>  dict_values([1, 2, 3])

# - in - Comprobar si un elemento se encuentra entre las llaves 
print('\n- in -')
"elemento" in dic.keys()		 	# >> False		CHECKING utilizando in


# - Sorted -
print('\n- Sorted -')
ejem = sorted(dic.keys())        	# RETURN una lista ordenada.
print(ejem)							# >> ['dos', 'tres', 'uno']
ejem = sorted(dic.values())        	# RETURN una lista de valores.
print(ejem)							# >> [1, 2, 3]
ejem = sorted(dic.items())			# Puede ser items incluso
print(ejem)							# >> [('dos', 2), ('tres', 3), ('uno', 1)]		Esta lista si puede ser accesada

# - len -
print('\n- Longitud -')				# RETURN la longitud de un diccionario
print(len(dic))						# >> 3

# - Get -
print('\n- Get -')					# RETURN un valor en definido que no se encuentre el valor buscado
print(dic.get('cuatro', 'No exits'))# >> No exits

# - Nesting -
print('\n- Nesting -')
#lista = [dic1, dic2, dic3]  		# NESTING diccionarios en una lista


dic = {"key": ["E1", "E2", "E3"]} 	# NESTING una lista en un diccionario.
print(dic)

dic = {"user1":{"Name": "Juan", "age": 30}} # NESTING Un diccionario en un diccionario.
print(dic)

# - Merge -
print('\n- Mergin -')				# MERGIN 2 dictionaries con unpacking operator **
dic1 = {"A": 1, "B": 2}
dic2 = {"C": 3, "D": 4}
merged = {**dic1, **dic2}	
print(merged)						# >> {'A': 1, 'B': 2, 'C': 3, 'D': 4}


