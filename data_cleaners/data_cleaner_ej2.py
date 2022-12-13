import pyreadr as prd
import pandas as pd


data= prd.read_r('data/tips.rda')

tips = data['tips']
print(tips.head())
print(tips.info())
print(type(tips))

tips.to_csv('data_clear/tips.csv', index=False)