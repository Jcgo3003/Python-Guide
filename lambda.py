print('lambda')
# - Is a small anonymous function.
# - Use them as an anonymous function inside another function(callbacks)
# - Can take any number of arguments, but can only have one expression.
# - Use lambda functions when an anonymous function is required for a short period of time.
# Syntax - lambda arguments : expression

l  = [ 1, 2,  3, 4, 5]
t1 = (10, 4,  5 )
t2 = ( 2, 5, 18 )
s = '1 2 3 4 5' 

print('Declaring')
ldb = lambda a : a + 10
print(ldb(5))		# >> 15

print('\nMultiple Argument')
ldb = lambda x, y, z, i: x + y + z + i
print(ldb(1,2,3,4))	# >> 10

print('Callbacks')
rtn = tuple(map(lambda i, j: i & j, t1, t2))# using  - bitwise and over two tuples
print(rtn)		# >> (2, 4, 0)

print('\nCurring')
def myfunc(n):
	print(f'n = {n}')
	return lambda a : a * n

mydoubler = myfunc(2)	# >> n = 2
mytripler = myfunc(3)   # >> n = 3

print(mydoubler(5))  	# >> 10
print(mytripler(5))  	# >> 15

# Referencia
# https://www.w3schools.com/python/python_lambda.asp
# https://realpython.com/python-map-function/#:~:text=loops%2C%20functions%2C%20and-,lambda%20functions,-would%20be%20helpful