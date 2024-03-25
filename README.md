# Awesome-EarthObservation-Code

A curated list of awesome tools, tutorials, code, helpful projects, links, stuff about Earth Observation and Geospatial stuff!

<p align="center">
  <img width="300" height="300" src="https://geogerservices.files.wordpress.com/2018/06/scenefromabovepodcast.jpg?w=300&h=300">
</p>

The [#scenefromabove podcast](https://scenefromabove.podbean.com/) aimed to be a mix of news, opinion, discussion and interviews. I am no longer involved in the podcast, however it is still going<br>

## Latest news

I have written a blog post about how this repo came into being. It includes a video of a talk I gave about it AND a podcast episode devoted to it. http://www.acgeospatial.co.uk/awesome-earthobservation-code/

Please note that this is <b>not</b> offically an awesome list.

<b> Update March 2024</b> Added a load of STAC links and some opendatacube ones. I accept PR's and you get a mention in the contributors file.

<b> A note of caution </b> During the QC of links I note that the vast majority are 18 + months old or considerbly older. Some repos are retired and still visible, some code is > 10 years old. Tread carefully.

Annotations are based on the headers - and where available - on the github accounts

<div align="center">



</div>


# Contents

| [<b>Earth Observation introduction</b>](#earth-observation-introduction) |<br>

| [Open EO](#open-eo) | [remotesensing.info](#remote-sensinginfo) | [Python processing](#python-processing-of-optical-imagery-non-deep-learning) | [Resources for R](#resources-for-r) | [Languages other than Python and R](#languages-other-than-python-and-r) | [Training and Learning](#training-and-learning) | [Deep Learning & Machine Learning](#deep-learning-and-machine-learning) | [GDAL of course](#gdal-of-course) | [Earth Observation coding on YouTube](#earth-observation-coding-on-youtube) | [Google Earth Engine](#earth-engine) | [Open Data Cube](#open-data-cube) | [Planetary Computer](#planetary-computer) | [QGIS and Grass](#qgis-and-grass) | [Climate & Weather resources](#climate-and-weather-based-resources) | [DEM projects](#dem-projects) | [SAR](#sar) | [LiDAR](#lidar) | [GEDI](#gedi) | [InSAR](#insar) | [Landuse](#landuse) | [Visualisation](#visualisation) | [EO code Competitions](#eo-code-competitions) | [ARD links](#ard-links) | [Useful EO code based twitter accounts](#useful-eo-code-based-twitter-accounts) | [List of Great GitHub accounts](#great-github-accounts) | [EO Geospatial companies or orgs making big contributions](#eo-geospatial-companies-or-orgs-making-big-contributions) |

| [Cloud Native Geospatial](#cloud-native-geospatial) | [STAC](#stac) | [COG](#cog)

These sections are non EO code specific, but included to be relevant <br>
| [Interesting Non EO parts Python](#interesting-non-eo-parts-python) | [Interesting Non EO parts other languages](#interesting-non-eo-parts-other-languages) | [Data](#data) | [A footnote on awesome](#a-footnote-on-awesome)

#### Start Here

## Earth Observation Introduction

If you are not familiar with Earth Observation then these links may help set context before you start using data. I didn't initially aim at including links like these but if you are not familiar with Earth Observation then some good resources to get you going may help prior to diving into code.

- [Earth Observation Text books](https://www.eoa.org.au/earth-observation-textbooks) - Earth Observation: Data, Processing and Applications is an Australian Earth Observation (EO) community undertaking to describe EO data, processing and applications in an Australian context and includes a wide range of local case studies to demonstrate Australia’s increasing usage of EO data.
- [ESA newcomers guide](https://business.esa.int/newcomers-earth-observation-guide) - The aim of this guide is to help non-experts in providing a starting point in the decision process for selecting an appropriate Earth Observation (EO) solution.
- [The state of satellites](https://landscape.satsummit.io/) - The satellite systems we use to capture, analyze, and distribute data about the Earth are improving every day, creating bold new opportunities for impact in global development.
- [Landsats Enduring Legacy](https://my.asprs.org/landsat) - pdf download over 600 pages of remote sensing!

You may also wish to navigate a search of the terms `satellite-imagery` and `earth-observation` to get the latest list of topics that have these terms in their headers

- [satellite-imagery](https://github.com/topics/satellite-imagery)
- [earth-observation](https://github.com/topics/earth-observation)

Two excellent videos (approx 20mins) about `Earth observation` 

[I Couldn't Find a Video Explaining Satellite Images, So I Made One](https://www.youtube.com/watch?v=xy5qR0cBFGs)

[How Radar Satellites See through Clouds (Synthetic Aperture Radar Explained)](https://www.youtube.com/watch?v=zMsCyEAOrh0)

Not sure the best place for data catalogs is but this is a good start if that interests you [Data Catalogs](https://github.com/opengeos/geospatial-data-catalogs)

## Open EO

OpenEO covers many of the bases, hard to know whether to break it into different categories, it has many components. At present I mention it here at the start only.<br>

- [Open EO](https://openeo.org/) - openEO develops an open API to connect `R`, `Python`, `JavaScript` and other clients to big Earth observation cloud back-ends in a simple and unified way.
- [openeo-processes](https://github.com/Open-EO/openeo-processes) - Interoperable processes for openEO's big Earth observation cloud processing [website](https://processes.openeo.org/)

## Remote Sensing.info

<b> All links have been changed - update your pointers Oct 2022 </b>

remotesening.info warrents its own section, the vast array of tools and processing software is incredible
[RemoteSensing](https://github.com/remotesensinginfo) - Short tutorials and reference to useful software tools for the acquisition and processing of remote sensed Earth Observation data
- [RSGISLib](http://rsgislib.org/rsgislib.html) - The Remote Sensing and GIS software library (RSGISLib) is a collection of tools for processing remote sensing and GIS datasets. The tools are accessed using `Python` bindings.
- [ARCSI](https://github.com/remotesensinginfo/arcsi) - Software to automate the production of optical analysis ready data (ARD) from Landsat, Sentinel-2 and others
- [eodatadown](https://github.com/remotesensinginfo/eodatadown) - The Earth Observation Data Downloader (EODataDown) is a tool for automatically downloading and processing EO data to an analysis ready data product. This software forms a core component of a monitoring system based on EO data.
- more to come..

## `Python` processing of optical imagery (non deep learning)

This section full of great code and projects related to processing optical satellite imagery with `Python` . This section is under review Sept 2020 and being split into further categories - please suggest groupings or re assignments if needed - the idea is to make the Python code examples here easier to find. Categories are highly subjective.

### Download

- [EODAG](https://eodag.readthedocs.io/en/latest/) - Command line tool and a plugin-oriented Python framework for searching, aggregating results and downloading remote sensed images while offering a unified API for data access regardless of the data provider.
- [Sedas API](https://github.com/SatelliteApplicationsCatapult/sedas_pyapi) - `Python` client library for the SeDAS API
- [esa_sentinel](https://github.com/jonas-eberle/esa_sentinel) - ESA Sentinel Search & Download API
- [get_modis](https://github.com/jgomezdans/get_modis) - Downloading MODIS data from the USGS repository `Python`
- [landsatexplore](https://github.com/yannforget/landsatxplore) - Search and download Landsat scenes from EarthExplorer. `Python`
- [pylandsat](https://github.com/yannforget/pylandsat) - Search, download, and preprocess Landsat imagery `Python`
- [Sentinel-download](https://github.com/olivierhagolle/Sentinel-download) - Automated download of Sentinel-2 L1C data from ESA (through wget) `Python`
- [sentinelsat](https://github.com/sentinelsat/sentinelsat) - Search and download Copernicus Sentinel satellite images [sentinelsat docs](https://sentinelsat.readthedocs.io/en/stable/) `Python`
- [LANDSAT-Download](https://github.com/olivierhagolle/LANDSAT-Download) - Automated download of LANDSAT data from USGS website
- [Landsat-Util](https://github.com/developmentseed/landsat-util) - A utility to search, download and process Landsat 8 satellite imagery `Python`
- [data-prep-scripts](https://lpdaac.usgs.gov/tools/data-prep-scripts/) - This collection of `R` and `Python` scripts can be used to download data and perform basic data processing functions such as georeferencing, reprojecting, converting, and reformatting data. All scripts are available for download from the LP DAAC User Resources [BitBucket Code Repository](https://git.earthdata.nasa.gov/projects/LPDUR).
- [Stream NASA data directly into Python objects](https://nbviewer.jupyter.org/gist/scottyhq/a1ddbb12f97764860160370229b19261) - Skip the download! Stream NASA data directly into Python objects from [blog post](https://medium.com/pangeo/intake-stac-nasa-4cd78d6246b7)
- [sat-extractor](https://github.com/FrontierDevelopmentLab/sat-extractor) - Extract Satellite Imagery from public constellations at scale `Python`

### Processing imagery - post processing

- [StarFM for Python](https://github.com/nmileva/starfm4py) - The STARFM fusion model for `Python` (image fusion)
- [Remote Sensing indicies calc](https://github.com/rander38/Remote-Sensing-Indices-Derivation-Tool) - Calculate spectral remote sensing indices from satellite imagery
- [EarthPy](https://github.com/earthlab/earthpy) - A package built to support working with spatial data using open source python. [docs](https://earthpy.readthedocs.io/en/latest/)
- [RasterFrames / pyrasterframes](https://github.com/locationtech/rasterframes) - brings together Earth-observation (EO) data access, cloud computing, and DataFrame-based data science. [docs](https://rasterframes.io/)
- [SIF tools](https://github.com/cfranken/SIF_tools) - some tools for accessing OCO-2 data
- [SIAC](https://github.com/MarcYin/SIAC) - A sensor invariant Atmospheric Correction (SIAC) [alg doc](http://www2.geog.ucl.ac.uk/~ucfafyi/Atmo_Cor/)
- [S2_TOA_TO_LAI](https://github.com/MarcYin/S2_TOA_TO_LAI) - From Sentinel 2 TOA reflectance to LAI
- [cresi](https://github.com/avanetten/cresi) - Road network extraction from satellite imagery, with speed and travel time estmates
- [6S_emulator](https://github.com/samsammurphy/6S_emulator) - Atmospheric correction in Python using a 6S emulator
- [bv](https://github.com/daleroberts/bv) - Quickly view satellite imagery, hyperspectral imagery, and machine learning image outputs directly in your iTerm2 terminal. `Python`
- [mapchete](https://github.com/ungarj/mapchete) - Tile-based geodata processing using rasterio & Fiona `Python`
- [unmixing](https://github.com/arthur-e/unmixing) - Interactive tools for spectral mixture analysis of multispectral raster data in `Python`
- [landsat and sentinel fusion](https://github.com/yannforget/landsat-sentinel-fusion) - Complementarity Between Sentinel-1 and Landsat 8 Imagery for Built-Up Mapping in Sub-Saharan Africa `Python`
- [Planet Movement](https://github.com/rhammell/planet-movement) - Find and process Planet image pairs to highlight object movement. `Python`

- [cedar-datacube](https://github.com/ceholden/cedar-datacube) - cedar - Create Earth engine Datacubes of Analytical Readiness `Python` [docs](https://ceholden.github.io/cedar-datacube/master/)
- [stems - Spatio-temporal Tools for Earth Monitoring Science](https://github.com/ceholden/stems) - Spatio-temporal Tools for Earth Monitoring Science `Python` [docs](https://ceholden.github.io/stems/master/)
- [ipyearth](https://github.com/davidbrochart/ipyearth) - An IPython Widget for Earth Maps `Python`
- [Python-for-remote-sensing](https://github.com/Seyed-Ali-Ahmadi/Python-for-Remote-Sensing) - `Python` codes for remote sensing applications will be uploaded. [blog](https://earthobserv.com/)
- [esda dissertation](https://github.com/Rabscuttler/esda-dissertation) - MSc Energy Systems & Data Analytics dissertation project notebooks - identifying solar PV from aerial imagery with computer vision `Python`
- [geff_notebooks](https://github.com/cvitolo/geff_notebooks) - Jupyter notebooks to post-process fire danger data using `Python`/`xarray`

- [river-width](https://github.com/redfoxgis/river-width) - Extracts water features from 4 band NAIP imagery and calculates river metrics. `Python`
- [get_river_width](https://github.com/briannapagan/get_river_width/blob/master/get_river_width.py) - Find the river width (and other properties) from a masked water image `Python`
- [extract_water](https://github.com/redfoxgis/extract_water/blob/master/extract_water.py) - Extract water from nIR imagery `Python`
- [pyresample](https://github.com/pytroll/pyresample) - Geospatial image resampling in `Python`
- [spatialist](https://github.com/johntruckenbrodt/spatialist) - A `Python` module for spatial data handling
- [CometTS](https://github.com/CosmiQ/CometTS) - Comet Time Series Toolset for working with a time-series of remote sensing imagery and user defined polygons
- [Telluric](https://github.com/satellogic/telluric) - telluric is a `Python` library to manage vector and raster geospatial data in an interactive and easy way
- [onearth](https://github.com/nasa-gibs/onearth) - High-performance web services for tiled raster imagery and vector tiles `Python`
- [geocube](https://github.com/corteva/geocube) - Tool to convert geopandas vector data into rasterized xarray data. `Python` [docs](https://corteva.github.io/geocube/stable/)
- [Opensource-OBIA_processing_chain](https://github.com/tgrippa/Opensource_OBIA_processing_chain) - An open-source semi-automated processing chain for urban OBIA classification. `Grass` `Python`
- [verde](https://github.com/fatiando/verde) - Processing and gridding spatial data using Green's functions
- [s2p](https://github.com/cmla/s2p) - Satellite Stereo Pipeline `Python`
- [xcube](https://github.com/dcs4cop/xcube) - xcube is a `Python` package for generating and exploiting data cubes powered by xarray, dask, and zarr
- [geonotebook](https://github.com/OpenGeoscience/geonotebook) - A Jupyter notebook extension for geospatial visualization and analysis `Python`
- [tatortot](https://github.com/GeoBigData/tatortot) - Prototype for a simple image annotation tool `Python`
- [tiletanic](https://github.com/DigitalGlobe/tiletanic) - `Python` library to support generalized geographic tiling schemes
- [Intro to Python GIS](https://automating-gis-processes.github.io) - Great free 3-day course by the University of Helsinki on GIS processing with Python
- [openaq-s5](https://github.com/JamesOConnor/openaq-s5) - Map openaq data onto Sentinel5P data using AWS lambda
- [vegetation health](https://github.com/tommylees112/vegetation_health) - Predicting vegetation health from precipitation and temperature
- [Satellite-Image-Analysis](https://github.com/MasterPhysicist/Satellite-Image-Analysis) - PlanetScope, Landsat-8 and Sentinel-2 Image analysis `Python` codes
- [felicette](https://github.com/plant99/felicette) - Satellite imagery for dummies. `Python`
- [CostalSat](https://github.com/kvos/CoastSat) - Global shoreline mapping tool from satellite imagery `Python`

- [Python-Remote-Sensing-Scripts](https://github.com/JavierLopatin/Python-Remote-Sensing-Scripts) - `Python` 3. X scripts for remote sensing processing
- [fc-up42](https://github.com/petescarth/fc-up42) - UP42 Block for Fractional Cover calculation from Sentinel 2 L2A Data `Python`
- [Opensource_OBIA_processing_chain](https://github.com/tgrippa/Opensource_OBIA_processing_chain) - An open-source semi-automated processing chain for urban OBIA classification.
- [nansat](https://github.com/nansencenter/nansat) - Scientist friendly Python toolbox for processing 2D satellite Earth observation data. `Python`[docs](https://nansat.readthedocs.io/en/latest/index.html)
- [nansat-lite](https://gitlab.com/jobel-open-source/nansat-lite) - nansat-lite is not a full nansat build for `Python` 3.5. Only bits of code from main classes, to start with. Eventually, if need it, more code will be added.
- [IEO](https://github.com/DrGuy/ieo) - Irish Earth Observation (IEO) remote sensing data processing Python module `Python`
- [IEOtools](https://github.com/DrGuy/IEOtools) - Tools for managing Earth observation data. Currently only supports Landsat imagery `Python`
- [pykic](https://github.com/EkicierNico/pykic) - 'Python' module for remote sensing and GIS domain (image/signal, vector, miscellaneous processing)
- [ukis-csmask](https://github.com/dlr-eoc/ukis-csmask) - masks clouds and cloud shadows in Sentinel-2, Landsat-8, Landsat-7 and Landsat-5 images `Python`
- [jeolib-pyjeo](https://github.com/ec-jrc/jeolib-pyjeo) - pyjeo is a library for image processing for geospatial data implemented in JRC Ispra. `Python`
- [pyrgis](https://github.com/PratyushTripathy/pyrsgis) - This repository cointains the source code of the 'pyrsgis' `Python` package. 
- [EOReader](https://github.com/sertit/eoreader) - Opensource `Python` library reading optical and SAR sensors, loading and stacking bands in a sensor-agnostic way.
- [LandSurfaceClustering](https://github.com/lhalloran/LandSurfaceClustering) - Land surface classification using remote sensing data with unsupervised machine learning (k-means) `Python`

### Cloud Native Geospatial
- [aws-sat-api-py](https://github.com/RemotePixel/remotepixel-api) - Process Satellite data using AWS Lambda functions
- [GeoLambda](https://github.com/developmentseed/geolambda) - Create and deploy Geospatial AWS Lambda functions `Python`
- [rio-viz](https://github.com/developmentseed/rio-viz) - Visualize Cloud Optimized GeoTIFF in browser `html` `Python`
- [Sentinel-s3](https://github.com/developmentseed/sentinel-s3) - `Python` libraries for extracting Sentinel-2's metadata from Amazon S3
- [geocore](https://github.com/Canadian-Geospatial-Platform/geocore) - GeoCore is an Open Source Cloud Native (AWS) Geospatial Catalog | GeoCore est un catalogue géospatial Open Source Cloud Native (AWS) 
- [cng-workshop](https://github.com/Element84/cng-workshop) - Intro to cloud-native geospatial workshop
- [cloud-native-geospatial](https://github.com/ua-datalab/cloud-native-geospatial) - resource [introduction to cloud native geospatial](https://ua-datalab.github.io/cloud-native-geospatial/)

#### STAC
- [stac-utils](https://github.com/stac-utils) - Tools for working with SpatioTemporal Asset Catalogs (STAC) (perhaps worth going here first for STAC) `Python` `Javascript`
  - [pystac](https://github.com/stac-utils/pystac) - `Python` library for working with any SpatioTemporal Asset Catalog (STAC)
    - [stactools](https://github.com/stac-utils/stactools) - Command line utility and `Python` library for STAC 
    - [pystac-client](https://github.com/stac-utils/pystac-client) - `Python` client for STAC Catalogs and APIs
  - [pgstac](https://github.com/stac-utils/pgstac) - Schema, functions and a `Python` library for storing and accessing STAC collections and items in `PostgreSQL` 
  - [stac-fastapi](https://github.com/stac-utils/stac-fastapi) - STAC API implementation with FastAPI. `Python`
  - [stac-fastapi-pgstac](https://github.com/stac-utils/stac-fastapi-pgstac) - PostgreSQL backend for stac-fastapi using pgstac
  - [STAC Spec](https://github.com/radiantearth/stac-spec) - SpatioTemporal Asset Catalog specification - making geospatial assets openly searchable and crawlable
  - [stac-validator](https://github.com/stac-utils/stac-validator) - Validator for the stac-spec `Python`
  - [stackstac](https://github.com/gjoseph92/stackstac) - Turn a list of STAC items into a 4D xarray DataArray `Python`
  - [stac-nb](https://github.com/darrenwiens/stac-nb) - STAC in Jupyter Notebooks `Python`
  - [qgis-stac-plugin](https://github.com/stac-utils/qgis-stac-plugin) - QGIS plugin for reading STAC APIs `Python`
  - [easystac](https://github.com/cloudsen12/easystac) - A `Python` package for simple STAC queries
  - [stac-utils](https://github.com/stac-utils/stac-task) - Provides a class interface for running custom algorithms on STAC ItemCollections `Python`
  - [pgstac](https://github.com/stac-utils/pgstac) - Schema, functions and a python library for storing and accessing STAC collections and items in PostgreSQL
  - [pystac-client](https://github.com/stac-utils/pystac-client) - `Python` client for searching STAC APIs
  - [stac-asset](https://github.com/stac-utils/stac-asset) - Read and download STAC Assets, using a variety of authentication schemes
  - [stac-server](https://github.com/stac-utils/stac-server) - A Node-based STAC API, AWS Serverless, OpenSearch `Javascript`
  - [elastic search](https://github.com/stac-utils/stac-fastapi-elasticsearch-opensearch) - Elasticsearch backend for stac-fastapi with Opensearch support. `Python`
  - [stac4s](https://github.com/stac-utils/stac4s) - A `Scala` library with primitives to build applications using the SpatioTemporal Asset Catalogs specification
  - [stac-rs](https://github.com/stac-utils/stac-rs) - `Rust` implementation of the SpatioTemporal Asset Catalog (STAC) specification
  - [stac-table](https://github.com/stac-utils/stac-table)
  - [stac-fields](https://github.com/stac-utils/stac-fields) - A minimal STAC library that contains a list of STAC fields with some metadata and helper functions for styling as HTML. `Javascript`
  - [titiler-pgstac](https://github.com/stac-utils/titiler-pgstac) - TiTiler + PgSTAC
  - [stac-api-validator](https://github.com/stac-utils/stac-api-validator) - A STAC API validation client `Python`
  - [xpystac](https://github.com/stac-utils/xpystac) - For extending xarray.open_dataset to accept pystac objects `Python`
  - [stac-pydantic](https://github.com/stac-utils/stac-pydantic) - Pydantic data models for the STAC spec `Python`
  - [stac-migrate](https://github.com/stac-utils/stac-migrate) - A tool to migrate Items, Catalogs and Collections from old versions to the most recent one. `Javascript`
  - [stac-node-validator](https://github.com/stac-utils/stac-node-validator) - Simple validator for STAC Items, Catalogs, and Collections. STAC 1.0.0 compliant! `Javascript`
  - [stac-geoparquet](https://github.com/stac-utils/stac-geoparquet) - Convert STAC items to geoparquet. `Python`
  - [stac-index](https://github.com/stac-utils/stac-index) - A service that lists all available and registered STAC catalogs and APIs.
  - [stac-check](https://github.com/stac-utils/stac-check) - Linting and validation tool for STAC assets
  - [stac-terminal](https://github.com/stac-utils/stac-terminal) - Output info on STAC Items in the terminal
  - [stac-layer](https://github.com/stac-utils/stac-layer) - Visualize a STAC Item or Collection on a Leaflet Map
  - [pgstac-rs](https://github.com/stac-utils/pgstac-rs) - `Rust` interface to pgstac

#### COG
- [COG Validator](https://github.com/rouault/cog_validator) - Cloud Optimized GeoTIFF validation service
- [titiler](https://github.com/developmentseed/titiler) - A modern dynamic tile server built on top of `FastAPI` and `Rasterio/GDAL`.
- [cogeo-mosaic](https://github.com/developmentseed/cogeo-mosaic) - Create and use COG mosaic based on mosaicJSON `Python`
- [Sentinel-2-cog](https://github.com/developmentseed/sentinel-2-cog) - Convert Sentinel-2 JPEG 2000 to COG with AWS Lambda `Python`
- [COG Dumper](https://github.com/mapbox/COGDumper) - Dumps tiles out of a cloud optimized geotiff `Python`
- [async-cog-reader](https://github.com/geospatial-jeff/async-cog-reader) - Read Cloud Optimized GeoTiffs without GDAL`Python`
- [aiocogeo](https://github.com/geospatial-jeff/aiocogeo) - Asynchronous cogeotiff reader `Python`
- [cogeotiff](https://github.com/blacha/cogeotiff) - High performance cloud optimised geotiff reader
- [ecw-converter](https://github.com/lifebit-ai/ecw-converter) - Dockerised `Python` scripts & Nextflow pipeline for converting ecw files to either geotiffs or Cloud Optimised Geotiffs (COGs) 
- [COG pptx/pdf](https://github.com/saheelBreezo/Cloud-Optimised-Geotiff/blob/master/Talk/Cloud_Optimized_GeoTIFF_Blue_Sky_Analytics.pdf) - talk on COG

### Case studies / Projects

- [Povetry predition using satellite imagery](https://github.com/carsonluuu/Poverty-Prediction-by-Satellite-Imagery) - Poverty Prediction by Combination of Satellite Imagery
- [Python from space](https://github.com/kscottz/PythonFromSpace) - `Python` Examples for Remote Sensing
- [count blue pixels](https://github.com/craic/count_shelters) - This project is an experiment in using simple image processing techniques on satellite images downloaded from Google Maps in order to quantify the relative density of temporary shelters in adjacent qudarants. `Python` `Ruby`
- [Satellite imagery analysis with Python](https://github.com/parulnith/Satellite-Imagery-Analysis-with-Python) - Getting acquainted with the concept of satellite imagery data and how it can be analyzed to investigate real-world environmental and humanitarian challenges. `Python` `Jupyter Notebooks` [associated blog](https://medium.com/analytics-vidhya/satellite-imagery-analysis-with-python-3f8ccf8a7c32)
- [Satellite imagery in Pakistan](https://github.com/iam-mhaseeb/Satellite-Imagery-Analysis-of-Vegetation-in-Southern-Pakistan) - This repository contains a study how we can examine the vegetation cover of a region with the help of satellite data. The notebook in this repository aims to familiarise with the concept of satellite imagery data and how it can be analyzed to investigate real-world environmental and humanitarian challenges.
- [SentinelBot](https://github.com/JamesOConnor/Sentinel_bot) - A twitter bot which processes raw sentinel data `Python` [SentinelBot on twitter](https://twitter.com/sentinel_bot)
- [ap-latem](https://github.com/dymaxionlabs/ap-latam) - Detection of slums and informal settlements from satellite imagery `Python`
- [local_structire_wpb-severity](https://github.com/mikoontz/local-structure-wpb-severity) - Analysis of drone imagery to characterize forest structure and severity of a tree killing insect `Python`
- [Truck_Detection_Sentinel2_COVID19](https://github.com/hfisser/Truck_Detection_Sentinel2_COVID19) - This repository is designated to detecting trucks using Sentinel-2 data. `Python`
- [Artificial Intelligence for Geospatial Analysis with Pytorch’s TorchGeo (multi parts)](https://towardsdatascience.com/artificial-intelligence-for-geospatial-analysis-with-pytorchs-torchgeo-part-1-52d17e409f09) - An end-to-end deep learning geospatial segmentation project using Pytorch and TorchGeo packages - [code](https://gist.github.com/cordmaur/d050973aa3ed980023e9239183a2cb66#file-earthsurfacewater_medium_2-ipynb)

### Company specific examples

(you may need to create an account to use these resources)

- [Planet notebooks](https://github.com/planetlabs/notebooks) - interactive notebooks from Planet Engineering `Python`
- [Planet-client-API](https://github.com/planetlabs/planet-client-python) - `Python` client for Planet APIs
- [Maxar GDBx tools](https://github.com/DigitalGlobe/gbdxtools) - Python SDK for using GBDX.
- [gdbx-surface-water](https://github.com/gena/gbdx-surface-water) - Reservoir surface area detection with Digital Globe imagery and Bayesian methods
- [SentinelHub-py](https://github.com/sentinel-hub/sentinelhub-py) - Download and process satellite imagery in Python using Sentinel Hub services.
- [sentinel2-cloud-detector](https://github.com/sentinel-hub/sentinel2-cloud-detector) - Sentinel Hub Cloud Detector for Sentinel-2 images in `Python`
- [Orbit predictor](https://github.com/satellogic/orbit-predictor) - Python library to propagate satellite orbits.
- [up42-py](https://github.com/up42/up42-py) - Python SDK for UP42, the geospatial marketplace and developer platform. `Python`
- [S2-superresolution](https://github.com/up42/s2-superresolution) - Deep Learning-based algorithm to upsample all Sentinel-2 bands to 10m. Also an example how to use GPUs on UP42. `Python`
- [icecube](https://github.com/iceye-ltd/icecube) - Create time-series datacubes for supervised machine learning with ICEYE SAR images. `Python`

### Reflectance / pre processing

- [Landsat7 errors](https://github.com/gena/landsat7-errors) - Identifies errors in raw values of Landsat 7
- [PyProSail](https://github.com/robintw/PyProSAIL) - Python interface to the ProSAIL leaf/canopy reflectance model
- [Py6S](https://github.com/robintw/Py6S) - A `Python`interface to the 6S Radiative Transfer Model
- [prosail](https://github.com/jgomezdans/prosail) - `Python` bindings for the PROSAIL canopy reflectance model
- [ACOLITE_MR](https://github.com/acolite/acolite_mr) - ACOLITE_MR: Atmospheric correction for aquatic applications of metre-scale satellites
- [radiometric_normalization](https://github.com/planetlabs/radiometric_normalization) - Implementation of radiometric normalization workflows `Python`
- [color_balance](https://github.com/planetlabs/color_balance) - Balance your colors! `Python`
- [data-retrieval-in-EO](https://gitlab.com/raul.lezameta/data-retrieval-in-EO/-/tree/master) - data-retrieval-in-EO, a project with reports from TU wien

### Python libraries related to EO

- [rasterio](https://github.com/mapbox/rasterio) - Rasterio reads and writes geospatial raster datasets
- [Xarray pyconuk 2018](https://github.com/robintw/XArray_PyConUK2018) - Code and slides for my talk at PyCon UK 2018 on XArray `Python`
- [RasterStats](https://github.com/perrygeo/python-rasterstats) - Summary statistics of geospatial raster datasets based on vector geometries. `Python`
- [SatPy](https://github.com/pytroll/satpy) - `Python` package for earth-observing satellite data processing
- [pyimpute](https://github.com/perrygeo/pyimpute) - Spatial classification and regression using Scikit-learn and Rasterio `Python`
- [dask-rasterio](https://github.com/dymaxionlabs/dask-rasterio) - Read and write rasters in parallel using Rasterio and Dask `Python`
- [rioxarray](https://github.com/corteva/rioxarray) - geospatial xarray extension powered by rasterio [docs](https://corteva.github.io/rioxarray/stable/)
- [xarray-spatial](https://github.com/makepath/xarray-spatial) - Raster-based Spatial Analysis for `Python`
- [actinia core](https://github.com/mundialis/actinia_core) - Actinia Core is an open source REST API for scalable, distributed, high performance processing of geographical data that uses mainly GRASS GIS for computational tasks. `Python`
- [actinia satellite plugin](https://github.com/mundialis/actinia_satellite_plugin) - This actinia plugin is designed for efficient satellite data handling, especially Landsat and Sentinel-2 scenes `Python`
- [Whitebox Python](https://github.com/giswqs/whitebox-python) - WhiteboxTools `Python` Frontend
- [ukis-pysat](https://github.com/dlr-eoc/ukis-pysat) - generic classes and functions to query, access and process multi-spectral and SAR satellite images

### Testing your code

- [image-similarity-measures](https://pypi.org/project/image-similarity-measures/) - Implementation of eight evaluation metrics to access the similarity between two images. `Python`
- [fake-geo-images](https://pypi.org/project/fake-geo-images/) - A module to programmatically create geotiff images which can be used for unit tests. `Python`

## Resources for `R`

R is not my area of expertise so this section is lighter than I'd like, plus I'd love to know what is a useful resource
Books! [Geospatial R Books](https://www.bigbookofr.com/geospatial.html) - some `R` books on geospatial

- [R-Spatial](https://rspatial.org/raster/rs/1-introduction.html) - This book provides a short introduction to satellite data analysis with R.
  - [Remote Sensing analysis with R](https://rspatial.org/raster/rs/index.html) - Builds on above R-Spatial
- [GDAL Cubes](https://cran.r-project.org/web/packages/gdalcubes/index.html) - Earth Observation Data Cubes from Satellite Image Collections. Also [here on github](https://github.com/appelmar/gdalcubes_R)
- [R code for ML in Sat imagery](https://gist.github.com/franzalex/a95e227cab9b146a6092) - # Random Forest image classification Adapted from [stackoverflow](http://gis.stackexchange.com/a/57786/12899).
- [whiteboxR](https://github.com/giswqs/whiteboxR) - An R frontend of the advanced geospatial data analysis platform - [whitebox-tools](https://github.com/jblindsay/whitebox-tools).
- [RasterVIS](https://cran.r-project.org/web/packages/rasterVis/index.html) - Methods for enhanced visualization and interaction with raster data. It implements visualization methods for quantitative data and categorical data, both for univariate and multivariate rasters. It also provides methods to display spatiotemporal rasters, and vector fields.
- [Landsat](https://cran.r-project.org/web/packages/landsat/index.html) - Processing of Landsat or other multispectral satellite imagery. Includes relative normalization, image-based radiometric correction, and topographic correction options.
- [rnoaa](https://github.com/ropensci/rnoaa) - R interface to many NOAA data APIs
- [MODISTools](https://github.com/ropensci/MODISTools) - Interface to the MODIS Land Products Subsets Web Services [Docs](https://docs.ropensci.org/MODISTools/)
- [A Step-by-Step Guide to Making 3D Maps with Satellite Imagery in R](https://www.tylermw.com/a-step-by-step-guide-to-making-3d-maps-with-satellite-imagery-in-r/) - Walk you through [on] how to obtain the data required to make these types of maps, as well as the R code used to generate them
- [landsatlinkr](https://github.com/jdbcode/LandsatLinkr) - An automated system for creating spectrally consistent and cloud-free Landsat image time series stacks from a combination of MSS, TM, ETM+, and OLI sensors [project](http://jdbcode.github.io/LandsatLinkr/)
- [planetR](https://github.com/bevingtona/planetR) - (early development) R tools to search, activate and download satellite imagery from the Planet API
- [ForestTools](https://github.com/andrew-plowright/ForestTools) - Detect and segment individual tree from remotely sensed data
- [lidR](https://github.com/Jean-Romain/lidR) - `R` package for airborne LiDAR data manipulation and visualisation for forestry application. Plus [lidRplugins](https://github.com/Jean-Romain/lidRplugins) - Extra functions and algorithms for lidR package
- [Spatiotemporal Arrays: Raster and Vector Datacubes](https://github.com/r-spatial/stars) - Spatiotemporal Arrays, Raster and Vector Data Cube
- [getSpatialData](https://github.com/16EAGLE/getSpatialData) - An `R` package making it easy to query, preview, download and preprocess multiple kinds of spatial data [docs](https://jakob.schwalb-willmann.de/getSpatialData/)
- [RStoolbox](https://bleutner.github.io/RStoolbox/) - RStoolbox is a R package providing a wide range of tools for your every-day remote sensing processing needs.
- [rHarmonics](https://github.com/MBalthasar/rHarmonics) - `R` package for harmonic modelling of time-series data
- [rerddap](https://github.com/ropensci/rerddap) - `R` client for working with ERDDAP servers [docs](https://docs.ropensci.org/rerddap/) reference the [ERDDAP Server](https://upwell.pfeg.noaa.gov/erddap/index.html)
- [Spatial_Data_in_R](https://github.com/joheisig/Spatial_Data_in_R) - SWIRL-course on spatial data in `R`
- [cognition-datasources](https://github.com/geospatial-jeff/cognition-datasources) - Standardized query interface for searching geospatial assets via STAC.
- [caliver](https://github.com/ecmwf/caliver) - caliver: CALIbration and VERification of gridded fire danger models `R`
- [clip_time_series](https://github.com/lecrabe/clip_time_series) - create snippets of Landsat and Sentinel imagery
- [RGISTools](https://github.com/spatialstatisticsupna/RGISTools) - Tools for Downloading, Customizing, and Processing Time Series of Satellite Images from Landsat, MODIS, and Sentinel
- [Grassland-Species-Classification](https://github.com/JavierLopatin/Grassland-Species-Classification) - Codes for: Javier Lopatin, Fabian E. Fassnacht, Teja Kattenborn, Sebastian Schmidtlein. Mapping plant species in mixed grassland communities using close range imaging spectroscopy. Remote Sensing of Environment 201, 12-23. `R`
- [UAV-InvasiveSpp](https://github.com/JavierLopatin/UAV-InvasiveSpp) - Mapping invasive tree species in Chile using UAV `R`
- [Peatland-carbon-stock](https://github.com/JavierLopatin/Peatland-carbon-stock) - Codes for: Lopatin, J., et al. (2019). Using aboveground vegetation attributes as proxies for mapping peatland belowground carbon stocks. Remote Sens. Environ. 231, 111217 `R`
- [SpeciesRichness-GLMvsRF-LiDAR](https://github.com/JavierLopatin/SpeciesRichness-GLMvsRF-LiDAR) - `R`-codes for: Lopatin, J., Dolos, K., Hernández, J., Galleguillos, M., Fassnacht, F. E. (2016): Comparing Generalized Linear Models and random forest to model vascular plant species richness using LiDAR data in a natural forest in central Chile. Remote Sensing of Environment 173, pp. 200–210. 10.1016/j.rse.2015.11.029
- [tree_segmentation](https://github.com/redfoxgis/tree_segmentation) - LiDAR tree segmentation `R`
- [swdt](https://github.com/be-marc/swdt) - Sentinel-1 Water Dynamics Toolkit `R`

- [What_are_data_cubes](https://edzer.github.io/UseR2020/#What_are_data_cubes) - Analyzing and visualising spatial and spatiotemporal data cubes - Part I
- [classifying_satellite_imagery_in_R](https://urbanspatial.github.io/classifying_satellite_imagery_in_R/) - For this tutorial, we use Landsat 8 imagery from Calgary
- [planetR](https://github.com/bevingtona/planetR) - `R` tools to search, activate and download satellite imagery from the Planet API. 
- [Landsat_land_surface_temperature](https://github.com/alyssakullberg/Landsat_land_surface_temperature) - `R` Estimate land surface temperature using Landsat satellite imagery. 

## Languages other than `Python` and `R`

- [Georust](https://github.com/georust) - A collection of geospatial tools and libraries written in `Rust`
- [ArchGDAL - Julia](https://github.com/yeesian/ArchGDAL.jl) - `Julia` A high level API for GDAL - Geospatial Data Abstract
  - [ArchGDAL docs](http://yeesian.com/ArchGDAL.jl/latest/)
- [Julia_Geospatial](https://github.com/acgeospatial/Julia_Geospatial) - Examples for a blog series on Geospatial `Julia` using ArchGDAL
- [GeoTrellis homepage](https://geotrellis.io/) - GeoTrellis is a geographic data processing engine for high performance applications. `Scala`
  - [GeoTrellis on Github - Scala](https://github.com/locationtech/geotrellis)
- [GDAL with GoLang](https://github.com/lukeroth/gdal) - `Go` (golang) wrapper for GDAL, the Geospatial Data Abstraction Library
- [C++ gdalcubes](https://github.com/appelmar/gdalcubes) - Earth observation data cubes from GDAL image collections `C++`
- [RSGLib](https://github.com/remotesensinginfo/rsgislib) - The remote sensing and GIS software library (RSGISLib) is a set of `C++` libraries and commands for the processing of spatial data (raster and vector). Functionality is via `Python` interface though
- [Perl extension for GDAL](https://metacpan.org/pod/Geo::GDAL) - Geo:: GDAL - `Perl` extension for the GDAL library for geospatial data
- [PDAL](https://github.com/PDAL/PDAL) - PDAL is Point Data Abstraction Library. GDAL for point cloud data.
- [force](https://github.com/davidfrantz/force) - Framework for Operational Radiometric Correction for Environmental monitoring in `c`
- [LLR-landTrendr](https://github.com/jdbcode/LLR-LandTrendr) - Landsat-based Detection of Trends in Disturbance and Recovery algorimth modified to accept LandsatLinkr-processed imagery. `IDL`
- [Global Forest Watch](https://github.com/Vizzuality/gfw) - Global Forest Watch: An online, global, near-real time forest monitoring tool
- [conda recipes](https://github.com/yannforget/conda-recipes) - Conda recipes for remote sensing `Shell`
- [Landsat-solar-elevation](https://github.com/jdbcode/landsat-solar-elevation) - A web app that plots annual solar elevation at the time of Landsat overpass for locations throughout the earth `JavaScript`
- [staccato](https://github.com/planetlabs/staccato) - `Java` implementation of the STAC spec
- [stac4s](https://github.com/azavea/stac4s) -a `scala` library with primitives to build applications using the SpatioTemporal Asset Catalogs specification
- [stac-browser](https://github.com/radiantearth/stac-browser) - A Vue-based STAC browser intended for static + dynamic deployment
- [EO Browser Custom Scripts](https://github.com/sentinel-hub/custom-scripts) - A repository of custom scripts to be used with Sentinel Hub `JavaScript`
- [sentinelhub-js](https://github.com/sentinel-hub/sentinelhub-js) - Download and process satellite imagery in `JavaScript` or `TypeScript` using Sentinel Hub services.
- [s3tbx](https://github.com/senbox-org/s3tbx) - A toolbox for the OLCI and SLSTR instruments on board of ESA's Sentinel-3 satellite - `Java`
- [s2tbx](https://github.com/senbox-org/s2tbx) - Sentinel 2 Toolbox (s2tbx) - `Java`
- [s1tbx](https://github.com/senbox-org/s1tbx) - The Sentinel-1 Toolbox - `Java`
- [snap_engine](https://github.com/senbox-org/snap-engine) - ESA Earth Observation Toolbox and `Java` Development Platform
- [Worldview](https://github.com/nasa-gibs/worldview) - Interactive interface for browsing global, full-resolution satellite imagery `Javascript` application [here](https://worldview.earthdata.nasa.gov/)
- [Orfeo ToolBox](https://gitlab.orfeo-toolbox.org/orfeotoolbox/otb) (OTB)- An open-source project for state-of-the-art remote sensing, including a fast image viewer, apps callable from `Bash`, `Python` or QGIS, and a powerful `C++` API.
- [landsat_preprocess](https://github.com/ceholden/landsat_preprocess) - IPython notebook documenting a workflow for preprocessing Landsat data `Shell`
- [stac-mode-validator](https://github.com/m-mohr/stac-node-validator) - Simple proof-of-concept to validate STAC Items, Catalogs, Collections and core extensions with node. `JavaScript`
- [aiforearth-landcover-app](https://github.com/vannizhang/aiforearth-landcover-app) - web mapping app to test, tweak and train the land cover classification from a deep neural network model
- [tiffhax](https://github.com/emilyselwood/tiffhax) - tiff metadata hex viewer `Go`
- [Fmask](https://github.com/GERSL/Fmask) - The software called Fmask (Function of mask) is used for automated clouds, cloud shadows, and snow masking for Landsats 4-8 and Sentinel 2 images. `Matlab`
- [resto](https://github.com/jjrom/resto) - A metadata catalog and search engine for geospatialized data `PHP` Stac!
- [pktools](http://pktools.nongnu.org/html/index.html) - pktools is a suite of utilities written in `C++` for image processing with a focus on remote sensing applications. It relies on the Geospatial Data Abstraction Library ([GDAL](http://www.gdal.org)) and OGR.
- [iris](https://github.com/ESA-PhiLab/iris) - Semi-automatic tool for manual segmentation of multi-spectral and geo-spatial imagery. `Javascript`

## Training and learning

- [Earth Data Lab](https://github.com/earthlab/earthlab.github.io) - A site dedicated to tutorials, course and other learning materials and resources developed by the Earth Lab team
- [EO College Github](https://github.com/EO-College)
  - [tomography_tutorial](https://github.com/EO-College/tomography_tutorial) - A tutorial for Synthetic Aperture Radar Tomography
- [profLewis-geog0111](https://github.com/profLewis/geog0111) - UCL Geography: 4th year course, Scientific Computing
- [Intro to Geospatial Vector and Raster](https://carpentries-incubator.github.io/geospatial-python/) - Data Carpentry’s aim is to teach researchers basic concepts, skills, and tools for working with data so that they can get more done in less time, and with less pain.
- [Andrew Cutts Github](https://github.com/acgeospatial) - I am an Earth Observation and Geospatial enthusiast, primarily using `Python` to automate and process images at scale using computer vision
  - [Satellite Imagery Python](https://github.com/acgeospatial/Satellite_Imagery_Python) - Sample sample scripts and notebooks on processing satellite imagery
  - [Geospatial Python Programming Course](https://github.com/acgeospatial/Geospatial_Python_CourseV1) - This is an collection of blog posts turned into a course format
- [Open Geo Tutorial V2](https://github.com/patrickcgray/open-geo-tutorial) - Tutorial of fundamental remote sensing and GIS methodologies using open source software in `Python`
- [Open Geo Tutorial V1](https://github.com/ceholden/open-geo-tutorial) - Tutorial of basic remote sensing and GIS methodologies using open source software (GDAL in `Python` or `R`)
- [Foss4gUKJupyter](https://github.com/samfranklin/foss4guk19-jupyter) - FOSS4G UK 2019 Workshop "Geoprocessing with Jupyter Notebooks"
- [Geoprocessing with Python - GIS circa 2009](https://www.gis.usu.edu/~chrisg/python/2009/) - This material is really old and some of it is outdated (not all, though!). One of these days I might get around to putting newer class materials online, but you're stuck with this for now.
- [training-workshop](https://github.com/planetlabs/training-workshop) - This repo contains all materials used on Planet's training workshop for Bahrain Defense Force
- [sentinel](https://github.com/techforspace/sentinel) - Repository created for the Earth Observation Sentinel project (use with SNAP) `Python`
- [Python for Geospatial Analysis](https://www.tomasbeuzen.com/python-for-geospatial-analysis/README.html) - A crashcourse introduction to using Python to wrangle, plot, and model geospatial data `Python`
- [pyGIS](https://github.com/mmann1123/pyGIS) - pyGIS is an online textbook covering all the core geospatial functionality available in `Python`. This includes handling vector and raster data, satellite remote sensing, machine learning and deep learning applications

## Deep learning and Machine Learning
- [future learn course - artificial intelligence for earth monitoring](https://www.futurelearn.com/courses/artificial-intelligence-for-earth-monitoring)
- [Segment-geospatial](https://github.com/opengeos/segment-geospatial) - A `Python` package for segmenting geospatial data with the Segment Anything Model (SAM). [docs](https://samgeo.gishub.org/) 

#### Curated lists

[Robin Cole on satellite imagery and deep learning resources](https://github.com/robmarkcole/satellite-image-deep-learning) - Resources for deep learning with satellite & aerial imagery. <b>This is the best place to go for this topic</b> I've removed 95% of the associated links from awesome-eo-code as it is just a repetition.

- [awesome-satellite-imagery-datasets](https://github.com/chrieke/awesome-satellite-imagery-datasets) - List of satellite image training datasets with annotations for computer vision and deep learning. `ARCHIVED REPO`
- [Deep Vector](https://github.com/deepVector/geospatial-machine-learning) - A curated list of resources focused on Machine Learning in Geospatial Data Science.

#### Labelling
- [satellite-imagery-labeling-tool](https://github.com/microsoft/satellite-imagery-labeling-tool) - This is a lightweight web-interface for creating and sharing vector annotations over satellite/aerial imagery scenes. 


## GDAL of course

- [GDAL Cheat Sheet](https://github.com/dwtkns/gdal-cheat-sheet) - Cheat sheet for GDAL/OGR command-line tools
- [GDAL / OGR cookbook](https://pcjericks.github.io/py-gdalogr-cookbook/) - This cookbook has simple code snippets on how to use the Python GDAL/OGR API
- [GDAL tutorial](https://jakobmiksch.eu/post/gdal_ogr/) - This blogpost gives in an introduction to GDAL/OGR and explains how the various command line tools can be used.
- [docker-base-gdal](https://github.com/perrygeo/docker-gdal-base) - A base docker image for geospatial applications
- [An Introduction to GDAL](https://www.youtube.com/watch?v=N_dmiQI1s24) - An Introduction to GDAL - Robert Simmon
- [A Gentle Introduction to GDAL prt 1](https://medium.com/planet-stories/a-gentle-introduction-to-gdal-part-1-a3253eb96082) - command line working
- [A Gentel Introduction to GDAL prt 2](https://medium.com/planet-stories/a-gentle-introduction-to-gdal-part-2-map-projections-gdalwarp-e05173bd710a) - Map Projections
- [A Gentel Introduction to GDAL prt 3](https://medium.com/planet-stories/a-gentle-introduction-to-gdal-part-3-geodesy-local-map-projections-794c6ff675ca) - Geodesy
- [loam](https://github.com/azavea/loam) - `Javascript` wrapper for GDAL in the browser
- [mrf](https://github.com/nasa-gibs/mrf) - GDAL-compatible file format driver designed for fast access to imagery

## Earth Observation coding on YouTube

(presenters listed where possible)<br>
There are many videos relating to Earth Observation and coding, especially Python. This is really such a small collection of videos here. I have attempted to only include ones with good audio and code examples.

- [xArray at PyConUK2018 - Robin Wilson](https://www.youtube.com/watch?v=Dgr_d8iEWk4) - Processing thousands of satellite images to understand air quality in the UK - it's efficient and easy with XArray
- [Visualizing & Analyzing Earth Science Data Using PyViz & PyData - Julia Signell](https://youtu.be/-XMXNmGRk5c?t=455) - In this talk, we'll work through some specific workflows and explore how various tools - such as Intake, Dask, Xarray, and Datashader - can be used to effectively analyze and visualize these data. Working from within the notebook, we'll iteratively build a product that is interactive, scalable, and deployable.
- [Hands on Satellite Imagery 2019 edition - Sara Safavi](https://www.youtube.com/watch?v=j15MryznWn4) - In this tutorial, gain hands-on experience exploring Planet’s publicly-available satellite imagery and using Python tools for geospatial and time-series analysis of medium- and high-resolution imagery data. Using free & open source libraries, learn how to perform foundational imagery analysis techniques and apply these techniques to real satellite data.
- [Python from space - Katherine Scott](https://www.youtube.com/watch?v=rUUgLsspTZA&t) - In this talk we will work through a jupyter notebook that covers the satellite data ecosystem and the python tools that can be used to sift through and analyze that data. Topics include python tools for using Open Street Maps data, the Geospatial Data Abstraction Library (GDAL), and OpenCV and NumPy for image processing.
- [Remote Sening with Python in Jupyter](https://www.youtube.com/watch?v=OsgZSlv4t-U) - In this video we're looking at using Google Earth Engine in Jupyter with the Python API.
- [Writing Image Processing Algorithms with ArcGIS/ArcPy - Jamie Drisdelle](https://www.youtube.com/watch?v=FenT61l-xyQ) - learn how your algorithms can integrate with the raster processing and visualization pipelines in ArcGIS. We’ll demonstrate the concept and discuss the API by diving deep into a few interesting examples with a special focus on multidimensional scientific rasters.
- [Google Earth Engine Python - Qiusheng Wu](https://www.youtube.com/playlist?list=PLAxJ4-o7ZoPccOFv1dCwvGI6TYnirRTg3) - Introducing the geemap Python package for interactive mapping with Google Earth Engine and ipyleaflet.
- [Google Earth Engine EE101 Condensed - Noel Gorelick](https://www.youtube.com/watch?v=m1ejxSi3l8s) - Introduction to the Earth Engine API and a conceptual overview of key functionality such as compositing, reducing, mapping, zonal statistics and cluminating with building a small app.
- [Image classification with RandomForests using the R language](https://www.youtube.com/watch?v=fal4Jj81uMA)In this video I show how to import a Landsat image into R and how to extract pixel data to train and fit a RandomForests model. I also explain how to conduct image classification and how to speed it up through parallel processing.
- [GeoPython 2019 stream](https://www.youtube.com/watch?v=3KRYObqpMlk) - 17:23 Machine Learning for Land Use/Landcover Statistics of Switzerland (Adrian Meyer), 50:58 How to structure geodata, 1:18:13 Terrain segmentation with label bootstrapping for lidar datasets, case of doline detection (Rok Mihevc), 2:34:41 Bias in machine learning, 3:06:23 Software for planning research aircraft missions (Reimar Bauer), 3:32:38 How Technology Moves Fast (PJ Hagerty) , 5:02:05 Spotting Sharks with the TensorFlow Object Detection API (Andrew Carter), 5:40:23 Center for Open Source Data and AI Technologies (CODAIT), 6:03:40 Bayesian modeling with spatial data using PyMC3 (Shreya Khurana) (Sound at 6:04:23 ^^), 7:02:45 Understanding and Implementing Generative Adversarial Networks(GANs) (Anmol Krishan Sachdeva), 7:37:00 Messaging with Satellites from Anywhere on the Planet (Andrew Carter), 8:04:52 Automation of the definition and optimizatino of census sampling areas using AREA (GRID3) (Freja Hunt), 8:35:26 Coastline Mapping with Python, Satellite Imagery and Computer Vision (Rachel Keay)
- [Google Earth Engine in QGIS](https://www.youtube.com/playlist?list=PL8jLygUmAosykCyE-5Pr6zpcB_UqnbFiZ) - This playlist looks at the GEE plugin for QGIS
- [Handling and analysing vector and raster data cubes with R](https://www.youtube.com/watch?v=9by7zsGms40) - Edzer Pebesma (Institute for Geoinformatics, University of Münster) Summary: vector and raster data cubes include vector and raster data as special cases, but extend this to vector time series, OD matrices, multi-band raster data, multi-band raster time series, multi-attribute vector or raster time series, and more general to array data where one ore more dimensions are associated with space and/or with time. Examples come from pretty much all areas dealing with spatiotemporal data. This tutorial will go through a large number of examples to illustrate this idea, mostly focusing on the packages stars and sf and those supporting their classes (like tmap, mapview, gstat, ggplot2).
- [QiushengWu's youtube](https://www.youtube.com/c/QiushengWu) - This youtube channel has pretty much everything you need Earth Engine, git, colab, Python, Geoscience. Highest quality stuff.
- [The OpenDataCube Conference 2021](https://www.youtube.com/playlist?list=PLlZzWSPAR5GbGTRR68XDKPonOL8dOyYB5) - Playlist from the 2021 conference
- [Dask and Geopandas](https://www.youtube.com/watch?v=ZpA9jgSqAkk) - Scalable geospatial data analysis with Dask| Dask Summit 2021

## Earth Engine

`JavaScript` & `Python` & `R`

Best to start here [Awesome_GEE](https://github.com/giswqs/Awesome-GEE) - A curated list of Google Earth Engine resources.

- [Earth Engine API](https://github.com/google/earthengine-api) - `Python` and `JavaScript` bindings for calling the Earth Engine API.
- [from GEE to Numpy to Geotiff](https://mygeoblog.com/2017/10/06/from-gee-to-numpy-to-geotiff/) - Use the GEE python api to export your data to numpy and store the result as a geotiff.
- [Google Earth Engine Community](https://github.com/gee-community) - This organization contains content contributed by the Earth Engine developer community. This is not an officially supported Google product.
- [Geo4Good 2019 workshop materials](https://sites.google.com/earthoutreach.org/geoforgood19/agenda/breakout-sessions) - 2019 material javascript and Python to be found here
- [2018 GEE summit - Dublin materials](https://sites.google.com/earthoutreach.org/eeus2018/agenda/session-descriptions) - 2018 material javascript and Python to be found here
- [10 tips for becoming an Earth Engine expert](https://medium.com/google-earth/10-tips-for-becoming-an-earth-engine-expert-b11aad9e598b) - Keiko Nomura shares her 10 favourite tips
- [Earth Engine Developer list](https://groups.google.com/forum/#!forum/google-earth-engine-developers) - registration required
- [Earth Engine Beginner's Cookbook](https://developers.google.com/earth-engine/tutorials/community/beginners-cookbook) - n this tutorial, we will introduce several types of geospatial data, and enumerate key Earth Engine functions for analyzing and visualizing them. This cookbook was originally created as a workshop during Yale-NUS Data 2.0 hackathon, and later updated for Yale GIS Day 2018 and 2019. `JavaScript`
- [Google Earth Engine Repos](https://github.com/topics/earth-engine) - all the repos matching `earth-engine`
- [geetools](https://github.com/fitoprincipe/geetools-code-editor) - A set of tools to use in Google Earth Engine Code Editor `JavaScript` [docs](https://github.com/fitoprincipe/geetools-code-editor/wiki)
- [gee-up](https://github.com/samapriya/geeup) - Simple CLI for Google Earth Engine Uploads [docs](https://pypi.org/project/geeup/)
- [gee_asset_manager](https://github.com/samapriya/gee_asset_manager_addon) - Google Earth Engine Asset Manager with Addons [docs](https://samapriya.github.io/gee_asset_manager_addon/)
- [Planet-GEE_Pipeline](https://github.com/samapriya/Planet-GEE-Pipeline-CLI) -Planet and Google Earth Engine Pipeline Command Line Interface Tool [docs](https://pypi.org/project/ppipe/)
- [GEE code archive](https://github.com/gena/ee-code-editor-archive) - Unsorted archived Earth Engine scripts `JavaScript`
- [Python GEE notebooks](https://github.com/giswqs/earthengine-py-notebooks) - A collection of 360+ Jupyter Python notebook examples for using Google Earth Engine with interactive mapping
- [GEE Map](https://github.com/giswqs/geemap) - A Python package for interactive mapping with Google Earth Engine, ipyleaflet, and ipywidgets
- [cloud frequency app](https://github.com/robintw/CloudFrequencyApp) - CloudFrequency webapp, using Google App Engine `Python` `JavaScript`
- [rgee](https://github.com/r-spatial/rgee) - Google Earth Engine for `R` [docs](https://csaybar.github.io/rgee/)
- [ee-tensorflow-notebooks](https://github.com/gee-community/ee-tensorflow-notebooks) - Repository to place example notebooks for Deep Learning applications with TensorFlow and Earth Engine.
- [remote-sensing-resistance](https://github.com/mikoontz/remote-sensing-resistance) - Does heterogeneity in forest structure make a forest resistant to wildfire?
- [GoogleEarthEngine](https://github.com/evan-delancey/GoogleEarthEngine) - forestry related work
- [ee-jupyter-examples](https://github.com/tylere/ee-jupyter-examples) - Example Jupyter Notebooks, including ones that use the Earth Engine `Python` API
- [jupyterlab-ee](https://github.com/tylere/jupyterlab-ee) - Experiments related to getting JupyterLab and Earth Engine to work together. `Python`
- [EEwPython](https://github.com/csaybar/EEwPython) - A series of Jupyter notebook to learn Google Earth Engine with `Python`
- [GoogleEarthEngine-side-projects](https://github.com/chrieke/GoogleEarthEngine-side-projects) - Google Earth Engine side projects and tutorial scripts `JavaScript`
- [ox_gee_tutorial](https://github.com/tommylees112/ox_gee_tutorial) - Oxford MSc Introduction to Hydrological Applications in Google Earth Engine
- [crop_yield_prediction](https://github.com/JiaxuanYou/crop_yield_prediction) - Crop Yield Prediction with Deep Learning with GEE
- [geecrop](https://github.com/profLewis/geecrop) - Earth Engine-based crop information
- [radiometric-slope-correction](https://github.com/ESA-PhiLab/radiometric-slope-correction) - Radiometric Slope Correction of Sentinel-1 data on Google Earth Engine
- [geebap](https://github.com/fitoprincipe/geebap) - Best Available Pixel (BAP) composite in Google Earth Engine (GEE) using the `Python` API
- [Ecuador_SEPAL](https://github.com/sig-gis/Ecuador_SEPAL) - processing script for Sentinel-2 and Landsat-8
- [geeguide](https://github.com/ndminhhus/geeguide) - Harmonization of Landsat and Sentinel 2 in Google Earth Engine, documentation and scripts
- [EE-Examples](https://github.com/gorelick/EE-Examples) - `Javascript` some (old?) example scripts from Noel Gorelick - lead author [Google Earth Engine: Planetary-scale geospatial analysis for everyone](https://www.sciencedirect.com/science/article/pii/S0034425717302900)
- [global-river-ice-dataset-from-landsat](https://github.com/seanyx/global-river-ice-dataset-from-Landsat) - `Python` (Google Earth Engine), `JavaScript` (Google Earth Engine) and `R` code to extract river ice condition from Landsat satellites, to develop empirical model, and to predict future changes in river ice
- [GEE_Functions](https://github.com/JavierLopatin/GEE_Functions) - A set of functions to work in Google Engine `Javascript`
- [HMS-Smoke](https://github.com/tianjialiu/HMS-Smoke) - HMS Smoke Explorer: To visualize NOAA's Hazard Mapping System (HMS) smoke product `Javascript`
- [Building_Identification_Damage_Assessment](https://github.com/welkinland/Building_Identification_Damage_Assessment) - Building Extraction and Damage Assessment from High Resolution Multi-spectral Images `Python`
- [Fire_Pattern_Analysis_CONUS](https://github.com/welkinland/Fire_Pattern_Analysis_CONUS) - Analysis of fire patterns and drivers in CONUS `Python`
- [Best Available Pixel](https://github.com/saveriofrancini/bap) - Best Available Pixel calculation using Google Earth Engine `Javascript`
- [ee-palettes](https://github.com/gee-community/ee-palettes) - A set of common color palettes for Google Earth Engine 

## Open Data Cube

- [Opendatacube](https://github.com/opendatacube)
  - [Datacube Core](https://github.com/opendatacube/datacube-core) - Open Data Cube analyses continental scale Earth Observation data through time `Python` `xarray`
  - [Datacube OWS](https://github.com/opendatacube/datacube-ows) - Open web services for the Open Data Cube. Supports WMS, WMTS and WCS for any dataset indexed into the ODC `Python`
- [ODC STAC](https://github.com/opendatacube/odc-stac) - A stand-alone Python library that allows the loading of STAC Items into an ODC-compatible Xarray `xarray` `Python`
- [data_cube_notebooks](https://github.com/ceos-seo/data_cube_notebooks) - Jupyter Notebook examples for our Data Cube capable algorithms and functions `Python`
- [Digital Earth Australia Notebooks](https://github.com/GeoscienceAustralia/dea-notebooks) - Repository for Jupyter Notebooks, tools and workflows for continental-scale earth observation/geospatial analysis with Open Data Cube and `xarray` `Python`
- [Digital Earth Africa Sandbox Notebooks](https://github.com/digitalearthafrica/deafrica-sandbox-notebooks) - Extra documentation about using ODC with Jupyter Notebooks with DE Africa-specific examples `xarray` `Python`
- [odc-tools](https://github.com/opendatacube/odc-tools) - ODC features that DEA is experimenting with or prototyping with the intention of being integrated into odc-core in the future
- [datacube-explorer](https://github.com/opendatacube/datacube-explorer) - Web-based exploration of Open Data Cube collections
- [openeo_odc_driver](https://github.com/SARScripts/openeo_odc_driver) - OpenEO processing engine written in `Python` based on OpenDataCube, `Xarray` and `Dask`.
- [geocube](https://github.com/corteva/geocube) - Tool to convert geopandas vector data into rasterized xarray data `Python`
- [odc-sh](https://github.com/sentinel-hub/odc-sh) - Sentinel Hub plugin for Open data cube
- [dea-coastlines](https://github.com/GeoscienceAustralia/dea-coastlines) - Extracting tidally-constrained annual shorelines and robust rates of coastal change from freely available Earth observation data at continental scale 

## Other Datacube-related Python

- [Google Earth Engine Python examples](https://github.com/renelikestacos/Google-Earth-Engine-Python-Examples) - Various examples for Google Earth Engine in `Python` using Jupyter Notebook 
- [stackstac](https://github.com/gjoseph92/stackstac) - Turn a STAC catalog into a dask-based xarray `Python`

## Planetary Computer


- [Mircosoft PlanetaryComputer](https://github.com/microsoft/PlanetaryComputer) - Issues, discussions, and information about the Microsoft Planetary Computer 
  - [reading-stac](https://planetarycomputer.microsoft.com/docs/quickstarts/reading-stac/) - Reading Data from the STAC API
  - [PlanetaryComputerExamples](https://github.com/microsoft/PlanetaryComputerExamples) - Examples of using the Planetary Computer `Python`
  - [sdk-python](https://github.com/microsoft/planetary-computer-sdk-for-python) - Planetary Computer SDK for `Python`
  - [planetary-computer-apis](https://github.com/microsoft/planetary-computer-apis)
  - [PlanetaryComputerDataCatalog](https://github.com/microsoft/PlanetaryComputerDataCatalog) - Data catalog for the Microsoft Planetary Computer [website](https://planetarycomputer.microsoft.com/)
- [planetary-computer-deep-dives](https://github.com/TomAugspurger/planetary-computer-deep-dives) - `Python`
- [Sentinel2 on planetary computer](https://github.com/Element84/geo-notebooks/blob/main/notebooks/odc-planetary-computer.ipynb) - notebook explores Sentinel-2 data on Microsoft's Planetary Computer `Python`
- [satio-pc](https://github.com/dzanaga/satio-pc) - Compute Sentinel features on Planetary Computer `Python`
- [gmv planetary computer S2 alerts](https://github.com/globalmangrovewatch/gmw_planetary_computer_s2_alerts) - Repo with the code producing the GMW alerts using the Microsoft Planetary Computer `Python`
- [hottest panchayats kerala](https://github.com/shijithpk/hottest-panchayats-kerala) - Figuring out what the hottest villages in Kerala are with the help of Microsoft's Planetary Computer. `Python` 

## QGIS and Grass

- [Qgis Earth Engine Plugin](https://github.com/gee-community/qgis-earthengine-plugin) - Integrates Google Earth Engine and QGIS using Python API
  - [QGIS Earth Engine Plugin - installation guide](https://gee-community.github.io/qgis-earthengine-plugin/)
- [grass-dev-py3-pdal](https://github.com/OSGeo/grass/tree/master/docker) - Dockerfile which compiles GRASS GIS 7.9 master with Python 3 and PDAL suppor
- [qgis-plugin-planet](https://github.com/planetlabs/qgis-planet-plugin) - Browse, filter, preview and download Planet Inc imagery in QGIS. `Python`
- [TSTools - archived](https://github.com/ceholden/TSTools) - QGIS2 plugin tools for remote sensing timeseries `Python`

## Climate and weather based resources

These are `Python` resources. Please see [R resources](#resources-for-r) for info on R

- [s3 tools](https://github.com/maximlamare/s3_tools) - A collection of sentinel 3 processing tools `Python`
- [eumetsat -python](https://github.com/guidocioni/eumetsat-python) - Shows how to read and plot satellite data from EUMETSAT NETCDF files `Python`
- [unidata on GOES-16](https://unidata.github.io/python-gallery/examples/mapping_GOES16_TrueColor.html) - This notebook shows how to make a true color image from the GOES-16 Advanced Baseline Imager (ABI) level 2 data. We will plot the image with matplotlib and Cartopy.`Python`
- [MetPy](https://github.com/Unidata/MetPy) - MetPy is a collection of tools in Python for reading, visualizing and performing calculations with weather data. `Python`
  - [MetPy docs](https://unidata.github.io/MetPy/latest/)`Python`
  - [aqua-monitor](https://github.com/Deltares/aqua-monitor) - Monitoring surface water changes from space at global scale. Also checkout the [app](https://aqua-monitor.appspot.com/) `Python`
- [Ocean Color - Modis](https://github.com/JackieVeatch/ocean_color) - introduction to accessing and plotting ocean color satellite data from MODIS `Python`
- [Climate data science](https://github.com/willyhagi/climate-data-science) - Climate Data Science and Earth Observation with `Python`
- [COST-EUMETSAT-Training](https://github.com/gher-ulg/COST-EUMETSAT-Training) - Material, data and presentations for the COST-EUMETSAT training school
- [eumetsat](https://github.com/openclimatefix/eumetsat) - Tools for downloading and processing satellite images from EUMETSAT
- [coda_eumetsat](https://github.com/nicolaerosca/coda_eumetsat) - Coda Eumetsat (coda.eumetsat.int) client for downloading data
- [ai4eo-forecast](https://gitlab.com/Pablo-DBG/ai4eo-forecast) - Developing an open source library to compare Earth Observation and weather forecast services with the actual measurements and assess the accuracy of the forescast `Python`

### EUMETlab

Such a vast collection of resources that it warrants a sub section within Climate and weather based resources

- [EUMETlab](https://gitlab.eumetsat.int/eumetlab) - This page contains groups of code repositories that have been made open to the public by EUMETSAT and our collaborators.
  - [atmosphere](https://gitlab.eumetsat.int/eumetlab/atmosphere/atmosphere) - LTPy - Learning tool for Python on Atmospheric Composition Data is a Python-based training course on Atmospheric Composition Data. The training course covers modules on data access, handling and processing, visualisation as well as case studies.
  - [sentinel-downloader](https://gitlab.eumetsat.int/eumetlab/cross-cutting-tools/sentinel-downloader) - Python-based Sentinel satellite data downloader. This script allows for batch downloading of Sentinel data selected by various criteria include date, location, sensor, child products, flags and more.
  - [olci-iop-processor](https://gitlab.eumetsat.int/eumetlab/oceans/ocean-science-studies/olci-iop-processor) - Code to produce Inherent Optical Properties from Level-2 OLCI data. 

## DEM projects

- [Tin Terrain](https://github.com/heremaps/tin-terrain) - A command-line tool for converting heightmaps in GeoTIFF format into tiled optimized meshes.
- [TauDEM](https://github.com/dtarb/TauDEM) - Terrain Analysis Using Digital Elevation Models (TauDEM) software for hydrologic terrain analysis and channel network extraction. [Docs](http://hydrology.usu.edu/taudem/taudem5/index.html)
- [DEM.net](https://github.com/dem-net/DEM.Net) - Digital Elevation model library in C#. 3D terrain models, line/point Elevations, intervisibility reports. [Docs](https://elevationapi.com/)
- [Stereo Mapping to create Elevation with Python](https://github.com/cmla/s2p) - Satellite Stereo Pipeline
- [DSM2DTM](https://github.com/mprakhar/DSM2DTM) - Code for the paper - Comparison of Digital Building Height Models Extracted from AW3D, TanDEM-X, ASTER, and SRTM Digital Surface Models over Yangon City `Python`
- [The Stereo Pipeline (NASA)](https://ti.arc.nasa.gov/tech/asr/groups/intelligent-robotics/ngt/stereo/) - The NASA Ames Stereo Pipeline (ASP) is a suite of free and open source automated geodesy and stereogrammetry tools designed for processing stereo imagery captured from satellites

## SAR

- [SAR docker](https://github.com/mortcanty/SARDocker) - Source files for Docker image mort/sardocker/
- [awesome SAR](https://github.com/lveci/awesome-sar) - A curated list of awesome Synthetic Aperture Radar (SAR) software, libraries, and resources.
- [pyroSAR](https://github.com/johntruckenbrodt/pyroSAR) - framework for large-scale SAR satellite data processing
- [PyRAT](https://github.com/birgander2/PyRAT) - General purpose Synthetic Aperture Radar (SAR) postprocessing software package `Python`
- [RITSAR](https://github.com/dm6718/RITSAR) - Synthetic Aperture Radar (SAR) Image Processing Toolbox for `Python`
- [PySAR](https://github.com/bminchew/PySAR) - PyAR is a perpetually incomplete, general-purpose toolbox for common post-processing tasks involving synthetic aperture radar (SAR).`Python` `C++`
- [sarbian](https://github.com/EO-College/sarbian) - a plug’n play Operation System (based on Debian Linux) with all the freely and openly available SAR processing software
- [OpeSARToolkit](https://github.com/ESA-PhiLab/OpenSarToolkit) - High-level functionality for the inventory, download and pre-processing of Sentinel-1 data in the `python` language.
- [infrastructure](https://github.com/ESA-PhiLab/infrastructure) - Mapping and monitoring of infrastructure in desert regions with Sentinel-1
- [OST_Notebook](https://github.com/ESA-PhiLab/OST_Notebooks) - The notebooks within this repository provide getting started tutorials for the use of the Open SAR Toolkit, found here in the ESA-philab github channel.
- [S1_ARD](https://github.com/johntruckenbrodt/S1_ARD) - repository for testing analysis-readiness of Sentinel-1 RTC backscatter `Python`
- [sea_ice_drift](https://github.com/nansencenter/sea_ice_drift) - Sea ice drift from Sentinel-1 SAR imagery using open source feature tracking `Python`
- [s1prepro](https://github.com/benjimin/s1prepro) - Automated pre-processing of Sentinel 1 (satellite radar imagery) `Python`
- [Spacenet6 - SAR buildings](https://github.com/SpaceNetChallenge/SpaceNet_SAR_Buildings_Solutions) - The winning solutions for the SpaceNet 6 Challenge `Python`
- [sentinel1-opds](https://github.com/earthobservatory/sentinel1-opds) - sentinel1-opds ingestion `Python`
- [rice_sentinel1](https://github.com/AndrewPham9/rice_sentinel1) - classify rice from sentinel 1 data `Python`
- [sentineldenoised](https://github.com/nansencenter/sentinel1denoised) - Thermal noise subtraction, scalloping correction, angular correction `Python`
- [sentinel1-Biodiversity](https://github.com/So-YeonBae/Sentinel1-Biodiversity) - Code, example dataset, and instructions of Sentinel-1 data pre-processing and pixel-based summary statistics used in "Radar vision for mapping forest biodiversity from space" `Python`
- [Step by step: Radar-based flood mapping with Python](https://un-spider.org/advisory-support/recommended-practices/recommended-practice-flood-mapping/python-step-by-step) and [github link](https://github.com/UN-SPIDER/radar-based-flood-mapping) - This repository contains a Jupyter Notebook for automatic flood extent mapping using space-based information. `Python`
- [STAC Sentinel1](https://github.com/stactools-packages/sentinel1) - stactools package for working with sentinel1 data `Python`
- [sarsen](https://github.com/bopen/sarsen) - Algorithms and utilities for Synthetic Aperture Radar (SAR) sensors
- [S1_NRB](https://github.com/SAR-ARD/S1_NRB) - A prototype processor for the Sentinel-1 Normalised Radar Backscatter product.

## LiDAR

- [ICESAT extraction script](https://gist.github.com/bzgeo/950f3db986b3513311ed42efe2395171) - Python script to convert from ICESat-2 ATL08 HDF data to shapefile. Usage: 'python icesat2_shp.py
- [ICESAT tools](https://github.com/icesat-2UT/PhoREAL) - Tools and code for Icesat-2 data analysis (Python)
- [usgs-lidar](https://github.com/hobu/usgs-lidar) - AWS Entwine Point Tiles USGS LiDAR Public Dataset GitHub repo
- [Lidar](https://github.com/giswqs/lidar) - Terrain and hydrological analysis based on LiDAR-derived digital elevation models (DEM)
- [IcePyx](https://github.com/icesat2py/icepyx) - Python tools for obtaining and working with ICESat-2 data

### GEDI

- [pyGEDI](https://github.com/EduinHSERNA/pyGEDI) - pyGEDI is a Python Package for NASA's Global Ecosystem Dynamics Investigation (GEDI) mission, data extraction, analysis, processing and visualization.
- [GEDI extraction script](https://gist.github.com/KMarkert/c68ccf53260d7b775b836bf2e11e2ec3) - Python script to take GEDI level 2 data and convert variables to a geospatial vector format
- [rGEDI](https://github.com/carlos-alberto-silva/rGEDI) - rGEDI: An R Package for NASA's Global Ecosystem Dynamics Investigation (GEDI) Data Visualization and Processing.
- [pysl4land](https://github.com/remotesensinginfo/pysl4land) - `Python` tools to process spaceborne lidar (GEDI and ICESAT2) for land (pySL4Land) applications
- [gedi](https://github.com/rodolfolotte/gedi) - `Python` tutorial to process and handle LiDAR GIDE datasets
- [sprnca_gedi](https://github.com/rbavery/sprnca_gedi) - WIP to map Foliage Height Diversity along the San Pedro Riparian Corridor with NASA's GEDI Lidar `Python`
- [GEDI_Yucatan](https://github.com/JohMast/GEDI_Yucatan) - Supplementary material for the study: Space Lidar for Archaeology? Reanalyzing GEDI Data for Detection of Ancient Maya Buildings `R`
- [q_research](https://github.com/HeatherKmtb/q_research) - For processing of ICESat GLAS, GEDI and ICESat-2 LiDAR data, to derive q parameter for canopy height to density relationship `Python`
- [gedi-tutorials](https://github.com/ornldaac/gedi_tutorials) - GEDI L3 and L4 Tutorials 

## InSAR

- [ISCE](https://github.com/isce-framework/isce3) - InSAR Scientific Computing Environment version 3 alpha
- [LiCSBAS](https://github.com/yumorishita/LiCSBAS) - LiCSBAS package to carry out InSAR time series analysis using LiCSAR products
- [MintPy](https://github.com/insarlab/MintPy) - Miami InSAR time-series software in Python
- [Pyrocko](https://pyrocko.org/) - Can be utilized flexibly for a variety of geophysical tasks, like seismological data processing and analysis, modelling of InSAR, GPS data and dynamic waveforms, or for seismic source characterization.
- [InSARFlow](https://github.com/levuvietphong/InSARFlow) - Parallel InSAR processing for Time-series analysis
- [PyRate](https://github.com/GeoscienceAustralia/PyRate) - A Python tool for estimating velocity and time-series from Interferometric Synthetic Aperture Radar (InSAR) data.
- [ARIRA-tools](https://github.com/aria-tools/ARIA-tools) - Tools for exploiting ARIA standard products `Python`
- [ISCE_utils](https://github.com/EJFielding/ISCE_utils) - Small utility scripts for working with InSAR Scientific Computing Environment (ISCE) products `Python`
- [ROI_PAC-Sentinel1](https://github.com/RaphaelGrandin/ROI_PAC-Sentinel1) - InSAR processing of Sentinel-1 using ROI_PAC
- [insar_scripts](https://github.com/scottyhq/insar_scripts) - Useful scripts for working with roipac data `Python`
- [isce2](https://github.com/isce-framework/isce2) - InSAR Scientific Computing Environment version 2 `Python`
- [snap2stamps](https://github.com/mdelgadoblasco/snap2stamps) - Using SNAP as InSAR processor for StaMPS

## Landuse

- [demeter](https://github.com/JGCRI/demeter) - A land use land cover disaggregation and change detection model  `Python`

## Visualisation

- [Tiled video!](http://gena.github.io/experiments/mapbox/debug/tiled-video-no2.html)
- [Video map](https://github.com/openearth/videomap) - Tools to create, , export and share video maps
- [Tree height and canopy cover map in 3D](https://github.com/nkeikon/GEDI-experiment) - Use Kepler.gl to visualise 3D and 2D data
- [Greppo](https://github.com/greppo-io/greppo) - Python framework for building geospatial web-applications 

## Regular blogs of significant interest or posts of interest

- [Philipp Gartner blog](https://philippgaertner.github.io/)
- [Series Temporelles](https://labo.obs-mip.fr/multitemp/)
- [The downlinq](https://medium.com/the-downlinq)
- [GEDI canopy data](https://medium.com/@abt0020/extracting-canopy-height-with-gedi-data-5af8c87df158) - How we processed data to retrieving canopy height

## EO code Competitions

- [challenges 2020](https://github.com/esowc/challenges_2020) - ECMWF Summer of Weather Code 2020 challenges
- [challenges 2021](https://github.com/esowc/challenges_2021) - ECMWF Summer of Weather Code 2021 challenges
- [Julia Wagemann github](https://github.com/jwagemann) - Making open meteorological and climate data better accessible. `Python`, `Jupyter` and `R`. 
- See also [Sentinel hub competitions](https://www.sentinel-hub.com/develop/community/contest/)
<br><i>'older' competitions of note</i></br>
- [Planet: Understanding the Amazon from Space](https://www.kaggle.com/c/planet-understanding-the-amazon-from-space/overview) - Use satellite data to track the human footprint in the Amazon rainforest
- [DeepGlobe Building Extraction Challenge](https://competitions.codalab.org/competitions/18544) - We would like to pose the challenge of automatically detecting buildings from satellite images.
- [DSTL feature extraction](https://www.kaggle.com/c/dstl-satellite-imagery-feature-detection) - Kagglers are challenged to accurately classify features in overhead imagery
- [crowdAI misisng maps challenge](https://www.aicrowd.com/challenges/mapping-challenge) - Building Missing Maps with Machine Learning
  - [openAI solution](https://github.com/neptune-ai/open-solution-mapping-challenge) - Open solution to the Mapping Challenge
- [AtmosHack2018](https://github.com/wekeo/AtmosHack2018) - Contains information and resources for Copernicus Hackathon 2018 in Helsinki
- [drivendataorg - cloud-cover-winners](https://github.com/drivendataorg/cloud-cover-winners) - Code from the winning submissions for the On Cloud N: Cloud Cover Detection Challenge 

## ARD links

- [S1_S2_ARD_code_list](https://github.com/jncc/s1-s2-ard-code-list) - A curated list supporting the use of Sentinel-1 and Sentinel-2 analysis-ready data (ARD) via application programming interface (API)

## Useful EO code based twitter accounts

- [pyGEDI](https://twitter.com/pyGEDI) - pyGEDI is a Python Package for NASA's Global Ecosystem Dynamics Investigation (GEDI) mission, data extraction, analysis, processing and visualization.

## Great Github accounts

Please do explore these accounts, there are some absolutely brilliant projects on these accounts. This was previously a section containing examples, but these are better grouped into the other headings and repitition of links removed. However I feel its very important to highlight individuals wherever possible, ordered by github account name.

| [Chis Holden](https://github.com/ceholden) | [Christoph Rieke](https://github.com/chrieke) | [gena](https://github.com/gena) | [jgomezdans](https://github.com/jgomezdans) - [blog](http://jgomezdans.github.io/) | [Johntruckhenbrodt](https://github.com/johntruckenbrodt) | [Marcus Netler](https://github.com/neteler) | [Oliverhagolle](https://github.com/olivierhagolle) | [PerryGeo](https://github.com/perrygeo) | [giswqs - Qiusheng Wu](https://github.com/giswqs) | [rhammell](https://github.com/rhammell) | [Remote pixel](https://github.com/RemotePixel) | [robintw](https://github.com/robintw) | [Evan Roualt](https://github.com/rouault) | [samapriya](https://github.com/samapriya) | [shakasom](https://github.com/shakasom) | [yannforget](https://github.com/yannforget) | [Pete Bunting](https://github.com/petebunting) | [Vincent Sarago](https://github.com/vincentsarago) | 

## EO Geospatial companies or orgs making big contributions

Github accounts only with examples of work. This section used to contain examples of work, these have been now regrouped into other sections to make them easier to find.

| [development seed](https://github.com/developmentseed) | [mapbox](https://github.com/mapbox) | [Planet Labs, now just Planet](https://github.com/planetlabs) | [Digital Globe - now Maxar](https://github.com/DigitalGlobe) | [Azavea](https://github.com/azavea) | [Radiant Earth foundation](https://github.com/radiantearth) | [Sentinel Hub](https://github.com/sentinel-hub) | [PyTroll](https://github.com/pytroll) | [CosmiQ](https://github.com/CosmiQ) | [Theia software and tools](https://www.theia-land.fr/en/softwares-and-tools/) | [sparkgeo](https://github.com/sparkgeo) | [Geoscience Australia](https://github.com/GeoscienceAustralia) | [Dymaxion Labs](https://github.com/dymaxionlabs) | [Satellogic](https://github.com/satellogic) | [senbox-org](https://github.com/senbox-org) | [Nasa-gibs](https://github.com/nasa-gibs) | [mundialis](https://github.com/mundialis) | [ESA_PhiLab](https://github.com/ESA-PhiLab) | [Element 84](https://github.com/Element84)

## Interesting Non EO parts Python

This bit could potentially become the most valuable resource. Lets not ignore other sectors/industries/data science, instead lets embrace it and learn from all that other amazing stuff! This my prelude to saying we are earth data scientists

- [realtime covid19 graphs in USA](https://github.com/k-sys/covid-19) - A collection of work related to COVID-19
- [Deep learning with Python notebooks](https://github.com/fchollet/deep-learning-with-python-notebooks) - Jupyter notebooks for the code samples of the book "Deep Learning with Python"
- [Python data science handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [A-Z of tips and tricks for Python](https://www.freecodecamp.org/news/an-a-z-of-useful-python-tricks-b467524ee747/) - 'Most of these ‘tricks’ are things I’ve used or stumbled upon during my day-to-day work. '
- [Visual intro into Numpy](https://jalammar.github.io/visual-numpy/)- Visualizing machine learning one concept at a time
- [Change your Jupyter Theme](https://github.com/dunovank/jupyter-themes) - Custom Jupyter Notebook Themes
- [Awesome Semantic Segmentation](https://github.com/mrgloom/awesome-semantic-segmentation) - awesome-semantic-segmentation
- [unidata Python workshop](https://unidata.github.io/python-training/workshop/workshop-intro/) - Would you like some in-depth training on the scientific Python ecosystem for atmospheric science and meteorology? Work through our workshop materials at your own pace to learn and practice the syntax, functionality, and utility of this powerful programming language, or return to the material after taking the workshop in-person to further your understanding of the material you were taught.
- [TernausNet - used in DSTL kaggle competition (came 3rd)](https://github.com/ternaus/TernausNet) - UNet model with VGG11 encoder pre-trained on Kaggle Carvana dataset
- [Introduction to Python for computational science](https://github.com/fangohr/introduction-to-python-for-computational-science-and-engineering) - Book: Introduction to Python for Computational Science and Engineering
- [Another Book on Data Science](https://www.anotherbookondatascience.com/) - Learn R and Python in Parallel
- [Xarray](https://github.com/pydata/xarray) - N-D labeled arrays and datasets in Python
- [Matplotlib colab notebook tutorial](https://colab.research.google.com/github/ageron/handson-ml2/blob/master/tools_matplotlib.ipynb#scrollTo=gG7Fh4EMV2ey) - This notebook demonstrates how to use the matplotlib library to plot beautiful graphs.
- [PostGIS raster cheatsheet](http://www.postgis.us/downloads/postgis20_raster_cheatsheet.pdf) - Useful tips on rasters in PostGIS
- [65 data science books on Springer](https://towardsdatascience.com/springer-has-released-65-machine-learning-and-data-books-for-free-961f8181f189) - not checked but perhaps useful
- [Intro to Numerical Computing - youtube](https://www.youtube.com/watch?v=V0D2mhVt7NE) - Intro to Numerical Computing with NumPy (Beginner) | SciPy 2018 Tutorial | Alex Chabot-Leclerc
- [Classification-Algorithm](https://github.com/usmanr149/Classification-Algorithm) - Classification algorithm workshop for WiMLDS `Python`
- [dtreeviz](https://github.com/parrt/dtreeviz) - A `Python` library for decision tree visualization and model interpretation.
- [Python_tips](https://github.com/gpetepg/python_tips) - Some Python tips for beginner to intermediate users. Also used as a personal cheat sheet.
- [introduction to ml with Python](https://github.com/amueller/introduction_to_ml_with_python) - Notebooks and code for the book "Introduction to Machine Learning with `Python`"
- [Matplotlib_Cheatsheet](https://nbviewer.jupyter.org/urls/gist.githubusercontent.com/Jwink3101/e6b57eba3beca4b05ec146d9e38fc839/raw/f486ca3dcad44c33fc4e7ddedc1f83b82c02b492/Matplotlib_Cheatsheet) - Matplotlib_Cheatsheet `Python`
- [GDSL-UL/Teaching_Links](https://github.com/GDSL-UL/Teaching_Links) - In this repo we have aimed to provide links to useful teaching resources for teaching Geographic / Spatial Data Science, GIS and Statistics. (perhaps misplaced in this list?)
- [practical-python](https://dabeaz-course.github.io/practical-python/) - Practical Python Programming A course by @dabeaz
- [GeoStats, Resources](https://github.com/GeostatsGuy/Resources/blob/master/README.md) - Geostatistics

## Interesting Non EO parts other languages

This section is aimed more a data science/programming resources that 'might' be applicable to Earth Observation, that are <b>not </b>Python

- [Efficient R programming](https://csgillespie.github.io/efficientR/) - This is the online version of the O’Reilly book: Efficient R programming. Code is [here](https://github.com/csgillespie/efficientR)

## Data

I don't really want to add many data resources to this list as it creeps out of scope but this part contains some good data links [not necessarily EO]

- [Environmental_Intelligence](https://github.com/rockita/Environmental_Intelligence) - Data for Environmental Intelligence: A mega list of Earth System Datasets covering earth observations, climate, water, forests, biodiversity, ecology, protected areas, natural hazards, marine and the tracking of UN's Sustainable Development Goals
- [gibs](https://earthdata.nasa.gov/eosdis/science-system-description/eosdis-components/gibs) - This is EO
- [awesome-gee-community-datasets](https://samapriya.github.io/awesome-gee-community-datasets/) - Community Datasets added by users and made available for use at large 

## A footnote on awesome

There are many awesome lists relating to 'Geo'. I use that term as widely as possible. This list is not meant to replace these lists. Earth Observation is still <b>way</b> behind the GIS world in terms of audience, reach, number of users etc. Things are changing though, by bringing these links together I hope you can see that there has been so much progress in the last 5 years. I do hope these links are helpful espcially to those who are new to Earth Observation, but also to people like me who with several years of experience think they may have seen it all - we haven't and there is still so much to learn. Earth Observation is not just an academic 'thing' or a basemap anymore, it forms the basis for a growing and diverse business environment. Lets embrace this.

Finally, I wanted to acknowledge a couple of awesome Earth Observation lists that you may list to check out:

- [Awesome Sentinel](https://github.com/Fernerkundung/awesome-sentinel) - curated list of awesome tools, tutorials and APIs for Copernicus Sentinel satellite data
- [awesome-remote-sensing](https://github.com/attibalazs/awesome-remote-sensing) - Collection of Remote Sensing Resources
- [awesome-Geospatial](https://github.com/sacridini/Awesome-Geospatial) - Long list of geospatial tools and resources
- [awesome-remote-sensing-change-detection](https://github.com/wenhwu/awesome-remote-sensing-change-detection) - List of datasets, codes, and contests related to remote sensing change detection.
- [Awesome Geospatial Companies](https://github.com/chrieke/awesome-geospatial-companies) - List of 500+ geospatial companies (GIS, Earth Observation, UAV, Satellite, Digital Farming, ..)

#### End

[![CC BY 1.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 1.0 International License][cc-by].

[![CC BY 1.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/1.0/
[cc-by-image]: https://i.creativecommons.org/l/by/1.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%201.0-lightgrey
