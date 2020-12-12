from tkinter import scrolledtext
from urllib.request import urlopen
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import *
from PIL import ImageTk,Image
from datetime import date, datetime, timedelta

'''Se hace el webscrapper de una pagina de protocolos de salud para tiendas de 
comestibles en epoca de Covid19 y se guarda en una lista de una longitud de 45 
caracteres utilizando el codigo de formato del taller 6'''
url = "https://blog.qupos.com/recomendaciones-para-minisuper-supermercados-covid-19"
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")
indice_final = 0
Recomendaciones_para_supermercados_Covid19 = []
contador = 1
for i in range(13):
    lineamientos = html.find('<p><span style="color: #000000;">')
    indice_inicial = lineamientos + len('<p><span style="color: #000000;">')
    indice_final = html.find("</span></p>")

    title = html[indice_inicial:indice_final]

    if i != 4:
        añadir = (str(contador) + "." + title)
        Recomendaciones_para_supermercados_Covid19.append(añadir)
        contador = contador + 1

    nueva_html = len(html[:indice_final + 11])
    html = html[nueva_html:]
contador = 1
covid = ''
for texto in Recomendaciones_para_supermercados_Covid19:
    lista = texto.split(' ')
    numero_caracteres = 45
    a = 0
    linea = ''
    for b in lista:
        calcular_len = len(b)
        a = a + calcular_len
        if a <= numero_caracteres:
            if a == numero_caracteres:
                linea = linea + b
            else:
                linea = linea + b + ' '
                a = a + 1
        else:
            lon_espacio = len(linea)
            if lon_espacio == numero_caracteres:
                covid = covid + '\n' + linea
                a = 0
                linea = ''
                linea = linea + b + ' '
                calcular_len = len(b)
                a = a + calcular_len + 1
            else:
                mult = numero_caracteres - lon_espacio
                linea = linea + (' ' * mult)
                covid = covid + '\n' + linea
                a = 0
                linea = ''
                linea = linea + b + ' '
                calcular_len = len(b)
                a = a + calcular_len + 1
    contador = contador + 1

    lon_espacio = len(linea)
    if lon_espacio == numero_caracteres:
        covid = covid + '\n' + linea
        a = 0
        linea = ''
        linea = linea + b + ' '
        calcular_len = len(b)
        a = a + calcular_len + 1
    else:
        mult = numero_caracteres - lon_espacio
        linea = linea + (' ' * mult)
        covid = covid + '\n' + linea
        a = 0
        linea = ''
        linea = linea + b + ' '
        calcular_len = len(b)
        a = a + calcular_len + 1

'''Se define el menu general que tiene botones para agregar inventario, ver inventario,
 quitar inventario, ver ganancias y ver protocolos de Covid 19'''
def menu_general():
    menu_general = Tk()

    menu_general.title("Menu")
    menu_general.geometry("400x400")
    menu_general.configure(bg="papaya whip")
    menu_general.iconbitmap('C:/Unal.ico')

    label = Label(menu_general, text="Menu", font=("Arial Bold", 20), bg='papaya whip')
    label.grid(row=0, column=1)

    agregar_inventario = Button(menu_general, text="Agregar productos", command=agregar_productos_inventario, bg='misty rose')
    agregar_inventario.grid(row=3, column=1)

    espacio = Label(menu_general, text='                        ', bg="papaya whip")
    espacio.grid(row=2, column=0)

    verinventario = Button(menu_general, text="Ver inventario", command=ver_inventario,bg='misty rose')
    verinventario.grid(row=5, column=1)
    espacio = Label(menu_general, text='                        ', bg="papaya whip")
    espacio.grid(row=4, column=0)

    quitar_inventario = Button(menu_general, text="Quitar productos", command=eliminar_inventario,bg='misty rose')
    quitar_inventario.grid(row=7, column=1)
    espacio = Label(menu_general, text='                        ', bg="papaya whip")
    espacio.grid(row=6, column=0)

    ver_ganancia = Button(menu_general, text="Ver ganancias", command=ver_ganancias,bg='misty rose')
    ver_ganancia.grid(row=10, column=1)
    espacio = Label(menu_general, text='                        ', bg="papaya whip")
    espacio.grid(row=9, column=0)

    covid = Button(menu_general, text="Covid19", command=recomendaciones,bg='misty rose')
    covid.grid(row=14, column=1)
    espacio = Label(menu_general, text='         ', bg="papaya whip")
    espacio.grid(row=13, column=3)

    salir = Button(menu_general, text="Salir", command=menu_general.quit, anchor=E,bg='misty rose')
    salir.grid(row=16, column=3, sticky=W + E, rowspan=1, columnspan=1)
    espacio = Label(menu_general, text='                        ', bg="papaya whip")
    espacio.grid(row=15, column=0)

    menu_general.mainloop()

