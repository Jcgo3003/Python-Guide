# --------------------------- TRANSFORMACIONES ---------------------------
# - Data -
print('\n- Data -')

str = str(10)					# INT to STRING
print(str)						# -> 10

b = bin(10)						# INT to BIN
print(b)						# -> 0b1010
print(b[2:])					# -> 1010 		Utilizando slice se puede obtener el num. sin Ob

print(ord('A'))					# -> 65   	CHAR to INT(ascii)
print(chr(65))					# -> 65   	INT(ascii) to CHAR

i = int('10')					# STRING to INT
print(i)						# -> 10

# Collections
print('\n- Collections -')

print("\n- To Lista -")
t = (0, 1, 2, 3, 4, 5)			# TRANSFORMAR utilisando list function
lista = list(t)					# Tuple to list
print(f'Tuple {t} to {lista}')	# -> Tuple (0, 1, 2, 3, 4, 5) to [0, 1, 2, 3, 4, 5]
s = {'uno', 'dos', 'tres'}		#	 
lista = list(s)					# Set a list
print(f'Set {s} to {lista}')	# -> Set {'tres', 'dos', 'uno'} to ['tres', 'dos', 'uno']

str = 'abc dfg'					#
lista = list(str)				# String to list of CHARS
print(f'Str {str} to  {lista}')	# -> ['a', 'b', 'c', ' ', 'd', 'f', 'g']

str = 'hij klm opq'				# STRING to list of words
print(str.split())				# -> ['hij', 'klm', 'opq']

str = list('Ejemplo')			# STRING to char list
print(str)						# -> ['E', 'j', 'e', 'm', 'p', 'l', 'o']

# - Tuples -
print("\n- To Tuple -")
l = [0, 1, 2, 3, 4, 5]		# TRANSFORMAR utilisando tuple function
t = tuple(l)				# Lista a tuple
print(f'lista {l} to  {t}')	# -> lista [0, 1, 2, 3, 4, 5] to  (0, 1, 2, 3, 4, 5)
s = {'uno', 'dos', 'tres'}	# 
t = tuple(s)				# Set a tuple
print(f'Set {s} to  {t}')	# -> Set {'tres', 'dos', 'uno'} to ('tres', 'dos', 'uno')
str = 'abc'					#
t = tuple(str)				# String to tuple
print(f'Str {str} to  {t}')	# -> Str abc to  ('a', 'b', 'c')

print("\n- To Set -")
l = [0, 1, 2, 3, 4, 5]		# TRANSFORMAR utilisando tuple function
s = set(l)					# Lista a set
print(f'lista {l} to  {s}')	# -> lista [0, 1, 2, 3, 4, 5] to  {0, 1, 2, 3, 4, 5}
t = ('uno', 'dos', 'tres')	# 
s = set(t)					# Tuple to set
print(f'Tuple {t} to  {s}')	# -> Set {'tres', 'dos', 'uno'} to ('tres', 'dos', 'uno')
str = 'abc'					#
s = set(str)				# String to set
print(f'Str {str} to  {s}')	# -> Str abc to  ('a', 'b', 'c')