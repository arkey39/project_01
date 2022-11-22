import pandas as pd 
import numpy as np 

# Открыть файл data.xlsx с помощью pandas
df = pd.read_excel('data.xlsx', sheet_name = 'Sheet1')

# Выберем ввсе значения, где sku = 'капуста'
df = df[df['sku'] == 'Капуста']

# Запишем датафрейм в файл task1.csv
df.to_csv(r'C:\Users\Andrei\miniforge3\envs\project_01\app\lesson_22.11.22\task1')