import numpy as np
import os
from PIL import Image
from abc import ABC, abstractmethod

class AlgorithmAbstractClass(ABC):
    """
    A generic interface for Algorithms. This is an abstract class and it defines the methods which needs to be implemented by the Algorithm 
    classes so that they can successfully communicate with the Testbench. It also provides functions which might be commonly used by the 
    algorithm classes. e.g. c_array.
    """

    @abstractmethod
    def __init__(self, args: dict):
        """
        The constructor of Algorithm Interface. Each class that implements this interface must provide a constructor that 
        will set default values.
        
        :param dict args: Contains additional parameters for Algorithm initialization and configurations
        """
        pass

    @abstractmethod
    def load_network(self):
        """
        This function loads the algorithm's network and store it in class variable for use in other functions. It must be called after Algorithm 
        interface is instantiated in order for later functions to use the network.
        """
        pass

    @abstractmethod
    def detect_image_file(self, cv2Image: Image, getImage: bool = True) -> list:
        """
        This function takes the image in CV2 format and applies the algorthm to detect the object in the image. A list of dictionaries is returned.
        Each dictionary contains the object it detected, percentage of surety of that object and a list of coordinates where the object is detected on
        the image. If the value of getImage is True(default) it also draws the bonding boxes on the image and returns the image with those bonding boxes
        as well.

        :param Image cv2Image: Image to be detected
        :param bool getImage: Bool if False only the predictions are returned. If True the bounding boxes are printed on the image and then the image is also returned.

        :returns: Predicted objects and the image
        :rtype: list[[str, float, (int, int, int, int)], Image]
        """
        pass

    @abstractmethod
    def set_config_file(self, filePath: str):
        """
        Setter for configuration file.

        :param str filePath: New path from where the config file is to be loaded in next network load.
        """
        pass

    @abstractmethod
    def set_weights_file(self, filePath: str):
        """
        Setter for weights file.

        :param str filePath: New path from where the weights file is to be loaded in next network load.
        """
        pass
    
    @abstractmethod
    def set_data_file(self, filePath: str):
        """
        Setter for data file.

        :param str filePath: New path from where the data file is to be loaded in next network load.
        """
        pass

    @abstractmethod
    def set_threshold(self, threshold: int):
        """
        Setter for threshold value. This threshold defines the minimum percentage of surety the algorithm has in order to detect the object in
        an image.

        :param int threshold: Threshold value.
        """
        pass

    @abstractmethod
    def get_threshold(self):
        """
        Return the threshold value. This threshold defines the minimum percentage of surety the algorithm has in order to detect the object in
        an image.

        :returns: Threshold value
        :rtype: int
        """
        pass

    @abstractmethod
    def reload_network(self):
        """
        This function reload the network with the new files provided by the user. If the new files are not provided it simply reloads the network
        with default files.
        """
        pass

    @abstractmethod
    def batch_detect(self, images: Image, dirPath: str) -> list:
        """
        This function takes a batch of images and runs the algorithm on them.

        :param Image images: List of images.
        :param str dirPath: The path of the directory where the detected images and detection results are stored.

        :returns: A list of detections found in the image
        :rtype: list[dict[str, str, float, (int, int, int, int)]]
        """
        pass

    @abstractmethod
    def get_batch_json(self, getAll:bool = False) -> str:
        """
        This function return a json file path which stores the results of batch_detect run. If getAll is True the results of all the batches run in this session are returned otherwise only the latest run's results are returned.

        :param bool getAll: If true the resuls of all previous runs is returned otherwise just the latest run is returned.

        :returns: The path to json file which contains the results.
        :rtype: str
        """
        pass

    @abstractmethod
    def get_batch_zip(self, getAll:bool = False) -> str:
        """
        This function return a zip file path which stores the predicted images of batch_detect run. If getAll is True the images of all the batches run in this session are returned otherwise only the images of latest run are returned.

        :param bool getAll: If true the resuls of all previous runs is returned otherwise just the latest run is returned.

        :returns: The path to zip file which contains the results.
        :rtype: str
        """
        pass

    @abstractmethod
    def get_colors(self) -> dict:
        """
        This function return a dictionary which contains the classes this algorithm is trained to predicte along with the colors each class is assigned for its bounding box in order to keep it separate from other classes.
        
        :returns: A dictionary of classes and its corresponding color in rbg form
        :rtype: dict[str, tuple(int, int, int)]
        """
        pass


    def c_array(self, ctype, values) -> list:
        """
        Returns the array in C format
        """
        arr = (ctype*len(values))()
        arr[:] = values
        return arr