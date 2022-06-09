# Python zen

# --- Naming ---
# lowercase_underscore - Variables, functions and attributes
var_uno = 1 					# Variables

def function_uno(var_uno):		# Funciones
	print('Python Zen way')     # Also attributes

# _leading_underscore
_protected_instance = 1			# Protected instance 

# __double_leading_underscore   
__private_instance_attribute = 1# Private instance attribute

# CapitalizeWord
ClassName = 1					# Class name

# Self for Intance methods 
# self.method = 1    			# SHOULD use self

# cls for Class methods 
# cls.method = 1				# cls method


# --- Expretions and statements --- 
# Iline negation 
a = True
b = False

if a is not b:
	print('Proper way')

if not a is b:
	print('NOT proper way!')


# Empty containers
l = []		
if not l: 
	print('Proper way')

if(len(l) == 0):
	print('Not proper way!')

# Not empty	containers
l = [1, 2, 3, 4]

if l: 
	print('Proper way')

if(len(l) != 0):
	print('Not proper way!')

# Avoid single-line if, for while loops !!!
# (If you can fit an expression on one line, 
# 		surround it with parentheses )
# Surround Multiline expressions with parentheses, instead of \

# --- import ---
import math 		# Must be always at the top of the file
from math import pi # Use absolute names for modules
# from . import date | If you must to do relative import use . import foo 
# Import by Sections
# import math   | Standard librarys
# import foo 	| Third-party modules
# import mine   | Own modules


	










