import pyreadr
import pandas as pd


data= pyreadr.read_r('data/tips.rda')
for i in data:
    print(i)
    print(type(data[i]))
    print(data[i].head(10))