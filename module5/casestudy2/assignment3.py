import pandas as pd
import matplotlib.pyplot as plt
df =  pd.read_csv('BigMartSalesData.csv')

df =  df.query("Year == 2011")
df = df.filter(['Month', 'Amount', 'Country', 'Quantity']).groupby(['Country'], as_index = False).sum()

salesCount  = df['Quantity']
country = df['Country']

plt.figure(figsize=(len(salesCount),len(country)))
plt.pie(salesCount, labels = country, autopct='%1.1f%%',shadow=True)
plt.savefig('assignment3.png')
plt.show()
