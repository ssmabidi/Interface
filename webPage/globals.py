# # TODO: Is this the best way to import interfaces?
import os, sys
import uuid

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dataSetInterface import DataSetInterface
from algorithmInterface import AlgorithmInterface

####################################################################################################
# TODO: - End here!!
####################################################################################################

import base64
from io import BytesIO
def pil_to_b64(im, enc_format="png", **kwargs):
     """
     Converts a PIL Image into base64 string for HTML displaying
     :param im: PIL Image object
     :param enc_format: The image format for displaying. If saved the image will have that extension.
     :return: base64 encoding
     """

     buff = BytesIO()
     im.save(buff, format=enc_format, **kwargs)
     encoded = base64.b64encode(buff.getvalue()).decode("utf-8")

     return encoded

datasetInstance = None
algoInstance = None

zurichInstance = DataSetInterface({"dataSetClass": "zurichDataset", "dataPath" : '/home/shahamat/Datasets/AGZ'}) #TODO: Read dataset path from user
auAirInstance = DataSetInterface({"dataSetClass": "auAirDataset", "dataPath" : '/home/shahamat/Datasets/auAir'}) #TODO: Read dataset path from user

yoloInstance = AlgorithmInterface({"algorithmClass": "yoloAlgorithm"})

####################################################################################################
# 000 - SET IMPLEMENTED INTERFACES FOR DROPDOWN OPTIONS
####################################################################################################
availableDatasets = [{'label': 'Zurich Dataset', 'value': 'zurichInstance'}, {'label': 'AuAir Dataset', 'value': 'auAirInstance'}]
availableAlgorithms = [{'label': 'YOLO Darknet Algorithm', 'value': 'yoloInstance'}]

datasetTypes = [{'label': 'Object Detection Dataset', 'value': 'objectDetection'}, {'label': 'Path Planning Dataset', 'value': 'pathPlanning'}]

####################################################################################################
# 001 - SET UPLOAD FILE PATHS FOR ALGORITHM CONFIGURATIONS
####################################################################################################
current_dir = os.getcwd()
upload_dir = current_dir + "/upload_files"

session_Id = uuid.uuid1()