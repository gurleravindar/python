numbers_list = list(map(int, input('Please enter numbers \n').split(' ')))

all_even_numbers = []

# loop over list
for i in numbers_list:
    if( i>=1000 and i<=3000):
        # length of each number
        split_word = len(str(i))
        eachnumber = i   
        iseven = False
        # checking number each letter in even or not   
        for eachletter in range(split_word):
            reminder =  eachnumber%10
            eachnumber = int(eachnumber/10)
            #  letter is even making flag is true else making flag as false and added break
            if(reminder%2 == 0):
                iseven = True
            else:
                iseven = False
                break
        # checking each letter of number is even and addig to list
        if(iseven):
            all_even_numbers.append(str(i))
        
print('even numbers', ', '.join(all_even_numbers))
    