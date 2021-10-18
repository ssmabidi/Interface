from dataSetAbstractClass import DataSetAbstractClass
import numpy as np
import os
from PIL import Image

class zurichDataset(DataSetAbstractClass):

    def __init__(self, args: list):
        # Default values for dataSets taken from related papers
        # Values for Zurich dataSet. Paper link: http://rpg.ifi.uzh.ch/docs/IJRR17_Majdik.pdf

        # Default Camera Parameters
        self.camera = {
            'type': "PinHole",
            'width': 1920,
            'height': 1080,
            'fps': 30,
            'RGB': 1
        }

        # Default path to images within the folder.
        self.paths = {
            'calibrationDataPath': '/calibration_data.npz',
            'logFilesPath': '/Log Files',
            'imageFilesPath': '/MAV Images'
        }
        self.dataPath = args["dataPath"]
        self.imageNames = sorted(os.listdir(self.dataPath + self.paths['imageFilesPath']))
        
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

        self.traingDataPercent = 30
        self.datasetType = 'pathPlanning'

        self.imageNameIndex = 0
        self.imageIndex = 0
    
    # For reading the Intrinsic Matrix lecture from Kyle Simek is used which is available at http://ksimek.github.io/2013/08/13/intrinsic/
    def getCameraParams(self) -> dict:
        calibrationdata = np.load(self.dataPath + self.paths['calibrationDataPath'])
        mtx = calibrationdata['intrinsic_matrix']
        dist = calibrationdata['distCoeff'][0]

        self.camera['fx'] = mtx[0][0]
        self.camera['s'] = mtx[0][1]
        self.camera['fy'] = mtx[1][1]
        self.camera['cx'] = mtx[0][2]
        self.camera['cy'] = mtx[1][2]

        self.camera['k1'] = dist[0]
        self.camera['k2'] = dist[1]
        self.camera['p1'] = dist[2]
        self.camera['p2'] = dist[3]
        self.camera['k3'] = dist[4]

        calibrationdata.close()

        return self.camera

    def getOrbParams(self) -> dict:
        return self.orb

    def getViewerParams(self) -> dict:
        return self.viewer

    def getDatasetType(self):
        return self.datasetType

    def getImageNames(self, fullPath=False) -> list:
        '''Returns a list of names of the images sorted by names'''
        if(fullPath):
            return [self.dataPath + self.paths['imageFilesPath'] + "/" + s for s in self.imageNames]
        else:
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

    def getImageAtIndex(self, i: int, cv2=False) -> Image:
        """Returns Image at index i. If i is greater than total number of images returns None."""
        if(i >= 0 and i < len(self.imageNames)):
            img = Image.open(self.dataPath + self.paths['imageFilesPath'] + "/" + self.imageNames[i])
            self.imageIndex = i
            if(cv2):
                return super().pilToCV2(img)
            return img
        else:
            return None

    def getNextImage(self, cv2=False) -> Image:
        retImg = None
        if(self.imageIndex < len(self.imageNames)):
            self.imageIndex += 1
            retImg = Image.open(self.dataPath + self.paths['imageFilesPath'] + "/" + self.imageNames[self.imageIndex])
            if(cv2):
                retImg = super().pilToCV2(retImg)
        return retImg

    def getPrevImage(self, cv2=False) -> Image:
        retImg = None
        if(self.imageIndex > 1):
            self.imageIndex -= 1
            retImg = Image.open(self.dataPath + self.paths['imageFilesPath'] + "/" + self.imageNames[self.imageIndex])
            if(cv2):
                retImg = super().pilToCV2(retImg)
        else:
            retImg = self.getCurrImage(cv2)
        return retImg

    def getCurrImage(self, cv2=False) -> Image:
        retImg = None
        if(self.imageIndex < len(self.imageNames)):
            retImg = Image.open(self.dataPath + self.paths['imageFilesPath'] + "/" + self.imageNames[self.imageIndex])
            if(cv2):
                retImg = super().pilToCV2(retImg)
        return retImg

    def getCurrImageIndex(self, cv2=False) -> Image:
        return self.imageIndex

    def setImageIndex(self, i: int = 0):
        '''Sets image index to i. Default value is 0. So, if no parameter is provided it resets the image counter.'''
        if(i > len(self.imageNames) or i < 0):
            raise TypeError("Invalid Index!!")
        else:
            self.imageIndex = i

    def getTotalImages(self):
        return len(self.imageNames)

    def getDatasetPath(self):
        return self.dataPath

    def getTrainingPercent(self):
        return self.traingDataPercent

    def setTrainingPercent(self, val):
        self.traingDataPercent = val

    def getDatasetType(self):
        return self.datasetType

    def getBatchImages(self, startIdx=0, batchSize=3, cv2=False):
        retArry = []
        
        endIdx = batchSize + startIdx
        if( endIdx > self.getTotalImages()):
            endIdx = self.getTotalImages() - 1

        for i in range(startIdx, endIdx):
            retArry.append(self.getImageAtIndex(i, cv2))

        return retArry