import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("BigMartSalesData.csv")
invoice_amounts = df.filter(["InvoiceDate", "Amount"]).groupby(
    "InvoiceDate", as_index=False).sum()

plt.scatter(invoice_amounts["InvoiceDate"], invoice_amounts["Amount"])
# invoice amounts are concentrated
plt.ylim(20000, 100000)
plt.savefig('assignment4.png')
plt.show()