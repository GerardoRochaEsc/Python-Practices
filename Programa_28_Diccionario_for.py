#Itera el diccionario teclado1 con un solo 
#bucle for que muestre esto en la consola:
teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}
#Se hace ek for para mostrar las categorias y características en forma de lista
for x in teclado1:
	print(x, '=', teclado1[x] + '.')