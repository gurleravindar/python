items = input('Please decinmal inputs \n')

items_split = items.split(',')

output = []

for p in items_split:
    x = int(p, 2)
    if not x%5:
        output.append(p)
print(','.join(output))
