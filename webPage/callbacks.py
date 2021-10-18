import random
import dash
from app import app

import plotly.express as px
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate
import dash_html_components as html
from dash.dependencies import Input, Output, State

import numpy as np
import globals as g_var

from globals import zurichInstance, auAirInstance, yoloInstance #imports needed separately for globals dict


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
    Input('dataset-dropdown', 'value'),
    Input('prev_image', 'n_clicks'),
    Input('first_image', 'n_clicks'),
    Input('last_image', 'n_clicks'),
    Input('rand_image', 'n_clicks'),
    Input('ground_truth', 'n_clicks'),])
def getNextImage(n_clicks, dataset, n_clicks1, n_clicks2, n_clicks3, n_clicks4, n_clicks5):
    if(dataset == None):
        g_var.datasetInstance = None
        raise PreventUpdate
    ctx = dash.callback_context
    triggerCause = ctx.triggered[0]['prop_id'].split('.')[0]

    g_var.datasetInstance = globals()[dataset]

    fig = None
    if(g_var.datasetInstance != None):
        if(triggerCause ==  'dataset-dropdown'):
            fig = go.Figure(px.imshow(g_var.datasetInstance.getCurrImage()))
        if(triggerCause == 'next_image'):
            fig = go.Figure(px.imshow(g_var.datasetInstance.getNextImage()))
        if(triggerCause == 'first_image'):
            fig = go.Figure(px.imshow(g_var.datasetInstance.getImageAtIndex(0)))
        if(triggerCause == 'last_image'):
            fig = go.Figure(px.imshow(g_var.datasetInstance.getImageAtIndex(g_var.datasetInstance.getTotalImages() - 1)))
        if(triggerCause == 'prev_image'):
            fig = go.Figure(px.imshow(g_var.datasetInstance.getPrevImage()))
        if(triggerCause == 'rand_image'):
            rand_num = random.randint(0, g_var.datasetInstance.getTotalImages())
            fig = go.Figure(px.imshow(g_var.datasetInstance.getImageAtIndex(rand_num)))

        if(triggerCause == 'ground_truth'):
            groundTruth = g_var.datasetInstance.getGroundTruth(g_var.datasetInstance.getCurrImageName())
            fig = go.Figure(px.imshow(groundTruth["orgImg"]))
            for bbox in groundTruth["annotations"]:
                category = g_var.datasetInstance.getCategory(bbox["class"])
                fig.add_shape(
                    type="rect",
                    x0=bbox["left"], 
                    y0=bbox["top"], 
                    x1=bbox["left"] + bbox["width"], 
                    y1=bbox["top"] + bbox["height"],
                    line=dict(color=category["color"], width=2, ),
                )
                fig.add_annotation(
                    x=bbox["left"], 
                    y=bbox["top"],
                    text=category["label"],
                    showarrow=False,
                    font=dict( size=16, color="#ffffff" ),
                    align="center",
                    opacity=1,
                    bgcolor="#000000",
                )

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
    if(algo == None):
        g_var.algoInstance = None
        raise PreventUpdate

    g_var.algoInstance = globals()[algo]

    if(g_var.datasetInstance == None):
        raise PreventUpdate

    fig = None
    img_detections = None
    if(g_var.datasetInstance != None):
        curr_img = g_var.datasetInstance.getCurrImage(cv2=True)
        img_detections = g_var.algoInstance.detect_image_file(curr_img)
        fig = go.Figure(px.imshow(img_detections[1]))
    return fig, str(img_detections[0]), np.array_str(img_detections[1])


####################################################################################################
# 005 - Algorithm Batch Apply 
####################################################################################################
@app.callback(
    [
    Output('batchDetections', 'children')],
    [Input('batch_apply_algo', 'n_clicks'),
    ])
def batchApplyAlgo(n_clicks):
    if(g_var.algoInstance == None or g_var.datasetInstance == None):
        raise PreventUpdate

    g_var.algoInstance.batch_detect()
    # fig = None
    # img_detections = None
    # if(g_var.datasetInstance != None):
    #     curr_img = g_var.datasetInstance.getCurrImage(cv2=True)
    #     img_detections = g_var.algoInstance.detect_image_file(curr_img)
    #     fig = go.Figure(px.imshow(img_detections[1]))
    return ["Applied"]


