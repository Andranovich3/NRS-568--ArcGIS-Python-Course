# Creating a function from previous code in the semester

import os
import arcpy

# Warm-up function to show handiness of process
# This function will take a list and multiply its contents by a factor, then fill and print the new results.
# i = list
# j = factor

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

# This function will read the contents of a folder, check for file type, and count the number of that file.
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

# This function will set the workspace, check and print a list of desired feature class type, and buffer them.
# x = your directory
# y = feature class type
# z = buffer distance

def lineBuffer(x,y,z):
  arcpy.env.workspace = x
  bufferFiles = arcpy.ListFeatureClasses("*", y)
  print bufferFiles
  for i in bufferFiles:
    inFeature = i + ".shp"
    outFeature = i[0:3] + "BufferOutput.shp"
    bufferDistance = z
    arcpy.Buffer_analysis(inFeature, outFeature, bufferDistance)


directory = "YOUR DIRECTORY HERE"
fileType = "ENTER FILE TYPE HERE" # Should be "Polygon" / "Polyline" / "Point"
distance = "ENTER BUFFER DISTANCE AND UNIT HERE" # Should be entered "'Numerical Distance' ' ' 'lowercase unit'"

lineBuffer(directory, fileType, distance)
print "Buffering analysis completed."
    
