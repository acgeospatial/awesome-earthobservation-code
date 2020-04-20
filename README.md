# Awesome-EarthObservation-Code

A curated list of awesome tools, tutorials, code, helpful projects, links, stuff about Earth Observation and Geospatial stuff!

## This list was started based on #scenefromabove podcast lunchtime discussions

This is being extended frequently in April 2020. Please note that this is <b>not</b> offically an awesome list (yet). Please help me to get it there by contributing and commenting. [guidelines](https://github.com/sindresorhus/awesome/blob/master/contributing.md)

Annotations are based on the headers - where available - on the github accounts

<div align="center">

# [Scene From Above Podcast](http://scenefromabove.org/)

</div>

Alastair Graham [@ajggeoger](https://twitter.com/ajggeoger) and Andrew Cutts [@map_andrew](https://twitter.com/map_andrew) come together to present an informal podcast [@eoscenefrom](https://twitter.com/eoscenefrom) looking at the world of modern remote sensing and EO.
Fuelled by their passion for all things raster and geospatial, the #scenefromabove podcast aims to be a mix of news, opinion, discussion and interviews. <br>

<p align="center">
  <img width="300" height="300" src="https://geogerservices.files.wordpress.com/2018/06/scenefromabovepodcast.jpg?w=300&h=300">
</p>

# Contents

<b>Shortcuts</b>

- [Python processing](#python-processing-of-imagery-non-deep-learning)<br>
- [Resources for R](#resources-for-r)<br>
- [Languages other than Python](#languages-other-than-python)<br>
- [Training and Learning](#training-and-learning)
- [Deep Learning & Machine Learning](#deep-learning-and-machine-learning)
- [Great GitHub accounts](#great-github-accounts-with-example-projects-where-possible)
- [GDAL of course](#gdal-of-course)
- [Earth Observation coding on YouTube](#earth-observation-coding-on-youtube)
- [Earth Engine](#earth-engine)
- [EO Geospatial companies or orgs making big contributions](#eo-geospatial-companies-or-orgs-making-big-contributions)
- [QGIS](#qgis)
- [Radar](#radar)
- [LiDAR](#lidar)
- [Visualisation](#visualisation)
- [EO code Competitions](#eo-code-competitions)
- [Useful EO code based twitter accounts](#useful-eo-code-based-twitter-accounts)
- [Interesting Non EO parts Python](#interesting-non-eo-parts-python)

#### Start Here

OpenEO covers many of the bases, hard to know whether to break it into different categories, it has many components. At present I mention it here at the start only.<br>

- [Open EO](https://openeo.org/) - openEO develops an open API to connect R, Python, JavaScript and other clients to big Earth observation cloud back-ends in a simple and unified way.

## Python processing of imagery non deep learning

- [StarFM for Python](https://github.com/nmileva/starfm4py) - The STARFM fusion model for Python (image fusion)
- [Python from space](https://github.com/kscottz/PythonFromSpace) - Python Examples for Remote Sensing
- [Stereo Mapping to create Elevation with Python](https://github.com/cmla/s2p) - Satellite Stereo Pipeline
- [count blue pixels](https://github.com/craic/count_shelters) - This project is an experiment in using simple image processing techniques on satellite images downloaded from Google Maps in order to quantify the relative density of temporary shelters in adjacent qudarants.
- [Satellite imagery analysis with Python](https://github.com/parulnith/Satellite-Imagery-Analysis-with-Python) - Getting acquainted with the concept of satellite imagery data and how it can be analyzed to investigate real-world environmental and humanitarian challenges.
  - [associated blog](https://medium.com/analytics-vidhya/satellite-imagery-analysis-with-python-3f8ccf8a7c32)
- [Povetry predition using satellite imagery](https://github.com/carsonluuu/Poverty-Prediction-by-Satellite-Imagery) - Poverty Prediction by Combination of Satellite Imagery
- [Remote Sensing indicies calc](https://github.com/rander38/Remote-Sensing-Indices-Derivation-Tool) - Calculate spectral remote sensing indices from satellite imagery
- [Satellite imagery in Pakistan](https://github.com/iam-mhaseeb/Satellite-Imagery-Analysis-of-Vegetation-in-Southern-Pakistan) - This repository contains a study how we can examine the vegetation cover of a region with the help of satellite data. The notebook in this repository aims to familiarise with the concept of satellite imagery data and how it can be analyzed to investigate real-world environmental and humanitarian challenges.
- [s3 tools](https://github.com/maximlamare/s3_tools) - A collection of sentinel 3 processing tools
- [eumetsat -python](https://github.com/guidocioni/eumetsat-python) - Shows how to read and plot satellite data from EUMETSAT NETCDF files
- [unidata on GOES-16](https://unidata.github.io/python-gallery/examples/mapping_GOES16_TrueColor.html) - This notebook shows how to make a true color image from the GOES-16 Advanced Baseline Imager (ABI) level 2 data. We will plot the image with matplotlib and Cartopy.
- [esa_sentinel](https://github.com/jonas-eberle/esa_sentinel) - ESA Sentinel Search & Download API 

## Resources for R

R is not my area of expertise so this section is lighter than I'd like, plus I'd love to know what is a useful resource

- [R-Spatial](https://rspatial.org/raster/rs/1-introduction.html) - This book provides a short introduction to satellite data analysis with R.
  - [Remote Sensing analysis with R](https://rspatial.org/raster/rs/index.html) - Builds on above R-Spatial
- [GDAL Cubes](https://cran.r-project.org/web/packages/gdalcubes/index.html) - Earth Observation Data Cubes from Satellite Image Collections.
- [Image Classification with RandomForests in R](http://amsantac.co/blog/en/2015/11/28/classification-r.html) - The goal of this post is to demonstrate the ability of R to classify multispectral imagery using RandomForests algorithms.
- [R code for ML in Sat imagery](https://gist.github.com/franzalex/a95e227cab9b146a6092) - # Random Forest image classification Adapted from [stackoverflow](http://gis.stackexchange.com/a/57786/12899).
- [whiteboxR](https://github.com/giswqs/whiteboxR) - An R frontend of the advanced geospatial data analysis platform - [whitebox-tools](https://github.com/jblindsay/whitebox-tools).

## Languages other than Python

- [Georust](https://github.com/georust) - A collection of geospatial tools and libraries written in Rust
- [ArchGDAL - Julia](https://github.com/yeesian/ArchGDAL.jl) - A high level API for GDAL - Geospatial Data Abstract
  - [ArchGDAL docs](http://yeesian.com/ArchGDAL.jl/latest/)
- [GeoTrellis homepage](https://geotrellis.io/) - GeoTrellis is a geographic data processing engine for high performance applications.
  - [GeoTrellis on Github - Scala](https://github.com/locationtech/geotrellis) 

## Training and learning

- [Earth Data Lab](https://github.com/earthlab/earthlab.github.io) - A site dedicated to tutorials, course and other learning materials and resources developed by the Earth Lab team
- [EO College Github](https://github.com/EO-College)
  - [tomography_tutorial](https://github.com/EO-College/tomography_tutorial) - A tutorial for Synthetic Aperture Radar Tomography 
- [Andrew Cutts Github](https://github.com/acgeospatial) - I am an Earth Observation and Geospatial enthusiast, primarily using Python to automate and process images at scale using computer vision
  - [Satelite Imagery Python](https://github.com/acgeospatial/Satellite_Imagery_Python) - Sample sample scripts and notebooks on processing satellite imagery
  - [Geospatial Python Programming Course](https://github.com/acgeospatial/Geospatial_Python_CourseV1) - This is an collection of blog posts turned into a course format
- [Open Geo Tutorial](https://github.com/patrickcgray/open-geo-tutorial) - Tutorial of fundamental remote sensing and GIS methodologies using open source software in python
- [Geoprocessing with Python - GIS circa 2009](https://www.gis.usu.edu/~chrisg/python/2009/) - This material is really old and some of it is outdated (not all, though!). One of these days I might get around to putting newer class materials online, but you're stuck with this for now.

## Deep learning and Machine Learning

(see [Christoph Rieke git hub](https://github.com/chrieke/awesome-satellite-imagery-datasets) for much much more)

- [CNN-Sentinel](https://github.com/jensleitloff/CNN-Sentinel) -Analyzing Sentinel-2 satellite data in Python with Keras (repository of our talks at Minds Mastering Machines 2019 and PyCon 2018)
- [Robin Cole on satellite imagery and deep learning resources](https://github.com/robmarkcole/satellite-image-deep-learning) - Resources for deep learning with satellite & aerial imagery
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

## Great Github accounts with example projects where possible

- [shakasom github](https://github.com/shakasom)
  - [Deep Learning for satellite imagery](https://github.com/shakasom/Deep-Learning-for-Satellite-Imagery) - Deep learning courses and projects
- [Remote pixel github](https://github.com/RemotePixel)
  - [aws-sat-api-py](https://github.com/RemotePixel/remotepixel-api) - Process Satellite data using AWS Lambda functions
- [Marcus Netler on github](https://github.com/neteler)
  - [grass-dev-py3-pdal](https://github.com/neteler/grass-dev-py3-pdal) - Dockerfile which compiles GRASS GIS 7.9 master with Python 3 and PDAL support
- [Christoph Rieke git hub](https://github.com/chrieke)
  - [awesome satellite imagery datasets (for deep learning)](https://github.com/chrieke/awesome-satellite-imagery-datasets) - List of satellite image training datasets with annotations for computer vision and deep learning
- [Fernerkundung](https://github.com/Fernerkundung/)
  - [Awesome Sentinel](https://github.com/Fernerkundung/awesome-sentinel) - curated list of awesome tools, tutorials and APIs for Copernicus Sentinel satellite data
  - [Sentinel Sat](https://github.com/sentinelsat/sentinelsat) - Search and download Copernicus Sentinel satellite images
    - [Sentinel Sat docs](https://sentinelsat.readthedocs.io/en/stable/)
- [giswqs - Qiusheng Wu github](https://github.com/giswqs)
  - [Python GEE notebooks](https://github.com/giswqs/earthengine-py-notebooks) - A collection of 360+ Jupyter Python notebook examples for using Google Earth Engine with interactive mapping
  - [GEE Map](https://github.com/giswqs/geemap) - A Python package for interactive mapping with Google Earth Engine, ipyleaflet, and ipywidgets
  - [Whitebox Python](https://github.com/giswqs/whitebox-python) - WhiteboxTools Python Frontend
- [Johntruckhenbrodt github](https://github.com/johntruckenbrodt)
  - [pyroSAR](https://github.com/johntruckenbrodt/pyroSAR) - framework for large-scale SAR satellite data processing 
  - [spatialist](https://github.com/johntruckenbrodt/spatialist) - A Python module for spatial data handling 

## GDAL of course

- [GDAL Cheat Sheet](https://github.com/dwtkns/gdal-cheat-sheet) - Cheat sheet for GDAL/OGR command-line tools
- [GDAL / OGR cookbook](https://pcjericks.github.io/py-gdalogr-cookbook/) - This cookbook has simple code snippets on how to use the Python GDAL/OGR API
- [GDAL tutorial](https://jakobmiksch.eu/post/gdal_ogr/) - This blogpost gives in an introduction to GDAL/OGR and explains how the various command line tools can be used.

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

## Earth Engine

- [from GEE to Numpy to Geotiff](https://mygeoblog.com/2017/10/06/from-gee-to-numpy-to-geotiff/) - Use the GEE python api to export your data to numpy and store the result as a geotiff.
- [Google Earth Engine Community](https://github.com/gee-community) - This organization contains content contributed by the Earth Engine developer community. This is not an officially supported Google product.
- [Geo4Good 2019 workshop materials](https://sites.google.com/earthoutreach.org/geoforgood19/agenda/breakout-sessions) - 2019 material javascript and Python to be found here

## EO Geospatial companies or orgs making big contributions

- Github accounts only with example of work
- Also contains (Python) libraries for processing satellite data
  This list aims at highlighting the great work some of the companies / organisations are doing or have done that contribute to the bigger ecosystem. Examples of the accounts work is not exhaustive, some do much more than shown below:

* [development seed](https://github.com/developmentseed)
  - [Landsat-Util](https://github.com/developmentseed/landsat-util) - A utility to search, download and process Landsat 8 satellite imagery
  - [GeoLamda](https://github.com/developmentseed/geolambda) - Create and deploy Geospatial AWS Lambda functions
* [mapbox](https://github.com/mapbox)
  - [rasterio](https://github.com/mapbox/rasterio) - Rasterio reads and writes geospatial raster datasets
  - [Robosat](https://github.com/mapbox/robosat) - Semantic segmentation on aerial and satellite imagery. Extracts features such as: buildings, parking lots, roads, water, clouds
* [Planet Labs, now just Planet](https://github.com/planetlabs)
  - [Planet notebooks](https://github.com/planetlabs/notebooks) - interactive notebooks from Planet Engineering
* [Digital Globe - now Maxar](https://github.com/DigitalGlobe)
  - [Maxar GDBx tools](https://github.com/DigitalGlobe/gbdxtools) - Python SDK for using GBDX.
* [Azavea](https://github.com/azavea)
  - [Azavea - RasterVision](https://github.com/azavea/raster-vision) - An open source framework for deep learning on satellite and aerial imagery.
* [Radiant Earth foundation](https://github.com/radiantearth)
  - [STAC Spec](https://github.com/radiantearth/stac-spec) - SpatioTemporal Asset Catalog specification - making geospatial assets openly searchable and crawlable
* [Sentinel Hub](https://github.com/sentinel-hub)
  - [EO Learn](https://github.com/sentinel-hub/eo-learn) - Earth observation processing framework for machine learning in Python
  - [EO Browser Custom Scripts](https://github.com/sentinel-hub/custom-scripts) - A repository of custom scripts to be used with Sentinel Hub
  - [EO flow](https://github.com/sentinel-hub/eo-flow) - Collection of TensorFlow 2.0 code for Earth Observation applications
* [Opendatacube](https://github.com/opendatacube)
  - [Opendatacube -core](https://github.com/opendatacube/datacube-core) - Open Data Cube analyses continental scale Earth Observation data through time
  - [Opendatacube notebooks](https://github.com/opendatacube/datacube-notebooks) - Extra documentation about using ODC with Jupyter Notebooks
* [PyTroll](https://github.com/pytroll)
  - [SatPy](https://github.com/pytroll/satpy) - Python package for earth-observing satellite data processing
  - [pyresample](https://github.com/pytroll/pyresample) - Geospatial image resampling in Python
* [CosmiQ](https://github.com/CosmiQ)
  - [Solaris](https://github.com/cosmiq/solaris) - CosmiQ Works Geospatial Machine Learning Analysis Toolkit
    - [docs](https://solaris.readthedocs.io/en/latest/)
  - [CometTS](https://github.com/CosmiQ/CometTS) - Comet Time Series Toolset for working with a time-series of remote sensing imagery and user defined polygons 
  - [SpaceNet6 Baseline](https://github.com/CosmiQ/CosmiQ_SN6_Baseline) - Baseline algorithm for the SpaceNet 6 Challenge 
* [Theia software and tools](https://www.theia-land.fr/en/softwares-and-tools/)
* [sparkgeo](https://github.com/sparkgeo)
  - [stac-validator](https://github.com/sparkgeo/stac-validator) - Validator for the stac-spec 
 * [Geoscience Australia](https://github.com/GeoscienceAustralia)
  - [PyRate](https://github.com/GeoscienceAustralia/PyRate) - A Python tool for estimating velocity and time-series from Interferometric Synthetic Aperture Radar (InSAR) data.
  - [dea-notebooks](https://github.com/GeoscienceAustralia/dea-notebooks) - Repository for Digital Earth Australia Jupyter Notebooks: tools and workflows for geospatial analysis with Open Data Cube and xarray
* [Dymaxion Labs](https://github.com/dymaxionlabs)
  - [dask-rasterio](https://github.com/dymaxionlabs/dask-rasterio) - Read and write rasters in parallel using Rasterio and Dask 
  - [ap-latem](https://github.com/dymaxionlabs/ap-latam) - Detection of slums and informal settlements from satellite imagery
## QGIS

- [Qgis Earth Engine Plugin](https://github.com/gee-community/qgis-earthengine-plugin) - Integrates Google Earth Engine and QGIS using Python API
  - [QGIS Earth Engine Plugin - installation guide](https://gee-community.github.io/qgis-earthengine-plugin/)

## Radar

- [SAR docker](https://github.com/mortcanty/SARDocker) - Source files for Docker image mort/sardocker/

## LiDAR

- [pyGEDI](https://github.com/EduinHSERNA/pyGEDI) - pyGEDI is a Python Package for NASA's Global Ecosystem Dynamics Investigation (GEDI) mission, data extraction, analysis, processing and visualization.
- [GEDI extraction script](https://gist.github.com/KMarkert/c68ccf53260d7b775b836bf2e11e2ec3) - Python script to take GEDI level 2 data and convert variables to a geospatial vector format
- [rGEDI](https://github.com/carlos-alberto-silva/rGEDI) - rGEDI: An R Package for NASA's Global Ecosystem Dynamics Investigation (GEDI) Data Visualization and Processing.
- [ICESAT extraction script](https://gist.github.com/bzgeo/950f3db986b3513311ed42efe2395171) - Python script to convert from ICESat-2 ATL08 HDF data to shapefile. Usage: 'python icesat2_shp.py
- [ICESAT tools](https://github.com/icesat-2UT/PhoREAL) - Tools and code for Icesat-2 data analysis (Python)

## Visualisation

- [Tiled video!](http://gena.github.io/experiments/mapbox/debug/tiled-video-no2.html)
- [Video map](https://github.com/openearth/videomap) - Tools to create,, export and share video maps

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

#### End
