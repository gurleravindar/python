numbers = input('Please enter 2 numbers \n')
numbers_split = numbers.split(',')

array = []


for i in range(int(numbers_split[0])):
    array.append([])
    for j in range(int(numbers_split[1])):
        array[i].append(i*j)
        
print(array)