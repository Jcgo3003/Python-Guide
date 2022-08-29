# Trucos para reducir codigo

# Funciones en variables 
print('- Funciones escondidas en variables -')
p = sum
print(p([10, 50])) 			# >> 60

# Escribir varias variables 
print('- Multiples variables por linea -')
x,y,z = 1, 2, 3 
print(x, y, z)


print('- Multiples variables mismo valor una linea -')
x=y=z = 0
print(x)		# >> 0
print(y)		# >> 0	
print(z)		# >> 0

# Multiples acciones en un if de una sola linea
print('- Multiples acciones en un solo if -')
n = 10
if n == 10: print('Diez'); n=1 	# >> Diez
print(n)						# 1

if n == 1: print('uno'); n=5;print('Tercer accion') # >> uno tercer accion 
print(n)						# 5

# Bitwise odd and even numbers
# Odd - Went odd will return 1
l = [x for x in range(11) if x & 1] # Normaly you would use if x % 2
print(l)		# >> [1, 3, 5, 7, 9]

# Even - Went even will return 0
l = [x for x in range(11) if (x & 1) == 0] # Normaly you would use if (x % 2) == 0]
print(l)		# >> [0, 2, 4, 6, 8, 10]




