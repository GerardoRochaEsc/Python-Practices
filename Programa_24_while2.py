# Valor inicial de x
x = 0
# while menor o igual que 30
while x <= 30:
	x += 1 
	# if para saltar ejecuciones del bucle
	if x == 4 or x == 6 or x == 10:
		print('Se saltó el valor ', x, ' de x')
		continue
	if x == 15:
		print('Se rompió la ejecución del bucle cuando x valía: ', x)
		break
	print(x)