import base64
import os
from urllib.parse import quote as urlquote
import cv2
import dash
from app import app

import plotly.express as px
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output, State

import numpy as np

import globals as g_var


import datetime
import io

import dash_table

import pandas as pd


####################################################################################################
####################################################################################################
####################################################################################################
# Callbacks for Datasets and Algorithms Page
####################################################################################################
####################################################################################################
####################################################################################################


####################################################################################################
# 001 - Dataset Selection Dropdown && 002 - Next Image Button Click
####################################################################################################
@app.callback(
    Output('dataset-image', 'figure'),
    [Input('next_image', 'n_clicks'),
    Input('dataset-dropdown', 'value')])
def getNextImage(n_clicks, dataset):
    if(dataset == None):
        raise PreventUpdate
    if(dataset == 'zurich'):
        g_var.datasetInstance = g_var.zurichInstance
    elif(dataset == 'AuAir'):
        g_var.datasetInstance = g_var.auAirInstance
    else:
        g_var.datasetInstance = None

    fig = None
    if(g_var.datasetInstance != None):
        fig = go.Figure(px.imshow(g_var.datasetInstance.getNextImage()))
    return fig


####################################################################################################
# 003 - Algorithm Selection Dropdown && # 004 - Apply Selected Algorithm on Current image
####################################################################################################
@app.callback(
    [Output('algorithm-image', 'figure'),
    Output('detections0', 'children'),
    Output('detections', 'children')],
    [Input('algorithm-dropdown', 'value'),
    Input('apply_algo', 'n_clicks')])
def applyAlgo(algo, apply_click):
    if(algo == None or g_var.datasetInstance == None):
        raise PreventUpdate
    if(algo == 'yolo'):
        g_var.algoInstance = g_var.yoloInstance
    else:
        g_var.algoInstance = None

    fig = None
    img_detections = None
    if(g_var.datasetInstance != None):
        curr_img = g_var.datasetInstance.getCurrImage(cv2=True)
        img_detections = g_var.algoInstance.detect_image_file(curr_img)
        fig = go.Figure(px.imshow(img_detections[1]))
    return fig, str(img_detections[0]), np.array_str(img_detections[1])


####################################################################################################
####################################################################################################
####################################################################################################
# Callbacks for Datasets Page
####################################################################################################
####################################################################################################
####################################################################################################

####################################################################################################
# 005 - Select Dataset
####################################################################################################
@app.callback(
    [Output('config-header', 'children')
    , Output('dataset-total-images', 'value')
    , Output('dataset-path', 'value')
    , Output('dataset-training-percent', 'value')
    , Output('camera-type', 'value')
    , Output('camera-width', 'value')
    , Output('camera-height', 'value')
    , Output('camera-fps', 'value')
    , Output('camera-colorEncoding', 'value')
    , Output('orb-nFeatures', 'value')
    , Output('orb-scaleFactor', 'value')
    , Output('orb-nLevels', 'value')
    , Output('orb-iniThFast', 'value')
    , Output('orb-minThFast', 'value')
    # , Output('dataset-training-percent', 'value')
    # , Output('dataset-training-percent', 'value')
    # , Output('dataset-training-percent', 'value')
    # , Output('dataset-training-percent', 'value')
    # , Output('dataset-training-percent', 'value')
    # , Output('dataset-training-percent', 'value')
    # , Output('dataset-training-percent', 'value')
    # , Output('dataset-training-percent', 'value')
    # , Output('dataset-training-percent', 'value')
    # , Output('dataset-training-percent', 'value')
    ],
    [Input('dataset-config-dropdown', 'value')])
def selectDatasetConfig(dataset):
    if(dataset == None):
        raise PreventUpdate
    if(dataset == 'zurich'):
        g_var.datasetInstance = g_var.zurichInstance
    elif(dataset == 'AuAir'):
        g_var.datasetInstance = g_var.auAirInstance
    else:
        g_var.datasetInstance = None

    header = 'Select a Dataset'
    if(g_var.datasetInstance != None):
        # g_var.availableDatasets
        header = dataset.capitalize() + ' Configurations'
        total_images = g_var.datasetInstance.getTotalImages()
        dataset_path = g_var.datasetInstance.getDatasetPath()
        traingDataPercent = g_var.datasetInstance.getTrainingPercent()
        cameraConfig = g_var.datasetInstance.get_cameraParams()
        orbConfig = g_var.datasetInstance.getOrbParams()
        traingDataPercent = g_var.datasetInstance.getTrainingPercent()
        traingDataPercent = g_var.datasetInstance.getTrainingPercent()
        traingDataPercent = g_var.datasetInstance.getTrainingPercent()
        traingDataPercent = g_var.datasetInstance.getTrainingPercent()
        traingDataPercent = g_var.datasetInstance.getTrainingPercent()
        traingDataPercent = g_var.datasetInstance.getTrainingPercent()
        traingDataPercent = g_var.datasetInstance.getTrainingPercent()
        traingDataPercent = g_var.datasetInstance.getTrainingPercent()
        print(orbConfig)
    return [header, total_images, dataset_path, traingDataPercent, cameraConfig['type'], cameraConfig['width'], cameraConfig['height'], 
     cameraConfig['fps'], cameraConfig['RGB'], orbConfig['nFeatures'], orbConfig['scaleFactor'], orbConfig['nLevels'], orbConfig['iniThFAST'],
     orbConfig['minThFAST'], 
    # traingDataPercent, traingDataPercent, traingDataPercent, traingDataPercent, traingDataPercent, traingDataPercent, traingDataPercent, traingDataPercent, traingDataPercent, traingDataPercent, traingDataPercent, traingDataPercent, traingDataPercent, traingDataPercent, traingDataPercent, traingDataPercent, traingDataPercent, traingDataPercent, traingDataPercent
    ]


####################################################################################################
####################################################################################################
####################################################################################################
# Callbacks for Algorithms Page
####################################################################################################
####################################################################################################
####################################################################################################

####################################################################################################
# 005 - Upload File
####################################################################################################


@app.callback(
    Output('callback-config-output', 'children'),
    [Input('upload-config-file', 'isCompleted')],
    [State('upload-config-file', 'fileNames'),
     State('upload-config-file', 'upload_id')],
)
def callback_on_completion(iscompleted, filenames, upload_id):
    if not iscompleted:
        return

    if filenames is not None:
        return html.Div([filenames[0] + "uploaded successfully." ])

    return html.Div("No Files Uploaded Yet!")


@app.callback(
    Output('callback-data-output', 'children'),
    [Input('upload-data-file', 'isCompleted')],
    [State('upload-data-file', 'fileNames'),
     State('upload-data-file', 'upload_id')],
)
def callback_on_completion(iscompleted, filenames, upload_id):
    if not iscompleted:
        return

    if filenames is not None:
        return html.Div([filenames[0] + "uploaded successfully." ])

    return html.Div("No Files Uploaded Yet!")

@app.callback(
    Output('callback-weights-output', 'children'),
    [Input('upload-weights-test-file', 'isCompleted')],
    [State('upload-weights-test-file', 'fileNames'),
     State('upload-weights-test-file', 'upload_id')],
)
def callback_on_completion(iscompleted, filenames, upload_id):
    if not iscompleted:
        return

    if filenames is not None:
        return html.Div([filenames[0] + "uploaded successfully." ])

    return html.Div("No Files Uploaded Yet!")