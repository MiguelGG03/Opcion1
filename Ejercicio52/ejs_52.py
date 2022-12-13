import pandas as pd

def main521():
    tips = pd.read_csv('data_clear/tips.csv')
    print(tips.describe().T)

def main522():
    tips = pd.read_csv('data_clear/tips.csv')
    print(tips.isna().sum())
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _')
    print('Valores nulos en total_bill: ', tips['total_bill'].isna().sum())
    print('Valores nulos en tip: ', tips['tip'].isna().sum())
    print('Valores nulos en sex: ', tips['sex'].isna().sum())
    print('Valores nulos en smoker: ', tips['smoker'].isna().sum())
    print('Valores nulos en day: ', tips['day'].isna().sum())
    print('Valores nulos en time: ', tips['time'].isna().sum())
    print('Valores nulos en size: ', tips['size'].isna().sum())

def main523():
    tips = pd.read_csv('data_clear/tips.csv')
    print('Por lo que tengo entendido, estos datos han sido sacados')
    print('de un restaurante estadounidense, y por lo que tengo entendido,')
    print('en los restaurantes estadounidenses es obligatorio dejar de propina')
    print('como minimo un 15 % o y incluso del 20 % del total de la cuenta,')
    print('por lo que no es de extrañar que tanto hombres como mujeres hayan')
    print('dejado propina, y por lo tanto, que el porcentaje de hombres y mujeres')
    print('que han dejado propina sera el porcentaje de hombres y mujeres que hay')
    print('en la muestra (dataset).')
    print('Hombres: ', tips['sex'][tips.sex=='Male'].count())
    print('Mujeres: ',tips['sex'][tips.sex=='Female'].count())
    print('Media hombres: ',(157/244)*100,'%')
    print('Media mujeres: ',(87/244)*100,'%')

def main524():
    tips=pd.read_csv('data_clear/tips.csv')
    pr1=input('Para que columna deseas verlo: \n'
                '1 - sex \n'
                '2 - smoker \n'
                '3 - day \n'
                '4 - time \n'
                '5 - size \n'
                '6 - todas \n'
                '>>> ')
    if pr1=='1':
        print(tips.groupby(by='sex').agg(['size','median','mean']))
    elif pr1=='2':
        print(tips.groupby(by='smoker').agg(['size','median','mean']))
    elif pr1=='3':
        print(tips.groupby(by='day').agg(['size','median','mean']))
    elif pr1=='4':
        print(tips.groupby(by='time').agg(['size','median','mean']))
    elif pr1=='5':
        print(tips.groupby(by='size').agg(['size','median','mean']))
    elif pr1=='6':
        print(tips.groupby(by='sex').agg(['size','median','mean']))
        print(tips.groupby(by='smoker').agg(['size','median','mean']))
        print(tips.groupby(by='day').agg(['size','median','mean']))
        print(tips.groupby(by='time').agg(['size','median','mean']))
        print(tips.groupby(by='size').agg(['size','median','mean']))
    else:
        print('Opcion incorrecta')
        main524()
    
def main525():
    tips=pd.read_csv('data_clear/tips.csv')
    print(tips.groupby(by='size').agg(['size','median','mean']))
    
def main526():
    pass

if __name__ == '__main__':
    main524()