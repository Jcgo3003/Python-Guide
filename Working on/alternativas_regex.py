""" Serie de ideas para sustituir ReGex in Python """



# Crear una funcion especificando una lista de letras
def is_vowel(x):
	return x in 'AEIOU aeiou'

print(is_vowel('E'))	# -> True
print(is_vowel('e'))	# -> True 
print(is_vowel(' '))	# -> True 
print(is_vowel('C'))	# -> False