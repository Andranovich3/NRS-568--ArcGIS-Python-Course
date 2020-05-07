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

yourDirectory = r"C:\Course_ArcGIS_Python_Students\Andarnovich-NRS-568--ArcGIS-Python-Course\CodingChallenge9\Data"  # Change directory here
arcpy.env.workspace = yourDirectory  # Sets the workspace for files
outputDirectory = os.path.join(yourDirectory, "TestFiles")  # Sets up a temporary file folder

if not os.path.exists(outputDirectory):  # Checks for folder's existence
    os.mkdir(outputDirectory)  # Creates the folder in the directory

locations = os.path.join(yourDirectory, "Site_Locations.shp") #AD Coded location correctly as you switch into your TestFiles Workspace
locations_list = []

# Creates a list of (x,y) coordinates and site names (stored as tuple)
with arcpy.da.SearchCursor(locations, ['SHAPE@XY', 'Site_Code']) as cursor:
    for row in cursor:
        locations_list.append(row)
print locations_list

# Obtains the spatial reference code of the site locations
referenceName = arcpy.Describe(locations).spatialReference.name
referenceNumber = arcpy.Describe(locations).spatialReference.factoryCode
print "The name of the coordinate system is " + referenceName + "."
print "The spatial reference number is " + str(referenceNumber) + "."

radLinesList = []
radLinesClipped = []
siteCodeList = []
bufferedSites = []
finalStatsList = []

# Creates the radiating lines shapefile and populates it with information
for a in locations_list:
    out_path = outputDirectory
    out_name = "radLines_" + a[1] + ".shp"  # Naming file after Site_Code field
    geometry_type = "POLYLINE"
    template = "#"
    has_m = "DISABLED"
    has_z = "DISABLED"
    spatial_ref = referenceNumber

    arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template, has_m, has_z, spatial_ref)

    origin_x, origin_y = a[0][0], a[0][1]
    distance = 1000000
    angle = 10  # in degrees

    OutputFeature = os.path.join(out_path, out_name)

    # create list of bearings
    angles = range(0, 360, angle)

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

    radLinesList.append(out_name)
    print "Radiating Lines shapefile for " + str(a[1]) + " created successfully!"

# Clips radiating line to Coastline shapefile
for b in radLinesList:
    arcpy.env.workspace = outputDirectory
    in_features = b
    clip = os.path.join(yourDirectory, "NB_Coastline.shp") #AD Coded location of input coastline correctly
    out_feature = "radLines_clip_" + b[9:11] + ".shp"
    xy_tolerance = ""

    arcpy.Clip_analysis(in_features, clip, out_feature, xy_tolerance)

    radLinesClipped.append(out_feature)
    print "Clipped file for " + b[9:11] + " created successfully!"

# Creates fetch lines (removes white space from clipped lines, able to measure only actual line length now)
for c in radLinesClipped:
    m_input = c
    m_output = "fetchLines_" + c[14:16] + ".shp"

    arcpy.MultipartToSinglepart_management(m_input, m_output)
    print "Fetch lines for " + c[14:16] + " created successfully!"

# Creates a list of site code names only
with arcpy.da.SearchCursor(locations, ['Site_Code']) as cursor:
    for row in cursor:
        siteCodeList.append(row[0].encode("utf-8"))

# Creates 10 meter buffer around each site location point
for x in siteCodeList:
    sites = arcpy.MakeFeatureLayer_management(os.path.join(yourDirectory, "Site_Locations.shp")) #AD fixed
    whereCategory = "Site_Code"
    whereResponse = x
    whereClause = "{} = '{}'".format(arcpy.AddFieldDelimiters(sites, whereCategory), whereResponse)
    print whereClause
    arcpy.SelectLayerByAttribute_management(sites, "NEW_SELECTION", whereClause)

    in_class = sites
    out_class = "Buffer_" + x + ".shp"
    buffer_distance = "10 Meters"
    line_side = "FULL"
    line_end_type = "ROUND"
    dissolve_option = "NONE"
    dissolve_field = ""
    method = "PLANAR"

    arcpy.Buffer_analysis(in_class, out_class, buffer_distance, line_side, line_end_type,
                      dissolve_option, dissolve_field, method)

#     bufferedSites.append(out_class)
#     print "Buffer created around site " + x + "!"
#
# print "Buffered site list: " + str(len(bufferedSites))
#
# #SelectByLocation - Intersect - Buffer > FetchLines
# for y in bufferedSites:

    #AD issue with your code was that m_output at this point was always C3...

    m_output = "fetchLines_" + x + ".shp"

    arcpy.MakeFeatureLayer_management(m_output,"m_output_1")
    arcpy.MakeFeatureLayer_management("Buffer_" + x + ".shp", "buffer_1")

    arcpy.SelectLayerByLocation_management("m_output_1", "INTERSECT", "buffer_1", "", "NEW_SELECTION", "NOT_INVERT")
    arcpy.CopyFeatures_management("m_output_1", "fetchLines_" + x + "_36Lines.shp")

    # Add geometry attribute to calculate length of fetch lines
    in_geo = "fetchLines_" + x + "_36Lines.shp"
    properties = "LENGTH"
    length_unit = ""
    area_unit = ""
    coordinate_system = ""

    arcpy.AddGeometryAttributes_management(in_geo, properties, length_unit, area_unit, coordinate_system)
    print "Shapefile containing all 36 lines for " + x + " created successfully!"

    in_table = in_geo
    out_table = "stats_table" + x + ".dbf"
    stat_fields = [['LENGTH', 'SUM'], ['LENGTH', 'STD']]

    arcpy.Statistics_analysis(in_table, out_table, stat_fields)
    finalStatsList.append(out_table)

    # I can't get any of the other statistics tables to display results, just the final one (C3). I know this is
    # because I must keep overwriting the previous table, but I don't know how to fix it and I've been at this for
    # long enough. Appreciate the help!
print len(finalStatsList)
print "Producing summary statistics"

arcpy.Merge_management(finalStatsList, "outputStats.dbf")

for i in finalStatsList:
    print i
    with arcpy.da.SearchCursor(i, ['FREQUENCY','SUM_LENGTH','STD_LENGTH']) as cursor:
        for row in cursor:
            print row

