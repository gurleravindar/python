import re
password = input('Please enter password \n')
password_message = ''

# checking password length between 6 to 12
if(len(password)>=6 and len(password)<=12):
    # checking password contain atleast [a-z] character
    if(not bool(re.search('[a-z]', password))):
        password_message ='Password contain atleast [a-z] character'
    # checking password contain atleast [A-Z] character
    elif(not bool(re.search('[A-Z]', password))):
        password_message = 'Password contain atleast [A-Z] character'
    # checking password conatin atleast [0-9] chacter
    elif(not bool(re.search('[0-9]', password))):
        password_message = 'Password contain atleast [0-9] number'
    # checking password contain atleasr $#@ character
    elif(not bool(re.search('[$#@]', password))):
        password_message='Password contain atleast 1 character from [$#@]'
    else:
        password_message='Strong password'
else:
    password_message = 'Password lenght should between 6 to 12'

print(password_message)