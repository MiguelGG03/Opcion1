import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main513():
    df = pd.read_csv('data_clear/auto-mpg.csv')
    #  Muestra la correlación entre las variables del dataset
    print(df.corr())
    #  Dibuja una gráfica que muestre la correlación entre las variables del dataset
    sns.heatmap(df.corr(), annot=True)
    plt.show()

if __name__ == '__main__':
    main513()