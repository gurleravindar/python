input_string = input('Please enter words as comma separated \n')

input_string  = input_string.split(',')

input_strig_sorted = sorted(input_string)

print(*input_strig_sorted, sep=',')