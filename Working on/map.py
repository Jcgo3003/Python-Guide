# ------------- Map -------------
# - Permite procesar y transformar todos los elementos en un iterable sin usar un for 
# - Aplica una función de transformación a cada elemento
# - Esta devuelve un objeto map, por lo que es necesario transformarlo antes
# - Soporta tanto funciones buil-int como funciones proprias

l = [1, 2, 3, 4, 5]

# - Aplicando una custom function a una lista
print('Aplicando una custom function a una lista')

def double(x):
	""" A function to double a number """
	return x*2
sol = list(map(double, l))
print(sol)

# - Aplicando una custom function a una lista
print('Aplicando una custom build-int a una lista')

res = list(map(l**2, l))
print(res)



