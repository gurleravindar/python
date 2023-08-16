# reading input from user
number = int(input('Please enter number \n'))

# Generating number up to given input using range
# Loop over to find factors and odd, even numbers
for i in range(1, number+1):
    if(number % i == 0):
        if(i%2 ==0):
            print(i, 'is a facotor of ', number, ' and it is even number')
        else:
            print(i, ' is a factor of ', number, ' and it is odd number')
