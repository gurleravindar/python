import random

random_list = []

for i in range(0,5):
    result = random.randint(1, 1000)

    while result:
        if(result%5 == 0 and result%7 ==0):
            random_list.append(result)
            break
        else:
            result =  random.randint(1, 1000)
            
print(random_list)