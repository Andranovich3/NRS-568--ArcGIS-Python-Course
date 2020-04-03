# Creating a function from previous code in the semester

# Warm-up function to show handiness of process
# This function will take a list(i) and multiply its contents by a factor(j), then fill and print the new results
def listMultiplier(i,j):
  newList = []
  for x in i:
    newNumber = x * j
    newList.append(newNumber)
  return newList


exampleList = [1,2,3,4,5]
exampleList2 = [10,20,30,40,50]
exampleList3 = [100,200,300,400,500]
exampleFactor = 10

print listMultiplier(exampleList, exampleFactor)
print listMultiplier(exampleList2, exampleFactor)
print listMultiplier(exampleList3, exampleFactor)
