# # TODO: Is this the best way to import interfaces?
import os, sys
import uuid

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dataSetInterface import DataSetInterface
from algorithmInterface import AlgorithmInterface

####################################################################################################
# 000 - COMMON FUNCTION
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


####################################################################################################
# 000 - UNIQUE SESSION ID FOR EACH USER
####################################################################################################
session_Id = uuid.uuid1()

####################################################################################################
# 001 - GET CURRENT PROJECT DIRECTORY
####################################################################################################
current_dir = os.getcwd()

####################################################################################################
# 002 - DATASET AND ALGORITHM INSTANCES TO BE USED THROUGHOUT THE TESTBENCH
####################################################################################################
datasetInstance = None
algoInstance = None

zurichInstance = DataSetInterface({"dataSetClass": "zurichDataset", "dataPath" : current_dir + '/Datasets/AGZ'}) #TODO: Read dataset path from user
auAirInstance = DataSetInterface({"dataSetClass": "auAirDataset", "dataPath" : current_dir + '/Datasets/auAir'}) #TODO: Read dataset path from user

yoloInstance = AlgorithmInterface({"algorithmClass": "yoloAlgorithm", "session_id": session_Id})

####################################################################################################
# 003 - SET IMPLEMENTED INTERFACES FOR DROPDOWN OPTIONS
####################################################################################################
availableDatasets = [{'label': 'Zurich Dataset', 'value': 'zurichInstance'}, {'label': 'AuAir Dataset', 'value': 'auAirInstance'}]
availableAlgorithms = [{'label': 'YOLO Darknet Algorithm', 'value': 'yoloInstance'}]

datasetTypes = [{'label': 'Object Detection Dataset', 'value': 'objectDetection'}, {'label': 'Path Planning Dataset', 'value': 'pathPlanning'}]

####################################################################################################
# 004 - SET UPLOAD FILE PATHS FOR ALGORITHM CONFIGURATIONS
####################################################################################################
upload_dir = current_dir + "/upload_files"

####################################################################################################
# 005 - SET DOWNLOAD FILE PATHS FOR ALGORITHM'S BATCH DETECTION FILES
# ####################################################################################################
download_dir = current_dir + "/download_files/" + str(session_Id)