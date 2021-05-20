#!/usr/bin/python

import sys


from interface import Interface

def main(argc, argv):
    print("In main")
    print('Number of arguments:', argc, 'arguments.')
    vocabularyPath = argv[1]
    dataSetPath = argv[2]
    # print(dataSetPath)




    interface = Interface({"dataPath" : dataSetPath, "dataSet": "Zurich"})
    # print(interface.get_cameraParams())

    # print(interface.getImageNames())

    # nextImageName = ""
    # while nextImageName is not None:
    #     nextImageName = interface.getNextImageName()
    #     print(nextImageName)

    print(interface.getImageAtIndex(0))

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
