import numpy as np
import os
from PIL import Image
from abc import ABC, abstractmethod

class DataSetInterface(ABC):
    '''A generic interface for Datasets. This interface defines the methods which will be called by the
    Algorithm interface in order to feed the data to the algorithms. The functions defined in this interface will be 
    implemented by the dataset specific classes'''

    def __init__(self, args: list):
        '''The constructor of Dataset Interface. Each class that implements this interface must provide a constructor that 
        will set default values. Some default values are already set in this constructor that could be overriden.'''
        # Default Camera Parameters
        self.camera = {
            'type': "PinHole",
            'width': 1920,
            'height': 1080,
            'fps': 30,
            'RGB': 1
        }
        # Default ORB parameters
        self.orb = {
        'nFeatures': 1000,
        'scaleFactor': 1.2,
        'nLevels': 8,
        'iniThFAST': 20,
        'minThFAST': 7
        }
        # Default Viewer parameters
        self.viewer = {
            'KeyFrameSize': 0.05,
            'KeyFrameLineWidth': 1,
            'GraphLineWidth': 0.9,
            'PointSize': 2,
            'CameraSize': 0.08,
            'CameraLineWidth': 3,
            'ViewpointX': 0,
            'ViewpointY': -0.7,
            'ViewpointZ': -1.8,
            'ViewpointF': 500
        }
        # Transformation from camera to body-frame (imu), Default is the transformation matrix of Zurich dataset
        self.transformationMatrix = [1, 0, 0, -0.07566,
                0, 1, 0, -0.02968,
                0, 0, 1, 0.03227,
                0.0, 0.0, 0.0, 1.0]
        # List to store image names
        self.imageNames = None
        # Indexes to traverse data
        self.imageNameIndex = 0
        self.imageIndex = 0        

    @abstractmethod
    def get_cameraParams(self) -> dict:
        '''Returns a dictionary with camera paremeter values.
        These values include [camera type "type", width of camera image "width", height of camera image "height",
        frames per second "fps", RGB or BGR "RGB", fx, fy, s, cx, cy, k1, k2, k3, p1, p2].
        Further values can be returned as required or provided by different datasets or algorithms.'''
        return self.camera

    @abstractmethod
    def getOrbParams(self) -> dict:
        '''Returns a dictionary with Oriented FAST and rotated BRIEF (ORB) paremeter values.
        These values include [number of features, scale factor between levels in the scale pyramid "scaleFactor", 
        Number of levels in the scale pyramid "nLevels", Fast threshold "iniThFAST" and "minThFAST"].
        Further values can be returned as required or provided by different datasets or algorithms.'''
        return self.orb

    @abstractmethod
    def getViewerParams(self) -> dict:
        '''Returns a dictionary with Viewer paremeter values.
        These values include [KeyFrameSize,  KeyFrameLineWidth, GraphLineWidth, PointSize, CameraSize,
        CameraLineWidth, ViewpointX, ViewpointY, ViewpointZ, ViewpointF].
        Further values can be returned as required or provided by different datasets or algorithms.'''
        return self.viewer

    def getImageNames(self) -> list:
        '''Returns a list of names of the images sorted by names'''
        return self.imageNames

    def getNextImageName(self) -> str:
        '''Returns the name of next image in order. If last image name was already provided in previous call it will return None.'''
        if(self.imageNames == None):
            raise TypeError("Object parameter 'self.imageNames' is not initialized")
        retFileName = None
        if(self.imageNameIndex < len(self.imageNames)):
            retFileName = self.imageNames[self.imageNameIndex]
            self.imageNameIndex += 1
        return retFileName
    
    @abstractmethod
    def getImageAtIndex(self, i: int) -> Image:
        '''Returns the image at index i. If i is greater than total number of images returns None.'''
        pass

    @abstractmethod
    def getNextImage(self) -> Image:
        '''Returns the next image in order. If last image was already provided in previous call it will return None.'''
        pass

    def setImageIndex(self, i: int = 0):
        '''Sets image index to i. Default value is 0. So, if no parameter is provided it resets the image counter.'''
        if(i > len(self.imageNames) or i < 0):
            raise TypeError("Invalid Index!!")
        else:
            self.imageIndex = i

