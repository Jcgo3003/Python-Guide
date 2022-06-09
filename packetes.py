# - Paquetes
print('\n- Paquetes -')
# - Un módulo de Python que puede contener submódulos o, recursivamente, subpaquetes.
# - Es bastante común importar subpaquetes y submódulos en un archivo __init__.py para que esten disponibles

import world # IMPORTANDO paquetes 

print(world)			# >> <module 'world' from '/Users/jbst/Documents/Notas Coding/Python/Python in deep/examples/world/__init__.py'>
print(world.africa)		# >> <module 'world.africa' from '/Users/jbst/Documents/Notas Coding/Python/Python in deep/examples/world/africa/__init__.py'>

print(dir())			# >> ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__',
print(world.__file__) 	# >> /Users/jbst/Documents/Notas Coding/Python/Python in deep/examples/world/__init__.py

from world import europe	# IMPORTANDO un paquete explicitamente

europe.greece			# greece submodule fue importado automaticamente
world.europe.norway		# Como world fue importado, europe tambien se encuentra dentro del namespace de world

# europe.spain			# Como spain no esta importado en __init__ provoca un error AttributeError: module 'world.europe' has no attribute 'spain'

import world.europe.spain # IMPORTANDO spain explicitamente

# Note that spain is also available directly inside the europe namespace
europe.spain			# NameError: name 'spain' is not defined
# spain 

from world.europe import norway # IMPORTANDO a noruega dos veces de esta manera hace que norway ahora este en el namespace
norway

# world.africa.zimbabwe	# zimbabwe al no estar importada en __init__ no existe por lo que causa un error AtributeError

from world.africa import zimbabwe # zimbabwe debe ser importado explicitamente

zimbabwe				# zimbabwe ahora ya esta disponible
