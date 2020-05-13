# Awesome-EarthObservation-Code

A curated list of awesome tools, tutorials, code, helpful projects, links, stuff about Earth Observation and Geospatial stuff!

<p align="center">
  <img width="300" height="300" src="https://geogerservices.files.wordpress.com/2018/06/scenefromabovepodcast.jpg?w=300&h=300">
</p>

## This list was started based on #scenefromabove podcast lunchtime discussions

This is being extended frequently in May 2020. Please note that this is <b>not</b> offically an awesome list (yet). Please help me to get it there by contributing and commenting. [guidelines](https://github.com/sindresorhus/awesome/blob/master/contributing.md)

<b> Update May 2020</b> We now have almost 300 links/resources. The focus at the moment is resorting and ordering all these links and potentially reclassifiying where needed. I think there are still 100-200 more resources potentially to add. I plan to add to <b>EO Geospatial companies or orgs making big contributions</b> section and then break into sections and just keep company. Still more to add prior to this.

Annotations are based on the headers - where available - on the github accounts

<div align="center">

# [Scene From Above Podcast](http://scenefromabove.org/)

</div>

Alastair Graham [@ajggeoger](https://twitter.com/ajggeoger) and Andrew Cutts [@map_andrew](https://twitter.com/map_andrew) come together to present an informal podcast [@eoscenefrom](https://twitter.com/eoscenefrom) looking at the world of modern remote sensing and EO.
Fuelled by their passion for all things raster and geospatial, the #scenefromabove podcast aims to be a mix of news, opinion, discussion and interviews. <br>

# Contents

<b>Shortcuts</b>

|   [Python processing](#python-processing-of-optical-imagery-non-deep-learning)   |   [Resources for R](#resources-for-r)   |   [Languages other than Python](#languages-other-than-python)  |  [Training and Learning](#training-and-learning)   |   [Deep Learning & Machine Learning](#deep-learning-and-machine-learning)   |   [List of Great GitHub accounts](#great-github-accounts)   |   [GDAL of course](#gdal-of-course)   |   [Earth Observation coding on YouTube](#earth-observation-coding-on-youtube)   |   [Google Earth Engine](#earth-engine)   |   [EO Geospatial companies or orgs making big contributions](#eo-geospatial-companies-or-orgs-making-big-contributions)   |   [Open Data Cube](#open-data-cube)   |   [QGIS and Grass](#qgis-and-grass)   |   [Climate & Weather resources](#climate-and-weather-based-resources)   |   [DEM projects](#dem-projects)   |   [SAR](#sar)   |   [LiDAR](#lidar)   |   [InSAR](#insar)   |   [Visualisation](#visualisation)   |   [EO code Competitions](#eo-code-competitions)   |   [Useful EO code based twitter accounts](#useful-eo-code-based-twitter-accounts)|

These sections are non EO code specific, but included to be relevant
|   [Interesting Non EO parts Python](#interesting-non-eo-parts-python)   |   [Interesting Non EO parts other languages](#interesting-non-eo-parts-other-languages)   |   [Data](#data)   |   [A footnote on awesome](#a-footnote-on-awesome)

#### Start Here

OpenEO covers many of the bases, hard to know whether to break it into different categories, it has many components. At present I mention it here at the start only.<br>

- [Open EO](https://openeo.org/) - openEO develops an open API to connect `R`, `Python`, `JavaScript` and other clients to big Earth observation cloud back-ends in a simple and unified way.

You may also wish to navigate a search of the terms `satellite-imagery` and `earth-observation` to get the lastest list of topics that have these terms in their headers
- [satellite-imagery](https://github.com/topics/satellite-imagery)
- [earth-observation](https://github.com/topics/earth-observation)

## `Python` processing of optical imagery non deep learning
This section full of great code and projects related to processing optical satellite imagery with `Python`
- [StarFM for Python](https://github.com/nmileva/starfm4py) - The STARFM fusion model for `Python` (image fusion)
- [Python from space](https://github.com/kscottz/PythonFromSpace) - `Python` Examples for Remote Sensing
- [count blue pixels](https://github.com/craic/count_shelters) - This project is an experiment in using simple image processing techniques on satellite images downloaded from Google Maps in order to quantify the relative density of temporary shelters in adjacent qudarants. `Python` `Ruby`
- [Satellite imagery analysis with Python](https://github.com/parulnith/Satellite-Imagery-Analysis-with-Python) - Getting acquainted with the concept of satellite imagery data and how it can be analyzed to investigate real-world environmental and humanitarian challenges. `Python` `Jupyter Notebooks` [associated blog](https://medium.com/analytics-vidhya/satellite-imagery-analysis-with-python-3f8ccf8a7c32)
- [Povetry predition using satellite imagery](https://github.com/carsonluuu/Poverty-Prediction-by-Satellite-Imagery) - Poverty Prediction by Combination of Satellite Imagery
- [Remote Sensing indicies calc](https://github.com/rander38/Remote-Sensing-Indices-Derivation-Tool) - Calculate spectral remote sensing indices from satellite imagery
- [Satellite imagery in Pakistan](https://github.com/iam-mhaseeb/Satellite-Imagery-Analysis-of-Vegetation-in-Southern-Pakistan) - This repository contains a study how we can examine the vegetation cover of a region with the help of satellite data. The notebook in this repository aims to familiarise with the concept of satellite imagery data and how it can be analyzed to investigate real-world environmental and humanitarian challenges.
- [esa_sentinel](https://github.com/jonas-eberle/esa_sentinel) - ESA Sentinel Search & Download API 
- [EarthPy](https://github.com/earthlab/earthpy) - A package built to support working with spatial data using open source python. [docs](https://earthpy.readthedocs.io/en/latest/)
- [RasterFrames / pyrasterframes](https://github.com/locationtech/rasterframes) - brings together Earth-observation (EO) data access, cloud computing, and DataFrame-based data science. [docs](https://rasterframes.io/)
- [SIF tools](https://github.com/cfranken/SIF_tools) - some tools for accessing OCO-2 data 
- [SIAC](https://github.com/MarcYin/SIAC) - A sensor invariant Atmospheric Correction (SIAC) [alg doc](http://www2.geog.ucl.ac.uk/~ucfafyi/Atmo_Cor/)
- [S2_TOA_TO_LAI](https://github.com/MarcYin/S2_TOA_TO_LAI) - From Sentinel 2 TOA reflectance to LAI 
- [cresi](https://github.com/avanetten/cresi) - Road network extraction from satellite imagery, with speed and travel time estmates 
- [COG Validator](https://github.com/rouault/cog_validator) - Cloud Optimized GeoTIFF validation service 
- [6S_emulator](https://github.com/samsammurphy/6S_emulator) - Atmospheric correction in Python using a 6S emulator 
- [bv](https://github.com/daleroberts/bv) - Quickly view satellite imagery, hyperspectral imagery, and machine learning image outputs directly in your iTerm2 terminal. `Python`
- [mapchete](https://github.com/ungarj/mapchete) - Tile-based geodata processing using rasterio & Fiona  `Python`
- [unmixing](https://github.com/arthur-e/unmixing) - Interactive tools for spectral mixture analysis of multispectral raster data in `Python`
- [Sedas API](https://github.com/SatelliteApplicationsCatapult/sedas_pyapi) - `Python` client library for the SeDAS API 
- [SentinelBot](https://github.com/JamesOConnor/Sentinel_bot) - A twitter bot which processes raw sentinel data `Python` [SentinelBot on twitter](https://twitter.com/sentinel_bot)
- [Py6S](https://github.com/robintw/Py6S) - A `Python`interface to the 6S Radiative Transfer Model 
- [Xarray pyconuk 2018](https://github.com/robintw/XArray_PyConUK2018) - Code and slides for my talk at PyCon UK 2018 on XArray `Python`
- [PyProSail](https://github.com/robintw/PyProSAIL) - Python interface to the ProSAIL leaf/canopy reflectance model 
- [gdbx-surface-water](https://github.com/gena/gbdx-surface-water) - Reservoir surface area detection with Digital Globe imagery and Bayesian methods 
- [Landsat7 errors](https://github.com/gena/landsat7-errors) - Identifies errors in raw values of Landsat 7 
- [get_modis](https://github.com/jgomezdans/get_modis) - Downloading MODIS data from the USGS repository `Python`
- [prosail](https://github.com/jgomezdans/prosail) - `Python` bindings for the PROSAIL canopy reflectance model 
- [landsatexplore](https://github.com/yannforget/landsatxplore) - Search and download Landsat scenes from EarthExplorer. `Python`
- [pylandsat](https://github.com/yannforget/pylandsat) - Search, download, and preprocess Landsat imagery `Python`
- [landsat and sentinel fusion](https://github.com/yannforget/landsat-sentinel-fusion) - Complementarity Between Sentinel-1 and Landsat 8 Imagery for Built-Up Mapping in Sub-Saharan Africa `Python`
- [pyimpute](https://github.com/perrygeo/pyimpute) - Spatial classification and regression using Scikit-learn and Rasterio `Python`
- [Planet Movement](https://github.com/rhammell/planet-movement) - Find and process Planet image pairs to highlight object movement. `Python` 
- [Sentinel-download](https://github.com/olivierhagolle/Sentinel-download) - Automated download of Sentinel-2 L1C data from ESA (through wget) `Python`
- [aws-sat-api-py](https://github.com/RemotePixel/remotepixel-api) - Process Satellite data using AWS Lambda functions
- [sentinelsat](https://github.com/sentinelsat/sentinelsat) - Search and download Copernicus Sentinel satellite images [sentinelsat docs](https://sentinelsat.readthedocs.io/en/stable/) `Python`
- [Whitebox Python](https://github.com/giswqs/whitebox-python) - WhiteboxTools `Python` Frontend
- [spatialist](https://github.com/johntruckenbrodt/spatialist) - A `Python` module for spatial data handling 
- [LANDSAT-Download](https://github.com/olivierhagolle/LANDSAT-Download) - Automated download of LANDSAT data from USGS website
- [RasterStats](https://github.com/perrygeo/python-rasterstats) - Summary statistics of geospatial raster datasets based on vector geometries. `Python`

## Resources for `R`

R is not my area of expertise so this section is lighter than I'd like, plus I'd love to know what is a useful resource

- [R-Spatial](https://rspatial.org/raster/rs/1-introduction.html) - This book provides a short introduction to satellite data analysis with R.
  - [Remote Sensing analysis with R](https://rspatial.org/raster/rs/index.html) - Builds on above R-Spatial
- [GDAL Cubes](https://cran.r-project.org/web/packages/gdalcubes/index.html) - Earth Observation Data Cubes from Satellite Image Collections. Also [here on github](https://github.com/appelmar/gdalcubes_R)
- [Image Classification with RandomForests in R](http://amsantac.co/blog/en/2015/11/28/classification-r.html) - The goal of this post is to demonstrate the ability of R to classify multispectral imagery using RandomForests algorithms.
- [R code for ML in Sat imagery](https://gist.github.com/franzalex/a95e227cab9b146a6092) - # Random Forest image classification Adapted from [stackoverflow](http://gis.stackexchange.com/a/57786/12899).
- [whiteboxR](https://github.com/giswqs/whiteboxR) - An R frontend of the advanced geospatial data analysis platform - [whitebox-tools](https://github.com/jblindsay/whitebox-tools).
- [RasterVIS](https://cran.r-project.org/web/packages/rasterVis/index.html) - Methods for enhanced visualization and interaction with raster data. It implements visualization methods for quantitative data and categorical data, both for univariate and multivariate rasters. It also provides methods to display spatiotemporal rasters, and vector fields. 
- [Landsat](https://cran.r-project.org/web/packages/landsat/index.html) - Processing of Landsat or other multispectral satellite imagery. Includes relative normalization, image-based radiometric correction, and topographic correction options.
- [rnoaa](https://github.com/ropensci/rnoaa) - R interface to many NOAA data APIs
- [MODISTools](https://github.com/ropensci/MODISTools) - Interface to the MODIS Land Products Subsets Web Services [Docs](https://docs.ropensci.org/MODISTools/)
- [A Step-by-Step Guide to Making 3D Maps with Satellite Imagery in R](https://www.tylermw.com/a-step-by-step-guide-to-making-3d-maps-with-satellite-imagery-in-r/) - Walk you through [on] how to obtain the data required to make these types of maps, as well as the R code used to generate them 
- [landsatlinkr](https://github.com/jdbcode/LandsatLinkr) - An automated system for creating spectrally consistent and cloud-free Landsat image time series stacks from a combination of MSS, TM, ETM+, and OLI sensors [project](http://jdbcode.github.io/LandsatLinkr/)
- [planetR](https://github.com/bevingtona/planetR) - (early development) R tools to search, activate and download satellite imagery from the Planet API

## Languages other than `Python`

- [Georust](https://github.com/georust) - A collection of geospatial tools and libraries written in `Rust`
- [ArchGDAL - Julia](https://github.com/yeesian/ArchGDAL.jl) - `Julia` A high level API for GDAL - Geospatial Data Abstract
  - [ArchGDAL docs](http://yeesian.com/ArchGDAL.jl/latest/)
- [Julia_Geospatial](https://github.com/acgeospatial/Julia_Geospatial) - Examples for a blog series on Geospatial `Julia` using ArchGDAL 
- [GeoTrellis homepage](https://geotrellis.io/) - GeoTrellis is a geographic data processing engine for high performance applications. `Scala`
  - [GeoTrellis on Github - Scala](https://github.com/locationtech/geotrellis) 
- [GDAL with GoLang](https://github.com/lukeroth/gdal) - `Go` (golang) wrapper for GDAL, the Geospatial Data Abstraction Library 
- [C++ gdalcubes](https://github.com/appelmar/gdalcubes) - Earth observation data cubes from GDAL image collections  `C++`
- [RSGLib](https://bitbucket.org/petebunting/rsgislib/src/bf7933996822/?at=default) - The remote sensing and GIS software library (RSGISLib) is a set of `C++` libraries and commands for the processing of spatial data (raster and vector). Functionality is via `Python` interface though
- [WhiteBox with Java](https://github.com/jblindsay/whitebox-geospatial-analysis-tools) - An open-source GIS and remote sensing package - `Java`
- [Perl extension for GDAL](https://metacpan.org/pod/Geo::GDAL) - Geo::GDAL - `Perl` extension for the GDAL library for geospatial data
- [PDAL](https://github.com/PDAL/PDAL) - PDAL is Point Data Abstraction Library. GDAL for point cloud data. 
- [force](https://github.com/davidfrantz/force) - Framework for Operational Radiometric Correction for Environmental monitoring in `c`
- [LLR-landTrendr](https://github.com/jdbcode/LLR-LandTrendr) - Landsat-based Detection of Trends in Disturbance and Recovery algorimth modified to accept LandsatLinkr-processed imagery. `IDL`
- [Global Forest Watch](https://github.com/Vizzuality/gfw) - Global Forest Watch: An online, global, near-real time forest monitoring tool 
- [conda recipes](https://github.com/yannforget/conda-recipes) - Conda recipes for remote sensing `Shell`


## Training and learning

- [Earth Data Lab](https://github.com/earthlab/earthlab.github.io) - A site dedicated to tutorials, course and other learning materials and resources developed by the Earth Lab team
- [EO College Github](https://github.com/EO-College)
  - [tomography_tutorial](https://github.com/EO-College/tomography_tutorial) - A tutorial for Synthetic Aperture Radar Tomography 
- [profLewis-geog0111](https://github.com/profLewis/geog0111) - UCL Geography: 4th year course, Scientific Computing
- [Intro to Geospatial Vector and Raster](https://carpentries-incubator.github.io/geospatial-python/) - Data Carpentry’s aim is to teach researchers basic concepts, skills, and tools for working with data so that they can get more done in less time, and with less pain.
- [Andrew Cutts Github](https://github.com/acgeospatial) - I am an Earth Observation and Geospatial enthusiast, primarily using `Python` to automate and process images at scale using computer vision
  - [Satelite Imagery Python](https://github.com/acgeospatial/Satellite_Imagery_Python) - Sample sample scripts and notebooks on processing satellite imagery
  - [Geospatial Python Programming Course](https://github.com/acgeospatial/Geospatial_Python_CourseV1) - This is an collection of blog posts turned into a course format
- [Open Geo Tutorial](https://github.com/patrickcgray/open-geo-tutorial) - Tutorial of fundamental remote sensing and GIS methodologies using open source software in `Python`
- [Foss4gUKJupyter](https://github.com/samfranklin/foss4guk19-jupyter) - FOSS4G UK 2019 Workshop "Geoprocessing with Jupyter Notebooks" 
- [Geoprocessing with Python - GIS circa 2009](https://www.gis.usu.edu/~chrisg/python/2009/) - This material is really old and some of it is outdated (not all, though!). One of these days I might get around to putting newer class materials online, but you're stuck with this for now.

## Deep learning and Machine Learning
<b>Curated lists</b>
- [Christoph Rieke git hub](https://github.com/chrieke/awesome-satellite-imagery-datasets) for much much more
- [Deep Vector](https://github.com/deepVector/geospatial-machine-learning) - A curated list of resources focused on Machine Learning in Geospatial Data Science. 
- [Robin Cole on satellite imagery and deep learning resources](https://github.com/robmarkcole/satellite-image-deep-learning) - Resources for deep learning with satellite & aerial imagery
<b>Specific examples</b>
- [TernausNetV2](https://github.com/ternaus/TernausNetV2) - TernausNetV2: Fully Convolutional Network for Instance Segmentation [paper](TernausNetV2: Fully Convolutional Network for Instance Segmentation) 
- [CNN-Sentinel](https://github.com/jensleitloff/CNN-Sentinel) -Analyzing Sentinel-2 satellite data in Python with Keras (repository of our talks at Minds Mastering Machines 2019 and PyCon 2018)
- [Image patches](https://github.com/Vooban/Smoothly-Blend-Image-Patches) - Using a U-Net for image segmentation, blending predicted patches smoothly is a must to please the human eye.
- [Fast AI Satellite imagery resources](https://forums.fast.ai/t/geospatial-deep-learning-resources-study-group/31044)
- [Crop yield prediction](https://github.com/meet-sapu/Crop-Yield-Prediction-Using-Satellite-Imagery) - The motive here is to predict the yield of crops of a particular farm by the change in pixels of the image of farm yearly. Uses Tensorflow
- [Houston Flooding with deep learning](https://github.com/Lichtphyz/Houston_flooding) - Using A Segmentation Neural Net to map out flooded areas of Houston TX using satellite imagery
- [Satellite Imagery Classification with R](https://github.com/kkgadiraju/SatelliteImageClassification) - Pixel based classification of satellite imagery - feature generation using Orfeo Toolbox, feature selection using Learning Vector Quantization, CLassification using Decision Tree, Neural Networks, Random Forests, KNN and Naive Bayes Classifier
- [SpaceNet building detection](https://github.com/motokimura/spacenet_building_detection) - Project to train/test convolutional neural networks to extract buildings from SpaceNet satellite imageries.
- [Road segmentation](https://github.com/Paulymorphous/Road-Segmentation) - Road Detection in satellite imagery. Semantic segmentation is the process of classifying each pixel of an image into distinct classes using deep learning. This aids in identifying regions in an image where certain objects reside.This aim of this project is to identify and segment roads in aerial imagery. Detecting roads can be an important factor in predicting further development of cities, and this concept plays a major role in GeoArchitect (A project which I started). Segmentation of roads is important to map-based applications and is used for finding distances or shortest routes between two places.
- [Super resolution (srcnn)](https://github.com/WarrenGreen/srcnn) - Super Resolution for Satellite Imagery
- [Pixel decoder](https://github.com/Geoyi/pixel-decoder) - A tool of running deep learning algorithms for semantic segmentation with satellite imagery
- [Detecting ships](https://github.com/ucalyptus/Detecting-Ships) - Using Satellite Imagery to detect ships (Basic Object Detection)
- [deepOSM](https://github.com/trailbehind/DeepOSM) - Train a deep learning net with OpenStreetMap features and satellite imagery.
- [Keras for computer vision (Maxime Lenormand GitHub)](https://github.com/MaxLenormand/Keras-for-computer-vision) - Introductions to Keras to perform computer vision tasks, with data exploration, error analysis and improving results. 
- [Airplane image classification](https://medium.com/@kylepob61392/airplane-image-classification-using-a-keras-cnn-22be506fdb53) - This article details building a ML pipeline to classify the presence of planes in satellite images using a Convolutional Neural Network (CNN).
- [TorchSat](https://github.com/sshuair/torchsat) - an open-source deep learning framework for satellite imagery analysis based on PyTorch. `Python` [docs](https://torchsat.readthedocs.io/en/latest/)
- [ml_drought](https://github.com/esowc/ml_drought) - Machine learning to better predict and understand drought `Python`. [docs](https://ml-clim.github.io/drought-prediction/)
- [pycrop yield prediction](https://github.com/gabrieltseng/pycrop-yield-prediction) - A PyTorch Implementation of Jiaxuan You's Deep Gaussian Process for Crop Yield Prediction `Python`
- [neat-EO](https://datapink.io/datapink/neat-EO/) - Efficient AI4EO OpenSource framework `Python`
- [dfc2020_baseline](https://github.com/lukasliebel/dfc2020_baseline) - Simple Baseline for the IEEE GRSS Data Fusion Contest 2020 `Python`
- [Planesnet](https://github.com/rhammell/planesnet) - Labeled training data for detection of aircraft in Planet satellite imagery 
- [Planesnet detector](https://github.com/rhammell/planesnet-detector) - Detect airplanes in Planet imagery using machine learning 
- [shipsnet](https://github.com/rhammell/shipsnet-detector) - Detect container ships in Planet imagery using machine learning 
- [Deep Learning for satellite imagery](https://github.com/shakasom/Deep-Learning-for-Satellite-Imagery) - Deep learning courses and projects
- [DeepNetsForEO](https://github.com/nshaud/DeepNetsForEO) - Deep networks for Earth Observation 

## Great Github accounts
Please do explore these accounts, there are some absolutely brilliant projects on these accounts. This was previously a section containing examples, but these are better grouped into the other headings and repitition of links removed. However I feel its very important to highlight individuals wherever possible, ordered by github account name.

|   [Christoph Rieke git hub](https://github.com/chrieke)   |   [Fernerkundung](https://github.com/Fernerkundung/)   |   [gena github](https://github.com/gena)   |   [jgomezdans github](https://github.com/jgomezdans) - [blog](http://jgomezdans.github.io/)   |   [Johntruckhenbrodt github](https://github.com/johntruckenbrodt)   |   [Marcus Netler on github](https://github.com/neteler)   |   [Oliverhagolle github](https://github.com/olivierhagolle)   |   [PerryGeo](https://github.com/perrygeo)   |   [giswqs - Qiusheng Wu github](https://github.com/giswqs)   |   [rhammell](https://github.com/rhammell)   |   [Remote pixel github](https://github.com/RemotePixel)   |   [robintw](https://github.com/robintw)   |   [Evan Roualt github](https://github.com/rouault)   |   [samapriya github](https://github.com/samapriya)   |   [shakasom github](https://github.com/shakasom)   |   [yannforget github](https://github.com/yannforget)   |


## GDAL of course

- [GDAL Cheat Sheet](https://github.com/dwtkns/gdal-cheat-sheet) - Cheat sheet for GDAL/OGR command-line tools
- [GDAL / OGR cookbook](https://pcjericks.github.io/py-gdalogr-cookbook/) - This cookbook has simple code snippets on how to use the Python GDAL/OGR API
- [GDAL tutorial](https://jakobmiksch.eu/post/gdal_ogr/) - This blogpost gives in an introduction to GDAL/OGR and explains how the various command line tools can be used.
- [docker-base-gdal](https://github.com/perrygeo/docker-gdal-base) - A base docker image for geospatial applications 

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

## Earth Engine
`JavaScript` & `Python` & `R`
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
- [rgee](https://github.com/csaybar/rgee) - Google Earth Engine for `R` [docs](https://csaybar.github.io/rgee/) 

## EO Geospatial companies or orgs making big contributions

Github accounts only with examples of work. Also contains (Python) libraries for processing satellite data. This list aims at highlighting the great work some of the companies / organisations are doing or have done that contribute to the bigger ecosystem. Examples of the accounts work is not exhaustive, some do much more than shown below:
- [development seed](https://github.com/developmentseed)
  - [Landsat-Util](https://github.com/developmentseed/landsat-util) - A utility to search, download and process Landsat 8 satellite imagery `Python`
  - [GeoLamda](https://github.com/developmentseed/geolambda) - Create and deploy Geospatial AWS Lambda functions `Python`
  - [LabelMaker](https://github.com/developmentseed/label-maker) - Data Preparation for Satellite Machine Learning [docs](http://devseed.com/label-maker/) `Python`
  - [rio-viz](https://github.com/developmentseed/rio-viz) - Visualize Cloud Optimized GeoTIFF in browser  `html` `Python`
  - [cogeo-mosaic](https://github.com/developmentseed/cogeo-mosaic) - Create and use COG mosaic based on mosaicJSON `Pythoon`
  - [Sentinel-2-cog](https://github.com/developmentseed/sentinel-2-cog) - Convert Sentinel-2 JPEG 2000 to COG with AWS Lambda `Python`
  - [Sentinel-s3](https://github.com/developmentseed/sentinel-s3) - Python libraries for extracting Sentinel-2's metadata from Amazon S3 
- [mapbox](https://github.com/mapbox)
  - [rasterio](https://github.com/mapbox/rasterio) - Rasterio reads and writes geospatial raster datasets
  - [Robosat](https://github.com/mapbox/robosat) - Semantic segmentation on aerial and satellite imagery. Extracts features such as: buildings, parking lots, roads, water, clouds
- [Planet Labs, now just Planet](https://github.com/planetlabs)
  - [Planet notebooks](https://github.com/planetlabs/notebooks) - interactive notebooks from Planet Engineering `Python`
  - [staccato](https://github.com/planetlabs/staccato) - `Java` implementation of the STAC spec 
  - [Planet-client-API](https://github.com/planetlabs/planet-client-python) - `Python` client for Planet APIs 
  - [training-workshop](https://github.com/planetlabs/training-workshop) - This repo contains all materials used on Planet's training workshop for Bahrain Defense Force
- [Digital Globe - now Maxar](https://github.com/DigitalGlobe)
  - [Maxar GDBx tools](https://github.com/DigitalGlobe/gbdxtools) - Python SDK for using GBDX.
- [Azavea](https://github.com/azavea)
  - [Azavea - RasterVision](https://github.com/azavea/raster-vision) - An open source framework for deep learning on satellite and aerial imagery.
  - [pystac](https://github.com/azavea/pystac) - `Python` library for working with any SpatioTemporal Asset Catalog (STAC) 
  - [loam](https://github.com/azavea/loam) - `Javascript` wrapper for GDAL in the browser 
  - [raster-vision-aws](https://github.com/azavea/raster-vision-aws) - A CloudFormation template for deploying Raster Vision Batch jobs to AWS. 
  - [stac4s](https://github.com/azavea/stac4s)  -a `scala` library with primitives to build applications using the SpatioTemporal Asset Catalogs specification 
- [Radiant Earth foundation](https://github.com/radiantearth)
  - [STAC Spec](https://github.com/radiantearth/stac-spec) - SpatioTemporal Asset Catalog specification - making geospatial assets openly searchable and crawlable
  - [stac-browser](https://github.com/radiantearth/stac-browser) - A Vue-based STAC browser intended for static + dynamic deployment
  - [mlhub-tutorials](https://github.com/radiantearth/mlhub-tutorials) - Tutorials to access Radiant MLHub Training Datasets `Python` [mlhub](https://mlhub.earth/)
- [Sentinel Hub](https://github.com/sentinel-hub)
  - [EO Learn](https://github.com/sentinel-hub/eo-learn) - Earth observation processing framework for machine learning in Python
  - [EO Browser Custom Scripts](https://github.com/sentinel-hub/custom-scripts) - A repository of custom scripts to be used with Sentinel Hub
  - [EO flow](https://github.com/sentinel-hub/eo-flow) - Collection of TensorFlow 2.0 code for Earth Observation applications
  - [SentinelHub-py](https://github.com/sentinel-hub/sentinelhub-py) - Download and process satellite imagery in Python using Sentinel Hub services. 
  - [sentinel2-cloud-detector](https://github.com/sentinel-hub/sentinel2-cloud-detector) - Sentinel Hub Cloud Detector for Sentinel-2 images in `Python`
  - [sentinelhub-js](https://github.com/sentinel-hub/sentinelhub-js) - Download and process satellite imagery in `JavaScript` or `TypeScript` using Sentinel Hub services. 
- [PyTroll](https://github.com/pytroll)
  - [SatPy](https://github.com/pytroll/satpy) - Python package for earth-observing satellite data processing
  - [pyresample](https://github.com/pytroll/pyresample) - Geospatial image resampling in Python
- [CosmiQ](https://github.com/CosmiQ)
  - [Solaris](https://github.com/cosmiq/solaris) - CosmiQ Works Geospatial Machine Learning Analysis Toolkit
    - [docs](https://solaris.readthedocs.io/en/latest/)
  - [CometTS](https://github.com/CosmiQ/CometTS) - Comet Time Series Toolset for working with a time-series of remote sensing imagery and user defined polygons 
  - [SpaceNet6 Baseline](https://github.com/CosmiQ/CosmiQ_SN6_Baseline) - Baseline algorithm for the SpaceNet 6 Challenge 
- [Theia software and tools](https://www.theia-land.fr/en/softwares-and-tools/)
- [sparkgeo](https://github.com/sparkgeo)
  - [stac-validator](https://github.com/sparkgeo/stac-validator) - Validator for the stac-spec 
- [Geoscience Australia](https://github.com/GeoscienceAustralia)
  - [PyRate](https://github.com/GeoscienceAustralia/PyRate) - A Python tool for estimating velocity and time-series from Interferometric Synthetic Aperture Radar (InSAR) data.
- [Dymaxion Labs](https://github.com/dymaxionlabs)
  - [dask-rasterio](https://github.com/dymaxionlabs/dask-rasterio) - Read and write rasters in parallel using Rasterio and Dask 
  - [ap-latem](https://github.com/dymaxionlabs/ap-latam) - Detection of slums and informal settlements from satellite imagery
- [Satellogic](https://github.com/satellogic)
  - [Telluric](https://github.com/satellogic/telluric) - telluric is a Python library to manage vector and raster geospatial data in an interactive and easy way 
  - [Orbit predictor](https://github.com/satellogic/orbit-predictor) - Python library to propagate satellite orbits. 
- [senbox-org](https://github.com/senbox-org) - SNAP - ESA's SentiNel Application Platform 
  - [s3tbx](https://github.com/senbox-org/s3tbx) - A toolbox for the OLCI and SLSTR instruments on board of ESA's Sentinel-3 satellite - `Java`
  - [s2tbx](https://github.com/senbox-org/s2tbx) - Sentinel 2 Toolbox (s2tbx) - `Java`
  - [s1tbx](https://github.com/senbox-org/s1tbx) - The Sentinel-1 Toolbox - `Java`
  - [snap_engine](https://github.com/senbox-org/snap-engine) - ESA Earth Observation Toolbox and `Java` Development Platform
- [Nasa-gibs](https://github.com/nasa-gibs) - for info [here](https://earthdata.nasa.gov/eosdis/science-system-description/eosdis-components/gibs)
  - [onearth](https://github.com/nasa-gibs/onearth) - High-performance web services for tiled raster imagery and vector tiles 
  - [Worldview](https://github.com/nasa-gibs/worldview) - Interactive interface for browsing global, full-resolution satellite imagery `Javascript` application [here](https://worldview.earthdata.nasa.gov/)
  - [mrf](https://github.com/nasa-gibs/mrf) - GDAL-compatible file format driver designed for fast access to imagery 
- [mundialis](https://github.com/mundialis)
  - [actinia core](https://github.com/mundialis/actinia_core) - Actinia Core is an open source REST API for scalable, distributed, high performance processing of geographical data that uses mainly GRASS GIS for computational tasks.
  - [actinia plugin](https://github.com/mundialis/actinia_satellite_plugin) - This actinia plugin is designed for efficient satellite data handling, especially Landsat and Sentinel-2 scenes 

## Open Data Cube
- [Opendatacube](https://github.com/opendatacube)
  - [Opendatacube -core](https://github.com/opendatacube/datacube-core) - Open Data Cube analyses continental scale Earth Observation data through time
  - [Opendatacube notebooks](https://github.com/opendatacube/datacube-notebooks) - Extra documentation about using ODC with Jupyter Notebooks
- [data_cube_ui](https://github.com/ceos-seo/data_cube_ui) - Data Cube user interface allowing users to interact with the Data Cube and run sample analysis cases
- [data_cube_utilities](https://github.com/ceos-seo/data_cube_utilities) - Various algorithms and processing functions for Data Cube raster data
- [Digital Earth Australia Notebooks](https://github.com/GeoscienceAustralia/dea-notebooks) - Repository for Jupyter Notebooks, tools and workflows for continental-scale earth observation/geospatial analysis with Open Data Cube and `xarray` `Python`

## QGIS and Grass

- [Qgis Earth Engine Plugin](https://github.com/gee-community/qgis-earthengine-plugin) - Integrates Google Earth Engine and QGIS using Python API
  - [QGIS Earth Engine Plugin - installation guide](https://gee-community.github.io/qgis-earthengine-plugin/)
- [grass-dev-py3-pdal](https://github.com/neteler/grass-dev-py3-pdal) - Dockerfile which compiles GRASS GIS 7.9 master with Python 3 and PDAL suppor
- [qgis-plugin-planet](https://github.com/planetlabs/qgis-planet-plugin) - Browse, filter, preview and download Planet Inc imagery in QGIS. `Python`

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


## DEM projects
- [Tin Terrain](https://github.com/heremaps/tin-terrain) - A command-line tool for converting heightmaps in GeoTIFF format into tiled optimized meshes. 
- [TauDEM](https://github.com/dtarb/TauDEM) - Terrain Analysis Using Digital Elevation Models (TauDEM) software for hydrologic terrain analysis and channel network extraction. [Docs](http://hydrology.usu.edu/taudem/taudem5/index.html)
- [DEM.net](https://github.com/dem-net/DEM.Net) - Digital Elevation model library in C#. 3D terrain models, line/point Elevations, intervisibility reports. [Docs](https://elevationapi.com/)
- [Stereo Mapping to create Elevation with Python](https://github.com/cmla/s2p) - Satellite Stereo Pipeline

## SAR

- [SAR docker](https://github.com/mortcanty/SARDocker) - Source files for Docker image mort/sardocker/
- [awesome SAR](https://github.com/lveci/awesome-sar) - A curated list of awesome Synthetic Aperture Radar (SAR) software, libraries, and resources. 
- [pyroSAR](https://github.com/johntruckenbrodt/pyroSAR) - framework for large-scale SAR satellite data processing 

## LiDAR

- [pyGEDI](https://github.com/EduinHSERNA/pyGEDI) - pyGEDI is a Python Package for NASA's Global Ecosystem Dynamics Investigation (GEDI) mission, data extraction, analysis, processing and visualization.
- [GEDI extraction script](https://gist.github.com/KMarkert/c68ccf53260d7b775b836bf2e11e2ec3) - Python script to take GEDI level 2 data and convert variables to a geospatial vector format
- [rGEDI](https://github.com/carlos-alberto-silva/rGEDI) - rGEDI: An R Package for NASA's Global Ecosystem Dynamics Investigation (GEDI) Data Visualization and Processing.
- [ICESAT extraction script](https://gist.github.com/bzgeo/950f3db986b3513311ed42efe2395171) - Python script to convert from ICESat-2 ATL08 HDF data to shapefile. Usage: 'python icesat2_shp.py
- [ICESAT tools](https://github.com/icesat-2UT/PhoREAL) - Tools and code for Icesat-2 data analysis (Python)
- [usgs-lidar](https://github.com/hobu/usgs-lidar) - AWS Entwine Point Tiles USGS LiDAR Public Dataset GitHub repo
- [Lidar](https://github.com/giswqs/lidar) - Terrain and hydrological analysis based on LiDAR-derived digital elevation models (DEM)  

## InSAR
- [ISCE](https://github.com/isce-framework/isce3) - InSAR Scientific Computing Environment version 3 alpha 
- [LiCSBAS](https://github.com/yumorishita/LiCSBAS) - LiCSBAS package to carry out InSAR time series analysis using LiCSAR products
- [MintPy](https://github.com/insarlab/MintPy) - Miami InSAR time-series software in Python
- [Pyrocko](https://pyrocko.org/) - Can be utilized flexibly for a variety of geophysical tasks, like seismological data processing and analysis, modelling of InSAR, GPS data and dynamic waveforms, or for seismic source characterization.
- [InSARFlow](https://github.com/levuvietphong/InSARFlow) - Parallel InSAR processing for Time-series analysis 

## Visualisation

- [Tiled video!](http://gena.github.io/experiments/mapbox/debug/tiled-video-no2.html)
- [Video map](https://github.com/openearth/videomap) - Tools to create,, export and share video maps
- [Tree height and canopy cover map in 3D](https://github.com/nkeikon/GEDI-experiment) - Use Kepler.gl to visualise 3D and 2D data

## Regular blogs of significant interest or posts of interest

- [Philipp Gartner blog](https://philippgaertner.github.io/)
- [Series Temporelles](https://labo.obs-mip.fr/multitemp/)
- [The downlinq](https://medium.com/the-downlinq)
- [GEDI canopy data](https://medium.com/@abt0020/extracting-canopy-height-with-gedi-data-5af8c87df158) - How we processed data to retrieving canopy height

## EO code Competitions

- [challenges 2020](https://github.com/esowc/challenges_2020) - ECMWF Summer of Weather Code 2020 challenges
- [SpaceNet](https://spacenetchallenge.github.io/) - See also CosmiQ Works blog the downlinq
- See also Sentinel hub
old competitions of note
- [Planet: Understanding the Amazon from Space](https://www.kaggle.com/c/planet-understanding-the-amazon-from-space/overview) - Use satellite data to track the human footprint in the Amazon rainforest
- [DeepGlobe Building Extraction Challenge](https://competitions.codalab.org/competitions/18544) - We would like to pose the challenge of automatically detecting buildings from satellite images.
- [DSTL feature extraction](https://www.kaggle.com/c/dstl-satellite-imagery-feature-detection) - Kagglers are challenged to accurately classify features in overhead imagery
- [crowdAI misisng maps challenge](https://www.crowdai.org/challenges/mapping-challenge) - Building Missing Maps with Machine Learning
  - [openAI solution](https://github.com/neptune-ai/open-solution-mapping-challenge) - Open solution to the Mapping Challenge

## Useful EO code based twitter accounts

- [pyGEDI](https://twitter.com/pyGEDI) - pyGEDI is a Python Package for NASA's Global Ecosystem Dynamics Investigation (GEDI) mission, data extraction, analysis, processing and visualization.

## Interesting Non EO parts Python

This bit could potentially become the most valuable resource. Lets not ignore other sectors/industries/data science, instead lets embrace it and learn from all that other amazing stuff!

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

## Interesting Non EO parts other languages
This section is aimed more a data science/programming resources that 'might' be applicable to Earth Observation, that are <b>not </b>Python
- [Efficient R programming](https://csgillespie.github.io/efficientR/) - This is the online version of the O’Reilly book: Efficient R programming. Code is [here](https://github.com/csgillespie/efficientR)
- [jupyterhub-platform-tutorials](https://github.com/luigidifraia/jupyterhub-platform-tutorials) = Tutorials to install and manage JupyterHub platforms with Kubernetes 

## Data
I don't really want to add many data resources to this list as it creeps out of scope but this part contains some good data links [not necessarily EO]
- [Environmental_Intelligence](https://github.com/rockita/Environmental_Intelligence) - Data for Environmental Intelligence: A mega list of Earth System Datasets covering earth observations, climate, water, forests, biodiversity, ecology, protected areas, natural hazards, marine and the tracking of UN's Sustainable Development Goals 

## A footnote on awesome
There are many awesome lists relating to 'Geo'. I use that term as widely as possible. This list is not meant to replace these lists. Earth Observation is still <b>way</b> behind the GIS world in terms of audience, reach, number of users etc. Things are changing though, by bringing these links together I hope you can see that there has been so much progress in the last 5 years. I do hope these links are helpful espcially to those who are new to Earth Observation, but also to people like me who with several years of experience think they may have seen it all - we haven't and there is still so much to learn. Earth Observation is not just an academic 'thing' or a basemap anymore, it forms the basis for a growing and diverse business environment. Lets embrace this.

Finally, I wanted to acknowledge a couple of awesome Earth Observation lists that you may list to check out:

- [Awesome Sentinel](https://github.com/Fernerkundung/awesome-sentinel) - curated list of awesome tools, tutorials and APIs for Copernicus Sentinel satellite data
- [awesome-remote-sensing](https://github.com/attibalazs/awesome-remote-sensing) - Collection of Remote Sensing Resources 
- [awesome-remote-sensing-papers](https://github.com/sacridini/awesome-remote-sensing-papers) - Selection of remote sensing papers 
- [awesome-Geospatial](https://github.com/sacridini/Awesome-Geospatial) - Long list of geospatial tools and resources 

#### End
