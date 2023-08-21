# example compay sorted order list below
a = [1,2, 4, 5, 6, 7,10, 23, 34, 45]

search_data = int(input('Please enter search data \n'))

# finding count of search number
count_of_search_data =  a.count(search_data)

if(count_of_search_data >=1):
    print('data found')
elif(count_of_search_data == 0):
    print("data not found")