'''La funcion recomendaciones tiene los protocolos de seguridad para el Covid19, utiliza scrollbar para ver todas las recomendaciones'''
def recomendaciones():
    recomen_covid19 = Tk()
    recomen_covid19.title("Recomendaciones Covid 19")
    recomen_covid19.geometry("400x400")
    recomen_covid19.configure(bg="lemon chiffon")

    espacio = Label(recomen_covid19, text='           ', bg="lemon chiffon")
    espacio.grid(row=0, column=0)

    recomendac = tk.Label(recomen_covid19, text="Recomendaciones para supermercados" + '\n' + "en contexto de COVID-19",font=("Arial Bold", 12), bg='lemon chiffon')
    recomendac.grid(row=0, column=0)

    boton_menu = Button(recomen_covid19, text="Menu principal", command=menu_general,bg='khaki')
    boton_menu.grid(row=4, column=0)

    barra = scrolledtext.ScrolledText(recomen_covid19,width=45,height=20,bg="lemon chiffon")
    barra.grid(row=2,column=0)

    barra.insert(INSERT,covid)

'''La funcion agregar productos inventario tiene 
las entradas para el nombre del producto, el precio, la fecha de vencimiento y 
cantidad de unidades, todo esto con labels para indicar que se debe ingresar'''
def agregar_productos_inventario():
    agregar_inventario = Tk()
    agregar_inventario.title("Agregar Inventario")
    agregar_inventario.geometry("400x400")
    agregar_inventario.configure(bg="thistle3")

    espacio = Label(agregar_inventario, text='                        ', bg="thistle3")
    espacio.grid(row=2, column=0)

    agregar_inventario_label = tk.Label(agregar_inventario, text="Agregar inventario", font=("Arial Bold", 20),bg='thistle3')
    agregar_inventario_label.grid(row=0, column=1)

    agregar_nombre_label = tk.Label(agregar_inventario, text="Nombre del producto:", font=("Arial Bold", 10),bg='thistle3')
    agregar_nombre_label.grid(row=1, column=1)

    agregar_nombre_entry = tk.Entry(agregar_inventario, width=30)
    agregar_nombre_entry.grid(column=1, row=2)

    agregar_precio_label = tk.Label(agregar_inventario, text="Precio del producto:", font=("Arial Bold", 10),bg='thistle3')
    agregar_precio_label.grid(row=3, column=1)

    agregar_precio_entry = tk.Entry(agregar_inventario, width=30)
    agregar_precio_entry.grid(column=1, row=4)

    agregar_vencimiento_label = tk.Label(agregar_inventario, text="Fecha de vencimiento del producto:",font=("Arial Bold", 10), bg='thistle3')
    agregar_vencimiento_label.grid(row=5, column=1)

    agregar_vencimiento_entry = tk.Entry(agregar_inventario, width=30)
    agregar_vencimiento_entry.grid(column=1, row=6)

    agregar_cantidad_label = tk.Label(agregar_inventario, text="Cantidad de unidades del producto:",font=("Arial Bold", 10), bg='thistle3')
    agregar_cantidad_label.grid(row=7, column=1)

    agregar_cantidad_entry = tk.Entry(agregar_inventario, width=30)
    agregar_cantidad_entry.grid(column=1, row=8)

    boton_guardar = Button(agregar_inventario, text="Guardar",command=lambda: llamar_datos(agregar_nombre_entry.get(), agregar_precio_entry.get(),agregar_vencimiento_entry.get(), agregar_cantidad_entry.get()),bg='plum2')
    boton_guardar.grid(row=9, column=1)

    boton_nuevo_producto = Button(agregar_inventario, text="Agregar nuevo producto",command=agregar_productos_inventario,bg='plum2')
    boton_nuevo_producto.grid(row=10, column=1)

    boton_menu = Button(agregar_inventario, text="Menu principal", command=menu_general,bg='plum2')
    boton_menu.grid(row=11, column=1)

