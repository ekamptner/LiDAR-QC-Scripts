# ---------------------------------------------------------------------------
# ParseLASInfo.py
# Created on: 2017-07-28
# Description: Parses LASInfo txt files into csv
# ---------------------------------------------------------------------------

# Modules
import csv
import os
import subprocess

# Local variables
inputFolder = input('Enter LAS folder directory: ')
outputFile = "T:\GIS\Projects\LiDAR\Project\QC\lasInfo\LasInfo_Citywide.csv"
statFolder = "T:\GIS\Projects\LiDAR\Project\QC\lasInfo"

os.chdir(inputFolder)
subprocess.call("T:/GIS/Projects/LiDAR/Project/tools/lasinfo -i *.las -otxt -cd")
call = "mv " + '"{}"'.format(inputFolder) + "/*.txt " + '"{}"'.format(statFolder)
subprocess.call(call)

os.chdir(statFolder)
for file in os.listdir(os.getcwd()):
    if file.endswith(".txt"):
        f = open(os.fsdecode(file))
        lines = f.readlines()
        filename = statFolder + "\\" + file

        # Header info
        tile = f.name.split('.')[0]
        version = lines[5][30:]
        pointFormat = lines[12][30:]
        minxyz = (lines[18][30:]).split(' ')
        minx = minxyz[0]
        miny = minxyz[1]
        minz = minxyz[2]
        maxxyz = (lines[19][30:]).split(' ')
        maxx = maxxyz[0]
        maxy = maxxyz[1]
        maxz = maxxyz[2]
        pointsByReturn = lines[24][39:]

        coord = lines[32][4:]
        horizontalcoord = coord[18:45]
        verticalcoord = coord[48:68]
        recordID = lines[28][23:]

        unclassified = ""
        ground = ""
        noise = ""
        water = ""
        rail = ""
        bridgeDeck = ""
        belowGround = ""
        subwayStair = ""
        withheld = ""
        overlap = ""

        # Number of returns based on type
        first = lines[52][32:]
        intermediate = lines[53][32:]
        last = lines[54][32:]
        single = lines[55][32:]

        coveredArea = lines[56][40:].split('/')[0]
        pointDensityAll = lines[57][27:-35]
        pointDensityLast = lines[57][42:-20]
        pointSpacingAll = lines[58][27:-26]
        pointSpacingLast = lines[58][42:-11]

        with open(filename) as myFile:
            for num, line in enumerate(myFile, 1):
                if '(1)' in line:
                    unclassified = line[:17].strip()
        with open(filename) as myFile:
            for num, line in enumerate(myFile, 1):
                if '(2)' in line:
                    ground = line[:17].strip()
        with open(filename) as myFile:
            for num, line in enumerate(myFile, 1):
                if '(7)' in line:
                    noise = line[:17].strip()
        with open(filename) as myFile:
            for num, line in enumerate(myFile, 1):
                if '(9)' in line:
                    water = line[:17].strip()
        with open(filename) as myFile:
            for num, line in enumerate(myFile, 1):
                if '(10)' in line:
                    rail = line[:17].strip()
        with open(filename) as myFile:
            for num, line in enumerate(myFile, 1):
                if '(17)' in line:
                    bridgeDeck = line[:17].strip()
        with open(filename) as myFile:
            for num, line in enumerate(myFile, 1):
                if '(20)' in line:
                    belowGround = line[:17].strip()
        with open(filename) as myFile:
            for num, line in enumerate(myFile, 1):
                if '(25)' in line:
                    subwayStair = line[:17].strip()
        with open(filename) as myFile:
            for num, line in enumerate(myFile, 1):
                if 'withheld' in line:
                    withheld = line[27:].strip()
        with open(filename) as myFile:
            for num, line in enumerate(myFile, 1):
                if 'overlap' in line:
                    overlap = line[34:].strip()

        row = (tile, recordID, version, pointFormat, horizontalcoord, verticalcoord, minx, miny, minz, maxx, maxy, maxz,
               pointsByReturn, first, intermediate, last, single, unclassified, ground, noise, rail, bridgeDeck,
               belowGround, subwayStair, withheld, overlap, coveredArea, pointSpacingAll, pointSpacingLast,
               pointDensityAll, pointDensityLast)

        # Open Output File
        with open(outputFile, "a", newline='') as file:
            writer = csv.writer(file, delimiter=",", dialect="excel", quotechar='"', quoting=csv.QUOTE_ALL)
            writer.writerow(row)
            file.close()
    else:
        continue

