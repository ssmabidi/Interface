#!/usr/bin/python

import sys
import time
# import cv2
import numpy as np
from matplotlib import pyplot as plt

from PIL import Image

from yoloAlgorithm import yoloAlgorithm

from zurichDataset import ZurichDataset


def main(argc, argv):
    """Testing interface functions"""
    print("In main")
    print('Number of arguments:', argc, 'arguments.')

    yoloInstance = yoloAlgorithm([])
    yoloInstance.load_network()
    yoloInstance.detect_image()

    vocabularyPath = argv[1]
    dataSetPath = argv[2]



    interface = ZurichDataset({"dataPath" : dataSetPath})
    cameraParams = interface.get_cameraParams()

    print(cameraParams)
    print(interface.getImageNames())

    # nextImageName = ""
    # while nextImageName is not None:
    #     nextImageName = interface.getNextImageName()
    #     print(nextImageName)


    interface.getImageAtIndex(0).show()


    size = (cameraParams['width'],cameraParams['height'])
    # out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
    image = ""
    # while image is not None:
    image = interface.getNextImage()
        # imageNp = np.array(image)
        # cv2.imshow('Image', imageNp)
        # plt.imshow(image)
        # image.show()
        # time.sleep(0.5)
        # image.close()
        # cv2.destroyAllWindows()
        
        # out.write(np.uint8(imageNp))
    # out.release()
        # image.show()
        # time.sleep(0.5)
        # # image.close()
        # # hide image
        # for proc in psutil.process_iter():
        #     if proc.name() == "display":
        #         proc.kill()


    # for i in range(1,argc):
    #     print(argv[i])
    # print('Argument List:', str(argv))

if __name__ == '__main__':

    main(len(sys.argv), sys.argv)

    # ./Examples/Monocular/mono_euroc
    # ARGS:
    #  ./Vocabulary/ORBvoc.txt ./Examples/Monocular/EuRoC.yaml ~/Datasets/EuRoc/MH01 ./Examples/Monocular/EuRoC_TimeStamps/MH01.txt dataset-MH01_mono
    #
    # ./Examples/Monocular-Inertial/mono_inertial_euroc
    # ARGS
    #  ./Vocabulary/ORBvoc.txt ./Examples/Monocular-Inertial/EuRoC.yaml ~/Datasets/EuRoc/MH01 ./Examples/Monocular-Inertial/EuRoC_TimeStamps/MH01.txt dataset-MH01_monoi
    #
    # ./Examples/Stereo/stereo_euroc
    #  ./Vocabulary/ORBvoc.txt ./Examples/Stereo/EuRoC.yaml ~/Datasets/EuRoc/MH01 ./Examples/Stereo/EuRoC_TimeStamps/MH01.txt dataset-MH01_stereo

    # parser = argparse.ArgumentParser(description='Create a ArcHydro schema')
    # parser.add_argument('--workspace', metavar='path', required=True,
    #                     help='the path to workspace')
    # parser.add_argument('--schema', metavar='path', required=True,
    #                     help='path to schema')
    # parser.add_argument('--dem', metavar='path', required=True,
    #                     help='path to dem')
    # args = parser.parse_args()
    # model_schema(workspace=args.workspace, schema=args.schema, dem=args.dem)
