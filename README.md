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

#### Start Here
## LiDAR
  * [pyGEDI](https://github.com/EduinHSERNA/pyGEDI) - pyGEDI is a Python Package for NASA's Global Ecosystem Dynamics Investigation (GEDI) mission, data extraction, analysis, processing and visualization. 
  * [GEDI extraction script](https://gist.github.com/KMarkert/c68ccf53260d7b775b836bf2e11e2ec3) - Python script to take GEDI level 2 data and convert variables to a geospatial vector format
  * [rGEDI](https://github.com/carlos-alberto-silva/rGEDI) - rGEDI: An R Package for NASA's Global Ecosystem Dynamics Investigation (GEDI) Data Visualization and Processing. 
  * [ICESAT extraction script](https://gist.github.com/bzgeo/950f3db986b3513311ed42efe2395171) - Python script to convert from ICESat-2 ATL08 HDF data to shapefile. Usage: 'python icesat2_shp.py
  * [ICESAT tools](https://github.com/icesat-2UT/PhoREAL) - Tools and code for Icesat-2 data analysis (Python)
## Training / learning
  * [Earth Data Lab](https://github.com/earthlab/earthlab.github.io) - A site dedicated to tutorials, course and other learning materials and resources developed by the Earth Lab team 
  * [Andrew Cutts Github](https://github.com/acgeospatial) - I am an Earth Observation and Geospatial enthusiast, primarily using Python to automate and process images at scale using computer vision
    * [Satelite Imagery Python](https://github.com/acgeospatial/Satellite_Imagery_Python) - Sample sample scripts and notebooks on processing satellite imagery 
    * [Geospatial Python Programming Course](https://github.com/acgeospatial/Geospatial_Python_CourseV1) - This is an collection of blog posts turned into a course format 
  * [Open Geo Tutorial](https://github.com/patrickcgray/open-geo-tutorial) - Tutorial of fundamental remote sensing and GIS methodologies using open source software in python 
  * [Geoprocessing with Python - GIS circa 2009](https://www.gis.usu.edu/~chrisg/python/2009/) - This material is really old and some of it is outdated (not all, though!). One of these days I might get around to putting newer class materials online, but you're stuck with this for now.
## QGIS
  * [Qgis Earth Engine Plugin](https://github.com/gee-community/qgis-earthengine-plugin) - Integrates Google Earth Engine and QGIS using Python API
    * [QGIS Earth Engine Plugin - installation guide](https://gee-community.github.io/qgis-earthengine-plugin/)
## Radar
  * [SAR docker](https://github.com/mortcanty/SARDocker) - Source files for Docker image mort/sardocker/
## Languages other than Python
  * [Georust](https://github.com/georust) - A collection of geospatial tools and libraries written in Rust
  * [ArchGDAL - Julia](https://github.com/yeesian/ArchGDAL.jl) - A high level API for GDAL - Geospatial Data Abstract
    * [ArchGDAL docs](http://yeesian.com/ArchGDAL.jl/latest/)
## Deep / Machine Learning (see [Christoph Rieke git hub](https://github.com/chrieke/awesome-satellite-imagery-datasets) for much much more)
  * [CNN-Sentinel](https://github.com/jensleitloff/CNN-Sentinel) -Analyzing Sentinel-2 satellite data in Python with Keras (repository of our talks at Minds Mastering Machines 2019 and PyCon 2018) 
  * [Robin Cole on satellite imagery and deep learning resources](https://github.com/robmarkcole/satellite-image-deep-learning) - Resources for deep learning with satellite & aerial imagery 
  * [Image patches](https://github.com/Vooban/Smoothly-Blend-Image-Patches) - Using a U-Net for image segmentation, blending predicted patches smoothly is a must to please the human eye.
  * [Fast AI Satellite imagery resources](https://forums.fast.ai/t/geospatial-deep-learning-resources-study-group/31044)
  * [Crop yield prediction](https://github.com/meet-sapu/Crop-Yield-Prediction-Using-Satellite-Imagery) - The motive here is to predict the yield of crops of a particular farm by the change in pixels of the image of farm yearly. Uses Tensorflow
  * [Houston Flooding with deep learning](https://github.com/Lichtphyz/Houston_flooding) - Using A Segmentation Neural Net to map out flooded areas of Houston TX using satellite imagery 
  * [Satellite Imagery Classification with R](https://github.com/kkgadiraju/SatelliteImageClassification) - Pixel based classification of satellite imagery - feature generation using Orfeo Toolbox, feature selection using Learning Vector Quantization, CLassification using Decision Tree, Neural Networks, Random Forests, KNN and Naive Bayes Classifier 
  * [SpaceNet building detection](https://github.com/motokimura/spacenet_building_detection) - Project to train/test convolutional neural networks to extract buildings from SpaceNet satellite imageries. 
  * [Road segmentation](https://github.com/Paulymorphous/Road-Segmentation) - Road Detection in satellite imagery. Semantic segmentation is the process of classifying each pixel of an image into distinct classes using deep learning. This aids in identifying regions in an image where certain objects reside.This aim of this project is to identify and segment roads in aerial imagery. Detecting roads can be an important factor in predicting further development of cities, and this concept plays a major role in GeoArchitect (A project which I started). Segmentation of roads is important to map-based applications and is used for finding distances or shortest routes between two places.
  * [Super resolution (srcnn)](https://github.com/WarrenGreen/srcnn) - Super Resolution for Satellite Imagery 
  * [Pixel decoder](https://github.com/Geoyi/pixel-decoder) - A tool of running deep learning algorithms for semantic segmentation with satellite imagery 
  * [Detecting ships](https://github.com/ucalyptus/Detecting-Ships) - Using Satellite Imagery to detect ships (Basic Object Detection)
  * [deepOSM](https://github.com/trailbehind/DeepOSM) - Train a deep learning net with OpenStreetMap features and satellite imagery.
## Visualisation
  * [Tiled video!](http://gena.github.io/experiments/mapbox/debug/tiled-video-no2.html)
  * [Video map](https://github.com/openearth/videomap) - Tools to create,, export and share video maps
## Regular blogs of significant interest
* [Philipp Gartner blog](https://philippgaertner.github.io/)
* [Series Temporelles](https://labo.obs-mip.fr/multitemp/)
* [Theia software and tools](https://www.theia-land.fr/en/softwares-and-tools/)
## Great Github accounts - with example projects where possible
* [shakasom github](https://github.com/shakasom)
  * [Deep Learning for satellite imagery](https://github.com/shakasom/Deep-Learning-for-Satellite-Imagery) - Deep learning courses and projects 
* [Remote pixel github](https://github.com/RemotePixel)
  * [aws-sat-api-py](https://github.com/RemotePixel/remotepixel-api) - Process Satellite data using AWS Lambda functions 
* [Marcus Netler on github](https://github.com/neteler)
  * [grass-dev-py3-pdal](https://github.com/neteler/grass-dev-py3-pdal) - Dockerfile which compiles GRASS GIS 7.9 master with Python 3 and PDAL support 
* [Christoph Rieke git hub](https://github.com/chrieke)
  * [awesome satellite imagery datasets (for deep learning)](https://github.com/chrieke/awesome-satellite-imagery-datasets) - List of satellite image training datasets with annotations for computer vision and deep learning 
* [Fernerkundung](https://github.com/Fernerkundung/) 
  * [Awesome Sentinel](https://github.com/Fernerkundung/awesome-sentinel) - curated list of awesome tools, tutorials and APIs for Copernicus Sentinel satellite data 
  * [Sentinel Sat](https://github.com/sentinelsat/sentinelsat) - Search and download Copernicus Sentinel satellite images
    * [Sentinel Sat docs](https://sentinelsat.readthedocs.io/en/stable/)
## GDAL of course
* [GDAL Cheat Sheet](https://github.com/dwtkns/gdal-cheat-sheet) - Cheat sheet for GDAL/OGR command-line tools 
* [GDAL / OGR cookbook](https://pcjericks.github.io/py-gdalogr-cookbook/) - This cookbook has simple code snippets on how to use the Python GDAL/OGR API
* [GDAL tutorial](https://jakobmiksch.eu/post/gdal_ogr/) - This blogpost gives in an introduction to GDAL/OGR and explains how the various command line tools can be used.
## Earth Observation coding on YouTube
* [xArray at PyConUK2018](https://www.youtube.com/watch?v=Dgr_d8iEWk4)
* [Visualizing & Analyzing Earth Science Data Using PyViz & PyData](https://youtu.be/-XMXNmGRk5c?t=455)
## Useful EO code based twitter accounts
* [pyGEDI](https://twitter.com/pyGEDI) - pyGEDI is a Python Package for NASA's Global Ecosystem Dynamics Investigation (GEDI) mission, data extraction, analysis, processing and visualization.
## Useful technical blog posts
* [GEDI canopy data](https://medium.com/@abt0020/extracting-canopy-height-with-gedi-data-5af8c87df158) - How we processed data to retrieving canopy height
## Python processing of imagery (non deep learning)
* [StarFM for Python](https://github.com/nmileva/starfm4py) - The STARFM fusion model for Python (image fusion)
* [Python from space](https://github.com/kscottz/PythonFromSpace) - Python Examples for Remote Sensing 
* [Stereo Mapping to create Elevation with Python](https://github.com/cmla/s2p) - Satellite Stereo Pipeline 
* [count blue pixels](https://github.com/craic/count_shelters) - This project is an experiment in using simple image processing techniques on satellite images downloaded from Google Maps in order to quantify the relative density of temporary shelters in adjacent qudarants.
* [Satellite imagery analysis with Python](https://github.com/parulnith/Satellite-Imagery-Analysis-with-Python) - Getting acquainted with the concept of satellite imagery data and how it can be analyzed to investigate real-world environmental and humanitarian challenges.
  * [associated blog](https://medium.com/analytics-vidhya/satellite-imagery-analysis-with-python-3f8ccf8a7c32)
* [Povetry predition using satellite imagery](https://github.com/carsonluuu/Poverty-Prediction-by-Satellite-Imagery) - Poverty Prediction by Combination of Satellite Imagery 
* [Remote Sensing indicies calc](https://github.com/rander38/Remote-Sensing-Indices-Derivation-Tool) - Calculate spectral remote sensing indices from satellite imagery 
* [Satellite imagery in Pakistan](https://github.com/iam-mhaseeb/Satellite-Imagery-Analysis-of-Vegetation-in-Southern-Pakistan) - This repository contains a study how we can examine the vegetation cover of a region with the help of satellite data. The notebook in this repository aims to familiarise with the concept of satellite imagery data and how it can be analyzed to investigate real-world environmental and humanitarian challenges. 
## Competitions
* [challenges 2020](https://github.com/esowc/challenges_2020) - ECMWF Summer of Weather Code 2020 challenges 
* See also Sentinel hub
## Earth Engine
* [from GEE to Numpy to Geotiff](https://mygeoblog.com/2017/10/06/from-gee-to-numpy-to-geotiff/) - Use the GEE python api to export your data to numpy and store the result as a geotiff.
* [Google Earth Engine Community](https://github.com/gee-community) - This organization contains content contributed by the Earth Engine developer community. This is not an officially supported Google product.
* [Geo4Good 2019 workshop materials](https://sites.google.com/earthoutreach.org/geoforgood19/agenda/breakout-sessions) - 2019 material javascript and Python to be found here
  * [GEE Map](https://github.com/giswqs/geemap) - A Python package for interactive mapping with Google Earth Engine, ipyleaflet, and ipywidgets
## EO / Geospatial companies making big contributions - Github accounts only with example of work
* [development seed](https://github.com/developmentseed)
  * [Landsat-Util](https://github.com/developmentseed/landsat-util) - A utility to search, download and process Landsat 8 satellite imagery 
  * [GeoLamda](https://github.com/developmentseed/geolambda) - Create and deploy Geospatial AWS Lambda functions 
* [mapbox](https://github.com/mapbox)
  * [rasterio](https://github.com/mapbox/rasterio) - Rasterio reads and writes geospatial raster datasets
  * [Robosat](https://github.com/mapbox/robosat) - Semantic segmentation on aerial and satellite imagery. Extracts features such as: buildings, parking lots, roads, water, clouds 
* [Planet Labs, now just Planet](https://github.com/planetlabs)
  * [Planet notebooks](https://github.com/planetlabs/notebooks) - interactive notebooks from Planet Engineering
* [Digital Globe - now Maxar](https://github.com/DigitalGlobe)
  * [Maxar GDBx tools](https://github.com/DigitalGlobe/gbdxtools) - Python SDK for using GBDX. 
* [Azavea](https://github.com/azavea)
  * [Azavea - RasterVision](https://github.com/azavea/raster-vision) - An open source framework for deep learning on satellite and aerial imagery.
* [Radiant Earth foundation](https://github.com/radiantearth)
  * [STAC Spec](https://github.com/radiantearth/stac-spec) - SpatioTemporal Asset Catalog specification - making geospatial assets openly searchable and crawlable
* [Sentinel Hub](https://github.com/sentinel-hub)
  * [EO Learn](https://github.com/sentinel-hub/eo-learn) - Earth observation processing framework for machine learning in Python 
  * [EO Browser Custom Scripts](https://github.com/sentinel-hub/custom-scripts) - A repository of custom scripts to be used with Sentinel Hub
  * [EO flow](https://github.com/sentinel-hub/eo-flow) - Collection of TensorFlow 2.0 code for Earth Observation applications 
## Interesting Non EO parts - Python
This bit could potentially become the most valuable resource. Lets not ignore other sectors/industries/data science, instead lets embrace it and learn from all that other amazing stuff!
* [realtime covid19 graphs in USA](https://github.com/k-sys/covid-19) - A collection of work related to COVID-19 
* [Deep learning with Python notebooks](https://github.com/fchollet/deep-learning-with-python-notebooks) - Jupyter notebooks for the code samples of the book "Deep Learning with Python" 
* [Python data science handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
* [A-Z of tips and tricks for Python](https://www.freecodecamp.org/news/an-a-z-of-useful-python-tricks-b467524ee747/) - 'Most of these ‘tricks’ are things I’ve used or stumbled upon during my day-to-day work. '
* [Visual intro into Numpy](https://jalammar.github.io/visual-numpy/)- Visualizing machine learning one concept at a time
* [Change your Jupyter Theme](https://github.com/dunovank/jupyter-themes) - Custom Jupyter Notebook Themes 
* [Awesome Semantic Segmentation](https://github.com/mrgloom/awesome-semantic-segmentation) - awesome-semantic-segmentation 
* [unidata Python workshop](https://unidata.github.io/python-training/workshop/workshop-intro/) - Would you like some in-depth training on the scientific Python ecosystem for atmospheric science and meteorology? Work through our workshop materials at your own pace to learn and practice the syntax, functionality, and utility of this powerful programming language, or return to the material after taking the workshop in-person to further your understanding of the material you were taught.
* [TernausNet - used in DSTL kaggle competition (came 3rd)](https://github.com/ternaus/TernausNet) - UNet model with VGG11 encoder pre-trained on Kaggle Carvana dataset
* [Introduction to Python for computational science](https://github.com/fangohr/introduction-to-python-for-computational-science-and-engineering) - Book: Introduction to Python for Computational Science and Engineering 
#### End
