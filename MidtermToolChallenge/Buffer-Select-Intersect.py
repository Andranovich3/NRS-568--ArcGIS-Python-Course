# For this midterm assignment, I've created a set of code which should check to see how Washington County would be affected
# by a sea level rise of 3 meters. The three tools I use are: buffer, select, and intersect. First, I create a buffer around
# a RI Coastline shapefile that I acquired from RIGIS (Unprojected / Datum: WGS84). Next, I create a new shapefile of just
# Washington County from a RI Towns shapefile that I acquired from Dr. Jason Parent's NRS 522 Advanced GIS class
# (RI StatePlane meters / Datum: NAD83). Lastly, I create an intersected layer of the two areas to show the effects of sea
# level rise, especially for coastal areas in Washington County. Note: Despite the layers being different projections, I
# believe I address that problem in line 21 by setting all output coordinate systems to WGS84. This may create minor distortion
# on the RI Towns shapefile, but it's negligible, in my opinion.

import os
import arcpy
arcpy.env.overwriteOutput = True  # Overwrites files when saving to avoid the script from crashing during repeated trials

yourDirectory = r"C:\Users\Public\PythonClass\Data"  # **Change contents of r"_" to whatever your directory will be.**
arcpy.env.workspace = yourDirectory  # Sets the workspace for files
outputDirectory = os.path.join(yourDirectory, "midtermTestFiles")  # Sets up a temporary file folder
if not os.path.exists(outputDirectory):  # Checks for folder's existence (it should not exist on the first trial)
    os.mkdir(outputDirectory)  # Creates the actual folder in the directory

arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)  # Sets all output coordinates to WGS84

# Tool 1: Creating a buffer around a RI coastline shapefile

inputShp = r"Coastline.shp"  # Input shapefile that we want to buffer
outputShp = os.path.join(outputDirectory, "CoastlineBuffer_3meters.shp")  # Output file joins created output directory
distance = "3 meter"  # Distance and units in which we want to buffer
sideType = "FULL"
lineEndType = "ROUND"
dissolveOption = "NONE"
dissolveField = "#"
method = "PLANAR"

arcpy.Buffer_analysis(inputShp, outputShp, distance, sideType, lineEndType, dissolveOption, dissolveField, method)

if arcpy.Exists(outputShp):
    print "Buffer file created successfully!"  # Checks to see if the buffered shapefile was created successfully

# Tool 2: Creating a new layer based on a selection by County

inputFeature = "towns.shp"
outputFeature = os.path.join(outputDirectory, "WashingtonCounty.shp")
whereCategory = "COUNTY"  # Change selection category here, remember to use all caps
whereResponse = 'WASHINGTON'  # Change selection criteria here, remember to use all caps
whereClause = "{} = '{}'".format(arcpy.AddFieldDelimiters(inputFeature, whereCategory), whereResponse)

arcpy.Select_analysis(inputFeature, outputFeature, whereClause)

if arcpy.Exists(outputFeature):
    print "Selection file created successfully!"  # Checks to see if the selection shapefile was created successfully

# Tool 3: Create an intersected layer of the two above layers

inputLayers = [outputShp, outputFeature]  # Input layers must be formatted into a list. List created while declaring variable.
outputLayer = os.path.join(outputDirectory, whereResponse + "CoastlineIntersect.shp")
joinAttributes = "ALL"  # Joins all attributes from both tables into the new shapefile

arcpy.Intersect_analysis(inputLayers, outputLayer, joinAttributes)

if arcpy.Exists(outputLayer):
    print "Intersect file created successfully!\n"  # Checks to see if the intersection shapefile was created successfully

print "All files created successfully.\n"

# A little bit of bonus spaghetti to finish it off

userInput = raw_input("Would you like to delete the files now: yes or no? ")
userInput = userInput.lower()

if userInput == "yes":
    arcpy.Delete_management(outputDirectory)
    print "Smell ya later, midterm files."
elif userInput == "no":
    print "Okay, keep enjoying these sweet, sweet files."
else:
    print "Please enter yes or no."
