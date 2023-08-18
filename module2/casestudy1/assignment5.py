input_string = input('Please eneter input \n')

output = ''
for i in range(len(input_string)):
    if(i%2==0):
        output = output + input_string[i]

print(output)