import pandas as pd
import schedule
import time
import os

# -------- 1) EXTRACT --------

def etl_process():
    print('Starting ETL process...')

directory_path = r"c:\Caminho da pasta com os arquivos csv" 

csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]

frames = []

for csv_file in csv_files:
    file_path = os.path.join(directory_path, csv_file)
    df = pd.read_csv(file_path, sep=',')
    frames.append(df)

result = pd.concat(frames, ignore_index=True)

# ---------- 3) LOAD ------------
result.to_csv('output_data.csv', index=False)

print("ETL process completed!")


# ---------- AUTOMATION ----------

schedule.every().month.at("08:00").do(etl_process) # Schedule the ETL job to run daily at a specific time

while True:
    schedule.run_pending()
    time.sleep(1)