'''La funcion llamar datos toma las entradas ingresadas en la funcion anterior y las guarda en la 
base de datos del inventario, en esta funcion tambien se validan los datos ingresados a traves de 
messageboxes en caso de error por parte del usuario'''
def llamar_datos(nombre, precio, fecha, cantidad):
    archivo = open('Base de datos productos.txt', 'r')
    matriz_inventario = []
    contador = 0
    for linea in archivo.readlines():
        linea = linea.split(',')
        matriz_inventario.append(linea)
    archivo.close()

    lista_nombres = []
    for linea in matriz_inventario:
        lista_nombres.append(linea[0])

    if nombre not in lista_nombres:
        contenido = nombre.rstrip() + ","
        contador = contador + 1
    if nombre in lista_nombres:
        messagebox.showinfo('Error', 'El producto ingresado ya existe en el inventario')
    if type(precio) == str:
        try:
            precio_validado = int(precio)
            contenido = contenido + precio.rstrip() + ","
            contador = contador + 1
        except ValueError:
            messagebox.showinfo('Error', 'El precio debe ser un numero entero')
    if fecha[2] == '/' and fecha[5] == '/' and int(fecha[:2]) < 32 and int(fecha[3:5]) < 13 and int(fecha[6:10]) > 2019:
        dia_vencimento_con_formato = datetime.strptime(fecha, '%d/%m/%Y')
        dia_actual = datetime.today()
        dia_vencimiento_referecia = dia_actual + timedelta(days=5)
        imprimir = 0
        if dia_vencimento_con_formato <= dia_vencimiento_referecia:
            imprimir = 1
        contenido = contenido + fecha.rstrip() + ","
        contador = contador + 1
    else:
        messagebox.showinfo('Error', 'La fecha ingresada no cumple con del formato dd/mm/aa')
    if type(cantidad) == str:
        try:
            cantidad_validado = int(cantidad)
            contenido = contenido + cantidad.rstrip() + "\n"
            contador = contador + 1
        except ValueError:
            messagebox.showinfo('Error', 'La cantidad de unidades debe ser un numero entero')

    if contador == 4:
        archivo = open('Base de datos productos.txt', 'a')
        archivo.write(contenido)
        archivo.close()
        if imprimir == 1:
            messagebox.showinfo('Atención',"El producto ingresado va a vencer pronto (En 5 dias o menos)")
        messagebox.showinfo('Guardado', 'El producto ha sido agregado al inventario')

