numbers = int(input('Please enter number > 0 \n'))
total_sum = 0
if(numbers<0):
    print("invalid number")
    exit
else:
    for i in range(1, numbers+1):
        total_sum = total_sum + i/ (i+1)
    print("total_sum", round(total_sum, 2))