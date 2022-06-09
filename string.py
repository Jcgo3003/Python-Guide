# ------------------------------------ string ------------------------------------
# Creando strings integradas con variables -
var, x, y = 10, 1, 2

# - Format
print('\n- Format -')					# INTEGRAR variables en un str python 3.5 y anteriores versiones
str = "{} Example {}".format(x, y) 		#
print(str)								# >> 1 Example 2
str = "{cuatro} Example {tres}".format(cuatro = 4, tres = 3) 	
print(str)								# >> 4 Example 3
str = "{0} Example {1}".format(x, y) 	#
print(str)								# >> 1 Example 2

# Formatting Types						# AGREGAR formato al string de salida
txt = "We have {:<8} chickens."
print(txt.format(49))
txt = "We have {:>8} chickens."
print(txt.format(49))

# - f string
print('\n- f string -')
str = f'{1000} texto!'					# INTEGRAR variables en un f string
print(str)								# >> 1 texto!
	
# ---------- Metodos ----------
# Metodos No destructivos - RETURN una copia de string
print('\n- Metodos No destructivos -')

# - Case -
print('\n- Case -')
str = ' The quick brown fox  '
print(str.upper()) 	# >>  THE QUICK BROWN FOX 	TRANSFORMAR str a mayusculas.
print(str.lower()) 	# >>  the quick brown fox 	TRANSFORMAR str a minúsculas.
print(str.title()) 	# >>  The Quick Brown Fox	TRANSFORMAR str primer letra a mayúscula|Sentence Case.
print(str)			# >>  The quick brown fox	Str permanece igual 

# strip/Eliminar \s -
print('\n- Strip -')		
print(str.rstrip()) 	# >>   The quick brown fox	ELIMINAR espacios blancos al final del string.
print(str.lstrip()) 	# >> The quick brown fox	ELIMINAR espacios blancos pero al principio del string.
print(str.strip()) 		# >> The quick brown fox	ELIMINAR espacios blancos de los dos lados en una sola ejecución.

# - Parse - 
print('\n- Parse -')
print(ord('a'))			# >> 97 	TRANSFORMA Char to ascii
print(chr(65))			# >> A 		TRANSFORMA un numbero ascii to char


# - Concatenar -
print('\n- Concanenar -')
str1 = 'hello '
str2 = 'world'
str_Final = str1 + str2 	# CONTATENAR 2 strings
print(str_Final)			# >> hello world

# - Join -
print('\n- Join -')
l = ['a', 'b', 'c', 'd', 'e']
print(*l)					# a b c d e  	Lista desempaquetada
print('$'.join(l))			# a$b$c$d$e 	Join

# - Acceder - 
print('\n- Acceder -')
print(str[1])				# >> T 		ACCEDER a un char				


print('\n- Slicinng -')

print(str[5:10])			# >> quick		CORTAR una seccion
print(str[9:4:-1])			# >> kciuq		CORTAR una seccion y desarrollarla al reves
print(str[::-1])  			# >>  xof nworb kciuq ehT  RETURN string al reves


print('\n- Miscellaneous -')
print('- eval -')   		# EJECUTA una operacion que este dada como string
rtn = eval('2 + 2')
print(rtn)					# -> 4
l = '1 2 3 4'
op = '+';
print(eval(op.join(l.split())))


# -       Escape sequences       -
# --------------------------------
# \0 - NUL character(\u0000)
# \0 - The NUL character (\u0000)  
# \b - Backspace (\u0008)
# \t - Horizontal tab (\u0009)
# \n - Newline (\u000A)
# \v - Vertical tab (\u000B)
# \f - Form feed (\u000C)
# \r - Carriage return (\u000D) 
# \" - Double quote (\u0022)
# \' - Apostrophe or single quote (\u0027)
# \\ - Backslash (\u005C)
# \xnn - The Unicode character specified by the two hexadecimal digits nn
# \unnnn - The Unicode character specified by the four hexadecimal digits nnnn
# \u{n} - The Unicode character specified by the codepoint n, where 
# n is one to six hexadecimal digits between 0 and 10FFFF (ES6)
