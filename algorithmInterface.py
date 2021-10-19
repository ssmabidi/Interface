from PIL import Image

class AlgorithmInterface():
    '''An interface for Algorithms. This interface intracts with the testbench and provides the algorithm classes with the data received from the 
    datasets through testbench. It defines the methods which are called by the testbench in order to communicate with the dataset classes.
    The functions defined in this interface simply calls the functions in different algorithm classes which implements the AlgorithmAbstract Class.
    
    Attributes:
        algorithmInstance -- The instance of algorithm class

    '''

    def __init__(self, args: dict):
        '''The constructor of Algorithm Interface. This constructor just reads which algorithm class is to be created and passes the arguments it
        recieves. The class name and file name should be matching in order to import the class.'''

        instanceClass = args["algorithmClass"]
        module = __import__(instanceClass)
        class_ = getattr(module, instanceClass)
        args.pop("algorithmClass")
        self.algorithmInstance = class_(args)

    def load_network(self):
        '''This function loads the algorithm's network and store it in class variable for use in other functions. It must be called after Algorithm 
        interface is instantiated in order for later functions to use the network.'''
        self.algorithmInstance.load_network()

    def detect_image_file(self, cv2Image: Image, getImage: bool = True) -> list:
        '''This function takes the image in CV2 format and applies the algorthm to detect the object in the image. A list of dictionaries is returned.
        Each dictionary contains the object it detected, percentage of surety of that object and a list of coordinates where the object is detected on
        the image. If the value of getImage is True(default) it also draws the bonding boxes on the image and returns the image with those bonding boxes
        as well.'''
        return self.algorithmInstance.detect_image_file(cv2Image, getImage)

    def set_config_file(self, filePath: str):
        '''Setter for configuration file.'''
        self.algorithmInstance.set_config_file(filePath)

    def set_weights_file(self, filePath: str):
        '''Setter for weights file.'''
        self.algorithmInstance.set_weights_file(filePath)

    def set_data_file(self, filePath: str):
        '''Setter for data file.'''
        self.algorithmInstance.set_data_file(filePath)

    def set_threshold(self, threshold: int):
        '''Setter for threshold value.'''
        self.algorithmInstance.set_threshold(threshold)

    def get_threshold(self) -> int:
        '''Returns the threshold value.'''
        return self.algorithmInstance.get_threshold()

    def reload_network(self):
        '''This function reloads the network.'''
        return self.algorithmInstance.reload_network()

    def batch_detect(self, images: Image) -> dict:
        '''This function runs the algorithm on all the images provided in images parameter and returns the results as a dictionary'''
        return self.algorithmInstance.batch_detect(images)