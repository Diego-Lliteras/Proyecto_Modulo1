from matplotlib import pyplot as plt

def principal_series(datos):
    salir = False
    while salir != True:
        estadoTXT = input('Lugar -> ').upper()
        if estadoTXT in regresa_estados(datos):
            fechas, contagios = regresa_meses_casos(datos, estadoTXT)
            grafica_linea(fechas, contagios, estadoTXT)
            salir = True
        else:
            print("Lugar inválido")

#Regresamos lista de estados
def regresa_estados(matriz):
    estados = []
    for i in range(1, len(matriz)):
        fila = matriz[i]
        estados.append(fila[2].replace('"', '').upper())
    return estados

def regresa_meses_casos(matriz, estado):
    datos_estado = []
    fechas = []
    for i in range(1, len(matriz)): #recorremos todos los estados en busca de la fila que corresponde al estado ingresado
        fila = matriz[i]
        #Si es el estado que buscamos iteramos esa fila
        if fila[2].replace('"', '').upper() == estado:
            for j in range(3, len(fila)): #recorremos la fila del estado
                split_fecha = matriz[0][j].replace('"', '').split("-")
                fecha_mes_ano = split_fecha[1] + "-" + split_fecha[2] #obtenemos la fecha en formato mes-año
                contagios_del_dia = int(matriz[i][j]) #obtenemos los contagios de ese día
                if fecha_mes_ano in fechas: #si la fecha en formato mes-año ya está en la lista debemos sumar los contagios de ese día
                    pos = fechas.index(fecha_mes_ano)
                    datos_estado[pos] = datos_estado[pos] + contagios_del_dia
                else: #si la fecha no está en la lista es la primera vez que tocamos este mes-año entonces lo insertamos al final de fechas junto con los contagios del día
                    fechas.append(fecha_mes_ano)
                    datos_estado.append(contagios_del_dia)
    return fechas, datos_estado

def grafica_linea(x, y, estado):
    fig, ax = plt.subplots(figsize=(15,10))
    ax.plot(x,y) # Gráfica de línea
    plt.xticks(x,rotation=90)
    plt.margins(0.1)
    plt.subplots_adjust(bottom=0.4)
    plt.grid(True)
    plt.title(f"Serie de tiempo {estado}")
    ax.set_xlabel("Contagios")
    ax.set_ylabel("Fechas")
    plt.show()