'''La funcion de ver inventario toma todos los datos guardados en la base de datos del inventario 
y los muestra organizadamente en una tabla'''
def ver_inventario():
    class Table:

        def __init__(self, root):

            for i in range(total_rows):
                for j in range(total_columns):
                    if j == 1:
                        self.e = Entry(root, width=12, fg='black', bg='azure',
                                       font=('Arial', 10, 'bold'))
                        self.e.grid(row=i + 1, column=j)
                        self.e.insert(END, lst[i][j])
                    elif j == 2:
                        self.e = Entry(root, width=12, fg='black', bg='azure',
                                       font=('Arial', 10, 'bold'))
                        self.e.grid(row=i + 1, column=j)
                        self.e.insert(END, lst[i][j])
                    elif j == 3:
                        self.e = Entry(root, width=10, fg='black', bg='azure',
                                       font=('Arial', 10, 'bold'))
                        self.e.grid(row=i + 1, column=j)
                        self.e.insert(END, lst[i][j])
                    else:
                        self.e = Entry(root, width=15, fg='black', bg='azure',
                                       font=('Arial', 10, 'bold'))

                        self.e.grid(row=i + 1, column=j)
                        self.e.insert(END, lst[i][j])
    archivo = open('Base de datos productos.txt', 'r')
    matriz_inventario = []
    for linea in archivo.readlines():
        linea = linea.split(',')
        matriz_inventario.append(linea)
    archivo.close()
    lst = matriz_inventario
    total_rows = len(matriz_inventario)
    total_columns = len(matriz_inventario[1])

    root = Tk()
    t = Table(root)
    root.title("Inventario")
    root.geometry("400x400")
    root.configure(bg="azure")
    root.iconbitmap('C:/Unal.ico')

    label = Label(root, text="Ver" + "\n" + "Inventario", font=("Arial Bold", 15), bg='azure')
    label.grid(row=0, column=0)

    espacio = Label(root, text='      ', bg="azure")
    espacio.grid(row=50, column=2)

    boton_menu = Button(root, text="Menu principal", command=menu_general)
    boton_menu.grid(row=51, column=2)

    root.mainloop()

'''La funcion de eliminar inventario tiene los las opciones de eliminar unidades y eliminar producto'''
def eliminar_inventario():
    quitar_inventario = Tk()
    quitar_inventario.title("Quitar productos del inventario")
    quitar_inventario.geometry("400x400")
    quitar_inventario.configure(bg="DarkSeaGreen1")

    quitar_inventario_label = tk.Label(quitar_inventario, text=" Menú quitar inventario", font=("Arial Bold", 18),bg='DarkSeaGreen1')
    quitar_inventario_label.grid(row=0, column=1)

    espacio = Label(quitar_inventario, text=' ', bg="DarkSeaGreen1")
    espacio.grid(row=2, column=0)

    boton_eliminar_unidades = Button(quitar_inventario, text='Eliminar Unidades', bg='DarkSeaGreen3',command=quitar_producto_unidades)
    boton_eliminar_unidades.grid(row=4, column=1)

    espacio = Label(quitar_inventario, text='                        ', bg="DarkSeaGreen1")
    espacio.grid(row=5, column=1)

    boton_eliminar_producto = Button(quitar_inventario, text='Eliminar Producto', bg='DarkSeaGreen3',command=eliminar_producto)
    boton_eliminar_producto.grid(row=6, column=1)

    espacio = Label(quitar_inventario, text='                        ', bg="DarkSeaGreen1")
    espacio.grid(row=9, column=0)

    espacio = Label(quitar_inventario, text='                        ', bg="DarkSeaGreen1")
    espacio.grid(row=10, column=0)

    boton_menu = Button(quitar_inventario, text="Menu principal", command=menu_general, bg='DarkSeaGreen3')
    boton_menu.grid(row=11, column=1)

'''La funcion de eliminar producto tiene la entrada para que el usuario ingrese el nombre del producto y asi poder eliminarlo'''
def eliminar_producto():
    quitar_productos = Tk()
    quitar_productos.title("Quitar productos del inventario")
    quitar_productos.geometry("400x400")
    quitar_productos.configure(bg="PaleGreen1")

    titulo_quitar_inventario_label = tk.Label(quitar_productos, text="Quitar del inventario",font=("Arial Bold", 18), bg='PaleGreen1')
    titulo_quitar_inventario_label.grid(row=0, column=1)

    nombre_producto_label = tk.Label(quitar_productos, text="Nombre del producto:", font=("Arial Bold", 10),bg='PaleGreen1')
    nombre_producto_label.grid(row=1, column=1)

    espacio = Label(quitar_productos, text='                        ', bg="PaleGreen1")
    espacio.grid(row=2, column=0)

    nombre_producto_entry = tk.Entry(quitar_productos, width=30)
    nombre_producto_entry.grid(column=1, row=3)

    espacio = Label(quitar_productos, text='                        ', bg="PaleGreen1")
    espacio.grid(row=4, column=0)

    boton_guardar = Button(quitar_productos, text="Guardar cambios",command=lambda: eliminar_producto_archivo(nombre_producto_entry.get()),bg='PaleGreen3')
    boton_guardar.grid(row=5, column=1)

    boton_menu_eliminar = Button(quitar_productos, text="Menu quitar inventario", command=eliminar_inventario,bg='PaleGreen3')
    boton_menu_eliminar.grid(row=6, column=1)

    boton_menu_principal = Button(quitar_productos, text="Menu principal", command=menu_general, bg='PaleGreen3')
    boton_menu_principal.grid(row=7, column=1)

