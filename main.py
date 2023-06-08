import os
import dia_mas_casos
import porcentajes_estado
import series_de_tiempo

def imprimir_menu():
    print('*'*60)
    print(f'{"**":58}**')
    print(f'{"** 1.- Día con más casos a nivel nacional":58}**')
    print(f'{"** 2.- % Casos confirmados de acuerdo a la poblaciòn":58}**')
    print(f'{"** 3.- Series de tiempo":58}**')
    print(f'{"** 4.- Salir":58}**')
    print(f'{"**":58}**')
    print('*'*60, '\n\n')

def extraer_datos():
    path = os.path.dirname(__file__)
    datos = []
    with open(path + '/Casos_Diarios_Estado_Nacional_Confirmados_20230531.csv', 'r') as f:
        linea = True
        while linea:
            linea = f.readline()
            if len(linea) > 0:  # Limpieza de datos.. 
                linea = linea[:-1]  # Se elimina el ultimo enter
                fila = linea.split(',')
                datos.append(fila)
    return datos

def main():
    opt = 0
    datos = extraer_datos()
    while opt != 4:
        imprimir_menu()
        opt = int(input('Opción--> '))
        if opt == 1:
            dia_mas_casos.tabla_dias_mas_contagios(datos)
        elif opt == 2:
            porcentajes_estado.principal_porcentajes(datos)
        elif opt == 3:
            series_de_tiempo.principal_series(datos)
        elif opt == 4:
            break
        else:
            print("Opción inválida")

if __name__ == '__main__':
    main()