# In this coding challenge, your objective is to utilize the radiating lines code used in class "9_Cursors"
# to take an input of sites from a provided Shapefile (Site_Locations.zip), use the radiating lines code to
# calculate "fetch distances" for each 10 degree bearing in a manner that originated from Davies & Johnson (2006).
# Finally, clip the resulting fetch lines by the NB_Coastline.zip shapefile, and report the mean plus standard
# deviation of the fetch distance for each site: 9 sites, A1....C3 in meters. We don't have wind data so can't
# calculate the estimate as accurately as in Davies & Johnson (2006).

import os
import arcpy
from math import radians, sin, cos
arcpy.env.overwriteOutput = True

yourDirectory = r"C:\Users\Public\PythonClass\Site_Locations" # **Change directory here**
arcpy.env.workspace = yourDirectory # Sets the workspace for files
outputDirectory = os.path.join(yourDirectory, "TestFiles") # Sets up a temporary file folder

if not os.path.exists(outputDirectory): # Checks for folder's existence
    os.mkdir(outputDirectory) # Creates the folder in the directory

locations = r"Site_Locations.shp"
locations_list = []

with arcpy.da.SearchCursor(locations, ['SHAPE@XY', 'Site_Code']) as cursor:
    for row in cursor:
        locations_list.append(row)
print locations_list

referenceName = arcpy.Describe(locations).spatialReference.name
referenceNumber = arcpy.Describe(locations).spatialReference.factoryCode
print "The name of the coordinate system is " + referenceName + "."
print "The spatial reference number is " + str(referenceNumber) + "."

for i in locations_list:
    out_path = outputDirectory
    out_name = "radLines_" + i[1] + ".shp" # Naming file after Site_Code field
    geometry_type = "POLYLINE"
    template = "#"
    has_m = "DISABLED"
    has_z = "DISABLED"
    spatial_ref = 32130

    arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template, has_m, has_z, spatial_ref)
    print "Radiating lines file for " + i[1] + " created successfully!"

    origin_x, origin_y = i[0][0], i[0][1]
    distance = 100000
    angle = 10  # in degrees

    OutputFeature = os.path.join(out_path, out_name)
    OutFeat = out_name

    #create list of bearings
    angles = range(0, 360,angle)
    for ang in angles:
        angle = float(int(ang))
        (disp_x, disp_y) = (distance * sin(radians(angle)), distance * cos(radians(angle)))
        (end_x, end_y) = (origin_x + disp_x, origin_y + disp_y)
        (end2_x, end2_y) = (origin_x + disp_x, origin_y + disp_y)

        cur = arcpy.InsertCursor(OutputFeature)
        lineArray = arcpy.Array()

        start = arcpy.Point()
        (start.ID, start.X, start.Y) = (1, origin_x, origin_y)
        lineArray.add(start)

        end = arcpy.Point()
        (end.ID, end.X, end.Y) = (2, end_x, end_y)
        lineArray.add(end)

        feat = cur.newRow()
        feat.shape = lineArray
        cur.insertRow(feat)

        lineArray.removeAll()
        del cur
