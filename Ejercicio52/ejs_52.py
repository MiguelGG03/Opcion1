import pandas as pd

def main521():
    tips = pd.read_csv('data_clear/tips.csv')
    print(tips.info())
    


if __name__ == '__main__':
    main521()