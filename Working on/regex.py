# Function	Description
import re




s = re.findall(r'[^\W_0-9cikmov]', "Don't match 1232 or cikmov") # >> ['D', 'n', 't', 'a', 't', 'h', 'r']
print(s)
# - Funciones - 
print('\n- Funciones -')
# findall	Returns a list containing all matches
# search	Returns a Match object if there is a match anywhere in the string
# split	Returns a list where the string has been split at each match
# sub	

# Metacharacters Supported by the re Module
# The following table briefly summarizes all the metacharacters supported by the re module. Some characters serve more than one purpose:

# Character(s)	Meaning
# .		Matches any single character except newline
# ^	 	Anchors a match at the start of a string
# ∙ 	Complements a character class
# $	Anchors a match at the end of a string
# *	Matches zero or more repetitions
# +	Matches one or more repetitions
# ?	∙ Matches zero or one repetition
# ∙ Specifies the non-greedy versions of *, +, and ?
# ∙ Introduces a lookahead or lookbehind assertion
# ∙ Creates a named group
# {}	Matches an explicitly specified number of repetitions
# \	∙ Escapes a metacharacter of its special meaning
# ∙ Introduces a special character class
# ∙ Introduces a grouping backreference
# []	Specifies a character class
# |	Designates alternation
# ()	Creates a group
# :
# #
# =
# !	Designate a specialized group
# <>	Creates a named group

# IMPORTANTE!!! 
# Es mejor escribir el regex y funciones en una sola linea
# r.findall('aeiou', str)  		-> Codigo bien escrito √ 
# regex = 'aeiou'				-> mal  x
# r.findall(regex, str)

# Referencia
# https://www.w3schools.com/python/python_regex.asp