'''La funcion eliminar producto de archivo toma el nombre ingresado en la funcion anterior 
y lo elimina de la base de datos, tiene validacion en caso de que el nombre no este en el inventario'''
def eliminar_producto_archivo(nombre):
    archivo = open('Base de datos productos.txt' , 'r')
    matriz_inventario = []
    for linea in archivo.readlines():
        linea = linea.split(',')
        matriz_inventario.append(linea)
    archivo.close()

    lista_nombres = []
    for linea in matriz_inventario:
        lista_nombres.append(linea[0])

    if nombre in lista_nombres:
        for linea in range(len(matriz_inventario)):
            if matriz_inventario[linea][0] == nombre:
                matriz_inventario.remove(matriz_inventario[linea])
                archivo = open('Base de datos productos.txt', 'w')
                for linea in matriz_inventario:
                    archivo.write(','.join(linea))
                archivo.close()
                messagebox.showinfo('Guardado', 'Guardado con éxito')
                break
    else:
        messagebox.showinfo('Error', 'El producto ingresado no esta en el inventario')

'''La funcion de quitar unidades de producto tiene las entradas para ingresar el nombre del producto y la cantidad de unidades a eliminar'''
def quitar_producto_unidades():
    quitar_unidades_inventario = Tk()
    quitar_unidades_inventario.title("Quitar unidades del inventario")
    quitar_unidades_inventario.geometry("400x400")
    quitar_unidades_inventario.configure(bg="SeaGreen1")

    titulo_quitar_inventario_label = tk.Label(quitar_unidades_inventario, text="Quitar del inventario",font=("Arial Bold", 18), bg='SeaGreen1')
    titulo_quitar_inventario_label.grid(row=0, column=1)

    nombre_producto_label = tk.Label(quitar_unidades_inventario, text="Nombre del producto:", font=("Arial Bold", 10),bg='SeaGreen1')
    nombre_producto_label.grid(row=1, column=1)

    espacio = Label(quitar_unidades_inventario, text='                        ', bg="SeaGreen1")
    espacio.grid(row=2, column=0)

    nombre_producto_entry = tk.Entry(quitar_unidades_inventario, width=30)
    nombre_producto_entry.grid(column=1, row=2)

    espacio = Label(quitar_unidades_inventario, text='                        ', bg="SeaGreen1")
    espacio.grid(row=3, column=0)

    cantidad_eliminar_label = tk.Label(quitar_unidades_inventario, text="Cantidad de unidades a eliminar:",font=("Arial Bold", 10), bg='SeaGreen1')
    cantidad_eliminar_label.grid(row=4, column=1)

    eliminar_cantidad_entry = tk.Entry(quitar_unidades_inventario, width=30)
    eliminar_cantidad_entry.grid(column=1, row=5)

    espacio = Label(quitar_unidades_inventario, text='                        ', bg="SeaGreen1")
    espacio.grid(row=6, column=0)

    boton_guardar = Button(quitar_unidades_inventario, text="Guardar cambios",command=lambda: eliminar_unidades_producto(nombre_producto_entry.get(),eliminar_cantidad_entry.get()),bg='SeaGreen3')
    boton_guardar.grid(row=7, column=1)

    boton_menu_eliminar = Button(quitar_unidades_inventario, text="Menu quitar inventario", command=eliminar_inventario,bg='SeaGreen3')
    boton_menu_eliminar.grid(row=8, column=1)

    boton_menu_principal = Button(quitar_unidades_inventario, text="Menu principal", command=menu_general,bg='SeaGreen3')
    boton_menu_principal.grid(row=9, column=1)

