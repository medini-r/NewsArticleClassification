import os
import csv

def load_files(mainFolderPath):
    data = {'business' : [], 'entertainment' : [], 'politics' : [] , 'sport' : [], 'tech' : [] }
    folders = [folder for folder in sorted(os.listdir(mainFolderPath))]
    for folder in folders :
        for file in os.listdir(mainFolderPath + "/" + folder):
            data[folder].append(file)
    return data


mainFolder = "C:/Users/Medini R/Desktop/bbc"
bbc_data = load_files(mainFolder)
print(bbc_data)


import pandas as pd

bbc_df = pd.DataFrame.from_dict(bbc_data, orient = 'index')
print(bbc_df)