print('Map') # ------------- Map -------------
# - Returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)
# - Permite procesar y transformar todos los elementos en un iterable sin usar un for 
# - Aplica una función de transformación a cada elemento
# - Esta devuelve un objeto map, por lo que es necesario transformarlo antes
# - Soporta tanto funciones buil-int como funciones proprias
# - map(function, iterable Obj1, iterable Obj2, etc...)

l  = [ 1, 2,  3, 4, 5]
t1 = (10, 4,  5 )
t2 = ( 2, 5, 18 )
s = '1 2 3 4 5' 

# Parsing data throug a function
print('Parsing data throug a function')
rtn = list(map(int, s.split(' ')))
print(rtn)		# >> [1, 2, 3, 4, 5]


# - Custom functions
print('\nCustom functions')
def double(x):
	return x*2

rtn = list(map(double, l))
print(rtn)		# >> [2, 4, 6, 8, 10]

# map + Funciones Lambda(anonimas)
print('\nLambda(anonimas)')
# using map() + lambda - bitwise and over two tuples
rtn = tuple(map(lambda i, j: i & j, t1, t2))
print(rtn)		# >> (2, 4, 0)


# Map through multiple iterable obj - dif. sizes iterable objets
print('\nMap through multiple iterable obj')
rtn = list(map(min, l, t1, t2))	# Because min can take multiple parameters it can perform his function over 3 iterables Obj.
print(rtn)		# >> [1, 2, 3]

rtn = tuple(map(max, l, t1, t2))
print(rtn)		# >> (10, 5, 18)

# Referencies
# https://www.geeksforgeeks.org/python-and-operation-between-tuples/