'''La funcion eliminar unidades del producto toma las entradas del el nombre y la cantidad de unidades a eliminar obtenidas en la funcion anterior,
 estos datos se ponen en una lista y se eliminan de la base de datos, tiene validación de datos en caso de que el 
 nombre del producto no este en el inventario o la cantidad de unidades a eliminar sea mayor a la existente en el inventario'''
def eliminar_unidades_producto(nombre, unidades):
    archivo = open('Base de datos productos.txt', 'r')
    matriz_inventario = []
    for linea in archivo.readlines():
        linea = linea.split(',')
        matriz_inventario.append(linea)
    archivo.close()

    lista_nombres = []
    lista_unidades = []
    lista_precios = []
    for linea in matriz_inventario:
        lista_nombres.append(linea[0])
        lista_unidades.append(linea[-1])
        lista_precios.append(linea[1])

    if nombre in lista_nombres:
        try:
            unidades = int(unidades)
            for linea in range(len(matriz_inventario)):
                if nombre == lista_nombres[linea]:
                    if unidades < int(lista_unidades[linea]):
                        matriz_inventario[linea][-1] = str(int(matriz_inventario[linea][-1]) - unidades) + '\n'
                        archivo = open('Base de datos productos.txt', 'w')
                        for line in matriz_inventario:
                            archivo.write(','.join(line))
                        archivo.close()
                        matriz_ventas = []
                        ventas = open('Productos_vendidos.txt', "r")
                        for linea1 in ventas.readlines():
                            linea1 = linea1.split(',')
                            matriz_ventas.append(linea1)
                        ventas.close()
                        lista_nombres_ventas = []
                        lista_ganacias_ventas = []
                        for a in matriz_ventas:
                            lista_nombres_ventas.append(a[0])
                            lista_ganacias_ventas.append(a[1])
                        if nombre in lista_nombres_ventas:
                            for indice in range(len(matriz_ventas)):
                                if nombre == lista_nombres_ventas[indice]:
                                    añadir = int(lista_precios[linea]) * int(unidades)
                                    suma = añadir + int(lista_ganacias_ventas[indice])
                                    matriz_ventas[indice][1] = str(suma)+'\n'
                                    ventas = open('Productos_vendidos.txt', 'w')
                                    for new_line in matriz_ventas:
                                        ventas.write(','.join(new_line))
                                    ventas.close()
                        else:
                            ventas = open('Productos_vendidos.txt', 'a')
                            ventas.writelines(nombre + "," + str(int(lista_precios[linea])*int(unidades)) + "\n")
                            ventas.close()
                            archivo.close()
                        messagebox.showinfo('Guardado', 'Guardado con éxito')
                    else:
                        messagebox.showinfo('Error', 'Ingrese numero de unidades menor al existente')
        except ValueError:
            messagebox.showinfo('Error', 'Cantidad debe ser numero entero')
    else:
        messagebox.showinfo('Error', 'El producto ingresado no esta en el inventario')

'''La funcion de ver ganancias mustra una grafica de las ganancias obtenidas por los productos vendidos'''
def ver_ganancias():
    ventas = open('Productos_vendidos.txt', "r")
    matriz_ganancias = []
    producto_x = []
    ganancias_y = []
    for linea in ventas.readlines():
        linea =linea.split(',')
        matriz_ganancias.append(linea)
    for i in matriz_ganancias:
        producto_x.append(i[0])
        numero_sin_0 = (int(i[1]) / 10000)
        ganancias_y.append(numero_sin_0)
    plt.plot(producto_x, ganancias_y)
    plt.title('Ganancias obtenidas por producto')
    plt.ylabel('Ganancias obtenidas/10000')
    plt.xlabel('Productos vendidos')

    plt.legend()
    plt.grid()
    plt.show()

