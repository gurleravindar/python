import numpy as np
import matplotlib.pyplot as plt

y = np.random.randn(20,20)

data = np.genfromtxt('CityTemps.csv', dtype=None, delimiter=',', encoding=None, names=True)

fransisco = data['SanFrancisco']
moscow = data["Moscow"]

plt.hist(fransisco, len(fransisco))
plt.hist(moscow, len(moscow))
plt.savefig('assignment2.png')
plt.show()



