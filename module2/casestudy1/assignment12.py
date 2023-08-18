numbers_list = [12,24,35,70,88,120,155]

numbers_list_duplicate = [12,24,35,70,88,120,155]

# checking and removing numbers divided 5 and 7

for i in range(len(numbers_list)):
    if(numbers_list[i] % 5 == 0 and numbers_list[i]% 7 == 0):
        numbers_list_duplicate.remove(numbers_list[i])


print(numbers_list_duplicate)