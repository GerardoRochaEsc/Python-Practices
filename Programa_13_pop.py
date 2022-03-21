#Elimina de la siguiente lista los elementos 'azul' y 'blanco'. Solo puedes eliminarlos utilizando el método pop(). Además, tendrás que guardar esos dos colores en una nueva lista.
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
c1 = colores.pop(1)
#Al eliminar se recorre el arreglo por lo que el blanco queda en la posicion 7
c2 = colores.pop(7)

colores_guardados = [c1, c2]
print(colores_guardados)
