import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Cars2015.csv")

df = df.drop(['Model','Type','LowPrice','HighPrice','Drive','CityMPG',
'HwyMPG','FuelCap','Length', 'Width','Wheelbase','Height','UTurn',
'Weight','Acc030','Acc060', 'QtrMile','PageNum','Size'], axis=1)

df['count'] = df.groupby('Make')['Make'].transform('count')

df.drop_duplicates('Make',inplace=True)

df.sort_values(by='count',ascending=False,inplace=True)

print(df.shape)  
#  (37,2)

plt.figure(figsize=(37,2))
plt.pie(df['count'], labels = df['Make'])
plt.show()

