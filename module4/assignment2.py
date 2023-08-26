import numpy as np
# reading file and separated by names space
data = np.genfromtxt('SalaryGender.csv', dtype=None, delimiter=',', encoding=None, names=True)

# Storing individual column into np arrays
# salaryNpArray =  np.array(data['Salary'])
genderNpArray =  np.array(data['Gender'])
# ageNpArray = np.array(data['Age'])
phdNpArray = np.array(data['PhD'])

mens_phd_count = 0
wowens_phd_count = 0

for i in range(len(genderNpArray)):
    if(genderNpArray[i] == 1 and phdNpArray[i] == 1 ):
        mens_phd_count = mens_phd_count + 1 
    elif(genderNpArray[i] == 0 and phdNpArray[i] == 1):
        wowens_phd_count = wowens_phd_count + 1

print("Mens Phd Count", mens_phd_count)
print("Womens Phd Count", wowens_phd_count)