import random
import dash
from app import app

import plotly.express as px
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc


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
    [Output('dataset-image', 'figure')
    , Output("dsnalgo-error-toast", "children")
    , Output("dsnalgo-error-toast", "is_open")
    ],
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

    toast_text = dash.no_update
    toast_open = False

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
            try:
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
            except Exception as inst:
                fig = dash.no_update
                toast_text = str(inst)
                toast_open = True

    return [fig, toast_text, toast_open]


####################################################################################################
# 003 - Algorithm Selection Dropdown && # 004 - Apply Selected Algorithm on Current image &&
# 005 - Algorithm Batch Apply
####################################################################################################
@app.callback(
    [Output('algorithm-image', 'figure'),
    Output('results_body', 'children'),
    Output('results_header', 'children'),
    Output('results_collapseable', 'is_open')],
    [Input('algorithm-dropdown', 'value'),
    Input('apply_algo', 'n_clicks'),
    Input('batch_apply_algo', 'n_clicks'),])
def applyAlgo(algo, apply_click, batch_click):

    ctx = dash.callback_context
    triggerCause = ctx.triggered[0]['prop_id'].split('.')[0]

    if(triggerCause == 'algorithm-dropdown' or triggerCause == 'apply_algo'):
        if(algo == None):
            g_var.algoInstance = None
            raise PreventUpdate

        g_var.algoInstance = globals()[algo]

        if(g_var.datasetInstance == None):
            raise PreventUpdate

        fig = None
        img_detections = None
        table_header = [
            html.Thead(html.Tr([html.Th("Detected Object"), html.Th("Accuracy"), html.Th("x0"), html.Th("y0"), html.Th("width"), html.Th("height")]))
        ]
        table_body = None
        if(g_var.datasetInstance != None):
            curr_img = g_var.datasetInstance.getCurrImage(cv2=True)
            img_detections = g_var.algoInstance.detect_image_file(curr_img)
            fig = go.Figure(px.imshow(img_detections[1]))
            colors = g_var.algoInstance.get_colors()
            rows = []
            for detect in img_detections[0]:
                category = detect[0]
                fig.add_shape(
                    type="rect",
                    x0=detect[2][0] - (int(detect[2][2]) / 2), 
                    y0=detect[2][1] - (int(detect[2][3]) / 2), 
                    x1=detect[2][0] + (int(detect[2][2]) / 2), 
                    y1=detect[2][1] + (int(detect[2][3]) / 2),
                    line=dict(color='rgb' + str(colors[category]), width=2, ),
                )
                fig.add_annotation(
                    x=detect[2][0] - (int(detect[2][2]) / 2), 
                    y=detect[2][1] - (int(detect[2][3]) / 2),
                    text=category + " [" + detect[1] + "]",
                    showarrow=False,
                    font=dict( size=16, color="#ffffff" ),
                    align="center",
                    opacity=1,
                    bgcolor="#000000",
                )
                rows.append(html.Tr([html.Td(detect[0]), html.Td(detect[1]), html.Td(detect[2][0]), html.Td(detect[2][1]), html.Td(detect[2][2]), html.Td(detect[2][3])]))
            table_body = [html.Tbody(rows)]
        table = dbc.Table(table_header + table_body, bordered = True)
        return [fig, table, "Detection Results", True]

    if(triggerCause == 'batch_apply_algo'):
        if(g_var.algoInstance == None or g_var.datasetInstance == None):
            raise PreventUpdate

        img_detections = g_var.algoInstance.batch_detect(g_var.datasetInstance.getBatchImages(cv2=True, getNames=True), dirPath=g_var.download_dir)
        table_header = [
            html.Thead(html.Tr([html.Th("Image Name"), html.Th("Detected Object"), html.Th("Accuracy"), html.Th("x0"), html.Th("y0"), html.Th("width"), html.Th("height")]))
        ]
        rows = []
        for image in img_detections:
            for detect in image["bbox"]:
                rows.append(html.Tr([html.Td(image["image_name"]), html.Td(detect[0]), html.Td(detect[1]), html.Td(detect[2][0]), html.Td(detect[2][1]), html.Td(detect[2][2]), html.Td(detect[2][3])]))
        table_body = [html.Tbody(rows)]
        table = dbc.Table(table_header + table_body, bordered = True)
        
        buttons = html.Div([ #Download Buttons row
            html.Div([
                dbc.Button("Download Current Results as JSON", id="download_json", color='dark', className='mr-1 mb-1',),
                dbc.Button("Download Current Detected Images as zip", id="download_zip", color='dark', className='mr-1 mb-1',),
                dbc.Button("Download All Results as JSON", id="download_json_all", color='dark', className='mr-1 mb-1',),
                dbc.Button("Download All Detected Images as zip", id="download_zip_all", color='dark', className='mr-1 mb-1',),
                dcc.Download(id="download-results"),
            ], className='col-12'),
        ], className = 'row')

        return [dash.no_update, [buttons, table], "Batch Apply Results", True]

    else:
        raise PreventUpdate

