import arcpy
import pythonaddins

class ButtonClass3(object):
    """Implementation for AddIns_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        # Get the current map document and the first data frame.
        mxd = arcpy.mapping.MapDocument('current')
        df = arcpy.mapping.ListDataFrames(mxd)[0]
        # Call the zoomToSelectedFeatures() method of the data frame class
        df.zoomToSelectedFeatures()