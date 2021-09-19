import cv2
import dash
from app import app

import plotly.express as px
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate
import dash_core_components as dcc

import numpy as np

import globals as g_var

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
    dash.dependencies.Output('dataset-image', 'figure'),
    [dash.dependencies.Input('next_image', 'n_clicks'),
    dash.dependencies.Input('dataset-dropdown', 'value')])
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
    [dash.dependencies.Output('algorithm-image', 'figure'),
    dash.dependencies.Output('detections0', 'children'),
    dash.dependencies.Output('detections', 'children')],
    [dash.dependencies.Input('algorithm-dropdown', 'value'),
    dash.dependencies.Input('apply_algo', 'n_clicks')])
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
    [dash.dependencies.Output('config-header', 'children')
    #, dash.dependencies.Output('detections23', 'children')
    ],
    [dash.dependencies.Input('dataset-config-dropdown', 'value')])
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
    return [header]