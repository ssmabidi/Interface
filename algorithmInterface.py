import numpy as np
import os
from PIL import Image
from abc import ABC, abstractmethod

class AlgorithmInterface(ABC):

    def __init__(self, args: list):
        '''The constructor of Dataset Interface. Each class that implements this interface must provide a constructor that 
        will set default values. Some default values are already set in this constructor that could be overriden.'''
        pass    
