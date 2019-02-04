########################################
# Author: Erika Kamptner
# Description: Reads raster properties (arcpy) for each deliverable and writes to a csv
# Date: 05/07/2018
########################################


import arcpy
import os
import csv
import xml.etree.ElementTree as ET

DEMs = input('Input list of DEM file paths: ')
# ex. [\path\to\file1, \path\to\file2]

for DEM in DEMs:
    inputDEM = DEM
    outputName = inputDEM.rsplit('\\', 1)[-1]
    
    outputDirectory = input('Output Directory: ')

    propertiesoutputFile = outputDirectory + 'properties_' + outputName + '.csv'
    metadataoutputFile = outputDirectory + 'metadata_' + outputName + '.csv'

    propertiesnames = ["name", "valueType", "minimum", "maximum", "top", "left", "right", "bottom", "cellsizeX", "cellsizeY",
                  "anyNoData"]

    metadatanames = ["name", "CRS type", "CRS", "CS Units", "PROJCSN", "PixelDepth", "Compression Type", "Format",
                  "Has Pyramids", "SourceType", "PixelType", "Time Begin", "Time End", "Purpose", "Abstract",
                  "Credit", "Supplemental Information", "Use Limitations", "Overview Measurement Desc",
                  "Overview Method Desc", "RMSE Desc", "RMSE Method Desc", "RMSE Val Type", "RMSE Val",
                  "NVA Desc", "NVA Method Desc", "NVA Val Type", "NVA Val",
                  "VVA Desc", "VVA Method Desc", "VVA Val Type", "VVA Val"]

    os.chdir(inputDEM)

    # create csvs and add header information
    with open(metadataoutputFile, "a", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=metadatanames)
        writer.writeheader()
        file.close()

    with open(propertiesoutputFile, "a", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=propertiesnames)
        writer.writeheader()
        file.close()

    # loop through metadata files
    for file in os.listdir(os.getcwd()):
         if file.endswith("tif.xml"):
             tree = ET.parse(file)

    # coordinate reference information
             for node in tree.findall('.//type'):
                 type = node.text

             for node in tree.findall('.//geogcsn'):
                 geogcsn = node.text

             for node in tree.findall('.//csUnits'):
                 csUnits = node.text

             for node in tree.findall('.//projcsn'):
                 projcsn = node.text

    #raster properties
             for node in tree.findall('.//PixelDepth'):
                 PixelDepth = node.text

             for node in tree.findall('.//CompressionType'):
                 CompressionType = node.text

             for node in tree.findall('.//Format'):
                 format = node.text

             for node in tree.findall('.//HasPyramids'):
                 HasPyramids = node.text

             for node in tree.findall('.//SourceType'):
                 SourceType = node.text

             for node in tree.findall('.//PixelType'):
                 PixelType = node.text

    # time of data capture
             for node in tree.findall('.//tmBegin'):
                 tmBegin = node.text

             for node in tree.findall('.//tmEnd'):
                 tmEnd = node.text

    # metadata (descriptions)
             for node in tree.findall('.//idPurp'):
                 idPurp = node.text

             for node in tree.findall('.//idAbs'):
                 idAbs = node.text

             for node in tree.findall('.//idCredit'):
                 idCredit = node.text

             for node in tree.findall('.//suppInfo'):
                 suppInfo = node.text

             for node in tree.findall('.//useLimit'):
                 useLimit = node.text

            #dqInfo
             for node in tree.findall('.//dqInfo/report[1]/measDesc'):
                 omeasDesc = node.text

             for node in tree.findall('.//dqInfo/report[1]/evalMethDesc'):
                 oevalMethDesc = node.text

             for node in tree.findall('.//dqInfo/report[2]/measDesc'):
                 RMSEmeasDesc = node.text

             for node in tree.findall('.//dqInfo/report[2]/evalMethDesc'):
                 RMSEevalMethDesc = node.text

             for node in tree.findall('.//dqInfo/report[2]//quanValType'):
                 RMSEquanValType = node.text

             for node in tree.findall('.//dqInfo/report[2]//quanVal'):
                 RMSEquanVal = node.text

             for node in tree.findall('.//dqInfo/report[3]/measDesc'):
                 NVAmeasDesc = node.text

             for node in tree.findall('.//dqInfo/report[3]/evalMethDesc'):
                 NVAevalMethDesc = node.text

             for node in tree.findall('.//dqInfo/report[3]//quanValType'):
                 NVAquanValType = node.text

             for node in tree.findall('.//dqInfo/report[3]//quanVal'):
                 NVAquanVal = node.text

             for node in tree.findall('.//dqInfo/report[4]/measDesc'):
                 VVAmeasDesc = node.text

             for node in tree.findall('.//dqInfo/report[4]/evalMethDesc'):
                 VVAevalMethDesc = node.text

             for node in tree.findall('.//dqInfo/report[4]//quanValType'):
                 VVAquanValType = node.text

             for node in tree.findall('.//dqInfo/report[4]//quanVal'):
                 VVAquanVal = node.text

             # new fields
             # distinfo
             for node in tree.findall('.//distributor/distorCont/rpIndName'):
                 rpIndName = node.text

             for node in tree.findall('.//distributor/distorCont/rpOrgName'):
                 rpOrgName = node.text

             for node in tree.findall('.//rpCntInfo/cntAddress/delPoint'):
                 delPoint = node.text

             for node in tree.findall('.//rpCntInfo/cntAddress/emailAdd'):
                 emailAdd = node.text

             for node in tree.findall('.//cntPhone/voiceNum'):
                 voiceNum = node.text

             # dataIdInfo
             for node in tree.findall('.//dataIdInfo/themeKeys/keyword'):
                 themeKeys = node.text

             for node in tree.findall('.//dataIdInfo/placeKeys/keyword'):
                 placeKeys = node.text

             for node in tree.findall('.//rpCntInfo/cntAddress/delPoint'):
                 delPoint = node.text

             for node in tree.findall('.//rpCntInfo/cntAddress/emailAdd'):
                 emailAdd = node.text

             for node in tree.findall('.//cntPhone/voiceNum'):
                 voiceNum = node.text

             items = [file, type, geogcsn, csUnits, projcsn, PixelDepth, CompressionType, format, HasPyramids, SourceType,
                      PixelType, tmBegin, tmEnd, idPurp, idAbs, idCredit, suppInfo, useLimit, omeasDesc, oevalMethDesc,
                      RMSEmeasDesc, RMSEevalMethDesc, RMSEquanValType, RMSEquanVal, NVAmeasDesc, NVAevalMethDesc,
                      NVAquanValType, NVAquanVal, VVAmeasDesc, VVAevalMethDesc, VVAquanValType, VVAquanVal]

             with open(metadataoutputFile, "a", newline='') as file:
                 writer = csv.writer(file, delimiter=",", dialect="excel", quotechar='"', quoting=csv.QUOTE_ALL)
                 writer.writerow(items)
                 file.close()

    # loop through raster files
    for file in os.listdir(os.getcwd()):
         if file.endswith(".tif"):
                rasterName = file.lower()
                valueType = arcpy.GetRasterProperties_management(rasterName, "VALUETYPE")
                minimum = arcpy.GetRasterProperties_management(rasterName, "MINIMUM")
                maximum = arcpy.GetRasterProperties_management(rasterName, "MAXIMUM")
                top = arcpy.GetRasterProperties_management(rasterName, "TOP")
                left = arcpy.GetRasterProperties_management(rasterName, "LEFT")
                right = arcpy.GetRasterProperties_management(rasterName, "RIGHT")
                bottom = arcpy.GetRasterProperties_management(rasterName, "BOTTOM")
                cellsizeX = arcpy.GetRasterProperties_management(rasterName, "CELLSIZEX")
                cellsizeY = arcpy.GetRasterProperties_management(rasterName, "CELLSIZEY")
                # anyNoData = arcpy.GetRasterProperties_management(rasterName, "ANYNODATA")

                items = [rasterName, valueType, minimum, maximum, top, left, right, bottom, cellsizeX, cellsizeY]

                with open(propertiesoutputFile, "a", newline='') as file:
                    writer = csv.writer(file, delimiter=",", dialect="excel", quotechar='"', quoting=csv.QUOTE_ALL)
                    writer.writerow(items)
                    file.close()
         else:
             continue

    print("CSV with Raster properties is located here: " + propertiesoutputFile)
    print("CSV with Raster metadata is located here: " + metadataoutputFile)

print("Done")
