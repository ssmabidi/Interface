from dataSetAbstractClass import DataSetAbstractClass
import numpy as np
import os
from PIL import Image

class zurichDataset(DataSetAbstractClass):
    """
    Zurich Dataset class. This is the final class whose instance is used in the dataset interface class. It provides the implementation of all the 
    functions defined in the datasetAbstractClass.
    """

    def __init__(self, args: list):
        """
        The constructor of Zurich Dataset Class.This function defines the default values for some configurations. These values can be overwritten
        by the user through the testbench by using appropriate setter functions. These default values are taken from the paper http://rpg.ifi.uzh.ch/docs/IJRR17_Majdik.pdf
        
        :attr camera:  dict
        :attr paths: dict
        :attr dataPath: str
        :attr imageNames: list
        :attr orb: dict
        :attr viewer: dict
        :attr traingDataPercent: int
        :attr datasetType: str
        :attr imageIndex: int
        :attr batchSize: int
        :attr startIdx: int

        :param dict[str] args: The param must contatin dataPath. This will define the dataSet path at which images are present.
        """

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

        self.imageIndex = 0
        self.batchSize = 50
        self.startIdx=  0
    
    def getCameraParams(self) -> dict:
        """
        Returns a dictionary with camera paremeter values.
        These values include [camera type "type", width of camera image "width", height of camera image "height",
        frames per second "fps", RGB or BGR "RGB", fx, fy, s, cx, cy, k1, k2, k3, p1, p2].
        Further values can be returned as required or provided by different datasets or algorithms.

        For reading the Intrinsic Matrix lecture from Kyle Simek is used which is available at http://ksimek.github.io/2013/08/13/intrinsic/

        :returns: Dictionary with camera parameters
        :rtype: dict[str, int, int, int, bool, float, float, float, float, float, float, float, float, float, float]
        """
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
        """
        Returns a dictionary with Oriented FAST and rotated BRIEF (ORB) paremeter values.
        These values include [number of features, scale factor between levels in the scale pyramid "scaleFactor", 
        Number of levels in the scale pyramid "nLevels", Fast threshold "iniThFAST" and "minThFAST"].
        Further values can be returned as required or provided by different datasets or algorithms.

        :returns: Dictionary with orb parameters
        :rtype: dict[int, float, int, float, float]
        """
        return self.orb

    def getViewerParams(self) -> dict:
        """
        Returns a dictionary with Viewer paremeter values.
        These values include [KeyFrameSize,  KeyFrameLineWidth, GraphLineWidth, PointSize, CameraSize,
        CameraLineWidth, ViewpointX, ViewpointY, ViewpointZ, ViewpointF].
        Further values can be returned as required or provided by different datasets or algorithms.
        
        :returns: Dictionary with viewer parameters
        :rtype: dict[float, float, float, float, float, float, float, float, float, float]
        """
        return self.viewer

    def getImageNames(self, fullPath: bool = False) -> list:
        """
        Returns a list of names of the images sorted by names. Return full path if bool fullPath is True. Otherwise just returns names .
        
        :param bool fullPath: if true return the complete path of the image otherwise just returns the name of the image.

        :returns: List with Image names
        :rtype: list[str]
        """
        if(fullPath):
            return [self.dataPath + self.paths['imageFilesPath'] + "/" + s for s in self.imageNames]
        else:
            return self.imageNames

    def getNextImageName(self) -> str:
        """
        Returns the name of next image in order. If last image name was already provided in previous call it will return None.

        :raises TypeError: ImageNames is not initialized

        :returns: The name of next image
        :rtype: str
        """
        if(self.imageNames == None):
            raise TypeError("Object parameter 'self.imageNames' is not initialized")
        retFileName = None
        if(self.imageIndex < len(self.imageNames)):
            retFileName = self.imageNames[self.imageIndex]
            self.imageIndex += 1
        return retFileName

    def getImageAtIndex(self, i: int, cv2: bool = False) -> Image:
        """
        Returns Image at index i. If i is greater than total number of images returns None. The image is returned in cv2 format if cv2 is True.
        Otherwise it is returned in PIL format.

        :param int i: the index at which image should be returned.
        :param bool cv2: if true the returned image is in CV2 format, otherwise PIL Image is returned

        :returns: Image in cv2 to pil format
        :rtype: Image
        """
        if(i >= 0 and i < len(self.imageNames)):
            img = Image.open(self.dataPath + self.paths['imageFilesPath'] + "/" + self.imageNames[i])
            self.imageIndex = i
            if(cv2):
                return super().pilToCV2(img)
            return img
        else:
            return None

    def getNextImage(self, cv2: bool = False) -> Image:
        """
        Returns next image in order. If last image was already provided in previous call it will return None. The image is returned in cv2 
        format if cv2 is True. Otherwise it is returned in PIL format.

        :param bool cv2: if true the returned image is in CV2 format, otherwise PIL Image is returned

        :returns: Image in cv2 to pil format
        :rtype: Image
        """
        retImg = None
        if(self.imageIndex < len(self.imageNames)):
            self.imageIndex += 1
            retImg = Image.open(self.dataPath + self.paths['imageFilesPath'] + "/" + self.imageNames[self.imageIndex])
            if(cv2):
                retImg = super().pilToCV2(retImg)
        return retImg

    def getPrevImage(self, cv2: bool = False) -> Image:
        """
        Returns previous image in order. If first image was already provided in previous call it will return first image again. The image is 
        returned in cv2 format if cv2 is True. Otherwise it is returned in PIL format.

        :param bool cv2: if true the returned image is in CV2 format, otherwise PIL Image is returned

        :returns: Image in cv2 to pil format
        :rtype: Image
        """
        retImg = None
        if(self.imageIndex > 1):
            self.imageIndex -= 1
            retImg = Image.open(self.dataPath + self.paths['imageFilesPath'] + "/" + self.imageNames[self.imageIndex])
            if(cv2):
                retImg = super().pilToCV2(retImg)
        else:
            retImg = self.getCurrImage(cv2)
        return retImg

    def getCurrImage(self, cv2: bool = False) -> Image:
        """
        Returns current image. The image is returned in cv2 format if cv2 is True. Otherwise it is returned in PIL format.
        
        :param bool cv2: if true the returned image is in CV2 format, otherwise PIL Image is returned

        :returns: Image in cv2 to pil format
        :rtype: Image
        """
        retImg = None
        if(self.imageIndex < len(self.imageNames)):
            retImg = Image.open(self.dataPath + self.paths['imageFilesPath'] + "/" + self.imageNames[self.imageIndex])
            if(cv2):
                retImg = super().pilToCV2(retImg)
        return retImg

    def getCurrImageIndex(self) -> int:
        """
        Returns the index of current image.

        :returns: The index of current image
        :rtype: int
        """
        return self.imageIndex

    def getCurrImageName(self) -> str:
        """
        Returns the name of current image file.
        
        :returns: The name of current image
        :rtype: str
        """
        return self.imageNames[self.imageIndex]

    def setImageIndex(self, i: int = 0):
        """
        Sets image index to i. Default value is 0. So, if no parameter is provided it resets the image counter.
        
        :raises TypeError: Index is invalid

        :param int i: The index to set
        """
        if(i > len(self.imageNames) or i < 0):
            raise TypeError("Invalid Index!!")
        else:
            self.imageIndex = i

    def getTotalImages(self):
        """
        Returns total number of images in the dataset.
        
        :returns: Total number of images in the dataset
        :rtype: int
        """
        return len(self.imageNames)

    def getDatasetPath(self):
        """
        Returns the dataset path.
        
        :returns: Full path to the dataset
        :rtype: str
        """
        return self.dataPath

    def getTrainingPercent(self):
        """
        Returns the percentage of training data in current dataset.

        :returns: Percentage of data for training
        :rtype: int
        """
        return self.traingDataPercent

    def setTrainingPercent(self, val: int):
        """
        Sets the percentage of training data in current dataset.

        :param int val: Percentage of data for training
        """
        self.traingDataPercent = val

    def getDatasetType(self) -> str:
        """
        Returns the type of the dataset.

        :returns: Type of dataset
        :rtype: str
        """
        return self.datasetType

    def getBatchImages(self, cv2: bool = False, getNames: bool = False) -> list:
        """
        Returns a batch of images.

        :param bool cv2: if true the returned image is in CV2 format, otherwise PIL Image is returned
        :param bool getNames: if true it also returns the names of the images, otherwise just the images are returned

        :returns: list of images
        :rtype: list[Image]
        """
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

    def getBatchSize(self) -> int:
        """
        Returns the size of batch of images.

        :returns: Size of batch
        :rtype: int
        """
        return self.batchSize

    def setBatchSize(self, size: int):
        """
        Sets the size of batch of images.
        
        :param int size: Size of batch
        """
        self.batchSize = int(size)