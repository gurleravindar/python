import pandas as pd
import matplotlib.pyplot as plt

# Reading data...
df = pd.read_csv("sample-salesv2.csv")

# Describe unite price
df['unit price'].describe() 
print(df)

#  Filter the data
data = {'name': df['name'], 'net_price': df['net_price'], 'date': df['date'] }
dataFrameTable =  pd.DataFrame(data)
print(dataFrameTable)


# Group all records according to the name and doing sum
df =  df[['name', 'net_price', 'date']].groupby(by='name').sum().reset_index()
plt.xlabel('Customer Name')
plt.ylabel('Sales')
plt.plot(df['name'], df['net_price'])
plt.show()

