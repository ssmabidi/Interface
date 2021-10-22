from PIL import Image

class AlgorithmInterface():
    """
    An interface for Algorithms. This interface intracts with the testbench and provides the algorithm classes with the data received from the 
    datasets through testbench. It defines the methods which are called by the testbench in order to communicate with the dataset classes.
    The functions defined in this interface simply calls the functions in different algorithm classes which implements the AlgorithmAbstract Class.
    """

    def __init__(self, args: dict):
        """
        The constructor of Algorithm Interface. This constructor just reads which algorithm class is to be created and passes the arguments it
        recieves. The class name and file name should be matching in order to import the class.
        
        :attr algorithmInstance: The instance of algorithm class

        :param dict[str, str] args: The param must contatin algorithmClass. This will define the algorithm class to be created and used with this instance. The other params provided with this instantiation are passed on to the created algorithm class.
        """

        instanceClass = args["algorithmClass"]
        module = __import__(instanceClass)
        class_ = getattr(module, instanceClass)
        args.pop("algorithmClass")
        self.algorithmInstance = class_(args)

    def load_network(self):
        """
        This function loads the algorithm's network and store it in class variable for use in other functions. It must be called after Algorithm 
        interface is instantiated in order for later functions to use the network.
        """
        self.algorithmInstance.load_network()

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
        return self.algorithmInstance.detect_image_file(cv2Image, getImage)

    def set_config_file(self, filePath: str):
        """
        Setter for configuration file.

        :param str filePath: New path from where the config file is to be loaded in next network load.
        """
        self.algorithmInstance.set_config_file(filePath)

    def set_weights_file(self, filePath: str):
        """
        Setter for weights file.

        :param str filePath: New path from where the weights file is to be loaded in next network load.
        """
        self.algorithmInstance.set_weights_file(filePath)

    def set_data_file(self, filePath: str):
        """
        Setter for data file.

        :param str filePath: New path from where the data file is to be loaded in next network load.
        """
        self.algorithmInstance.set_data_file(filePath)

    def set_threshold(self, threshold: int):
        """
        Setter for threshold value. This threshold defines the minimum percentage of surety the algorithm has in order to detect the object in
        an image.

        :param int threshold: Threshold value.
        """
        self.algorithmInstance.set_threshold(threshold)

    def get_threshold(self) -> int:
        """
        Return the threshold value. This threshold defines the minimum percentage of surety the algorithm has in order to detect the object in
        an image.

        :returns: Threshold value
        :rtype: int
        """
        return self.algorithmInstance.get_threshold()

    def reload_network(self):
        """
        This function reload the network with the new files provided by the user. If the new files are not provided it simply reloads the network
        with default files.
        """
        return self.algorithmInstance.reload_network()

    def batch_detect(self, images: Image, dirPath: str) -> dict:
        """
        This function takes a batch of images and runs the algorithm on them.

        :param Image images: List of images.
        :param str dirPath: The path of the directory where the detected images and detection results are stored.

        :returns: A list of detections found in the image
        :rtype: list[dict[str, str, float, (int, int, int, int)]]
        """
        return self.algorithmInstance.batch_detect(images, dirPath)

    def get_batch_json(self, getAll:bool = False) -> str:
        """
        This function return a json file path which stores the results of batch_detect run. If getAll is True the results of all the batches run in this session are returned otherwise only the latest run's results are returned.

        :param bool getAll: If true the resuls of all previous runs is returned otherwise just the latest run is returned.

        :returns: The path to json file which contains the results.
        :rtype: str
        """
        return self.algorithmInstance.get_batch_json(getAll)

    def get_batch_zip(self, getAll:bool = False) -> str:
        """
        This function return a zip file path which stores the predicted images of batch_detect run. If getAll is True the images of all the batches run in this session are returned otherwise only the images of latest run are returned.

        :param bool getAll: If true the resuls of all previous runs is returned otherwise just the latest run is returned.

        :returns: The path to zip file which contains the results.
        :rtype: str
        """
        return self.algorithmInstance.get_batch_zip(getAll)

    def get_colors(self) -> dict:
        """
        This function return a dictionary which contains the classes this algorithm is trained to predicte along with the colors each class is assigned for its bounding box in order to keep it separate from other classes.
        
        :returns: A dictionary of classes and its corresponding color in rbg form
        :rtype: dict[str, tuple(int, int, int)]
        """
        return self.algorithmInstance.get_colors()