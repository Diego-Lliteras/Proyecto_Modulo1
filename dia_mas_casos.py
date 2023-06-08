from matplotlib import pyplot as plt

def tabla_dias_mas_contagios(datos):
    resultado, estados, fechas= regresa_mayores(datos)
    datos_transformados = transforma_datos(estados, resultado, fechas)
    titulos = ['Estado', 'Fecha', 'Contagios']
    muestra_tabla(datos_transformados, titulos)
    estados = estados[:-1]
    resultado = resultado[:-1]
    lista_numerica = [int(elemento) for elemento in resultado]
    grafica_linea(estados, lista_numerica)

def regresa_mayores(matriz):
    res = []
    estados = []
    fechas = []
    for i in range(1, len(matriz)):
        fila = matriz[i]
        estados.append(fila[2].replace('"', ''))
        mayor = 0
        fecha = ''
        for j in range(3, len(fila)):
            if int(fila[j]) > int(mayor):
                mayor = fila[j]
                fecha = matriz[0][j]
        res.append(mayor)
        fechas.append(fecha)
    return res, estados, fechas

def transforma_datos(estados, contagios, fechas):
    datos = []
    for i in range(len(estados)):
        renglon = [str(estados[i]), fechas[i] ,contagios[i]]
        datos.append(renglon)
    return datos

def muestra_tabla(datos, column_labels):
    fig, ax = plt.subplots(figsize=(10,6))
    ax.table(cellText=datos, colLabels=column_labels, loc="center")
    ax.axis('tight')
    ax.axis('off')
    plt.show()

def grafica_linea(x, y):
    fig, ax = plt.subplots(figsize=(15,10))
    ax.plot(x,y) # Gráfica de línea
    plt.xticks(x,rotation=45)
    plt.margins(0.1)
    plt.subplots_adjust(bottom=0.4)
    plt.grid(True)
    plt.title("Día con más casos por estado")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    plt.show()
