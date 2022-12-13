import pandas as pd

def main521():
    tips = pd.read_csv('data_clear/tips.csv')
    print(tips.head())
    print(tips.info())

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


if __name__ == '__main__':
    main522()