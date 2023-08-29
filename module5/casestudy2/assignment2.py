import pandas as pd
import matplotlib.pyplot as plt
df =  pd.read_csv('BigMartSalesData.csv')

df =  df.query("Year == 2011")
df = df.filter(['Month', 'Amount']).groupby(['Month'], as_index = False).sum()
x =  df['Month']
y =  df['Amount']

plt.bar(x, y)
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Month vs sales")
plt.grid()
plt.savefig('assignment2.png')
plt.show()