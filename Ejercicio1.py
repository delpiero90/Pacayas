#Calcular el precio final de cualquier producto, si se sabe que la tasa de impuesto al valor agregado es
#de un 13 %. El algoritmo debe recibir el nombre del producto y el precio, y debe imprimir el nombre
#del producto y el precio final. Para los efectos del ejercicio, TODOS los productos pagan impuesto.

# declaración e inicialización de variables y constantes
precioFinalProducto = 0.0
tasaImpuesto = 0.13
nombreProducto = ""
precioProducto = 0.0
# entrada de datos
nombreProducto = input('Ingrese el nombre del producto: ')
precioProducto = float(input('Ingrese el precio del producto: '))
# proceso
precioFinalProducto = precioProducto + (precioProducto * tasaImpuesto)
# salida
print(f'El nombre del producto es: {nombreProducto} y su precio es: {precioFinalProducto}')
