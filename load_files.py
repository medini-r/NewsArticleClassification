import os
import pandas as pd
import csv
mainFolder = "C:/Users/Medini R/Desktop/bbc"

folders = ["business","entertainment","politics","sport","tech"]

os.chdir(mainFolder)

x = []
y = []

for folder in folders:
    files = os.listdir(folder)
    for text_file in files:
        path = folder + "/" + text_file
        x.append(open(path).readlines())
        y.append(folder)
   
bbc_dict = {'category': y, 'article': x}  
bbc_df = pd.DataFrame(bbc_dict)
bbc_df = bbc_df.sort_values(by = 'article')
bbc_df.to_csv('../bbc_dataset.csv', index=False)

bbc = pd.read_csv('../bbc_dataset.csv')
bbc.head(2225)