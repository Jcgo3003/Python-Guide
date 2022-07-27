# Functional programing - Pure functions
# - computations are done by combining functions that take arguments and return a concrete value (or values) as a result. 
# - These functions don’t modify their input arguments and don’t change the program’s state. 
# - They just provide the result of a given computation. 
# - Also know as pure functions.
# Advantages
# Develop because you can code and use every function in isolation
# Debug and test because you can test and debug individual functions without looking at the rest of the program
# Understand because you don’t need to deal with state changes throughout the program
# Functional programming uses iterables(lists, arrays, etc)  to represent the data along with a set of functions that operate on that data and transform it. 
# three commonly used techniques: map, filter and reducing

# Mapping 
# Applying a transformation function to an iterable to produce a new iterable. 
# Items in the new iterable are produced by calling the transformation function on each item in the original iterable.

# Filtering
# Applying a predicate or Boolean-valued function to an iterable to generate a new iterable. 
# Items in the new iterable are produced by filtering out any items in the original iterable that make the predicate function return false.

# Reducing 
# Applying a reduction function to an iterable to produce a single cumulative value.

# ITS MORE PYTHONING WORKING WITH LIST COMPREHENTIONS OR GENERATORS than functional programing


l = [*range(10)]

if all(x < 11 for x in l): # RETURNS True if all elements in a iterable object pass a given command
	print('True')		   # >> True