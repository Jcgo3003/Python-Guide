# Python repr() Method
# returns a string containing a printable representation of an object. 
# The repr() function calls the underlying __repr__() function of the object.
# Syntax:
# repr(obj)
import datetime

rtn = repr(10)
print(type(rtn))		# >> <class 'str'>
print(rtn)				# >> '10'
rtn = repr(10.5)
print(rtn)				# >> '10.5'
rtn = repr(True)
print(rtn) 				# >> 'True'
rtn = repr(4+2)
print(rtn)				# >> '6'


now = datetime.datetime.now()
print(now)				# >> 2022-07-06 15:45:44.508961 

rtn = repr(now)		
print(rtn)				# >> datetime.datetime(2022, 7, 6, 15, 45, 44, 508961)




print('\n- f-String -')
n = 1
print(f'str {n!r}')		# >> str 1
print(f'str {n}')		# >> str 1
print(f'date {now}') 	# >> date 2022-07-06 15:44:54.489542
print(f'date {now!r}')	# >> datetime.datetime(2022, 7, 6, 15, 44, 54, 489542)

