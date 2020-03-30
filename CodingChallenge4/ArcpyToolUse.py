import arcpy # Imports arcpy toolbox
arcpy.env.overwriteOutput = True # Overwrites files with the same name to avoid the script from
                                    crashing during repeated trials

arcpy.env.workspace = r"E:\Python\Mike's Folder\Coastline" # Sets workspace, can be changed easily

inputFeatures = r"Coastline.shp" # Input shapefile that we want to buffer
outputFeatures = r"CoastlineOutput.shp" # Name of the outputted buffer file
distance = "100 meters" # Distance and units in which we want to buffer
sideType = "FULL"
lineEndType = "ROUND"
dissolveOption = "NONE"
dissolveField = "#"
method = "PLANAR"
arcpy.Buffer_analysis(inputFeatures, outputFeatures, distance, sideType,
                      lineEndType, dissolveOption, dissolveField, method)

if arcpy.Exists(outputFeatures):
    print "Created file successfully!" # Checks to see if the buffered shapefile was created successfully
