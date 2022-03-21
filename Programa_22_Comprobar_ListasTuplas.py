#Haz una tupla que contenga cuatro colores de tu elección.
#Tendrás que poner una condición con el condicional if para cada color que le avise 
#al usuario que el color está en la tupla con un mensaje como este: print('El color rojo está admitido') 
#y una condición False para contemplar cualquier color que no esté en la tupla con un mensaje como este: print('Color no admitido').
# No puedes utilizar el operador ==. Además tendrás que hacer esto con un input() que permita introducir un color al usuario.
colores= ('azul','rojo','verde','naranja')
color = (input('Elije un color:\n'))
if color in colores[0]:
	print('El color azul está admitido')
elif color in colores[1]:
	print('El color rojo está admitido')
elif color in colores[2]:
	print('El color verde está admitido')
elif color in colores[3]:
	print('El color naranja está admitido')
else:
	print('Color no admitido')