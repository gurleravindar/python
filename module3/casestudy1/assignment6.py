def divisibleBy7AndNotMultipleOf5(number):
    if(number % 7 == 0 and number % 5 != 0 ):
        return True
    else:
        return False

separated_string = ''
for i in range(2000, 3201):
    isCorrectNumber = divisibleBy7AndNotMultipleOf5(i)
    if(isCorrectNumber):
        separated_string =  separated_string + str(i) + ','

print(separated_string)