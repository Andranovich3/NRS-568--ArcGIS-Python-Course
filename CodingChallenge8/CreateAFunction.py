# Creating a function from previous code in the semester

import os
import arcpy

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

# This function will read the contents of a folder, check for file type, and convert to feature.
# a = your workspace
# b = file extension

def checkFolder(a,b):
  arcpy.env.workspace = a
  rasterList = arcpy.ListRasters("*", b)
  rasterList = [x for x in rasterList if "_BQA.tif" not in x]
  print "The files ending in " + b + " are " + str(rasterList) + "."
  print "The number of files in that folder are " + str(len(rasterList)) + "."
  
checkFolder(YOUR WORKSPACE HERE, "TIF")
print "All done."
