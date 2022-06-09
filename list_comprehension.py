# list comprehension 
l = ['a', 'b', 'c', 'd', 'e', 'f']


sol = [ord(x) for x in l]
print(sol)


# list comprehension condicionales
l = [1, 2, 3, 4, 5, 6]

sol = ['odd' if x % 2 else 'even' for x in l]
print(sol)