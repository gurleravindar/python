import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('Hurricanes.csv', dtype=None, delimiter=',', encoding=None, names=True)

years = data['Year']
hurricans = data["Hurricanes"]

plt.xlabel('Years')
plt.ylabel('Hurricans')

plt.bar(years, hurricans)
plt.savefig('assignment1.png')

plt.show()


