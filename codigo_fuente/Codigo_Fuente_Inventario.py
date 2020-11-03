from datetime import date, datetime, timedelta

#función para guardar el primer nombre de producto ingresado y crear la lista de productos
def guardar_nombre_primera_vez(nombre_producto):

    global lista_productos
    lista_productos = []
    lista_productos.append(nombre_producto)
    return lista_productos

#función para guardar el nombre del producto y agregarlo a la lista
def guardar_nombre (nombre_producto,lista_productos):


    lista_productos.append(nombre_producto)
    return lista_productos

#función para guardar el primer nombre de precio ingresado y crear la lista de precios
def guardar_precio_primera_vez(precio_producto):

    global lista_precios
    lista_precios = []
    lista_precios.append(precio_producto)
    return lista_precios

#función para guardar el precio del producto y agregarlo a la lista
def guardar_precio (precio_producto,lista_precios):

    lista_precios.append(precio_producto)
    return lista_precios


#función para saber si el producto ingresando esta pronto a vencerse
def guardar_fecha_vencimiento (fecha_vencimiento_producto, nombre_producto):
    dia_vencimento_con_formato = datetime.strptime(fecha_vencimiento_producto, '%d/%m/%Y')
    dia_actual = datetime.today()
    dia_vencimiento_referecia = dia_actual + timedelta(days=5)
    if dia_vencimento_con_formato <= dia_vencimiento_referecia :
        print("El producto "+nombre_producto+" va a vencer pronto (En 5 dias o menos)")

#función para saber cuantas unidades hay en el inventario e inicia la lista
def guardar_numero_unidades_primera_vez (numero_unidades_producto):
    global lista_unidades
    lista_unidades = []
    lista_unidades.append(numero_unidades_producto)
    return lista_unidades

#funcion para añadir unidades a la lista
def guardar_numero_unidades (numero_unidades_producto,lista_unidades):
    lista_unidades.append(numero_unidades_producto)
    return lista_unidades

#función para saber las ganancias que se van a tener al vender todo el inventario
def ganacias (lista_precios,listas_unidades,numero_productos_inventario):
    ganacias_totales = 0
    for g in range (len(lista_precios)):
        for k in range (len(listas_unidades)):
            if g == k:
                valor = int(lista_precios[g])
                multiplicar = int(listas_unidades[k])
                ganancias = multiplicar*valor
                ganacias_totales = ganacias_totales + ganancias
    print("Si se venden todos los productos que hay en el inventario las ganacias serian de",ganacias_totales)

#función para saber cuantas unidades hay en el inventario
def numero_productos_inventario(lista_unidades,numero_productos_ingresar):
    cant_productos_inventario = 0
    for h in lista_unidades:
        numero = int(h)
        cant_productos_inventario = cant_productos_inventario + numero
    print("Hay ",cant_productos_inventario,"unidades en todo el inventario")

#función para imprimir inventario
def imprimir_inventario(lista_productos, lista_precio, lista_unidades,numero_productos_ingresar):
    for a in range(numero_productos_ingresar):
        print('Producto:\t{}\nPrecio:\t\t{}\nNum.Unid:\t{}\n'.format(lista_productos[a], lista_precio[a], lista_unidades[a]))



#función para restar articulos vendidos
def articulos_vendidos (lista_productos,lista_precios,lista_unidades,numero_productos_ingresar):
    numero_productos_vendidos = int(input()) #Ingrese el numero de productos vendidos  (Distintos) Ej: 2
    for nu in range (numero_productos_vendidos):
        nombre_producto_ven = str(input()) #Ingrese el nombre del producto vendido Ej: Cafe
        numero_unidades_producto_ven = int(input()) #Ingrese el numero de unidades  vendidas del producto Ej: 4

        contador = 0
        for probar in lista_productos:
            if nombre_producto_ven == probar:
                probar_unidades = lista_unidades[contador]
                probar_unidades = probar_unidades - numero_unidades_producto_ven
                lista_unidades[contador] = probar_unidades
            contador = contador + 1


    print("El inventario actualizado es:")
    for a in range(numero_productos_ingresar):
        print('Producto:\t{}\nNum.Unid:\t{}\n'.format(lista_productos[a], lista_unidades[a]))


#función para entrar los datos
def main():
    global numero_productos_ingresar
    numero_productos_ingresar = int(input()) #Ingrese el numero de productos (Distintos) Ej: 4

    for n in range(numero_productos_ingresar):
        if n == 0:
            nombre_producto = str(input()) #Ingrese el nombre del producto Ej: Sal
            precio_producto = str(input()) #Ingrese el precio del producto Ej: 5000
            fecha_vencimiento_producto = str(input()) #Ingrese la fecha de vencimiento del producto Ej: 11/11/2020 (Usar formato dia/mes/año)
            numero_unidades_producto = int(input())#Ingrese el numero de unidades del producto Ej: 5
            guardar_nombre_primera_vez(nombre_producto)
            guardar_precio_primera_vez(precio_producto)
            guardar_fecha_vencimiento(fecha_vencimiento_producto,nombre_producto)
            guardar_numero_unidades_primera_vez(numero_unidades_producto)
        else:
            nombre_producto = str(input())#Ingrese el nombre del producto Ej: Sal
            precio_producto = str(input())#Ingrese el precio del producto Ej: 5000
            fecha_vencimiento_producto = str(input())#Ingrese la fecha de vencimiento del producto Ej: 11/11/2020 (Usar formato dia/mes/año)
            numero_unidades_producto = int(input())#Ingrese el numero de unidades del producto Ej: 5
            guardar_nombre(nombre_producto,lista_productos)
            guardar_precio(precio_producto, lista_precios)
            guardar_fecha_vencimiento(fecha_vencimiento_producto, nombre_producto)
            guardar_numero_unidades(numero_unidades_producto, lista_unidades)

    numero_productos_inventario(lista_unidades,numero_productos_ingresar)
    ganacias(lista_precios,lista_unidades, numero_productos_ingresar)
    print("El inventario actual de la tienda:")
    imprimir_inventario(lista_productos, lista_precios, lista_unidades,numero_productos_ingresar)

    print("Quiere ingresar los articulos vendidos?")
    articulos_vendidos_pregunta = str(input()) # Responder con Si o No la pregunta
    if articulos_vendidos_pregunta == 'Si':
        articulos_vendidos (lista_productos, lista_precios, lista_unidades, numero_productos_ingresar)
    else:
        print("Fin del programa")



main()
