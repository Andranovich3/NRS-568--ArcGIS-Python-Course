For this final challenge in NRS 568, I created a Python toolbox to be executed in ArcMap. This style of toolbox is much more

user friendly than a "traditional" style of toolbox because you can create the toolbox and all its parameters entirely in

a Python processing program, completely removing the need for a user to interact with a GUI in ArcMap and change anything.

This toolbox will contain three (3) tools, including a List Raster tool, a 10-meter Buffer tool, and an NDVI Calculator.

Example data to practice with is provided in the accompanying .zip file.

Tool Descriptions:

Tool #1 - Two inputs: a folder location to search and a file extension type. Searches the folder input for the file extension type, then prints out the files that match and prints a count total.

Tool #2 - (Min) Two inputs, (Max) six inputs: takes in a feature class object (point, multi-point, polyline, polygon) and an output location for the produced file. The tool then adds a 10-meter buffer. The tool can buffer up to three inputs at one time.

Tool #3 - Three inputs: two satellite images and an output location. The two satellite images MUST be a Near-infrared band and a Red Visibile Light band in order for the calculation to produce accurately. I could not get a .zip file containing example data for this tool to upload (file size too large).
