# Short Circuiting
# - and | Si valor de la izquierda es false | Derecha ni si quiera sera evaluada
print('- and -')# Si valor de la izquierda True | Return valor de la derecha
rtn = False and 'hello'
print(rtn)			# >> False

rtn = True and 'hello'
print(rtn)			# >> Hello

rtn = 10 and 11 # And actuando como operadores > < | Si izq es False; derecha ni si quiera sera evaluada 
print(rtn)				# >> 11
rtn = 10 and 5 # And actuando como operadores > <  | Si izq es False; derecha ni si quiera sera evaluada
print(rtn)				# >> 5

# - Or - Si el valor de la izquierda es False | Return valor derecha
print('\n- or -')

rtn = 10 or 11 # Or actuando  como shorcut | Si es izq es True dejara izq
print(rtn)				# >> 10	

rtn = 10 or 5 # Or actuando  como shorcut  | Si es izq es True dejara izq
print(rtn)				# >> 10	

rtn = 'hello' or 'bla'
print(rtn)				# >> hello

rtn = 0 or 'bla'
print(rtn)				# >> bla

rtn = 0 or False
print(rtn)				# >> False

# Shor circuit 
print('- Ejemplos -')
n = 5	# rtn will only sum 2 if n > 0
rtn = 5 + 2*(n>0) 
print(rtn) 				# >> 7

n = 0
rtn = 5 + 2*(n>0) 
print(rtn) 				# >> 5

n = 1
rtn = 5 =-(n<1)	# 5 + 1 only if n < 1


# Lista 
print('\n- Lista -')
l = [] # Empty list

if l:
	print('Lista con valores')
else: 
	print('Lista Vacia')

# >> Lista vacia
# IMPORTANTEbool()! Es considerado Pythonic utilizar de esta manera la traduccion de Python
# De algunos valores; Pero esto no es una regla en todos lo lenguajes, Javascript
# Traduce una lista vacia a true.

print('\n- Tranformaciones a boolean -')
print('- Matriz -')
l = [1, 2, 3];
print(bool(l))				# >> true

l = []
print(bool(l)) 				# >> false

print('\n- Diccionarios -');
o = {'a': 1, 'b':2, 'c':3};
print(bool(o)) 				# >> true

o = {}
print(bool(o))				# >> false


print('\n- Strings -');
print(bool('hello'))		# >> true
print(bool(''))				# >> false

print('\n- Numbers -');
print(bool(12))				# >> true
print(bool(0))				# >> false


# Reaferencies
# https://www.pythontutorial.net/python-basics/python-boolean/#:~:text=Python%20boolean%20data%20type%20has,tuple%2C%20and%20an%20empty%20dictionary.
# https://www.geeksforgeeks.org/short-circuiting-techniques-python/



