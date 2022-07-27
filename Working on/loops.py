''' Loops con diversas opciones para crear listas y obtener informacion '''
print('--- Loops ---')
l = [('Quesadilla', 3.5),('Tacos', 5), ('Pizza slice', 1)]


print('\n- Enumerate -')
for i,(name, price) in enumerate(l):
	print('#%d  %-10s  %.1f' % (i+1, name, price))  # c style format
#1  Quesadilla  3.5
#2  Tacos       5.0
#3  Pizza slice  1.0
print('-n List Comprehension-')

l = [x for x in range(11)] 
print(l)				    # >> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Seleccionando valores 
l = [x for x in range(11) if not x%2]
print(l)				 	# >> [0, 2, 4, 6, 8, 10]




						  