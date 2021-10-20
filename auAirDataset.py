from dataSetAbstractClass import DataSetAbstractClass
import os
from PIL import Image
import json
import random
        

class auAirDataset(DataSetAbstractClass):

    def __init__(self, args: list):
        # Default values for dataSets taken from related papers
        
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
            'imageFilesPath': '/auair2019data/images',
            'annotations': '/annotations_v1.1.json'
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

        self.traingDataPercent = 25
        self.datasetType = 'objectDetection'

        self.imageIndex = 0
        self.batchSize = 50

        with open(self.dataPath + self.paths['annotations']) as f:
            self.dataFile = json.load(f)

        self.categories = {}
        
        for category in self.dataFile["categories"]:
            r = lambda: random.randint(0,255)
            self.categories[category] = '#%02X%02X%02X' % (r(),r(),r())

        self.annotations = {item['image_name']:item for item in self.dataFile["annotations"]}

    def getCameraParams(self) -> dict:
        return self.camera

    def getOrbParams(self) -> dict:
        return self.orb

    def getViewerParams(self) -> dict:
        return self.viewer

    def getDatasetType(self) -> str:
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
        if(self.imageIndex < len(self.imageNames)):
            retFileName = self.imageNames[self.imageIndex]
            self.imageIndex += 1
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

    def getCurrImageName(self) -> str:
        return self.imageNames[self.imageIndex]

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

    def getBatchImages(self, cv2=False, getNames: bool = False):
        retArry = []

        if(self.startIdx > self.getTotalImages()):
            self.startIdx = 0
        
        endIdx = self.batchSize + self.startIdx
        if( endIdx > self.getTotalImages()):
            endIdx = self.getTotalImages() - 1

        for i in range(self.startIdx, endIdx):
            if (getNames):
                retArry.append({"name": self.imageNames[i], "image": self.getImageAtIndex(i,cv2)})
            else:
                retArry.append(self.getImageAtIndex(i, cv2))

        self.startIdx += self.batchSize
        return retArry

    def getGroundTruth(self, imageName: str, getOriginalImage: bool = True) -> dict:
        retImg = None
        if(getOriginalImage):
            retImg = self.getImageAtIndex(self.imageNames.index(imageName))
        return {"annotations": self.annotations[imageName]["bbox"], "orgImg": retImg}

    def getCategory(self, classIdx: int):
        category = list(self.categories)[classIdx]
        color = self.categories[category]
        return {"label": category, "color": color}