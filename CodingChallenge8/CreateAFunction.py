# Creating a function from previous code in the semester

import os
import arcpy

# Warm-up function to show handiness of process
# This function will take a list and multiply its contents by a factor, then fill and print the new results.
# i = list
# j = factor

def listMultiplier(i, j):
    newList = []
    for x in i:
        newNumber = x * j
        newList.append(newNumber)
    return "The new list is " + str(newList) + "."

exampleList = [1, 2, 3, 4, 5]
exampleList2 = [10, 20, 30, 40, 50]
exampleList3 = [100, 200, 300, 400, 500]
exampleFactor = 10

print listMultiplier(exampleList, exampleFactor)
print listMultiplier(exampleList2, exampleFactor)
print listMultiplier(exampleList3, exampleFactor)

# This function will read the contents of a folder, check for raster file types, and count the number of that file.
# To show this function in action, please use CodingChallenge8Data.zip
# a = your workspace
# b = raster file extension

def checkRaster(a, b):
    arcpy.env.workspace = a
    rasterList = arcpy.ListRasters("*", b)
    rasterList = [x for x in rasterList if "_BQA.tif" not in x]
    print "The files ending in " + b + " are " + str(rasterList) + "."
    print "The number of " + b + " files in that folder is " + str(len(rasterList)) + "."

workspace = r"C:\Users\Public\PythonClass\Class_8\CodingChallenge8Data" # Change workspace here
fileType = "TIF" # Change raster file type here

checkRaster(workspace, fileType)
print "All done."

# This function will set the workspace, check and print a list of desired feature class type, and buffer them.
# To show this function in action, please use CodingChallenge8Data2.zip
# x = your directory
# y = feature class type
# z = buffer distance

def lineBuffer(x, y, z):
    arcpy.env.workspace = x
    bufferFiles = arcpy.ListFeatureClasses("*", y)
    print "The files of " + y + " feature class type are " + str(bufferFiles)
    for i in bufferFiles:
        inFeature = i
        outFeature = i[0:3] + "BufferOutput.shp"
        bufferDistance = z
        arcpy.Buffer_analysis(inFeature, outFeature, bufferDistance)

directory = r"C:\Users\Public\PythonClass\Class_8\CodingChallenge8Data2" # Change workspace here
fileType = "Polyline"  # Should be "Polygon" / "Polyline" / "Point"
distance = "100 feet"  # Should be entered "'### (unit of distance)"

lineBuffer(directory, fileType, distance)
print "Buffering analysis completed."
