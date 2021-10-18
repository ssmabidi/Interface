import numpy as np
import os
from PIL import Image
from abc import ABC, abstractmethod

class AlgorithmAbstractClass(ABC):
    '''A generic interface for Algorithms. This is an abstract class and it defines the methods which needs to be implemented by the Algorithm 
    classes so that they can successfully communicate with the Testbench. It also provides functions which might be commonly used by the 
    algorithm classes. e.g. c_array.'''

    @abstractmethod
    def __init__(self, args: list):
        '''The constructor of Algorithm Interface. Each class that implements this interface must provide a constructor that 
        will set default values.'''
        pass

    @abstractmethod
    def load_network(self):
        '''This function loads the algorithm's network and store it in class variable for use in other functions. It must be called after Algorithm 
        interface is instantiated in order for later functions to use the network.'''
        pass

    # @abstractmethod
    # def detect_image(self, file_name):
    #     pass

    @abstractmethod
    def detect_image_file(self, cv2Image, getImage = True):
        pass

    @abstractmethod
    def set_config_file(self, filePath):
        pass

    @abstractmethod
    def set_weights_file(self, filePath):
        pass
    
    @abstractmethod
    def set_data_file(self, filePath):
        pass

    @abstractmethod
    def set_threshold(self, threshold):
        pass

    @abstractmethod
    def get_threshold(self):
        pass

    @abstractmethod
    def reload_network(self):
        pass

    @abstractmethod
    def batch_detect(self):
        pass

    def c_array(self, ctype, values) -> list:
        arr = (ctype*len(values))()
        arr[:] = values
        return arr