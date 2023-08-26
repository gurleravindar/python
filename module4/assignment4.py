import pandas as pd

data = pd.read_csv('SalaryGender.csv')

# storing phd data

phd_data = data.filter(['PhD'])

phd_count = phd_data.query('PhD == 1')

print('PhD count', len(phd_count))