####################################################################################################
####################################################################################################
####################################################################################################
# Callbacks for Datasets Page
####################################################################################################
####################################################################################################
####################################################################################################

####################################################################################################
# 001 - Select Dataset && # 002 - #006 - View Images
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
    , Output('viewer-kfs', 'value')
    , Output('viewer-kflw', 'value')
    , Output('viewer-glw', 'value')
    , Output('viewer-ps', 'value')
    , Output('viewer-cs', 'value')
    , Output('viewer-clw', 'value')
    , Output('viewer-cpX', 'value')
    , Output('viewer-vpY', 'value')
    , Output('viewer-vpZ', 'value')
    , Output('viewer-cpF', 'value')
    , Output('dataset-view-image', 'figure')
    , Output('dataset-type-dropdown', 'value')
    , Output('img-range', 'max')
    , Output("notification-toast", "children")
    , Output("notification-toast", "is_open")
    , Output("basic-info-toast", "children")
    , Output("basic-info-toast", "is_open")
    ],
    [Input('dataset-config-dropdown', 'value')
    , Input('img-first', 'n_clicks')
    , Input('img-prev', 'n_clicks')
    , Input('img-next', 'n_clicks')
    , Input('img-last', 'n_clicks')
    , Input('img-range', 'value')
    ]
    )
def selectDatasetConfig(dataset, btnFirst, btnPrev, btnNext, btnLast, rangeVal):

    ctx = dash.callback_context
    triggerCause = ctx.triggered[0]['prop_id'].split('.')[0]

    if(dataset == None):
        g_var.datasetInstance = None
        raise PreventUpdate

    g_var.datasetInstance = globals()[dataset]    

    header = 'Select a Dataset'

    notificationText = "Dataset Loaded"
    notificationAlert = True
    basicInfoText = dash.no_update
    basicInfoAlert = False

    fig = None
    if(g_var.datasetInstance != None):
        header = dataset.capitalize() + ' Configurations'
        total_images = g_var.datasetInstance.getTotalImages()
        dataset_path = g_var.datasetInstance.getDatasetPath()
        traingDataPercent = g_var.datasetInstance.getTrainingPercent()
        cameraConfig = g_var.datasetInstance.getCameraParams()
        orbConfig = g_var.datasetInstance.getOrbParams()
        viewerConfig = g_var.datasetInstance.getViewerParams()
        datasetType = g_var.datasetInstance.getDatasetType()
        if(triggerCause == 'dataset-config-dropdown'):
            fig = go.Figure(px.imshow(g_var.datasetInstance.getCurrImage()))
        else:
            notificationText = dash.no_update
            notificationAlert = False
        if(triggerCause == 'img-next'):
            fig = go.Figure(px.imshow(g_var.datasetInstance.getNextImage()))
            basicInfoText = "Next Image Loaded"
            basicInfoAlert = True
        if(triggerCause == 'img-first'):
            basicInfoText = "First Image Loaded"
            basicInfoAlert = True
            fig = go.Figure(px.imshow(g_var.datasetInstance.getImageAtIndex(0)))
        if(triggerCause == 'img-last'):
            basicInfoText = "Last Image Loaded"
            basicInfoAlert = True
            fig = go.Figure(px.imshow(g_var.datasetInstance.getImageAtIndex(total_images - 1)))
        if(triggerCause == 'img-prev'):
            basicInfoText = "Previous Image Loaded"
            basicInfoAlert = True
            fig = go.Figure(px.imshow(g_var.datasetInstance.getPrevImage()))
        if(triggerCause == 'img-range'):
            basicInfoText = "Image Number " + str(rangeVal) + " loaded"
            basicInfoAlert = True
            fig = go.Figure(px.imshow(g_var.datasetInstance.getImageAtIndex(rangeVal)))

    return [header, total_images, dataset_path, traingDataPercent, cameraConfig['type'], cameraConfig['width'], cameraConfig['height'], 
     cameraConfig['fps'], cameraConfig['RGB'], orbConfig['nFeatures'], orbConfig['scaleFactor'], orbConfig['nLevels'], orbConfig['iniThFAST'],
     orbConfig['minThFAST'], viewerConfig['KeyFrameSize'], viewerConfig['KeyFrameLineWidth'], viewerConfig['GraphLineWidth'], viewerConfig['PointSize'],
     viewerConfig['CameraSize'], viewerConfig['CameraLineWidth'], viewerConfig['ViewpointX'], viewerConfig['ViewpointY'], viewerConfig['ViewpointZ'],
     viewerConfig['ViewpointF'], fig, datasetType, total_images, notificationText, notificationAlert, basicInfoText, basicInfoAlert
    ]

