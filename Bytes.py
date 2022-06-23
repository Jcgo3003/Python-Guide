# Differenst between byte and a string
# - Bytes contain raw unsigned 8-bit vaulues displayed in ASCII

a = '\x65'.upper()
print(list(a)) # >> ['E']
print(a)	   # >> E

a = b'\x65'
print(list(a)) # >> [101]
print(a)	   # >> b'e'

a = b'\x65'.upper() 
print(list(a)) # >> [69]
print(a)	   # >> b'E'

# Strings  cotain Unicode points that represent textual characters
a = 'life on mars a\u0890L
print(list(a)) # >>['l', 'i', 'f', 'e', ' ', 'o', 'n', ' ', 'm', 'a', 'r', 's', ' ', 'a', '\u0890', ' ']
print(a)	   # >> life on mars a࢐