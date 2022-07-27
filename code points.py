# Code Points
# - Built-in functions chr() and ord() are used to convert between 
# 	Unicode code points and characters.
# - A character can also be represented by writing a hexadecimal Unicode code point 
#   with \x, \u, or \U in a string literal.
# - Unicode points are given in Hex and dec

# Convertions
print('- Character to Unicode point') # -  ord()  -
print('- Character to Dec')
letter = 'A'			
rtn = ord(letter)		# Unicode point is given in 'Int' type
print(rtn, type(rtn))	# >> 65 <class 'int'>		| 65 Its the value to 'A' in ASCII Code Point

print('- Character to Hex/Bin')
hx = hex(ord('A'))		# From dec to hex(str)
print(hx, type(hx))		# >> 0x41 <class 'str'>

rtn = format(ord('A'), '#x')# Straight to hex format from a chr
print(rtn, type(rtn))	# >> 0x41 <class 'str'>
rtn = format(ord('A'), '#b')# Straight to bin format from a chr
print(rtn, type(rtn))	# >> 0b1000001 <class 'str'>

rtn = format(ord('A'), 'x')# Straight to hex format from a chr
print(rtn, type(rtn))	# >> 41 <class 'str'>
rtn = format(ord('A'), 'b')# Straight to bin format from a chr
print(rtn, type(rtn))	# >> 1000001 <class 'str'>

print('\nUnicode point to Character')# -  chr()  -
print('- Dec to Character')
dec = 70
rtn = chr(dec)			# From a dec to a ASCII Character relative
print(rtn, type(rtn)) 	# >> F <class 'str'>

print('- Hex|Bin to Character')# Hex|Bin as strings
hx = '0x41'					   # hex as a string
dec = int(hx, 16)			   # hex to dec
rtn = chr(dec)				   # dec to ascii code point
print(rtn, type(rtn))  # >> A <class 'str'>

bn = '0b1000001'				# bin as a string
dec = int(bn, 2)			    # bin to dec
rtn = chr(dec)				    # dec to ascii code point
print(rtn, type(rtn))  # >> A <class 'str'>

print('- Hex|Bin as integers to Character')# Hex|Bin would be converted to Dec by deafault
hx = 0x41
rtn = chr(hx)				   # chr(65)		| like a dec to ascii code point
print(rtn, type(rtn))  # >> A <class 'str'>

bn = 0b1000001
rtn = chr(bn)				    # chr(65)		|
print(rtn, type(rtn))  # >> A <class 'str'>

print('\nForm Escape \\') # Adding a escape '\' to a hex code translates it straight to a ASCII
letter_hx = '\x65' 		  # String to hexadecimal code-point	
print(letter_hx, type(letter_hx)) # >> e <class 'str'>

letter_up = letter_hx.upper() # As '\x65' its interpretated as string you can use string Methods on it
print(letter_up)	   # >> E

print('\nUnicode escape styles ')# Again '\' hex code translates it straight to a ASCII
print('-Form \\uXXXX escape-') 	 # And string you can use string Methods on it
letter = '\u0041'				
print(letter, letter.lower(), type(letter))# >> A a <class 'str'>

print('-Symbols')
what = '\u0890'				
print(what, list(what),type(what))# >> ࢐ <class 'str'>

print('life on mars\u0890')# >> life on mars a࢐

print('- Form U+XXXX')
hx = 'U+0041'				# U+0041 	| Hex Code Point -> Hex
str = hx.lstrip('U+')		# 0041 		| Hex to Dec
dec = int(str, 16)			# 65        | Dec to ASCII		
rtn = chr(dec)				# 'A'		| ASCII
print(hx, str, dec, rtn)# >> U+0041 0041 65 A
print(type(hx), type(str), type(dec), type(rtn))# >> <class 'str'> <class 'str'> <class 'int'> <class 'str'>			

print('\nMultiple Unicode code points')# Multiple Unicode code points
# ord() does not support such emoji and an error raises
# rtn = ord('🇯🇵')  - TypeError: ord() expected a character, but string of length 2 found
jp = '🇯🇵'
rtn = jp.encode('utf-8')
print(jp, rtn)		# >> 🇯🇵 b'\xf0\x9f\x87\xaf\xf0\x9f\x87\xb5'  | Here you can see the encoding for these Characters in UTF-8

# A deep look into encoding bytes in 'Advanced encoding-decoding bytes' 
print('\nSome other Code Points')# Some other encodings are not well interpreted by the console
uno = '%C3%A9'     # Percent-encoded hex UTF8 (probably from URLs)
dos = '&#10152;'	# named HTML
tres =  '&middot'; # XML entity
print(uno, dos, tres)
# >> %C3%A9 &#10152; &middot

print('\nWarnigs') 
# In raw strings where escape sequences are disabled, the string is treated as is.
str = '\u0041'
print(str, len(str),type(str))		# >> A 1 <class 'str'>

raw_str = r'\u0041'			
print(raw_str,len(raw_str), type(raw_str))# >> \u0041 6 <class 'str'>

# Referencies
# https://note.nkmk.me/en/python-chr-ord-unicode-code-point/#:~:text=In%20Python%2C%20the%20built%2Din,Unicode%20code%20points%20and%20characters.&text=A%20character%20can%20also%20be,U%20in%20a%20string%20literal.