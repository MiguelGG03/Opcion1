import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
    sns.barplot(data=tips, x='sex', y='tip')
    plt.show()
    
def main526():
    tips=pd.read_csv('data_clear/tips.csv')
    pr1=input('Para que columna deseas verlo (con respecto de tip): \n'
                '1 - sex \n'
                '2 - smoker \n'
                '3 - day \n'
                '4 - time \n'
                '5 - size \n'
                '>>> ')
    if pr1=='1':
        sns.barplot(data=tips,x='sex',y='tip')
        plt.show()
    elif pr1=='2':
        sns.barplot(data=tips,x='smoker',y='tip')
        plt.show()
    elif pr1=='3':
        sns.barplot(data=tips,x='day',y='tip')
        plt.show()
    elif pr1=='4':
        sns.barplot(data=tips,x='time',y='tip')
        plt.show()
    elif pr1=='5':
        sns.barplot(data=tips,x='size',y='tip')
        plt.show()
    else:
        print('Opcion incorrecta')
        main526()

def main527():
    print('Para mi, las variables que mas afectan a cuanta propina dejan los clientes\n'
            'son el sexo, el dia de la semana y el tamanio del grupo, ya que el sexo\n'
            'porque los hombres suelen dejar mas propina que las mujeres, el dia de la\n'
            'semana porque los fines de semana suelen dejar mas propina que los dias\n'
            'de diario, y el tamanio del grupo , porque cuantos mas son mas propina \n'
            'suelen dejar. Los fumadores no afectan a la propina, ya que no dejan mas\n'
            'propina que los no fumadores.')

def main528():
    tips=pd.read_csv('data_clear/tips.csv')
    print('Tercer cuartil de tip: ',tips['tip'].quantile(0.75))
    print(tips[tips['tip']>=tips['tip'].quantile(0.75)])

def main529():
    tips=pd.read_csv('data_clear/tips.csv')
    data=tips[tips['tip']>=tips['tip'].quantile(0.75)]
    pr1=input('Que histograma desea ver: \n'
                '1 - smoker \n'
                '2 - day \n'
                '3 - time \n'
                '4 - size \n'
                '>>> ')
    if pr1=='1':
        sns.histplot(data=data,x='smoker')
        plt.show()
    elif pr1=='2':
        sns.histplot(data=data,x='day')
        plt.show()
    elif pr1=='3':
        sns.histplot(data=data,x='time')
        plt.show()
    elif pr1=='4':
        sns.histplot(data=data,x='size')
        plt.show()
    else:
        print('Opcion incorrecta')
        main529()

        

    

if __name__ == '__main__':
    main529()