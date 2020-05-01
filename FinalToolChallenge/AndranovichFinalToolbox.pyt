# For this final challenge in NRS 568, I created a Python toolbox to be executed in ArcMap. This style of toolbox is much more
# user friendly than a "traditional" style of toolbox because you can create the toolbox and all its parameters entirely in
# a Python processing program, completely removing the need for a user to interact with a GUI in ArcMap and change anything.
# This toolbox will contain three (3) tools, including a List Raster tool, a 10-meter Buffer tool, and an NDVI Calculator.
# Example data to practice with is provided in the accompanying .zip file.

import arcpy

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the .pyt file)."""
        self.label = "AndranovichFinalToolbox"
        self.alias = ""
        # List of tool classes associated with this toolbox
        self.tools = [ListRasters, Buffer10meters, Produce_NDVI]


class ListRasters(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "List Rasters Tool"
        self.description = "This tool will search a desired folder and list all raster files of a specified type."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        parameters = []
        input_line = arcpy.Parameter(name="input_line",
                                     displayName="Enter the desired folder:",
                                     datatype="DEFolder",
                                     parameterType="Required",
                                     direction="Input")
        parameters.append(input_line)
        file_type = arcpy.Parameter(name="file_type",
                                    displayName="Enter the raster file extension:",
                                    datatype="GPString",
                                    parameterType="Required",
                                    direction="Input")
        parameters.append(file_type)
        return parameters

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        input_line = parameters[0].valueAsText
        file_type = parameters[1].valueAsText

        arcpy.env.workspace = input_line
        rasterList = arcpy.ListRasters("*", file_type)
        rasterList = [x for x in rasterList if "_BQA.tif" not in x]
        arcpy.AddMessage("The files ending in " + file_type + " are " + str(rasterList) + ".")
        arcpy.AddMessage("The number of " + file_type + " files in that folder is " + str(len(rasterList)) + ".")
        return


class Buffer10meters(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Buffer 10-meters Tool"
        self.description = "This tool will take up to three feature class objects and apply a 10-meter buffer."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        parameters = []
        shp1 = arcpy.Parameter(name="shp1",
                               displayName="Enter your first shapefile:",
                               datatype="DEFeatureClass",
                               parameterType="Required",
                               direction="Input")
        parameters.append(shp1)
        shp1_output = arcpy.Parameter(name="shp1_output",
                                      displayName="Enter the output destination for the first buffered shapefile:",
                                      datatype="DEFeatureClass",
                                      parameterType="Required",
                                      direction="Output")
        parameters.append(shp1_output)
        shp2 = arcpy.Parameter(name="shp2",
                               displayName="Enter your second shapefile, if needed:",
                               datatype="DEFeatureClass",
                               parameterType="Optional",
                               direction="Input")
        parameters.append(shp2)
        shp2_output = arcpy.Parameter(name="shp2_output",
                                      displayName="Enter the output destination for the second buffered shapefile:",
                                      datatype="DEFeatureClass",
                                      parameterType="Optional",
                                      direction="Output")
        parameters.append(shp2_output)
        shp3 = arcpy.Parameter(name="shp3",
                               displayName="Enter your third shapefile, if needed:",
                               datatype="DEFeatureClass",
                               parameterType="Optional",
                               direction="Input")
        parameters.append(shp3)
        shp3_output = arcpy.Parameter(name="shp3_output",
                                      displayName="Enter the output destination for the third buffered shapefile:",
                                      datatype="DEFeatureClass",
                                      parameterType="Optional",
                                      direction="Output")
        parameters.append(shp3_output)
        return parameters

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        shp1 = parameters[0].valueAsText
        shp1_output = parameters[1].valueAsText
        shp2 = parameters[2].valueAsText
        shp2_output = parameters[3].valueAsText
        shp3 = parameters[4].valueAsText
        shp3_output = parameters[5].valueAsText

        inputFeatures = shp1
        outputFeatures = shp1_output
        distance = "10 meters"
        sideType = "FULL"
        lineEndType = "ROUND"
        dissolveOption = "NONE"
        dissolveField = "#"
        method = "PLANAR"
        arcpy.Buffer_analysis(inputFeatures, outputFeatures, distance, sideType,
                              lineEndType, dissolveOption, dissolveField, method)

        if len(parameters) > 2:
            inputFeatures = shp2
            outputFeatures = shp2_output
            distance = "10 meters"
            sideType = "FULL"
            lineEndType = "ROUND"
            dissolveOption = "NONE"
            dissolveField = "#"
            method = "PLANAR"
            arcpy.Buffer_analysis(inputFeatures, outputFeatures, distance, sideType,
                                  lineEndType, dissolveOption, dissolveField, method)

        if len(parameters) > 4:
            inputFeatures = shp3
            outputFeatures = shp3_output
            distance = "10 meters"
            sideType = "FULL"
            lineEndType = "ROUND"
            dissolveOption = "NONE"
            dissolveField = "#"
            method = "PLANAR"
            arcpy.Buffer_analysis(inputFeatures, outputFeatures, distance, sideType,
                                  lineEndType, dissolveOption, dissolveField, method)
        arcpy.AddMessage("Buffering of files completed!")
        return


class Produce_NDVI(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "NDVI Calculation Tool"
        self.description = "This tool will take in two .TIF bands and produce an NDVI output from them."
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        parameters = []
        band_4 = arcpy.Parameter(name="band_4",
                                 displayName="Enter location for Band 4 of satellite imagery:",
                                 datatype="GPRasterLayer",
                                 parameterType="Required",
                                 direction="Input")
        parameters.append(band_4)
        band_5 = arcpy.Parameter(name="band_5",
                                 displayName="Enter location for Band 5 of satellite imagery:",
                                 datatype="GPRasterLayer",
                                 parameterType="Required",
                                 direction="Input")
        parameters.append(band_5)
        ndvi_output = arcpy.Parameter(name="ndvi_output",
                                      displayName="Enter a destination for the NDVI output:",
                                      datatype="GPRasterLayer",
                                      parameterType="Required",
                                      direction="Output")
        parameters.append(ndvi_output)
        return parameters

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        band_4 = parameters[0].valueAsText
        band_5 = parameters[1].valueAsText
        ndvi_output = parameters[2].valueAsText

        arcpy.gp.RasterCalculator_sa('Float("' + band_5 + '"-"' + band_4 + '") / Float("' + band_5 + '"+"' + band_4 + '")',
        ndvi_output)
        arcpy.AddMessage("NDVI calculations completed!")
        return
