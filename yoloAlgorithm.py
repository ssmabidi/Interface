import json
import os
from PIL.Image import Image
from pathlib import Path
from zipfile import ZipFile
from algorithmAbstractClass import AlgorithmAbstractClass

import cv2
from yoloFiles import darknet

import gc
import torch

class yoloAlgorithm(AlgorithmAbstractClass):

    def __init__(self, args: list):
        '''The constructor of yoloAlgorithm Class. This function defines the default values for some configurations. These values can be overwritten
        by the user through the testbench by using appropriate setter functions'''
        self.yolo_config = 'yoloFiles/yolov4.cfg'
        self.data_file = 'yoloFiles/coco.data'
        self.weights_file = 'yoloFiles/yolov4.weights'
        self.thresh = 0.5
        self.network = None
        self.batch_json = None
        self.batch_zip = None
        self.batch_json_all = None
        self.batch_zip_all = None

    def load_network(self):
        '''This function loads the algorithm's network and store it in class variable for use in other functions. It must be called after Algorithm 
        interface is instantiated in order for later functions to use the network.'''

        if(self.network):
            darknet.free_network_ptr(self.network)
        gc.collect()
        torch.cuda.empty_cache()

        networkInfo = darknet.load_network(self.yolo_config, self.data_file, self.weights_file)
        self.network = networkInfo[0]
        self.class_names = networkInfo[1]
        self.colors = networkInfo[2]

        self.network_width = darknet.network_width(self.network)
        self.network_height = darknet.network_height(self.network)

    def detect_image_file(self, cv2Image: Image, getImage: bool = True) -> list:
        '''This function takes the image in CV2 format and applies the algorthm to detect the object in the image. A list of dictionaries is returned.
        Each dictionary contains the object it detected, percentage of surety of that object and a list of coordinates where the object is detected on
        the image. If the value of getImage is True(default) it also draws the bonding boxes on the image and returns the image with those bonding boxes
        as well.'''
        darknet_image = darknet.make_image(self.network_width, self.network_height, 3)

        image_rgb = cv2.cvtColor(cv2Image, cv2.COLOR_BGR2RGB)
        image_resized = cv2.resize(image_rgb, (self.network_width, self.network_height), interpolation=cv2.INTER_LINEAR)

        darknet.copy_image_from_bytes(darknet_image, image_resized.tobytes())
        detections = darknet.detect_image(self.network, self.class_names, darknet_image, thresh=self.thresh)
    
        darknet.free_image(darknet_image)
        image = darknet.draw_boxes(detections, image_resized, self.colors)
        
        if(getImage):
            return detections, image
        else:
            return detections

    def set_config_file(self, filePath: str):
        '''Setter for configuration file.'''
        self.yolo_config = filePath

    def set_weights_file(self, filePath: str):
        '''Setter for weights file.'''
        self.weights_file = filePath
    
    def set_data_file(self, filePath: str):
        '''Setter for data file'''
        self.data_file = filePath

    def set_threshold(self, threshold: int):
        '''Setter for threshold value. This threshold defines the minimum percentage of surety the algorithm has in order to detect the object in
        an image.'''
        self.thresh = threshold

    def get_threshold(self) -> int:
        '''Return the threshold value. This threshold defines the minimum percentage of surety the algorithm has in order to detect the object in
        an image.'''
        return self.thresh

    def reload_network(self):
        '''This function reload the network with the new files provided by the user. If the new files are not provided it simply reloads the network
        with default files.'''
        darknet.free_network_ptr(self.network)
        gc.collect()
        torch.cuda.empty_cache()
        self.load_network()

    def batch_detect(self, images, dirPath):
        detections = []
        Path(dirPath).mkdir(parents=True, exist_ok=True)
        
        zipObj = ZipFile(dirPath + '/images.zip', 'w')
        zipObjAll = ZipFile(dirPath + '/imagesAll.zip', 'a')
        
        for img in images:
            detc, im = self.detect_image_file(img["image"])
            detections.append({"image_name": img["name"], "bbox": detc})
            name=img["name"]
            retval, buf = cv2.imencode('.' + name.split(".")[-1], im)
            zipObj.writestr(name, buf)
            zipObjAll.writestr(name, buf)


        with open(dirPath + '/data.json', 'w') as file:
            json.dump(detections, file, indent=4)

        with open(dirPath + '/dataAll.json', 'a') as file:
            json.dump(detections, file, indent=4)

        self.batch_json = dirPath + '/data.json'
        self.batch_zip = dirPath + '/images.zip'
        self.batch_json_all = dirPath + '/dataAll.json'
        self.batch_zip_all = dirPath + '/imagesAll.zip'
        return detections

    def get_batch_json(self, getAll:bool = False):
        if(getAll):
            return self.batch_json_all
        else:
            return self.batch_json

    def get_batch_zip(self, getAll:bool = False):
        if(getAll):
            return self.batch_zip_all
        else:
            return self.batch_zip