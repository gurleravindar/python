string = input('Please enter string \n')

count  = {}

for i in range(len(string)):
    if(count.get(string[i])):
        count[string[i]] = count[string[i]] + 1
    else:
        count[string[i]] = 1


for key in count:
    print(key,count[key], sep="," )