####################################################################################################
# 006 - 009 - Download JSON  and Zip Files
####################################################################################################
@app.callback(
    Output("download-results", "data"),
    [Input("download_json", "n_clicks"),
    Input("download_json_all", "n_clicks"),
    Input("download_zip", "n_clicks"),
     Input("download_zip_all","n_clicks")]
)
def download_results(n_clicks, n_clicks1, n_clicks2, n_clicks3):
    ctx = dash.callback_context
    triggerCause = ctx.triggered[0]['prop_id'].split('.')[0]

    if(triggerCause == 'download_json'):
        return dcc.send_file(g_var.algoInstance.get_batch_json())
    if(triggerCause == 'download_json_all'):
        return dcc.send_file(g_var.algoInstance.get_batch_json(getAll=True))
    if(triggerCause == 'download_zip'):
        return dcc.send_file(g_var.algoInstance.get_batch_zip())
    if(triggerCause == 'download_zip_all'):
        return dcc.send_file(g_var.algoInstance.get_batch_zip(getAll=True))
    else:
        raise PreventUpdate


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
    , Output('dataset-batch-size', 'value')
    ],
    [Input('dataset-config-dropdown', 'value')
    , Input('img-first', 'n_clicks')
    , Input('img-prev', 'n_clicks')
    , Input('img-next', 'n_clicks')
    , Input('img-last', 'n_clicks')
    , Input('img-range', 'value')
    ],
    [State("dataset-config-dropdown","options")]
    )
def selectDatasetConfig(dataset, btnFirst, btnPrev, btnNext, btnLast, rangeVal, options):

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
        the_label = [x['label'] for x in options if x['value'] == dataset]
        header = the_label[0] + ' Configurations'
        total_images = g_var.datasetInstance.getTotalImages()
        dataset_path = g_var.datasetInstance.getDatasetPath()
        traingDataPercent = g_var.datasetInstance.getTrainingPercent()
        cameraConfig = g_var.datasetInstance.getCameraParams()
        orbConfig = g_var.datasetInstance.getOrbParams()
        viewerConfig = g_var.datasetInstance.getViewerParams()
        datasetType = g_var.datasetInstance.getDatasetType()
        datasetBatchSize = g_var.datasetInstance.getBatchSize()
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
     viewerConfig['ViewpointF'], fig, datasetType, total_images, notificationText, notificationAlert, basicInfoText, basicInfoAlert, datasetBatchSize
    ]

####################################################################################################
# 007 - set Training Data Percent
####################################################################################################
@app.callback(
    [ Output("basic-config-toast", "children")
    , Output("basic-config-toast", "is_open")
    ],
    [ Input('dataset-training-percent', 'value'),
      Input("dataset-batch-size", "value")
    ]
    )
def setBasicConfig(dsTrainVal, batchSize):
    ctx = dash.callback_context
    triggerCause = ctx.triggered[0]['prop_id'].split('.')[0]

    if(triggerCause == "dataset-training-percent"):
        g_var.datasetInstance.setTrainingPercent(dsTrainVal)
        notificationText = "Training Data Percentage Updated Successfully"
        return [notificationText, True]
    elif(triggerCause == "dataset-batch-size"):
        g_var.datasetInstance.setBatchSize(batchSize)
        notificationText = "Batch Size Updated Successfully"
        return [notificationText, True]
    else:
        raise PreventUpdate


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

