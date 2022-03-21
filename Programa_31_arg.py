#¿Cuántos argumentos se utilizan en cada una de estas llamadas?
def colores(*args):
	pass
colores('rojo', 'azul', 'verde', 'amarillo') #4 argumentos
colores('lila', 'negro', 'rojo') #3 argumentos
colores('rosa') # 1 argumento
colores('marrón', 'naranja') # 2 argumentos

#Completa el siguiente fragmento de código:
def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')
#Faltaba agregarle parametros a la funcion
colores('verde','amarillo')

#Crea una función que realice la suma de 
#cinco números utilizando solo *args. 
#Debes imprimir el resultado en la consola. 
#La suma no se realizará directamente sobre el print().
def suma(*args):
	res=args[0]+args[1]+args[2]+args[3]+args[4]
	print('El resultado de la suma es:',res)
suma(5, 123, 343, 7432, 986, 325)