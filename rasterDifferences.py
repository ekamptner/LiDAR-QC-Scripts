import arcpy, os
from arcpy.sa import *

arcpy.CheckOutExtension("Spatial")

# set folder variables
demFolder1 = input('DEM 1 for comparison: ')
demFolder2 = input('DEM 2 for comparison: ')
outputdiffs = input('Output difference raster: ')
outputvectors = input('Output difference vector (shp): ')

# get raster lists
arcpy.env.workspace = demFolder1
demList1 = sorted(arcpy.ListRasters())

arcpy.env.workspace = demFolder2
demList2 = sorted(arcpy.ListRasters())

print("Lists collected")

arcpy.env.workspace = outputdiffs

# create raster differences
for (a, b) in zip(demList1, demList2):

     dem1 = arcpy.sa.Raster(os.path.join(demFolder1, a))
     dem2 = arcpy.sa.Raster(os.path.join(demFolder2, b))
     print("Raster Calculation for: ", dem1, dem2)

     outDifference = abs(dem1 - dem2)

     ouputRasterFinal = outDifference.save(os.path.join(outputdiffs, a.replace(".tif", "_") + b))

     # create vector of raster
     # first, create simplified boolean vector
     rasterDiffs = Con(outDifference & outDifference, 1)

     vectorDiffs = arcpy.RasterToPolygon_conversion(rasterDiffs,
                                                     os.path.join(outputvectors, a.replace(".tif", "_") +
                                                                  b.replace(".tif", "") + ".shp"),
                                                     "NO_SIMPLIFY", "VALUE")

arcpy.CheckInExtension("Spatial")
