print('Between Numeric Systems')# Between Numeric Systems

print('Dec to Bin')# Dec to bin
bn = bin(10)
print(bn, type(bn))	# >> 0b1010 <class 'str'>

bn = format(10, '#b')
print(bn, type(bn)) # >> 0b1010 <class 'str'>

bn = format(10, 'b')
print(bn, type(bn)) # >> 1010 <class 'str'>
 
print('Bin to Dec') # Bin to Dec
dec = int('1010', 2)
print(dec)			# >> 10	

print('\nDec to Hex') # Dec to hex 
hx = hex(10)
print(hx, type(hx)) # >> 0xa <class 'str'>

hx = format(10, '#x') 
print(hx, type(hx)) # >> 0xa <class 'str'>

hx = format(10, 'x') 
print(hx, type(hx)) # >> a <class 'str'>

print('Hex to Dec')
dec = int('a', 16)
print(dec)			# >> 10	

print('\nWarnings')
print('Un-expected translations')# Un-expected translations
bn = 0b1000001 	    # The console translates bin|hex to dec by default if there's no ' '.
print(bn, type(bn)) # >> 65 <class 'int'>
hx = 0x41
print(hx, type(hx)) # >> 65 <class 'int'>

print(eval('0b1000001'))# >> 65
print(eval('0x41'))     # >> 65

rtn = chr(bn)		# Bin to ascii Unicode point			| Not '0b100001' as would be spected
print(rtn, type(rtn))# A <class 'str'> 

rtn = chr(hx)		# Hex to ascii Unicode point by default | Not '0x41' as would be spected
print(rtn, type(rtn))# A <class 'str'> 

# int() Method only supports str as first parameter
# dec = int(bn , 2) | TypeError: int() can't convert non-string with explicit base



str = str(bn)	    # '0b1000001'  
print(str, type(str))# 65 <class 'str'>  | Str method translates bn to a dec string by default



