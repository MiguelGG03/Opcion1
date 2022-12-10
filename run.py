from Ejercicio51.ejs_51 import (main511,main512,main513,main514,main515,main516,main517)

def main():
    pr1=input('Que ejercicio desea ver?:\n'
    '1. Ejercicio 5.1\n'
    '2. Ejercicio 5.2\n'
    '>>> ')
    if pr1=='1':
        pr2=input('Que apartado desea ver?:\n'
        '1. Apartado 5.1.1\n'
        '2. Apartado 5.1.2\n'
        '3. Apartado 5.1.3\n'
        '4. Apartado 5.1.4\n'
        '5. Apartado 5.1.5\n'
        '6. Apartado 5.1.6\n'
        '7. Apartado 5.1.7\n'
        '>>> ')
        if pr2=='1':
            main511()
        elif pr2=='2':
            main512()
        elif pr2=='3':
            main513()
        elif pr2=='4':
            main514()
        elif pr2=='5':
            main515()
        elif pr2=='6':
            main516()
        elif pr2=='7':
            main517()
        else:
            print('No es una opcion valida')
            main()