from Ejercicio51.ejs_51 import (main511,main512,main513,main514,main515,main516,main517)
from Ejercicio52.ejs_52 import (main521,main522,main523,main524,main525,main526,main527,main528,main529,main5210)

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
    elif pr1=='2':
        pr2=input('Que apartado desea ver?:\n'
        '1. Apartado 5.2.1\n'
        '2. Apartado 5.2.2\n'
        '3. Apartado 5.2.3\n'
        '4. Apartado 5.2.4\n'
        '5. Apartado 5.2.5\n'
        '6. Apartado 5.2.6\n'
        '7. Apartado 5.2.7\n'
        '8. Apartado 5.2.8\n'
        '9. Apartado 5.2.9\n'
        '10. Apartado 5.2.10\n'
        '>>> ')
        if pr2=='1':
            main521()
        elif pr2=='2':
            main522()
        elif pr2=='3':
            main523()
        elif pr2=='4':
            main524()
        elif pr2=='5':
            main525()
        elif pr2=='6':
            main526()
        elif pr2=='7':
            main527()
        elif pr2=='8':
            main528()
        elif pr2=='9':
            main529()
        elif pr2=='10':
            main5210()
        else:
            print('No es una opcion valida')
            main()
    else:
        print('No es una opcion valida')
        main()

if __name__ == '__main__':
    main()