
import csv
readingfile = open('bank-data.csv', 'r')
csvFile = csv.reader(readingfile)
# it will skip the reading the headers
next(csvFile, None)

# list to store eligibale professions 
professions = []

for lines in csvFile:
    # checking professsion and profession is eligible
    if(lines[1] and lines[3] == 'yes'):
        # checking profession is eligible and not in list, add profession to list
       if lines[1] not in professions:
        professions.append(lines[1])

print(professions)

profession_name =  input('Please enter pofession to check to eligible \n')

if profession_name in professions:
    print('ELigible')
else:
    print("No Eligible")

