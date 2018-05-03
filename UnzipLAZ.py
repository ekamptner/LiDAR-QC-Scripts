# ---------------------------------------------------------------------------
# UnzipLAS.py
# Created on: 2017-08-15
# Description: Unzips LAZ files and generates ESRI stat files
# ---------------------------------------------------------------------------

# Import modules
import os
import arcpy
from arcpy import env
import subprocess

arcpy.CheckOutExtension("3D")

# Set up environment
env.workspace = "T:\GIS\Projects\LiDAR\Project\dev"
arcpy.env.overwriteOutput = True

# Input variables:
lazFolder = input('Enter LAZ folder directory: ')
lasFolder = input('Enter LAS folder directory: ')
qcName = input('Enter QC name: ')

info = "statistics\Info_" + qcName + ".shp"
lasDataset = "lasDataset\lasDataset_" + qcName + ".lasd"
lasStats = "statistics\lasStats_" + qcName + ".txt"
projection = "PROJCS['NAD_1983_StatePlane_New_York_Long_Island_FIPS_3104_Feet',GEOGCS['GCS_North_American_1983'," \
             "DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0]," \
             "UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic']," \
             "PARAMETER['False_Easting',984250.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-74.0]," \
             "PARAMETER['Standard_Parallel_1',40.66666666666666],PARAMETER['Standard_Parallel_2',41.03333333333333]," \
             "PARAMETER['Latitude_Of_Origin',40.16666666666666],UNIT['Foot_US',0.3048006096012192]]"

# Run LASZIP
os.chdir(lazFolder)
print("Start: Unzip LAZ")
subprocess.call("T:/GIS/Projects/LiDAR/Project/tools/laszip *.laz")
print("Complete: Unzip LAZ")

# Make LAS Directory and move LAS files
print("Start: Make directory")
subprocess.call(["mkdir", lasFolder])
print("Complete: Created " + lasFolder)
call = "mv " + '"{}"'.format(lazFolder) + "/*.las " + '"{}"'.format(lasFolder)
subprocess.call(call)
print("Complete: LAS files moved to " + lasFolder)

# Point File Information
print("Start: Point File Information")
arcpy.PointFileInformation_3d(lasFolder, info, "LAS", ".las", projection, "NO_RECURSION", "EXTRUSION", "DECIMAL_POINT", "NO_SUMMARIZE", "LAS_SPACING")
print("Complete: Point File Information")

# Create LAS Dataset
print("Start: Create LAS Dataset")
arcpy.CreateLasDataset_management(lasFolder, lasDataset, "NO_RECURSION", "", projection, "COMPUTE_STATS", "RELATIVE_PATHS")
print("Complete: Create LAS Dataset")

# LAS Statistics
arcpy.LasDatasetStatistics_management(lasDataset, "SKIP_EXISTING_STATS", lasStats, "LAS_FILES", "COMMA", "DECIMAL_POINT")

arcpy.CheckInExtension("3D")
print("Job Complete")