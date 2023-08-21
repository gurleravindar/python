sentence  =  input('Please enter the words of sentence \n')

sentence_splits = sentence.split(' ')

sentence_splits_list_sorted =  sorted(list(set(sentence_splits)))

print(*sentence_splits_list_sorted, sep=' ')