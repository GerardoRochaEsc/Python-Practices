#Al siguiente código añádele un par de rangos de edad. Uno de 18 años hasta 45 y otro de más de 100 años hasta 120.
edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad.')
elif edad <= 1 and edad < 18:
	print('Eres menor de edad.')
elif edad == 18 and edad <= 45:
	print('Eres mayor de edad.')
elif edad <= 100:
	print('Eres mayor de edad.')
elif edad > 100 and edad <=120:
	print('Eres mayor de edad.')
else:
	print('Edad no válida.')