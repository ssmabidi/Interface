from dataSetInterface import DataSetInterface
import numpy as np
import os
from PIL import Image

class auAirDataset(DataSetInterface):

    def __init__(self, args: list):
        # Default values for dataSets taken from related papers
        # Values for Zurich dataSet. Paper link: http://rpg.ifi.uzh.ch/docs/IJRR17_Majdik.pdf
        self.camera = {
            'type': "PinHole",
            'width': 1920,
            'height': 1080,
            'fps': 30,
            'RGB': 1
        }
        self.paths = {
            'imageFilesPath': '/images'
        }
        self.dataPath = args["dataPath"]
        self.imageNames = sorted(os.listdir(self.dataPath + self.paths['imageFilesPath']))
        self.imageNameIndex = 0
        self.imageIndex = 0
        # unzipped_file = zipfile.ZipFile("sample.zip", "r")

        self.traingDataPercent = 25
    
    # Don't know camera parameters. TODO: need to search
    def get_cameraParams(self) -> dict:
        return super().get_cameraParams()

    # TODO: Implement details after more research
    def getOrbParams(self) -> dict:
        return super().getOrbParams()

    # TODO: Implement details after more research
    def getViewerParams(self) -> dict:
        return self.Viewer
