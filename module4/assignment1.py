import numpy as np
# reading file and separated by names space
data = np.genfromtxt('SalaryGender.csv', dtype=None, delimiter=',', encoding=None, names=True)

# Storing individual column into np arrays
salaryNpArray =  np.array(data['Salary'])
genderNpArray =  np.array(data['Gender'])
ageNpArray = np.array(data['Age'])
phdNpArray = np.array(data['PhD'])

print('Salary', salaryNpArray)