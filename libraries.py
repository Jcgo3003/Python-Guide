# Some Handy Python Libraries

# URL parser
from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=',keep_blank_values=True) # RETURN diccionario
print(repr(my_values))	# >> {'red': ['5'], 'blue': ['0'], 'green': ['']}
print(my_values['red']) # >> ['5']

# Collections - Data procesing	
import collections
l = [1,2,3,2,1,5,6,5,5,5]
rtn = [item for item, count in collections.Counter(l).items() if count > 1]
print(rtn)		# >> [1, 2, 5]			- Counter RTN duplicate items

  
# timeit - measuring the execution time of your python code snippets
# timeit runs your snippet of code millions of times (default value 
# is 1000000) so that you get the statistically most relevant measurement of code execution time!
#  timeit.timeit(stmt, setup, timer, number) accepts four arguments: 
# - stmt which is the statement you want to measure; it defaults to ‘pass’.
# - setup which is the code that you run before running the stmt; it defaults to ‘pass’. 
#   We generally use this to import the required modules for our code.
# - timer which is a timeit.Timer object; it usually has a sensible default value so you don’t have to worry about it.
# - number which is the number of executions you’d like to run the stmt.
import timeit

# code snippet to be executed only once
mysetup = "from math import sqrt"

mycode = '''
def counter(x):
	return sum(range(1,x+1))
counter(4)
'''

time = timeit.timeit(setup = mysetup,
                     stmt = mycode,
                     number = 10000)
print(f'My code run in {time} seconds')

print('Bitwise operations')
import operator     # operator library lets you perform also bitwise operations
x = operator.iand(1, 6);
print(x, 1 & 6 ) 

x = operator.ior(1, 6);
print(x, 1| 6 )

x = operator.ixor(1, 4) # xor is AVAILABLE in this library
print(x)

