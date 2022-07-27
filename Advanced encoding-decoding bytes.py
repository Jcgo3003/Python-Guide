# Basic
str_original = 'Hello'

bytes_encoded = str_original.encode(encoding='utf-8')
print(bytes_encoded, type(bytes_encoded))  # >> b'Hello' <class 'bytes'>

str_decoded = bytes_encoded.decode()
print(str_decoded)          # >> Hello
print(type(str_decoded))    # <class 'str'>

print('str_original == str_decoded =', str_original == str_decoded)

# Code Point
print('Code Points')
cyrillic = 'Ф'
utf8 = cyrillic.encode('utf-8')	 # Same string  
utf16 = cyrillic.encode('utf16') # different byte encoding
print(utf8, utf16)				 # >> b'\xd0\xa4' b'\xff\xfe$\x04'

# Every Code Poit encoding has his own rules to encode to bytes
# latin = cyrillic.encode('latin1') # byte encoding 
# UnicodeEncodeError: 'latin-1' codec can't encode character '\u0424' in position 0: ordinal not in range(256)

# Python console encoding
print('\nPython console encode')
what = '\u0890'					  # String \uXXXX escape Style
print(what, list(what),type(what))# >> ࢐ ['\u0890'] <class 'str'>

byte = what.encode('utf-8')
print(byte)		  # >> b'\xe0\xa2\x90'
print('\xe0\xa2\x90')# >> à¢ 	| Python decodes to latin1
print(byte.decode('latin1'))	    # >> à¢

# Advaced Encoding
print('\n- Advanced Encoding -')
s = 'Madoka\xe2\x98\x85Magica'
print(s,type(s))		  # >> MadokaâMagica <class 'str'>

rtn = s.encode('latin1') # str to bytes | encoding with latin1
print(rtn,type(rtn))     # >> b'Mahou Shoujo Madoka\xe2\x98\x85Magica'  <class 'bytes'>

rtn = s.encode('utf-8') # str to bytes | encoding with utf-8
print(rtn,type(rtn))     # >> b'Madoka\xc3\xa2\xc2\x98\xc2\x85Magica' <class 'bytes'>

rtn = s.encode('latin1').decode('utf8') # Encoding to Bytes(latin1) and decoding to str(utf-8)
print(rtn, type(rtn))	      # >> Mahou Shoujo Madoka★Magica <class 'str'>

rtn = s.encode('utf-8').decode('latin1') # Encoding to Bytes(utf8) and decoding to str(latin1)
print(rtn, type(rtn))	      # >> MadokaÃ¢ÂÂMagica <class 'str'>

# ATENTION!!! You MUST to use the right encoding in order to get right the string unicode repr
# From s = 'Madoka\xe2\x98\x85Magica' | Encoding to Bytes(latin1) and decoding to str(utf-8)
# >> Mahou Shoujo Madoka★Magica <class 'str'>	This one is how it has to be
# From s = 'Madoka\xe2\x98\x85Magica' | Encoding to Bytes(utf8) and decoding to str(latin1)
# >> MadokaÃ¢ÂÂMagica <class 'str'> ERROR!!!

# The latin1 encoding map 1:1 to the first 256 code points in Unicode.
# it will parse every character one by one
# 'Madoka\xe2\x98\x85Magica' ->  b'Mahou Shoujo Madoka\xe2\x98\x85Magica'
# encode('latin1') translates the code points directly back to bytes. 
# Then you can .decode('utf8') the bytes properly.

# Deeper
print('\n- Strings -')# 
star = '★'		 			# star in utf-8 encoding
print(star, type(star))		# >> ★ <class 'str'>

latin = 'â'# star in latin1 encoding
print(latin, type(latin))	# â <class 'str'> 

print('\n- Encoding | Str repr to Byte repr -')# Character to Encoded bytes
rtn = star.encode('utf-8')			 # from utf-8 string repr to byte repr
print(star,rtn)	# >> ★ b'\xe2\x98\x85' | from ★ str repr to b'\xe2\x98\x85' byte  -  
print(type(star),type(rtn))          # >> <class 'str'> <class 'bytes'>

rtn = latin.encode('latin1')		 # from latin string repr to byte repr
print(latin, rtn)	# >> â b'\xe2\x98\x85' | From â string to b'\xe2\x98\x85' byte 
print(type(latin),type(rtn))     # >> <class 'str'> <class 'bytes'>


# Warning !!! You MUST to use the right encoding to the str - trying to encode with the wrong encoding 
# rtn = star.encode('latin1') # UnicodeEncodeError: 'latin-1' codec can't encode character '\u2605' in position 0: ordinal not in range(256)
print('\nDecoding | Byte repr to Str repr -')
byte = b'\xe2\x98\x85' 				# byte
utf = byte.decode('utf-8')			# byte repr - to utf string repr
print(byte, utf)					# >> b'\xe2\x98\x85' ★
print(type(byte),type(utf))         # >> <class 'bytes'> <class 'str'> 

latin = byte.decode('latin1')		# byte repr - to latin string repr
print(byte, latin)					# b'\xe2\x98\x85' â
print(type(byte),type(latin))       # >> <class 'bytes'> <class 'str'> 

print('\nEncoding/Decoding | From one encoding to another(utf-8 -> latin1)')		
# To cross from any encoding you MUST to pass to bytes before.
# rtn = star.encode('latin1') # UnicodeEncodeError: 'latin-1' codec can't encode character '\u2605' in position 0: ordinal not in range(256)

rtn = star.encode('utf-8').decode('latin1')
# from ★ str repr to b'\xe2\x98\x85' byte to â string
print(star ,star.encode('utf-8'), rtn)# >> â b'\xe2\x98\x85' ★
print(type(star),type(star.encode('utf-8')), type(rtn))# >> <class 'str'> <class 'bytes'> <class 'str'>


rtn = latin.encode('latin1').decode('utf8') 
print(latin ,latin.encode('latin1'), rtn)		# >> â b'\xe2\x98\x85' ★
print(type(latin ),type(latin.encode('latin1')), type(rtn))# >> <class 'str'> <class 'bytes'> <class 'str'>

# Reference
# https://stackoverflow.com/questions/42778346/python-3-string-with-xhh-hex-values-to-unicode
