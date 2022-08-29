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

print('\n[]')
print('Offset from left')
print('123456789'[1:])  # >> 2345789 			
print('123456789'[2:])  # >> 345789 			

print('\nOffset from right')
print('123456789'[:-1])   # >> 12345678
print('123456789'[:-2])   # >> 12345678

print('\nInverting strings')
print('123456789'[::-1])  # >> 987654321	
print('offset right')
print('123456789'[:0:-1]) # >> 98765432
print('123456789'[:1:-1]) # >> 9876543
print('offset left')
print('123456789'[8::-1]) # >> 987654321
print('123456789'[7::-1]) # >> 87654321