import arcpy

arcpy.env.workspace = input('Workspace to write to: ')
lazdata = input('LAZ Directory: ')
outputname = input('Output Filename: ')

arcpy.management.CreatePointCloudSceneLayerPackage(lazdata,
                                                   outputname,
                                                    arcpy.SpatialReference(2263), # output coord
                                                   'NAD_1983_To_WGS_1984_New_York_31',# transform
                                                   ["INTENSITY", "CLASS_CODE", "RETURNS"], #attributes
                                                   0, 0.1, 0.1, 
                                                   arcpy.SpatialReference(2263), #input coord
                                                   "1.X") #version

print(arcpy.GetMessages(0))
