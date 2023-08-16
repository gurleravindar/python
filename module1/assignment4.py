sentence = input('Please enter sentence \n')

letters_count=0
digits_Count=0

for s in sentence:
    if(s.isnumeric()):
        digits_Count = digits_Count +1
    else:
        letters_count=letters_count +1


print('LETTERS: ', letters_count)
print('DIGITS: ', digits_Count)
