
import csv
readingfile = open('bank-data.csv', 'r')
csvFile = csv.reader(readingfile)
# it will skip the reading the headers
next(csvFile, None)
# list to store eligibale professions 
professions = []
ages = []
for lines in csvFile:
    # checking professsion and profession is eligible
    if(lines[1] and lines[3] == 'yes'):
        # checking profession is eligible and not in list, add profession to list
       if lines[1] not in professions:
        # convertig to lowercase for case in sensitive
        professions.append(lines[1].lower())
    # storing ages in list
    ages.append(int(lines[0]))

print('Elible Propessions:',professions)
# sorting ages
ages = sorted(ages)
max_min_ages =  {'max_age': ages[len(ages)-1], 'min_age':ages[0]}
print("Max, Min ages:", max_min_ages)

print('Enter Profession to check eligible and Enter END to exit')

while True:
    profession_name = input()
    if(profession_name == 'END' or profession_name == 'end'):
        break
    elif(profession_name.lower() in professions):
        print("Eligible")
    else:
        print('Not Eligible')


