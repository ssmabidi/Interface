import numpy as np
import os
from PIL import Image
from abc import ABC, abstractmethod

class AlgorithmInterface(ABC):

    def __init__(self, args: list):
        '''The constructor of Dataset Interface. Each class that implements this interface must provide a constructor that 
        will set default values. Some default values are already set in this constructor that could be overriden.'''
        pass    

    
    def set_config_file(self, filePath):
        self.yolo_config = filePath

    def set_weights_file(self, filePath):
        self.weights_file = filePath
    
    def set_data_file(self, filePath):
        self.data_file = filePath