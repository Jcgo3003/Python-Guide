# Bitwise Operations
print('- and -')
# 0100  - 4  |  Bitwise And Operation entre un numero par(even) 
# 0001  - 1  |  y '1' el resultado es cero 
# 0000  - 0  | '&' para Bitwise Operation
val1 = '0100'
val2 = '0001'
print(val1, val2)   # >> 0111 0100
print(int(val1, 2), int(val2, 2))# >> 5 1
print(4 & 1) # >> 0

# 0101  - 5  |  Bitwise And Operation entre un numero impar(odd) 
# 0001  - 1  |  y '1' el resultado es uno 
# 0001  - 1  
val1 = '0101'
val2 = '0001'
print(val1, val2)   # >> 0111 0100
print(int(val1, 2), int(val2, 2))# >> 5 1
print(5 & 1) # >> 1

print('\n- or -')
val1 = '0100'       #                       0100
val2 = '0001'       #                       0001
print(val1, val2)   # >> 0100 0001      
print(int(val1, 2), int(val2, 2))# >> 4 1
print(4 | 1)        # >> 5                  0101

val1 = '0101'       #                       0101
val2 = '0001'       #                       0001
print(val1, val2)   # >> 0111 0100          
print(int(val1, 2), int(val2, 2))# >> 5 1
print(5 | 1)        # >> 5                  0101

print('\n- Bitwise Complement Operator (~ tilde)-') 
# Takes one number and inverts all bits of it.
val_bin = '0010'            # 2 = 0010
val_dec = int(val_bin, 2)   # ~0010 = 1101 = 13 Bitwise Complement Operation  
print(val_bin, val_dec)     # >> 0010 2
print(bin(~val_dec) , ~val_dec)# >> -0b11 -3

# Expected output: 13           # Correct Output : -3
# The compiler returns the 2’s complement of the input value.

# The bitwise complement operator should be used carefully!!!. 
# The result of ~ operator on a small number can be a big number 
# if stored in an unsigned variable. And the result may be a negative 
# number if the result is stored in a signed variable 
# (assuming that the negative numbers are stored in 2’s 
# complement form where the leftmost bit is the 3sign bit).

# 2º Complemento
print('\n- Operacion para obtener el Segundo Complemento -')

val_bin = '0011'                # '0011'
val_dec = int(val_bin, 2)       # 3
print(val_bin, val_dec)         # >> 0011 2
print('Primer complemento')
val_bin = '1101'
val_dec = int(val_bin, 2) 
print(val_bin, val_dec)         # >> 1101 13
print('Suma')
val_bin = '1110'                # 1101 + 0001 = 1110
val_dec = int(val_bin, 2) 
print(val_bin, val_dec)         # >> 1110 14
print('Segundo complemento')
val_bin = '0001'                # ~110 = 0001
val_dec = int(val_bin, 2)       #
print(val_bin, val_dec)         # >> 0001 1




# Shifting 
print('\n- Shifting -')# Desplasa agrega cierta cantidad de 0 la izquierda o derecha 
x_bin = '00111100'   
x_dec = int(x_bin, 2)       
print(x_bin, x_dec)      # >> 00111100 60

rtn = x_dec << 2         # 
print(bin(rtn)[2:], rtn) # >> 11110000 240

rtn = x_dec >> 2         # 00001111
print(bin(rtn)[2:], rtn) # >> 1111 15

print('\nAtention!')
# ATENCION left shift Agrega ceros !!!
# it's not using a fixed width where bits are discarded
# while many languages use a fixed width based on the data type, 
# Python expands the width to cater for extra bits.
# 1111 1111 << 4 gives 1111 1111 0000   like this!!! 
# 1111 1111 << 4 NOT 1111 0000  - Fixed width 8   
x_bin = '11111111'
x_dec = int(x_bin,2)
print(x_bin, x_dec) # >> 11111111 255

rtn = x_dec << 4
print(bin(rtn)[2:],rtn) # >> 111111110000 4080

# Para corregir esto se puede utilizar 8-bit filtro con and
filtro = '11111111'
filtro = int(filtro, 2)
print(filtro)       # >> 255

rtn = x_dec << 4
print(bin(rtn)[2:], rtn)# >> 111111110000 4080
rtn = (x_dec << 4) & filtro
print(bin(rtn)[2:], rtn)# >> 11110000 240



# Usos
print('\n- Usos -')
print('Filtro') # Getting ONLY the lower 4 bits of an integer
#     201: 1100 1001
# AND  15: 0000 1111
# ------------------
#  IS   9  0000 1001
print(int('11001001', 2), int('1111', 2))# >> 201 15
rtn = 201 & 15 
print(bin(rtn)[2:],rtn)# >> 1001 9

# lista de pares
print('\nGetting even and odds with And')
par = [i for i in range(11) if not i&1]
print(par)   # >> [0, 2, 4, 6, 8, 10]

inpar = [i for i in range(11) if i&1]
print(inpar)   # >> [1, 3, 5, 7, 9]

print('\nPack two 4-bit values inton an 8-bit one')
# The & 15 operation will make sure that both values only have the lower 4 bits.
# The << 4 is a 4-bit shift left to move val1 into the top 4 bits of an 8-bit value.
# The | combines these two together.
# If val1 is 7 and val2 is 4:
#                 val1            val2
#                 ====            ====
#  & 15 (and)   xxxx-0111       xxxx-0100  & 15
#  << 4 (left)  0111-0000           |
#                   |               |
#                   +-------+-------+
#                           |
# | (or)                0111-0100
val1 = '0111'
val2 = '0100'
print(val1, val2)   # >> 0111 0100
print(int(val1, 2), int(val2, 2))# >> 7 4
val1 = int('0111', 2)
val2 = int('0100', 2)
packed_val = ((val1 & 15) << 4) | (val2 & 15)
print(bin(packed_val)[2:], packed_val)# >> 1110100 116
 
print('\n- Colores hex to rgb -')

def hexToRgb(value):
    # Convert string to hexadecimal number (base 16)
    num = (int(value.lstrip("#"), 16))
    print(bin(num).lstrip('0b'), num)
    # Shift 16 bits to the right, and then binary AND to obtain 8 bits representing red
    r = ((num >> 16) & 0xFF) # Se agrega & en caso de que sea el resultado sea ''
    print(bin(num>>16).lstrip('b0'), r)

    # Shift 8 bits to the right, and then binary AND to obtain 8 bits representing green
    g = ((num >> 8) & 0xFF) # 0xFF = 255
    print(bin(num)[2:], bin(num>>8).lstrip('b0'))

    # Simply binary AND to obtain 8 bits representing blue
    b = (num & 0xFF)        # 0xFF = 255
    print(bin(num & 255).lstrip('b0'))

    return (r, g, b)

rojo = '#FF5733'
print(hexToRgb(rojo)) # >> (255, 87, 51)
azul = '#0086FF'
print(hexToRgb(azul)) # >> (0, 134, 255)

# Assert es un metodo de sistema por lo que los mensajes llegaran en la consola
# En caso de que la comparacion no sea igual
assert 1 == True




# Referencia
# https://stackoverflow.com/questions/1746613/bitwise-operation-and-usage
# https://www.geeksforgeeks.org/bitwise-complement-operator-tilde/#:~:text=The%20bitwise%20complement%20operator%20is,complement%20is%20~%20(Tilde).