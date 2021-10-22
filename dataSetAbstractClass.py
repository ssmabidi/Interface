from abc import ABC, abstractmethod
from PIL import Image
import numpy as np


class DataSetAbstractClass(ABC):
    """
    A generic interface for Datasets. This is an abstract class and it defines the methods which needs to be implemented by the Dataset 
    classes so that they can successfully communicate with the Testbench. It also provides functions which might be commonly used by the 
    dataset classes. e.g. pilToCV2, which converts pil image to cv2 image. This function is used in all dataset classes so it is defined 
    in here. Other such functions can be defined here if needed.
    """

    @abstractmethod
    def __init__(self, args: list):
        """
        The constructor of Dataset Interface. Each class that implements this interface must provide a constructor that 
        will set default values. Some default values are already set in this constructor that could be overriden.

        :param dict args: Contains additional parameters for Dataset initialization and configurations
        """
        pass

    @abstractmethod
    def getCameraParams(self) -> dict:
        """
        Returns a dictionary with camera paremeter values.
        These values include [camera type "type", width of camera image "width", height of camera image "height",
        frames per second "fps", RGB or BGR "RGB", fx, fy, s, cx, cy, k1, k2, k3, p1, p2].
        Further values can be returned as required or provided by different datasets or algorithms.

        :returns: Dictionary with camera parameters
        :rtype: dict[str, int, int, int, bool, float, float, float, float, float, float, float, float, float, float]
        """
        pass

    @abstractmethod
    def getOrbParams(self) -> dict:
        """
        Returns a dictionary with Oriented FAST and rotated BRIEF (ORB) paremeter values.
        These values include [number of features, scale factor between levels in the scale pyramid "scaleFactor", 
        Number of levels in the scale pyramid "nLevels", Fast threshold "iniThFAST" and "minThFAST"].
        Further values can be returned as required or provided by different datasets or algorithms.

        :returns: Dictionary with orb parameters
        :rtype: dict[int, float, int, float, float]
        """
        pass

    @abstractmethod
    def getViewerParams(self) -> dict:
        """
        Returns a dictionary with Viewer paremeter values.
        These values include [KeyFrameSize,  KeyFrameLineWidth, GraphLineWidth, PointSize, CameraSize,
        CameraLineWidth, ViewpointX, ViewpointY, ViewpointZ, ViewpointF].
        Further values can be returned as required or provided by different datasets or algorithms.
        
        :returns: Dictionary with viewer parameters
        :rtype: dict[float, float, float, float, float, float, float, float, float, float]
        """
        pass

    @abstractmethod
    def getImageNames(self, fullPath: bool = False) -> list:
        """
        Returns a list of names of the images sorted by names. Return full path if bool fullPath is True. Otherwise just returns names .
        
        :param bool fullPath: if true return the complete path of the image otherwise just returns the name of the image.

        :returns: List with Image names
        :rtype: list[str]
        """
        pass

    @abstractmethod
    def getNextImageName(self) -> str:
        """Returns the name of next image in order. If last image name was already provided in previous call it will return None.

        :returns: The name of next image
        :rtype: str
        """
        pass

    @abstractmethod
    def getImageAtIndex(self, i: int, cv2: bool = False) -> Image:
        """
        Returns Image at index i. If i is greater than total number of images returns None. The image is returned in cv2 format if cv2 is True.
        Otherwise it is returned in PIL format.

        :param int i: the index at which image should be returned.
        :param bool cv2: if true the returned image is in CV2 format, otherwise PIL Image is returned

        :returns: Image in cv2 to pil format
        :rtype: Image
        """
        pass

    @abstractmethod
    def getNextImage(self, cv2: bool = False) -> Image:
        """Returns next image in order. If last image was already provided in previous call it will return None. The image is returned in cv2 
        format if cv2 is True. Otherwise it is returned in PIL format.

        :param bool cv2: if true the returned image is in CV2 format, otherwise PIL Image is returned

        :returns: Image in cv2 to pil format
        :rtype: Image
        """
        pass

    @abstractmethod
    def getPrevImage(self, cv2: bool = False) -> Image:
        """
        Returns previous image in order. If first image was already provided in previous call it will return first image again. The image is 
        returned in cv2 format if cv2 is True. Otherwise it is returned in PIL format.

        :param bool cv2: if true the returned image is in CV2 format, otherwise PIL Image is returned

        :returns: Image in cv2 to pil format
        :rtype: Image
        """
        pass

    @abstractmethod
    def getCurrImage(self, cv2: bool = False) -> Image:
        """
        Returns current image. The image is returned in cv2 format if cv2 is True. Otherwise it is returned in PIL format.
        
        :param bool cv2: if true the returned image is in CV2 format, otherwise PIL Image is returned

        :returns: Image in cv2 to pil format
        :rtype: Image
        """
        pass

    @abstractmethod
    def getCurrImageIndex(self) -> int:
        """
        Returns the index of current image.

        :returns: The index of current image
        :rtype: int
        """
        pass

    @abstractmethod
    def getCurrImageName(self) -> str:
        """
        Returns the name of current image file.
        
        :returns: The name of current image
        :rtype: str
        """
        pass

    @abstractmethod
    def setImageIndex(self, i: int = 0):
        """
        Sets image index to i. Default value is 0. So, if no parameter is provided it resets the image counter.
        
        :param int i: The index to set
        """
        pass

    @abstractmethod
    def getTotalImages(self) -> int:
        """
        Returns total number of images in the dataset.
        
        :returns: Total number of images in the dataset
        :rtype: int
        """
        pass

    @abstractmethod
    def getDatasetPath(self) -> str:
        """
        Returns the dataset path.
        
        :returns: Full path to the dataset
        :rtype: str
        """
        pass

    @abstractmethod
    def getTrainingPercent(self) -> int:
        """
        Returns the percentage of training data in current dataset.

        :returns: Percentage of data for training
        :rtype: int
        """
        pass

    @abstractmethod
    def setTrainingPercent(self, val: int):
        """
        Sets the percentage of training data in current dataset.

        :param int val: Percentage of data for training
        """
        pass

    @abstractmethod
    def getDatasetType(self) -> str:
        """
        Returns the type of the dataset.

        :returns: Type of dataset
        :rtype: str
        """
        pass

    @abstractmethod
    def getBatchImages(self, cv2: bool = False, getNames: bool = False) -> list:
        """
        Returns a batch of images.

        :param bool cv2: if true the returned image is in CV2 format, otherwise PIL Image is returned
        :param bool getNames: if true it also returns the names of the images, otherwise just the images are returned

        :returns: list of images
        :rtype: list[Image]
        """
        pass

    @abstractmethod
    def getBatchSize(self):
        """
        Returns the size of batch of images.

        :returns: Size of batch
        :rtype: int
        """
        pass

    @abstractmethod
    def setBatchSize(self, size: int):
        """
        Sets the size of batch of images.
        
        :param int size: Size of batch
        """
        pass

    def pilToCV2(self, pil_image: Image) -> Image:
        """
        Returns an image in CV2 format. This function is defined here because it is needed by all the classes which implements this abstract class.

        :param Image pil_image: Image in PIL format

        :returns: Image in CV2 format
        :rtype: Image
        """
        pil_image = pil_image.convert('RGB') 
        open_cv_image = np.array(pil_image) 
        # Convert RGB to BGR 
        open_cv_image = open_cv_image[:, :, ::-1].copy()
        
        return open_cv_image 
