import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data

#  Dibuja una gráfica que muestre la relación entre las variables del dataset

def main():
    df = pd.read_csv('data_clear/auto-mpg.csv')
    pr1 = input('Que grafica desea ver? (1-8):\n'
    '1. mpg vs. horsepower\n'
    '2. mpg vs. weight\n'
    '3. mpg vs. displacement\n'
    '4. mpg vs. acceleration\n'
    '5. mpg vs. model_year\n'
    '6. mpg vs. origin\n'
    '7. mpg vs. cylinders\n'
    '8. mpg vs. car_name\n'
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
    elif pr1 == '8':
        sns.lmplot(x='car_name', y='mpg', data=df)
        plt.show()
    else:
        print('No es una opcion valida')
        main()

if __name__ == '__main__':
    main()
    