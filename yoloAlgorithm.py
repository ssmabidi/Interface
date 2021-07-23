from algorithmInterface import AlgorithmInterface

# import numpy as np
# import os
# from PIL import Image
import cv2
from yoloFiles import darknet

def c_array(ctype, values):
    arr = (ctype*len(values))()
    arr[:] = values
    return arr
    
class yoloAlgorithm(AlgorithmInterface):

    def __init__(self, args: list):
        '''The constructor of yoloAlgorithm Class. Each class that implements this interface must provide a constructor that 
        will set default values. Some default values are already set in this constructor that could be overriden.'''
        print("In Yolo Init")
        self.yolo_config = 'yoloFiles/yolov4.cfg'
        self.data_file = 'yoloFiles/coco.data'
        self.weights_file = 'yoloFiles/yolov4.weights'

    def load_network(self):
        networkInfo = darknet.load_network(self.yolo_config, self.data_file, self.weights_file)
        print(networkInfo)
        self.network = networkInfo[0]
        self.class_names = networkInfo[1]
        self.colors = networkInfo[2]

    def detect_image(self):
        img = cv2.imread('yoloFiles/person.jpg')

        img = img.transpose(2,0,1)
        c = img.shape[0]
        h = img.shape[1]
        w = img.shape[2]
        img = (img/255.0).flatten()
        data = c_array(darknet.c_float, img)
        im = darknet.IMAGE(w,h,c,data)

        # img_ins = darknet.IMAGE
        detections = darknet.detect_image(self.network, self.class_names, im)
        print(detections)

    