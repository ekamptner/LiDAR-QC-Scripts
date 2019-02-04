# LiDAR QC Scripts

This repository includes python scripts used to automate QC tasks for the 2017 NYC LiDAR project carried out by the Department of Information Technology and Telecommunication.

The scripts in this repo were used as follows:

| Script | Use | 
| --- | --- |
| LasInfo.py | Runs LasInfo tool and writes output to single CSV for all LAS files. Requires LasTools installation.
| UnzipLAZ.py | Runs LasTools to unzip compressed LAZ files to LAS format. Requires LasTools installation. 
| rasterDifferences.py| Utilizes ArcGIS geoprcessing tools to perform raster calculations. Was used to help identify any extreme elevation difference between models. Writes output to difference shapefile. Requires arcpy. 
| rasterProperty.py | Utilizes ArcGIS geoprcessing tools to read attributes on rasters. Writes output to single CSV. Requires arcpy.
| createSceneLayerPk.py | Used to create scene layer package for LAZ point clouds. 
