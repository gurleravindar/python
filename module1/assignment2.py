
#  Taking sewuence of words with sperated by space 
#  split with space
#  map over split words to generate list
sentence_list = list(map(str, input("Please enter sequence of words separarated by space \n").split(' ')))

# setences before sort
print("bofore sort sentence list", sentence_list, )

# sorting sentence alphabetically 
sentence_list.sort()

#  sentence after sort
print("after sort sentence list", sentence_list)