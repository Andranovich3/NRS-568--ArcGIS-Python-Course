import arcpy
import csv
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r'E:\Python Class\Class_5_Files'

# Turns combined data set sheet into a CSV

data = []
with open("CombinedData.csv") as combinedData_csv:
    csv_reader = csv.reader(combinedData_csv, delimiter=',')
    line_count = 0

    # Searches row[0] (scientificName) for species name
    for row in csv_reader:
        if line_count != 0:
            if row[0] not in data:
                data.append(row[0])  # Finds two new entries as expected
        if line_count == 0:
            print "Column names are: " + str(row)  # Prints column names
            line_count += 1
        line_count += 1

print data  # Prints data list, which has ['Halichoerus grypus', 'Pagophilus groenlandicus']
print("Processed " + str(line_count) + " lines.")

# Start a loop to process the CSV twice, once for each species

for i in data:
    with open("CombinedData.csv") as combinedData_csv:
        csv_reader = csv.reader(combinedData_csv, delimiter=',')

        file = open(i[0:2] + ".csv", "w")  # Creates a file based on the scienctificName 1st + 2nd letter
        file.write("scientificName,decimalLongitude,decimalLatitude\n")  # Writes in our column names
        for row in csv_reader:
            if row[0] == i:  # Loop for extracting all the data lines
                string = ",".join(row)  # Creates an extracted line of data
                string = string + "\n"  # Adds a new line command to start the next line of data
                file.write(string)  # Actually prints the line of data in the CSV file
        file.close() # Essential to avoid an error about unreadable column names

    # Converts the newly split CSV into a Shapefile

    in_Table = i[0:2] + ".csv"  # Name of the newly split CSV
    x_coords = "decimalLongitude"
    y_coords = "decimalLatitude"
    out_Layer = "CombinedData"
    saved_Layer = i[0:2] + ".shp"  # Name of the new Shapefile

    spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984

    lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, "")
    arcpy.CopyFeatures_management(lyr, saved_Layer)

    # Save to a layer file
    arcpy.CopyFeatures_management(lyr, saved_Layer)
    if arcpy.Exists(saved_Layer):
        print "Created file successfully!"

    # Extact the Extent -> the XMin, XMax, YMin, YMax of the generated shapefile.

    desc = arcpy.Describe(saved_Layer)
    XMin = desc.extent.XMin
    XMax = desc.extent.XMax
    YMin = desc.extent.YMin
    YMax = desc.extent.YMax

    # Creates a fishnet from newly created Shapefile

    arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)

    outFeatureClass = i[0:2] + "2.shp"  # Name of output fishnet

    # Set the origin of the fishnet

    originCoordinate = str(XMin) + " " + str(YMin)  # Left bottom of our point data
    yAxisCoordinate = str(XMin) + " " + str(YMin + 1.0)  # This sets the orientation on the y-axis, so we head north
    cellSizeWidth = "0.25"
    cellSizeHeight = "0.25"
    numRows = ""  # Leave blank, as we have set cellSize
    numColumns = ""  # Leave blank, as we have set cellSize
    oppositeCorner = str(XMax) + " " + str(YMax)  # i.e. max x and max y coordinate
    labels = "NO_LABELS"
    templateExtent = "#"  # No need to use, as we have set yAxisCoordinate and oppositeCorner
    geometryType = "POLYGON"  # Create a polygon, could be POLYLINE

    arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                                   cellSizeWidth, cellSizeHeight, numRows, numColumns,
                                   oppositeCorner, labels, templateExtent, geometryType)

    # Check to see if worked
    if arcpy.Exists(outFeatureClass):
        print "Created Fishnet file successfully!"

    # Create the Heatmap by spatially joining the Shapefile and the Fishnet

    target_features = i[0:2] + "2.shp"
    join_features = i[0:2] + ".shp"
    out_feature_class = i[0:2] + "heatmap.shp"
    join_operation = "JOIN_ONE_TO_ONE"
    join_type = "KEEP_ALL"
    field_mapping = ""
    match_option = "INTERSECT"
    search_radius = ""
    distance_field_name = ""

    arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                               join_operation, join_type, field_mapping, match_option,
                               search_radius, distance_field_name)

    # Check to see if worked
    if arcpy.Exists(out_feature_class):
        print "Created Heatmap file successfully!"
