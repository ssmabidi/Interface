# Testbench for UAVs
[![Known Vulnerabilities](https://snyk.io/test/github/ssmabidi/Interface/badge.svg)](https://snyk.io/test/github/ssmabidi/Interface)
## About
The project Testbench for UAVs is an opensource project written as a part of Research and Development (RnD) project for [Autonomous Systems (MSc)](https://www.h-brs.de/en/inf/study/master/autonomous-systems) studies at [Hochschule Bonn-Rhein-Sieg (H-BRS)](https://www.h-brs.de/en). This project presents a testbench for UAVS. It can be used to test different datasets with different algorithms. Currently it supports 2 datasets and 1 algorithm but it can be easily extended by implementing the interfaces it provides.

## Table of Contents

> * [Testbench for UAVs](#testbench-for-uavs)
>   * [About](#about)
>   * [Table of Contents](#table-of-contents)
>   * [Installation](#installation)
>       * [Setup the Datasets](#setup-the-datasets)
>       * [Setup the Algorithms](#setup-the-algorithms)
>       * [Run the Testbench](#run-the-testbench)
>   * [Usage](#usage)
<!-- >     * [Screenshots](#screenshots)
>     * [Features](#features)
>   * [Code](#code)
>     * [Content](#content)
>     * [Requirements](#requirements)
>     * [Limitations](#limitations)
>     * [Build](#build)
>     * [Deploy (how to install build product)](#deploy-how-to-install-build-product)
>   * [Resources (Documentation and other links)](#resources-documentation-and-other-links)
>   * [Contributing / Reporting issues](#contributing--reporting-issues)
>   * [License](#license)
>   * [About Nuxeo](#about-nuxeo) -->

## Installation
To install the project first clone the repository. And move into it.
```
git clone git@github.com:ssmabidi/Interface.git
cd Interface
```
### Setup the Datasets
Next create a folder `Datasets` in the Interface folder and download the datasets. We need to download [The Zurich Urban Micro Aerial Vehicle Dataset](http://rpg.ifi.uzh.ch/zurichmavdataset.html) and [The AU-AIR Dataset](https://bozcani.github.io/auairdataset)
```
mkdir Datasets
cd Datasets
```

**Zurich Dataset**

To download and setup the zurich dataset run the following commands
```
wget "web.eee.sztaki.hu/~majdik/AGZ/AGZ.zip"
unzip AGZ.zip
```
After the unzip is complete the Zurich Dataset is ready for use in the Testbench.

**Au-Air Dataset**

To download and setup Au-Air dataset first create a auAir folder
```
mkdir auAir
cd auAir
```
Then download the AU-AIR images from the following link and extract them into this folder.

Images: https://drive.google.com/open?id=1pJ3xfKtHiTdysX5G3dxqKTdGESOBYCxJ (2.2 GB)

Extract this zip file in auAir directory. Following commands can be used for extraction.
```
cd auAir
unzip auair2019data.zip 
```

After the download and unzip is complete, then download the AU-AIR annotations and place them in `auAir` folder.

Annotations **(V.1.1)**: https://drive.google.com/file/d/1GyoBK-NalDFfAtRt9LO6FBujbObyaZLv/view?usp=sharing (55 MB)

Make sure the name of annotations file is `annotations_v1.1.json`

### Setup the Algorithms
The project currently supports just one Algorithm [YOLOv4: Optimal Speed and Accuracy of Object Detection](https://arxiv.org/abs/2004.10934).

**YOLOv4**

The project uses a yolo library which is build with GPU enabled. Make sure CUDA is installed in order for algorithm part to run successfully. Then download pre trained YOLOv4 weights using the following commands.
```
cd ../../yoloFiles/
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights
```

### Requirements file
Install the requirements present in `requirements.txt` using pip
```
cd ..
pip3 install -r requirements.txt
```

### Run the Testbench
To run the application navigate to the root folder and start the project using following commands
```
python3 webPage/index.py
```
Then open any web browser and navigate to http://127.0.0.1:8050/

## Usage


## Contributing [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/ssmabidi/Interface)