####################################################################################################
# 007 - set Training Data Percent
####################################################################################################
@app.callback(
    [ Output("basic-config-toast", "children")
    , Output("basic-config-toast", "is_open")
    ],
    [ Input('dataset-training-percent', 'value')
    ]
    )
def setTrainingPercent(dsTrainVal):
    g_var.datasetInstance.setTrainingPercent(dsTrainVal)
    notificationText = "Training Data Percentage Updated Successfully"
    return [notificationText, True]


####################################################################################################
####################################################################################################
####################################################################################################
# Callbacks for Algorithms Page
####################################################################################################
####################################################################################################
####################################################################################################

####################################################################################################
# 001 - Select Algorithm
####################################################################################################
@app.callback(
    [ Output("algo-notification-toast", "children")
    , Output("algo-notification-toast", "is_open")
    , Output('algorithm-threshold', 'value')
    ],
    [ Input('algorithm-config-dropdown', 'value')
    , Input('reload-network', 'n_clicks')
    ]
    )
def selectAlgoConfig(algo, n_clicks):

    ctx = dash.callback_context
    triggerCause = ctx.triggered[0]['prop_id'].split('.')[0]

    if(triggerCause == 'algorithm-config-dropdown'):
        if(algo == None):
            g_var.algoInstance = None
            raise PreventUpdate

        g_var.algoInstance = globals()[algo]

        thresholdVal = g_var.algoInstance.get_threshold();
        notificationText = "Algorithm Selected"
        return [notificationText, True, thresholdVal]
    
    elif(triggerCause == 'reload-network'):
        g_var.algoInstance.reload_network()

        notificationText = "Network loaded successfully"
        return [notificationText, True, dash.no_update]

    else:
        raise PreventUpdate


####################################################################################################
# 001 - Update Basic Config - Set Threshold
####################################################################################################
@app.callback(
    [ Output("algo-basic-config-toast", "children")
    , Output("algo-basic-config-toast", "is_open")
    ],
    [ Input('algorithm-threshold', 'value')
    ]
    )
def selectAlgoConfig(threshold):

    ctx = dash.callback_context
    triggerCause = ctx.triggered[0]['prop_id'].split('.')[0]

    if(triggerCause == 'algorithm-threshold'):
        if g_var.algoInstance is None:
            raise PreventUpdate
        g_var.algoInstance.set_threshold(threshold)
        notificationText = "Threshold Updated Successfully"
        return [notificationText, True]

    else:
        raise PreventUpdate


####################################################################################################
# 001 - Upload Config File
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
        g_var.algoInstance.set_config_file(g_var.upload_dir+"/"+upload_id+"/"+filenames[0])
        return html.Div([filenames[0] + " uploaded successfully." ])

    return html.Div("No Files Uploaded Yet!")

####################################################################################################
# 002 - Upload Data File
####################################################################################################
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
        g_var.algoInstance.set_data_file(g_var.upload_dir+"/"+upload_id+"/"+filenames[0])
        return html.Div([filenames[0] + " uploaded successfully." ])

    return html.Div("No Files Uploaded Yet!")

####################################################################################################
# 003 - Upload Weights File
####################################################################################################
@app.callback(
    Output('callback-weights-output', 'children'),
    [Input('upload-weights-file', 'isCompleted')],
    [State('upload-weights-file', 'fileNames'),
     State('upload-weights-file', 'upload_id')],
)
def callback_on_completion(iscompleted, filenames, upload_id):
    if not iscompleted:
        return

    if filenames is not None:
        g_var.algoInstance.set_weights_file(g_var.upload_dir+"/"+upload_id+"/"+filenames[0])
        return html.Div([filenames[0] + " uploaded successfully." ])

    return html.Div("No Files Uploaded Yet!")