'''La funcion de login tiene el logo del inventario y las entradas para el usuario y la contraseña'''
def login():
    ventana = tk.Tk()
    ventana.title("Login")
    ventana.geometry('400x400')
    ventana.configure(background='pale turquoise')

    espacio = tk.Label(ventana, text='         ', bg="pale turquoise")
    espacio.grid(row=0, column=0)

    logo = ImageTk.PhotoImage(Image.open(r'C:\logo_recortado2.png').resize((130, 120)))
    label = Label(image=logo, bg='pale turquoise')
    label.grid(row=2, column=1)

    espacio = tk.Label(ventana, text='         ', bg="pale turquoise")
    espacio.grid(row=3, column=0)
    label = tk.Label(ventana, text='Login', font=('Arial bold', 25), bg='pale turquoise')
    label.grid(row=3,column=1)

    espacio = tk.Label(ventana, text='             ', bg="pale turquoise")
    espacio.grid(row=1, column=0)

    label1 = tk.Label(ventana, text='Usuario',font=('Arial bold', 18),  bg='pale turquoise')
    label1.grid(row=7,column=0)
    usuario_entry = tk.Entry(ventana, width=30)
    usuario_entry.grid(column = 1, row=7)

    label2 = tk.Label(ventana, text='Contraseña',font=('Arial bold', 18), bg='pale turquoise')
    label2.grid(row=9,column=0)
    contraseña_entry = tk.Entry(ventana, width=30)
    contraseña_entry.grid(column = 1, row=9)

    espacio = tk.Label(ventana, text='             ', bg="pale turquoise")
    espacio.grid(row=15, column=0)
    espacio = tk.Label(ventana, text='             ', bg="pale turquoise")
    espacio.grid(row=11, column=0)
    espacio = tk.Label(ventana, text='             ', bg="pale turquoise")
    espacio.grid(row=12, column=0)
    nuevo_usuario = Button(ventana, text="Registrar nuevo usuario", command=lambda:res_nuevo_usurario(ventana),bg = 'medium turquoise')
    nuevo_usuario.grid(row=13, column=1)

    ingresar = Button(ventana, text="Ingresar", command=lambda: comprobar_usu_con(usuario_entry.get(),contraseña_entry.get()), bg='medium turquoise')
    ingresar.grid(row=10, column=1)

    ventana.mainloop()

'''La funcion de comprobar usuario toma las entradas de la funcion anterior y las valida en caso de que el usuario no coincida con la contraseña'''
def comprobar_usu_con(usu,contr):
    archivo = open('Base de datos usurios.txt', 'r')
    datos = []

    for linea in archivo.readlines():
        datos.append(linea)

    datos_nuevos = []
    for a in datos:
        a = a[:-1]
        datos_nuevos.append(a.split(':'))


    diccionario = {}
    for b in datos_nuevos:
        diccionario[b[0]] = b[1]

    for llave in diccionario.keys():
        diccionario[llave] = diccionario[llave].split(",")

    datos_login = {}
    for llave in diccionario.keys():
        datos_login[llave] = diccionario[llave][1]


    archivo.close()

    if usu in datos_login.keys():
        if datos_login[usu] == contr:
            menu_general()
        else:
            messagebox.showinfo('Error', 'Contraseña Incorrecta')
    else:
        messagebox.showinfo('Error', 'Usuario inexistente')

