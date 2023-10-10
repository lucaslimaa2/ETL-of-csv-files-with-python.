import pandas as pd
import schedule
import time
import os

directory_path = r"c:\Users\anton\OneDrive\Área de Trabalho\Repositórios\CSVs to practice" 

csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]

frames = []

for csv_file in csv_files:
    file_path = os.path.join(directory_path, csv_file)
    df = pd.read_csv(file_path, sep=',')
    frames.append(df)

result = pd.concat(frames, ignore_index=True)

result.to_csv('output_data.csv', index=False)