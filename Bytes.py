# Differenst between byte and a string
# - Bytes contain raw unsigned 8-bit values displayed in ASCII

# Coded Bytes
print('\n- Coded Bytes -')
byte = b'\x65'	   		 # Declaring a byte
print(byte, type(byte))  # >> b'e' <class 'bytes'>

print('\nBytes To string -')
str = byte.decode()
print(str, type(str))	 # >> e 

print('\Character to bytes')
str = 'A'
rtn = str.encode('utf-8')
print(rtn)				# >> b'A'

print('\nInt to bytes')
# An int object can be used to represent the same value in the format of the byte. 
# The integer represents a byte, is stored as an array with its most significant digit (MSB)
# stored at either the start or end of the array
# Syntax: int.to_bytes(length, byteorder)
# length – desired length of the array in bytes .
# byteorder – order of the array to carry out conversion of an int to bytes. 
# 		little - Most significant bit(MSB) is stored at the end and least at the beginning 
# 		big - MSB is stored at start and LSB at the end. 

i = 1234
bytes_l = i.to_bytes(2, 'little')	# Parsing a int to bytes
bytes_b = i.to_bytes(2, 'big')		# 
print(bytes_l, bytes_b)				# b'\x08\x00\x00' b'\x00\x00\x08'
print(type(bytes_l), type(bytes_b))	# <class 'bytes'> <class 'bytes'>

# Encoding the same value as string its not the same and MUST never be used !!!
str = '8'
utf8 = str.encode('utf-8')	 # Same string 
utf16 = str.encode('utf16')  # different byte encoding
latin1 = str.encode('latin1')# different byte encoding
print(utf8, utf16, latin1)   # >> b'8' b'\xff\xfe8\x00' b'8'

# utf8_l = bytes_l.decode('utf-8')	
# utf8_b = bytes_b.decode('utf-8')
# print(utf8_l, utf8_b)				#      
# utf16_l = bytes_l.decode('utf-16')
# utf16_b = bytes_b.decode('utf-16')
# print(utf16_l)
# UnicodeDecodeError: 'utf-16-le' codec can't decode byte 0x00 in position 4: truncated data


print('\nWarnings')
print('List translates bytes into int ASCII Code point')
print(list(byte),type(list(byte)[0]), type(list(byte))) # >> [101] <class 'int'>   <class 'list'>  