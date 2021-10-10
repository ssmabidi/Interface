####################################################################################################
# TODO: - Testing!! This part of code should be refactored out of this file and placed somewhere
# ------- else
####################################################################################################


# # TODO: Is this the best way to import interfaces?
import os, sys
import uuid
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from zurichDataset import ZurichDataset
from auAirDataset import auAirDataset
from yoloAlgorithm import yoloAlgorithm


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

zurichInstance = ZurichDataset({"dataPath" : '/home/shahamat/Datasets/AGZ'}) #TODO: Read dataset path from user
auAirInstance = auAirDataset({"dataPath" : '/home/shahamat/Datasets/auair2019data'}) #TODO: Read dataset path from user

yoloInstance = yoloAlgorithm([])

# yoloInstance.load_network()

####################################################################################################
# 000 - SET IMPLEMENTED INTERFACES FOR DROPDOWN OPTIONS
####################################################################################################
availableDatasets = [{'label': 'Zurich Dataset', 'value': 'zurich'}, {'label': 'AuAir Dataset', 'value': 'AuAir'}]
availableAlgorithms = [{'label': 'YOLO Darknet Algorithm', 'value': 'yolo'}]

datasetTypes = [{'label': 'Object Detection Dataset', 'value': 'objectDetection'}, {'label': 'Path Planning Dataset', 'value': 'pathPlanning'}]

####################################################################################################
# 001 - SET UPLOAD FILE PATHS FOR ALGORITHM CONFIGURATIONS
####################################################################################################
current_dir = os.getcwd()
upload_dir = current_dir + "/upload_files"

session_Id = uuid.uuid1()