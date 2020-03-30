# Task 1 - Use what you have learned to process the Landsat files provided, this time, you know you are
# interested in the NVDI index which will use Bands 4 (red, aka vis) and 5 (near-infrared, aka nir) from the
# Landsat 8 imagery. Data provided are monthly (a couple are missing due to cloud coverage) during the
# year 2015 for the State of RI.

# Before you start, here is a suggested workflow:

# 1) Extract the Step_3_data.zip file into a known location.
# 2) For each month provided, you want to calculate the NVDI, using the equation: nvdi = (nir - vis) / (nir + vis)
# https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index. Consider using the Raster Calculator Tool
# in ArcMap and using "Copy as Python Snippet" for the first calculation.

# The only rule is, you should run your script once, and generate the NVDI for ALL MONTHS provided. As part of your
# code submission, you should also provide a visualization document (e.g. an ArcMap layout), showing the patterns for
# an area of RI that you find interesting.

import os
import arcpy

arcpy.CheckOutExtension("Spatial")
listMonths = ["02", "04", "05", "07", "10", "11"]
outputDirectory = r"E:\Python Class\Class_6_Files\Step_3_data_lfs\NVDI_Outputs"
if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)

for month in listMonths:
    arcpy.env.workspace = r"E:\Python Class\Class_6_Files\Step_3_data_lfs\2015" + month
    print "Extracting Bands 4 and 5 from folder 2015" + month
    bandFour = arcpy.ListRasters("*", "TIF")
    bandFour = [x for x in bandFour if "B4" in x]
    print "The file for Band 4 is " + str(bandFour) + "."
    bandFive = arcpy.ListRasters("*", "TIF")
    bandFive = [x for x in bandFive if "B5" in x]
    print "The file for Band 5 is " + str(bandFive) + "."
    arcpy.gp.RasterCalculator_sa('Float("' + bandFive[0] + '"-"' + bandFour[0] + '") / Float("' + bandFive[0] + '"+"' + bandFour[0] + '")',
                                 os.path.join(outputDirectory, "NVDI_2015" + month + ".tif"))
    if month == "02":
        print "Finishing NDVI Composite for February 2015." + "\n"
    if month == "04":
        print "Finishing NDVI Composite for April 2015." + "\n"
    if month == "05":
        print "Finishing NDVI Composite for May 2015." + "\n"
    if month == "07":
        print "Finishing NDVI Composite for July 2015." + "\n"
    if month == "10":
        print "Finishing NDVI Composite for October 2015." + "\n"
    if month == "11":
        print "Finishing NDVI Composite for November 2015." + "\n"
