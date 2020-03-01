list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']
overlapList = []
uniqueList = []

# Find Overlapping Elements using a nested for loop
for i in list_a:
    for z in list_b:
        if i == z:
            overlapList.append(i)
print "The items " + str(overlapList) + " appear in both lists!"

# Find Unique Elements using two nested for loops

for i in list_a:
    if not i in list_b:
        uniqueList.append(i)

for z in list_b:
    if not z in list_a:
        uniqueList.append(z)

print "The items " + str(uniqueList) + " only appear once!"

