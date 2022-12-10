import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data

#  Dibuja una gráfica que muestre la relación entre las variables del dataset

def main511():
    df = pd.read_csv('data_clear/auto-mpg.csv')
    pr1 = input('Que grafica desea ver? (1-7):\n'
    '1. mpg vs. horsepower\n'
    '2. mpg vs. weight\n'
    '3. mpg vs. displacement\n'
    '4. mpg vs. acceleration\n'
    '5. mpg vs. model_year\n'
    '6. mpg vs. origin\n'
    '7. mpg vs. cylinders\n'
    '>>> ')
    if pr1 == '1':
        sns.lmplot(x='horsepower', y='mpg', data=df)
        plt.show()
    elif pr1 == '2':
        sns.lmplot(x='weight', y='mpg', data=df)
        plt.show()
    elif pr1 == '3':
        sns.lmplot(x='displacement', y='mpg', data=df)
        plt.show()
    elif pr1 == '4':
        sns.lmplot(x='acceleration', y='mpg', data=df)
        plt.show()
    elif pr1 == '5':
        sns.lmplot(x='model_year', y='mpg', data=df)
        plt.show()
    elif pr1 == '6':
        sns.lmplot(x='origin', y='mpg', data=df)
        plt.show()
    elif pr1 == '7':
        sns.lmplot(x='cylinders', y='mpg', data=df)
        plt.show()
    else:
        print('No es una opcion valida')
        main511()

def main512():
    print('Ejercicio 5.2')
    print('Existe correlacion entre las siguientes variables:')
    print('cylinders & displacement')
    print('cylinders & horsepower')
    print('cylinders & weight')
    print('displacement & horsepower')
    print('displacement & weight')
    print('horsepower & weight')

def main513():
    df = pd.read_csv('data_clear/auto-mpg.csv')
    #  Muestra la correlación entre las variables del dataset
    print(df.corr())
    #  Dibuja una gráfica que muestre la correlación entre las variables numericas del dataset
    sns.heatmap(df.corr(), annot=True)
    plt.show()

def main514():
    df = pd.read_csv('data_clear/auto-mpg.csv')
    # Dibuja un diagrama de dispersion que este en funcion de weight y horsepower, dependiendo del numero de displacements
    sns.lmplot(x='weight', y='horsepower', data=df, hue='cylinders', fit_reg=False)
    plt.show()

def main515():
    df = pd.read_csv('data_clear/auto-mpg.csv')
    sns.lmplot(x='weight', y='horsepower', data=df, hue='model_year', fit_reg=False)
    plt.show()
    print('Sabemos que cuanto mas moderno es el coche,')
    print('tiende a pesar menos y a tener menos potencia.')
    print('Tambien se puede ver que con el paso de los años,')
    print('los coches han ido reducioendo el numero de cilindros\npor normas generales (tambien puede existir algun dato\nque se escape de la normalidad).')

def main516():
    df = pd.read_csv('data_clear/auto-mpg.csv')
    sns.lmplot(x='weight', y='horsepower', data=df[df['model_year']==70], hue='model_year', fit_reg=False)
    plt.show()

if __name__ == '__main__':
    main516()
    