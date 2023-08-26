import pandas as pd

data = pd.read_csv('SalaryGender.csv')

# storing data age and phd data
age_phd_data = data.filter(['Age', 'PhD'])

# Delete data who not have phd

after_delete_data =  age_phd_data.drop(age_phd_data[age_phd_data['PhD'] == 0].index)

print(after_delete_data)
