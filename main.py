def imprimir_menu():
    print('*'*60)
    print(f'{"**":58}**')
    print(f'{"** 1.- Día con más casos a nivel nacional":58}**')
    print(f'{"** 2.- % Casos confirmados de acuerdo a la poblaciòn":58}**')
    print(f'{"** 3.- Series de tiempo":58}**')
    print(f'{"** 4.- Salir":58}**')
    print(f'{"**":58}**')
    print('*'*60, '\n\n')

def main():
    opt = 0
    while opt != 4:
        imprimir_menu()
        opt = int(input('Opción--> '))
        if opt == 1:
            print('Opción 1')
        elif opt == 2:
            print('Aqui va lo tuyo shaddi!')
        elif opt == 3:
            print('Opción 3')
        elif opt == 4:
            break
        else:
            print("Opción inválida")

if __name__ == '__main__':
    main()