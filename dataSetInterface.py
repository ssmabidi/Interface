from PIL import Image

class DataSetInterface():
    '''An interface for Datasets. This interface intracts with the testbench and provides the data from the datasets.
    It defines the methods which are called by the testbench in order to feed the data to the algorithms through Algorithm Interface.
    The functions defined in this interface simply calls the functions in different dataset classes which implements the DatasetAbstract Class.
    
    Attributes:
        dataSetInstance -- The instance of dataSet class
    '''

    def __init__(self, args: dict):
        '''The constructor of Dataset Interface. This constructor just reads which dataset class is to be created and passes the arguments it recieves.
        The class name and file name should be matching in order to import the class.'''

        instanceClass = args["dataSetClass"]
        module = __import__(instanceClass)
        class_ = getattr(module, instanceClass)
        args.pop("dataSetClass")
        self.dataSetInstance = class_(args)

    def getCameraParams(self) -> dict:
        '''Returns a dictionary with camera paremeter values.
        These values include [camera type "type", width of camera image "width", height of camera image "height",
        frames per second "fps", RGB or BGR "RGB", fx, fy, s, cx, cy, k1, k2, k3, p1, p2].
        Further values can be returned as required or provided by different datasets or algorithms.'''
        
        return self.dataSetInstance.getCameraParams()

    def getOrbParams(self) -> dict:
        '''Returns a dictionary with Oriented FAST and rotated BRIEF (ORB) paremeter values.
        These values include [number of features, scale factor between levels in the scale pyramid "scaleFactor", 
        Number of levels in the scale pyramid "nLevels", Fast threshold "iniThFAST" and "minThFAST"].
        Further values can be returned as required or provided by different datasets or algorithms.'''
        
        return self.dataSetInstance.getOrbParams()

    def getViewerParams(self) -> dict:
        '''Returns a dictionary with Viewer paremeter values.
        These values include [KeyFrameSize,  KeyFrameLineWidth, GraphLineWidth, PointSize, CameraSize,
        CameraLineWidth, ViewpointX, ViewpointY, ViewpointZ, ViewpointF].
        Further values can be returned as required or provided by different datasets or algorithms.'''
        
        return self.dataSetInstance.getViewerParams()

    def getImageNames(self, fullPath: bool = False) -> list:
        '''Returns a list of names of the images sorted by names. Return full path if bool fullPath is True. Otherwise returns relative path.'''
        
        return self.dataSetInstance.getImageNames(fullPath)

    def getNextImageName(self) -> str:
        '''Returns the name of next image in order. If last image name was already provided in previous call it will return None.'''
        
        return self.dataSetInstance.getNextImageName()


    def getImageAtIndex(self, i: int, cv2: bool = False) -> Image:
        """Returns Image at index i. If i is greater than total number of images returns None. The image is returned in cv2 format if cv2 is True.
        Otherwise it is returned in PIL format."""
        
        return self.dataSetInstance.getImageAtIndex(i, cv2)

    def getNextImage(self, cv2: bool = False) -> Image:
        '''Returns next image in order. If last image was already provided in previous call it will return None. The image is returned in cv2 
        format if cv2 is True. Otherwise it is returned in PIL format.'''
        
        return self.dataSetInstance.getNextImage(cv2)

    def getPrevImage(self, cv2: bool = False) -> Image:
        '''Returns previous image in order. If first image was already provided in previous call it will return first image again. The image is 
        returned in cv2 format if cv2 is True. Otherwise it is returned in PIL format.'''
        
        return self.dataSetInstance.getPrevImage(cv2)

    def getCurrImage(self, cv2: bool = False) -> Image:
        '''Returns current image. The image is returned in cv2 format if cv2 is True. Otherwise it is returned in PIL format.'''
        
        return self.dataSetInstance.getCurrImage(cv2)

    def getCurrImageIndex(self) -> Image:
        '''Returns the index of current image.'''
        
        return self.dataSetInstance.getCurrImageIndex()

    def getCurrImageName(self) -> str:
        '''Returns the name of current image file.'''
        
        return self.dataSetInstance.getCurrImageName()

    def setImageIndex(self, i: int = 0):
        '''Sets image index to i. Default value is 0. So, if no parameter is provided it resets the image counter. Does not return any value.'''
        
        self.dataSetInstance.getCurrImageIndex(i)

    def getTotalImages(self) -> int:
        '''Returns total number of images in the dataset.'''
        
        return self.dataSetInstance.getTotalImages()

    def getDatasetPath(self) -> str:
        '''Returns the dataset path.'''
        
        return self.dataSetInstance.getDatasetPath()

    def getTrainingPercent(self) -> int:
        '''Returns the percentage of training data in current dataset.'''
        
        return self.dataSetInstance.getTrainingPercent()

    def setTrainingPercent(self, val: int):
        '''Sets the percentage of training data in current dataset.'''
        
        self.dataSetInstance.setTrainingPercent(val)

    def getDatasetType(self) -> str:
        '''Returns the type of the dataset.'''
        
        return self.dataSetInstance.getDatasetType()

    def getBatchImages(self, cv2: bool = False, getNames: bool = False) -> list:
        '''Returns a batch of images.'''
        
        return self.dataSetInstance.getBatchImages(cv2, getNames)

    def getGroundTruth(self, imageName: str):
        if(self.dataSetInstance.getDatasetType() == "objectDetection"):
            return self.dataSetInstance.getGroundTruth(imageName)
        else:
            raise Exception("This Function is only available for Object Detection DataSets.")

    def getCategory(self, classIdx: int):
        if(self.dataSetInstance.getDatasetType() == "objectDetection"):
            return self.dataSetInstance.getCategory(classIdx)
        else:
            raise Exception("This Function is only available for Object Detection DataSets.")
