# Leyendo archivos CVS
print('Leyendo archivos CVS')
import csv							# Modulo para leer un cvs
	
filename = "data/addresses.csv"	 	# Declarando archivo

with open(filename) as file_cvs:	# ABRIENDO el archivo y dandole un alias
    reader = csv.reader(file_cvs) 	# CREANDO el objeto lector
    print(reader)					# >> <_csv.reader object at 0x108eb97b0>
    header_row = next(reader) 		# Leyendo el header del archivo
    print(header_row)				# >> ['John', 'Doe', '120 jefferson st.', 'Riverside', ' NJ', ' 08075']
    print(header_row[1])			# >> Doe

    states, cps = [], []

    for row in reader:
    	print(row)					# reader es un objeto iterable
    	state = row[4]				# 
    	states.append(state)
    	cp = row[5]
    	cps.append(cp)

print('\n- Datos obtenidos -')
print(cps)    	
print(states)


print('\n- Json -')
import json                        # IMPORNTADO el modulo 

filename = 'data/test.json'		   # CARGANDO el archivo

with open(filename) as f:		   # ABRIENDO el archivo
	data = json.load(f)			   # CARGANDO los datos


print(data.keys())      # >> dict_keys(['type', 'metadata', 'features', 'bbox'])

read = './data/test_read.json'			   # CARGANDO un nuevo archivo

with open(read, 'w') as f:          
	json.dump(data, f, indent=4)   # CREAR una archivo facil de leer


with open('./data/obj.json', 'w') as f:
    dic = {'uno':1, 'dos':2, 'abc':['a', 'b', 'c'] }
    json.dump(dic, f, indent=2)





