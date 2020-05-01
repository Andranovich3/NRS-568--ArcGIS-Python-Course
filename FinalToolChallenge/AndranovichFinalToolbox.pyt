# For this final challenge in NRS 568, I created a Python toolbox to be executed in ArcMap. This style of toolbox is much more
# user friendly than a "traditional" style of toolbox because you can create the toolbox and all its parameters entirely in
# a Python processing program, completely removing the need for a user to interact with a GUI in ArcMap and change anything.
# This toolbox will contain _____ (_) tools, including ____,____,____, and ____. Example data to practice with is provided
# in the accompanying .zip file.

import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "AndranovichFinalToolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = None
        return params

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
        return
