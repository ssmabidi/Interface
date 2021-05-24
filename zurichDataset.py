from dataSetInterface import DataSetInterface
import numpy as np
import os
from PIL import Image

class ZurichDataset(DataSetInterface):

    # TODO: Currently these values are copied from EuRoC dataset. Need to update for zurich
    orb = {
        'zurich': {
            'nFeatures': 1000,
            'scaleFactor': 1.2,
            'nLevels': 8,
            'iniThFAST': 20,
            'minThFAST': 7
        }
    }

    # TODO: Currently these values are copied from EuRoC dataset. Need to update for zurich
    viewer = {
        'zurich': {
            'KeyFrameSize': 0.05,
            'KeyFrameLineWidth': 1,
            'GraphLineWidth': 0.9,
            'PointSize': 2,
            'CameraSize': 0.08,
            'CameraLineWidth': 3,
            'ViewpointX': 0,
            'ViewpointY': -0.7,
            'ViewpointZ': -1.8,
            'ViewpointF': 500
        }
    }

    # Transformation from camera to body-frame (imu)
    transformationMatrix = {
        'zurich': [1, 0, 0, -0.07566,
               0, 1, 0, -0.02968,
              0, 0, 1, 0.03227,
               0.0, 0.0, 0.0, 1.0]
    }

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
            'calibrationDataPath': '/calibration_data.npz',
            'logFilesPath': '/Log Files',
            'imageFilesPath': '/MAV Images'
        }
        self.dataPath = args["dataPath"]
        self.imageNames = sorted(os.listdir(self.dataPath + self.paths['imageFilesPath']))
        self.imageNameIndex = 0
        self.imageIndex = 0
        # unzipped_file = zipfile.ZipFile("sample.zip", "r")
    
    # For reading the Intrinsic Matrix lecture from Kyle Simek is used which is available at http://ksimek.github.io/2013/08/13/intrinsic/
    def get_cameraParams(self) -> dict:
        calibrationdata = np.load(self.dataPath + self.paths['calibrationDataPath'])
        mtx = calibrationdata['intrinsic_matrix']
        dist = calibrationdata['distCoeff'][0]
        print(self.camera['type'])

        self.camera['fx'] = mtx[0][0]
        self.camera['s'] = mtx[0][1]
        self.camera['fy'] = mtx[1][1]
        self.camera['cx'] = mtx[0][2]
        self.camera['cy'] = mtx[1][2]

        self.camera['k1'] = dist[0]
        self.camera['k2'] = dist[1]
        self.camera['p1'] = dist[2]
        self.camera['p2'] = dist[3]
        self.camera['k3'] = dist[4]

        calibrationdata.close()

        return self.camera

    # TODO: Implement details after more research
    def getOrbParams(self) -> dict:
        return self.orb

    # TODO: Implement details after more research
    def getViewerParams(self) -> dict:
        return self.Viewer

    def getImageAtIndex(self, i: int) -> Image:
        """Returns Image at index i. If i is greater than total number of images returns None."""
        # print(self.dataPath + self.paths['imageFilesPath'] + "/" + self.imageNames[i])
        if(i >= 0 and i < len(self.imageNames)):
            img = Image.open(self.dataPath + self.paths['imageFilesPath'] + "/" + self.imageNames[i])
            return img
        else:
            return None

    def getNextImage(self) -> Image:
        retImg = None
        if(self.imageIndex < len(self.imageNames)):
            retImg = Image.open(self.dataPath + self.paths['imageFilesPath'] + "/" + self.imageNames[self.imageIndex])
            self.imageIndex += 1
        return retImg
