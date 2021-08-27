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
        self.thresh = 0.5
        

    def load_network(self):
        networkInfo = darknet.load_network(self.yolo_config, self.data_file, self.weights_file)
        # print(networkInfo)
        self.network = networkInfo[0]
        self.class_names = networkInfo[1]
        self.colors = networkInfo[2]

        self.network_width = darknet.network_width(self.network)
        self.network_height = darknet.network_height(self.network)

    def detect_image(self, file_name):
        img = cv2.imread(file_name)

        img = img.transpose(2,0,1)
        c = img.shape[0]
        h = img.shape[1]
        w = img.shape[2]
        img = (img/255.0).flatten()
        data = c_array(darknet.c_float, img)
        im = darknet.IMAGE(w,h,c,data)

        # img_ins = darknet.IMAGE
        detections = darknet.detect_image(self.network, self.class_names, im)
        return detections

    def detect_image_file(self, cv2Image, getDetections = True, getImage = True):
        darknet_image = darknet.make_image(self.network_width, self.network_height, 3)

        image_rgb = cv2.cvtColor(cv2Image, cv2.COLOR_BGR2RGB)
        image_resized = cv2.resize(image_rgb, (self.network_width, self.network_height), interpolation=cv2.INTER_LINEAR)

        darknet.copy_image_from_bytes(darknet_image, image_resized.tobytes())
        detections = darknet.detect_image(self.network, self.class_names, darknet_image, thresh=self.thresh)
    
        darknet.free_image(darknet_image)
        image = darknet.draw_boxes(detections, image_resized, self.colors)
        # toRet = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        if(getImage):
            return detections, image

        else:
            return detections