'''La funcion de registro nuevo usuario tiene las entradas para el nombre, el usuario, la 
contraseña (y la confirmacion de contraseña) y si es dueño o empleado'''
def res_nuevo_usurario(n_usuario):

    ventana1 = Toplevel(n_usuario)
    ventana1.title("Registrar Nuevo Usuario")
    ventana1.geometry('400x400')
    ventana1.configure(background='SteelBlue2')
    espacio = tk.Label(ventana1, text='      ', bg="SteelBlue2")
    espacio.grid(row=0, column=0)
    label = tk.Label(ventana1, text='Registrar\nNuevo\nUsuario', font=('Arial bold', 18), bg='SteelBlue2')
    label.grid(row=0, column=1, columnspan=1)

    label1 = tk.Label(ventana1, text='Nombre', font=('Arial bold', 15), bg='SteelBlue2')
    label1.grid(row=3, column=0)
    nombre_entry = tk.Entry(ventana1, width=30)
    nombre_entry.grid(column=1, row=3)
    espacio = tk.Label(ventana1, text='            ', bg="SteelBlue2")
    espacio.grid(row=1, column=1,columnspan=2)

    label1 = tk.Label(ventana1, text='Usuario', font=('Arial bold', 15), bg='SteelBlue2')
    label1.grid(row=4, column=0)
    usuario_entry = tk.Entry(ventana1, width=30)
    usuario_entry.grid(row=4,column=1)

    label1 = tk.Label(ventana1, text='Contraseña', font=('Arial bold', 15), bg='SteelBlue2')
    label1.grid(row=5, column=0)
    nueva_contraseña_entry = tk.Entry(ventana1, width=30)
    nueva_contraseña_entry.grid(row=5, column=1)

    label1 = tk.Label(ventana1, text=' Confirmar Contraseña', font=('Arial bold', 12), bg='SteelBlue2')
    label1.grid(row=6, column=0)
    contraseña_comfir_entry = tk.Entry(ventana1, width=30)
    contraseña_comfir_entry.grid(row=6, column=1)

    selected = tk.IntVar()

    opcion_1 = Radiobutton(ventana1, text='Dueño', value=1, variable=selected, bg='SteelBlue2')
    opcion_1.grid(column=1, row=7)
    opcion_2 = Radiobutton(ventana1, text='Empleado', value=2, variable=selected, bg='SteelBlue2')
    opcion_2.grid(column=1, row=8)

    nuevo_usuario = Button(ventana1, text="Guardar nuevo usuario", command=lambda:guardar_nuevo_usuario(nombre_entry.get(), usuario_entry.get(), nueva_contraseña_entry.get(), contraseña_comfir_entry.get(), selected.get()), bg='SteelBlue3')

    nuevo_usuario.grid(row=9, column=1)

    '''La funcion guardar nuevo usuario toma las entradas de la funcion anterior y las valida en caso de que 
    el nombre tenga un numero, el usuario tenga espacios o ya exista en la base de datos, la contraseña y la 
    confirmacion de contraseña no coincidan; despues de comprobar todos los datos los guarda en la base de datos de login'''
    def guardar_nuevo_usuario(nombre, nuevo_usuario, nuevo_contraseña, confirm_nueva_contraseña, cargo):
        archivo = open('Base de datos usurios.txt', 'r')

        datos = []

        for linea in archivo.readlines():
            datos.append(linea)

        datos_nuevos = []
        for a in datos[:-1]:
            a = a[:-1]
            datos_nuevos.append(a.split(':'))

        base_registar_usuario = {}
        for b in datos_nuevos:
            base_registar_usuario[b[0]] = b[1]

        archivo.close()
        contador = 0
        if '1' in nombre or '2' in nombre or '3' in nombre or '4' in nombre or '5' in nombre or '6' in nombre or '7' in nombre or '8' in nombre or '9' in nombre or '0' in nombre:
            messagebox.showinfo('Error', 'Nombre Inválido')
            contador = 1
        if ' ' in nuevo_usuario:
            messagebox.showinfo('Error', 'Usuario no puede contener espacios')
            contador = 1
        if nuevo_contraseña != confirm_nueva_contraseña:
            messagebox.showinfo('Error', 'Confirmación de contraseña incorrecta')
            contador = 1
        if nuevo_usuario in base_registar_usuario.keys():
            messagebox.showinfo('Error', 'Usuario ingresado ya existe')
            contador = 1
        if contador == 0:
            archivo = open('Base de datos usurios.txt', 'a')
            salto_linea = '\n'
            archivo.write(salto_linea)
            guardar_usuario = ("{}:({},{},{})".format(nuevo_usuario, nombre, nuevo_contraseña, cargo))
            archivo.write(guardar_usuario)
            archivo.close()
            messagebox.showinfo('Guardado', 'Su usuario ha sido registrado con éxito')

def main():
    login()

main()