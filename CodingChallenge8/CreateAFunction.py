# Creating a function from previous code in the semester

# This function will take a list(i) and multiply its contents by a factor(j), then fill and print the new results
def listMultiplier (i,j):
  newList = []
  for x in i:
    newNumber = x * j
    newList.append(newNumber)
  return newList


exampleList = [1,2,3,4,5]
exampleFactor = 10

print listMultiplier(exampleList, ExampleFactor)
