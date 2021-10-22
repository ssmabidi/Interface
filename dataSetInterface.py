from PIL import Image

class DataSetInterface():
    """
    An interface for Datasets. This interface intracts with the testbench and provides the data from the datasets.
    It defines the methods which are called by the testbench in order to feed the data to the algorithms through Algorithm Interface.
    The functions defined in this interface simply calls the functions in different dataset classes which implements the DatasetAbstract Class.
    """

    def __init__(self, args: dict):
        """
        The constructor of Dataset Interface. This constructor just reads which dataset class is to be created and passes the arguments it recieves.
        The class name and file name should be matching in order to import the class.
        
        :attr datasetInstance: The instance of dataset class

        :param dict[str, str] args: The param must contatin dataSetClass. This will define the dataSet class to be created and used with this instance. The other params provided with this instantiation are passed on to the created dataSe class.
        """

        instanceClass = args["dataSetClass"]
        module = __import__(instanceClass)
        class_ = getattr(module, instanceClass)
        args.pop("dataSetClass")
        self.dataSetInstance = class_(args)

    def getCameraParams(self) -> dict:
        """
        Returns a dictionary with camera paremeter values.
        These values include [camera type "type", width of camera image "width", height of camera image "height",
        frames per second "fps", RGB or BGR "RGB", fx, fy, s, cx, cy, k1, k2, k3, p1, p2].
        Further values can be returned as required or provided by different datasets or algorithms.

        :returns: Dictionary with camera parameters
        :rtype: dict[str, int, int, int, bool, float, float, float, float, float, float, float, float, float, float]
        """
        
        return self.dataSetInstance.getCameraParams()

    def getOrbParams(self) -> dict:
        """
        Returns a dictionary with Oriented FAST and rotated BRIEF (ORB) paremeter values.
        These values include [number of features, scale factor between levels in the scale pyramid "scaleFactor", 
        Number of levels in the scale pyramid "nLevels", Fast threshold "iniThFAST" and "minThFAST"].
        Further values can be returned as required or provided by different datasets or algorithms.

        :returns: Dictionary with orb parameters
        :rtype: dict[int, float, int, float, float]
        """
        
        return self.dataSetInstance.getOrbParams()

    def getViewerParams(self) -> dict:
        """
        Returns a dictionary with Viewer paremeter values.
        These values include [KeyFrameSize,  KeyFrameLineWidth, GraphLineWidth, PointSize, CameraSize,
        CameraLineWidth, ViewpointX, ViewpointY, ViewpointZ, ViewpointF].
        Further values can be returned as required or provided by different datasets or algorithms.
        
        :returns: Dictionary with viewer parameters
        :rtype: dict[float, float, float, float, float, float, float, float, float, float]
        """
        
        return self.dataSetInstance.getViewerParams()

    def getImageNames(self, fullPath: bool = False) -> list:
        """
        Returns a list of names of the images sorted by names. Return full path if bool fullPath is True. Otherwise just returns names .
        
        :param bool fullPath: if true return the complete path of the image otherwise just returns the name of the image.

        :returns: List with Image names
        :rtype: list[str]
        """
        
        return self.dataSetInstance.getImageNames(fullPath)

    def getNextImageName(self) -> str:
        """
        Returns the name of next image in order. If last image name was already provided in previous call it will return None.

        :returns: The name of next image
        :rtype: str
        """
        
        return self.dataSetInstance.getNextImageName()


    def getImageAtIndex(self, i: int, cv2: bool = False) -> Image:
        """
        Returns Image at index i. If i is greater than total number of images returns None. The image is returned in cv2 format if cv2 is True.
        Otherwise it is returned in PIL format.

        :param int i: the index at which image should be returned.
        :param bool cv2: if true the returned image is in CV2 format, otherwise PIL Image is returned

        :returns: Image in cv2 to pil format
        :rtype: Image
        """
        
        return self.dataSetInstance.getImageAtIndex(i, cv2)

    def getNextImage(self, cv2: bool = False) -> Image:
        """
        Returns next image in order. If last image was already provided in previous call it will return None. The image is returned in cv2 
        format if cv2 is True. Otherwise it is returned in PIL format.

        :param bool cv2: if true the returned image is in CV2 format, otherwise PIL Image is returned

        :returns: Image in cv2 to pil format
        :rtype: Image
        """
        
        return self.dataSetInstance.getNextImage(cv2)

    def getPrevImage(self, cv2: bool = False) -> Image:
        """
        Returns previous image in order. If first image was already provided in previous call it will return first image again. The image is 
        returned in cv2 format if cv2 is True. Otherwise it is returned in PIL format.

        :param bool cv2: if true the returned image is in CV2 format, otherwise PIL Image is returned

        :returns: Image in cv2 to pil format
        :rtype: Image
        """
        
        return self.dataSetInstance.getPrevImage(cv2)

    def getCurrImage(self, cv2: bool = False) -> Image:
        """
        Returns current image. The image is returned in cv2 format if cv2 is True. Otherwise it is returned in PIL format.
        
        :param bool cv2: if true the returned image is in CV2 format, otherwise PIL Image is returned

        :returns: Image in cv2 to pil format
        :rtype: Image
        """
        
        return self.dataSetInstance.getCurrImage(cv2)

    def getCurrImageIndex(self) -> int:
        """
        Returns the index of current image.

        :returns: The index of current image
        :rtype: int
        """
        
        return self.dataSetInstance.getCurrImageIndex()

    def getCurrImageName(self) -> str:
        """
        Returns the name of current image file.
        
        :returns: The name of current image
        :rtype: str
        """
        
        return self.dataSetInstance.getCurrImageName()

    def setImageIndex(self, i: int = 0):
        """
        Sets image index to i. Default value is 0. So, if no parameter is provided it resets the image counter.
        
        :param int i: The index to set
        """
        
        self.dataSetInstance.getCurrImageIndex(i)

    def getTotalImages(self) -> int:
        """
        Returns total number of images in the dataset.
        
        :returns: Total number of images in the dataset
        :rtype: int
        """
        
        return self.dataSetInstance.getTotalImages()

    def getDatasetPath(self) -> str:
        """
        Returns the dataset path.
        
        :returns: Full path to the dataset
        :rtype: str
        """
        
        return self.dataSetInstance.getDatasetPath()

    def getTrainingPercent(self) -> int:
        """
        Returns the percentage of training data in current dataset.

        :returns: Percentage of data for training
        :rtype: int
        """
        
        return self.dataSetInstance.getTrainingPercent()

    def setTrainingPercent(self, val: int):
        """
        Sets the percentage of training data in current dataset.

        :param int val: Percentage of data for training
        """
        
        self.dataSetInstance.setTrainingPercent(val)

    def getDatasetType(self) -> str:
        """
        Returns the type of the dataset.

        :returns: Type of dataset
        :rtype: str
        """
        
        return self.dataSetInstance.getDatasetType()

    def getBatchImages(self, cv2: bool = False, getNames: bool = False) -> list:
        """
        Returns a batch of images.

        :param bool cv2: if true the returned image is in CV2 format, otherwise PIL Image is returned
        :param bool getNames: if true it also returns the names of the images, otherwise just the images are returned

        :returns: list of images
        :rtype: list[Image]
        """
        
        return self.dataSetInstance.getBatchImages(cv2, getNames)

    def getGroundTruth(self, imageName: str) -> dict:
        """
        Returns the ground truth objects of the image. The name of image is required because the annotaions file does not have the ground truths in order.

        :param str imagename: name of the image whose ground truths are to be returned.

        :raises Exception: function is not implemented by instance class 

        :returns: dictionary of detected objects with bounding boxes and image
        :rtype: dict[str: dict[int, int, int, int, int], Image]
        """
        if(self.dataSetInstance.getDatasetType() == "objectDetection"):
            return self.dataSetInstance.getGroundTruth(imageName)
        else:
            raise Exception("This Function is only available for Object Detection DataSets.")

    def getCategory(self, classIdx: int) -> dict:
        """
        Returns the label of the class at the index and its assigned color in rgb 

        :param int classIdx: index of the classes

        :raises Exception: function is not implemented by instance class 

        :returns: label of the class at the index and its assigned color in rgb
        :rtype: dict[str, (int, int, int)
        """
        if(self.dataSetInstance.getDatasetType() == "objectDetection"):
            return self.dataSetInstance.getCategory(classIdx)
        else:
            raise Exception("This Function is only available for Object Detection DataSets.")

    def getBatchSize(self) -> int:
        """
        Returns the size of batch of images.

        :returns: Size of batch
        :rtype: int
        """
        return self.dataSetInstance.getBatchSize()

    def setBatchSize(self, size: int):
        """
        Sets the size of batch of images.
        
        :param int size: Size of batch
        """
        self.dataSetInstance.setBatchSize(size)