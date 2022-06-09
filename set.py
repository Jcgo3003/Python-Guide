# ----------------------------------- Set/Conjunto ----------------------------------
# - Colección desordenada, inmodificable(frozenset) y no indexada.
# - Los elementos no se pueden modificar, PERO puede eliminar elementos y agregar.
# - Están desordenados, no se sabe en que orden aparecerán los elementos.
# - Pueden ser de cualquier tipo datos
# - Duplicates Not Allowed!!! 	Duplicate values will be ignored
# - Basados en las hast tables
# - Representa la noción matemática de un conjunto.
# - Tiene un método altamente optimizado para verificar si un elemento existe(mejor que listas)  
# - Frozenset son objetos inmutables

# - Declarando -
print('\n- Declarando -')
s = {'uno', 2, True}	# Declarando un set
print(s)				# >> {'uno', True, 2}  - Se desordeno

# - Agregando elementos -
print('\n- Agregando -')
print(s.add(4))			# AGREGA un elemento, RETURN None , add() toma solo un paramentro.
print(s)				# >> {True, 2, 'uno', 4} 	 

# Sin duplicados
print('\n- Sin duplicados -')
s = {2,'uno', 2, True, 2} # Los duplicados seran ignorados
print(s)				# >> {'uno', True, 2}

# Type of
print('\n- typeof -')	# OBTENER el tipo de dato
print(type(s))			# >> <class 'set'>

# - Metodos -
print('\n- Metodos -')
print(len(s))			# >> 3 OBTENER la longitud del set

# - Contat elemenst -
print('\n- Concat - ')
s1 = {1, 2, 3}		
s2 = {4, 5, 6}
merged = {*s1, *s2} # MEZCLAR dos sets con Asterisk Operators *
print(merged)		# >> [1, 2, 3, 4, 5, 6]


# - Constructor -
print('\n- Constructor -')	# CONSTRUCTOR set
s = set(('dos', 1, False))	# Los elementos deben estar dentro de un doble parentesis
print(s)					# >> {False, 1, 'dos'} 

print("\n- Tranformation -")
l = [0, 1, 2, 3, 4, 5]		# TRANSFORMAR utilisando tuple function
s = set(l)					# Lista a set
print(f'lista {l} to  {s}')	# >> lista [0, 1, 2, 3, 4, 5] to  {0, 1, 2, 3, 4, 5}
t = ('uno', 'dos', 'tres')	# 
s = set(t)					# Tuple to set
print(f'Tuple {t} to  {s}')	# >> Set {'tres', 'dos', 'uno'} to ('tres', 'dos', 'uno')
str = 'abc'					#
s = set(str)				# String to set
print(f'Str {str} to  {s}')	# >> Str abc to  ('a', 'b', 'c')


# - Frozenset -			
print('\n- Frozenset -')	# CREA un set/conjunto frozen que es inmutable.
s = frozenset(('tres', 1, True)) # CONSTRUCTOR de frozenset
print(s)					# >> frozensit({1, 'tres'})
#s.add(10)					# Son inmutables!!! - AttributeError 'frozenset' object has no attribute 'add'
print(type(s))				# >> <class 'frozenset'>





# Referencias
# https://www.geeksforgeeks.org/sets-in-python/