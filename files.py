print('--- Leyendo archivos ---')
# Leyendo archivos 

filename = "data/archivo.txt"	 		# Declarando archivo

# with open('text_files/filename.txt')  # ABRIENDO archivo

# With
print('- With -')						
# - With tiene una mejor sintaxis y manejo de excepciones. --- MEJOR
# - cerrará automáticamente el archivo.
with open(filename, 'r') as file:		# ABRIENDO archivo bajo un alias, CONVIRTIENDO el contenido en '_io.TextIOWrapper' object
    contents = file.read()	 	 		# CONVIRTIENDO a file en un str 
    lines = file.readlines()			# IMPORTANTE!!! el objeto que solo puede ser utilizado una vez

print(lines)							# -> []				POR ESO lines es una lista vacia
print(contents)							# -> 'London, the capital of England and the United Kingdom, is a...'

# with open(filename, 'r') as file:		
#     lines = file.readlines()			# Ahora lines se utiliza primero
#     contents = file.read()

# print(f'lines {lines}')				# -> lines ['London, the capital...
# print(f'contents {contents}')			# -> contents 		 Por eso contents esta vacio
	
	
print('\n- open -')			# IMPORTANTE open es un metodo mas antiguo
file = open(filename, 'r')
lines = file.readlines()	# Readlines utiliza \n para separar cada elemento en una lista
contents = file.read()		# Al igual que antes file solo puede ser utilizado una sola vez

print(lines)				# -> ['London,		Imprimiendo una lista de lineas
print(lines[2])				# -> At its cen..	Imprimiendo un elemento de la lista
print(len(lines))			# -> 5 				Tamano de la lista

print(contents)				# ->				Vacio

file.close()				# ES OBLIGATORIO cerrar el archivo al terminar!!!




# # Filepaths
# print('\n- Filepaths Absoluta/relativa -')

# # directorio_archivo = '/home/bla/bla_bla/bla_bla_bla/tu_archivo.txt'	# ABRIR un archivo direcion absoluta
# directorio_archivo = './data/archivo.txt'		# ABRIR un archivo direcion relativa

# with open(directorio_archivo) as archivo:
# 	contents = archivo.read()
# 	lines = archivo.readlines()

# print(contents)							# Imprimiendo el resultado	 'London, the capital of England and the United Kingdom..'
# print(lines)							# Imprimiendo una lista de lineas []

# # Pathlib
# print('\n- Pathlib -')
# from pathlib import Path

# filename = Path('data/test.txt')
# filename.touch(exist_ok=True)  				# Crea un archivo, si ya exite no hara nadax

# # Leyendo lineas de los archivos 
# print('\n- Leyendo lineas de un archivo -')	

# file = "data/test.txt"						# ASIGNANDO el archivo a una variable

# with open(file) as archivo: 			# ABRIENDO el archivo, que solo estara abierto dentro de
# 	for linea in archivo:				# Scope de with
# 		print(linea)
# 	lineas = archivo.readlines()		# readlines() function Permite guardar las lineas en una lista

# print(lineas)							# Imprimiendo lista de lineas

# # Solo se puede manipular el archivo dentro del scope de with

# # Escribir un archivo ---------------------------------------------------
# print('\n- Escribir archivo -')
# archivo = Path('data/archivo2.txt')					# Declarando archivo
# archivo.touch(exist_ok=True)
# # Texto
# Paris = """	Also known as the Latin Quarter,
# 		the 5th arrondissement is home to the Sorbonne university 
# 		and student-filled cafes. It's also known for its bookshops, 
# 		including the famed Shakespeare & Company. Family-friendly attractions 
# 		include the Jardin des Plantes botanical gardens and the National Museum of Natural History. 
# 		The stately Panthéon building holds the remains of notables like Voltaire and Marie Curie."""

# with open(archivo, 'w') as file:		# Abriendo archivo, o creandolo si no existe
# 	file.write(Paris)					# Escribiendo archivo

# # Estos son los modos disponibles
# # se abre en read modo por defecto
# # read mode ('r'), - Lee el archivo Default mode
# # write mode ('w') - Escribe sobre lo que ya existente
# # append mode ('a') - Agrega mas informacion sobre la ya existente
# # read/write mode ('r+') - Agrega los cambios sobre lo que ya esta escrito
# 			

# - Method	Description
# close()	Closes an opened file. It has no effect if the file is already closed.
# detach()	Separates the underlying binary buffer from the TextIOBase and returns it.
# fileno()	Returns an integer number (file descriptor) of the file.
# flush()	Flushes the write buffer of the file stream.
# isatty()	Returns True if the file stream is interactive.
# read(n)	Reads at most n characters from the file. Reads till end of file if it is negative or None.
# readable()	Returns True if the file stream can be read from.
# readline(n=-1)	Reads and returns one line from the file. Reads in at most n bytes if specified.
# readlines(n=-1)	Reads and returns a list of lines from the file. Reads in at most n bytes/characters if specified.
# seek(offset,from=SEEK_SET)	Changes the file position to offset bytes, in reference to from (start, current, end).
# seekable()	Returns True if the file stream supports random access.
# tell()	Returns an integer that represents the current position of the file's object.
# truncate(size=None)	Resizes the file stream to size bytes. If size is not specified, resizes to current location.
# writable()	Returns True if the file stream can be written to.
# write(s)	Writes the string s to the file and returns the number of characters written.
# writelines(lines)	Writes a list of lines to the file.

# Referencia
# https://www.programiz.com/python-programming/file-operation