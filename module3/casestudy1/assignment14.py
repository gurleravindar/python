input_string = input('Please enter string \n')

upper_count = 0
lower_count = 0


for i in range(len(input_string)):
    if(input_string[i].isalpha()):
        if(input_string[i].isupper()):
            upper_count = upper_count + 1
        else:
            lower_count = lower_count + 1 

print('UPPER CASE', upper_count)
print('LOWER CASE', lower_count)
