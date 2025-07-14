import pandas as pd

df = pd.read_csv('Month_1/Week_2/Iris Species Archive/Iris.csv')
df['processed'] = df['SepalLengthCm']*2
print(df.head())

df.to_csv('processed_iris.csv', index=False)
print("File Saved")