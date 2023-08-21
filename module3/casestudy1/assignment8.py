import math

c = 50
h = 30

numbers = input("Please enter number sepated by commana \n")

numbers = numbers.split(',')

square_root_list = []


for d in range(len(numbers)):
    q = math.sqrt((2*c*int(numbers[d]))/h)
    square_root_list.append(round(q, 0))

print(*square_root_list, sep=',')