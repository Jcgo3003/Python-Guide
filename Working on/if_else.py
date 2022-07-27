
print('if/else statement en una linea') # (codiciones):(consecuencias) 	- if/else stament en una sola linea

s = ['Th3 br0nw', '11234']

for x in s:
	for y in x:
		if y.isalpha() or y==" ":print(y,end="")
	else: print('- else statement -')


m=input()
print("snake_case"if"_"in m else("PascalCase"if m[0].isupper() else"camelCase"))