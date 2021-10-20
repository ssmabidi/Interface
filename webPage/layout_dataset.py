import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import layouts_common as common_layout
import globals

####################################################################################################
# 002 - Datasets
####################################################################################################

datasetsPage = html.Div([

    #####################
    #Row 1 : Header
    common_layout.get_header(),

    #####################
    #Row 2 : Nav bar
    common_layout.get_navbar('datasets'),

    #####################
    #Row 3
    common_layout.get_emptyrow(),

    #####################
    #Row 4 : Filters
    html.Div([ # External row
        html.Div([ # External 12-column

            html.Div([ # Internal row

                #Internal columns
                html.Div([], className = 'col-2'), # Blank 2 columns

                #Filter pt 1
                html.Div([
                    html.Div([
                        html.H5(children='Select a Dataset:', style = {'text-align' : 'left', 'color' : common_layout.corporate_colors['medium-blue-grey']}),
                        #DataSet selection
                        html.Div([
                            dcc.Dropdown(id = 'dataset-config-dropdown',
                                options = globals.availableDatasets,
                                value = None,
                                placeholder = "Select a Dataset",
                                style = {'font-size': '13px', 'color' : common_layout.corporate_colors['medium-blue-grey'], 'white-space': 'nowrap', 'text-overflow': 'ellipsis'}
                            )
                        ], style = {'width' : '70%', 'margin-top' : '5px'})
                    ], style = {'margin-top' : '10px', 'margin-bottom' : '5px', 'text-align' : 'left', 'paddingLeft': 5})
                ], className = 'col-4' ), # Filter part 1

                html.Div([], className = 'col-2') # Blank 2 columns

            ], className = 'row') # Internal row

        ],
        className = 'col-12',
        style = common_layout.filterdiv_borderstyling) # External 12-column

    ],
    className = 'row sticky-top'), # External row

    #####################
    #Row 5
    common_layout.get_emptyrow(),

    #####################
    #Row 6 : Charts
    html.Div([ # External row

        html.Div([], className = 'col-1'), # Blank 1 column

        html.Div([ # External 10-column

            html.Div([
                dbc.Alert(
                    id="notification-toast",
                    is_open=False,
                    duration=2000,
                ),
            ]),
            html.H2(id = "config-header", style = {'color' : common_layout.corporate_colors['white']}),
    
            html.Div([ # Internal row
                # Dataset Image Column
                html.Div([
                    dbc.Card([
                        dbc.CardHeader("Basic Information"),
                        html.Div([
                            dbc.Alert(
                                id="basic-info-toast",
                                is_open=False,
                                duration=2000,
                            ),
                        ]),
                        dbc.CardBody([
                            dbc.FormGroup([
                                dbc.Label("Total number of images", width=2),
                                dbc.Col(
                                    dbc.Input(type="text", id="dataset-total-images", placeholder="0", disabled=True
                                ), width=3, ),
                                dbc.Col(width=1), #empty column
                                dbc.Label("Dataset Tyoe", width=2),
                                dbc.Col(
                                    dcc.Dropdown(id = 'dataset-type-dropdown',
                                        options = globals.datasetTypes,
                                        value = None,
                                        placeholder = "Select a Dataset Type",
                                        style = {'font-size': '13px', 'color' : common_layout.corporate_colors['medium-blue-grey'], 'white-space': 'nowrap', 'text-overflow': 'ellipsis'}
                                ), width=3, ),
                            ], row=True,),

                            dbc.Row([
                                dbc.Label("View Sample data from the Dataset", width=12),
                                dbc.Col([
                                    dbc.Button("First Image", id='img-first', color="light", className="mr-1"),
                                    dbc.Button("Previous Image", id='img-prev', color="light", className="mr-1"),
                                    dbc.Button("Next Image", id='img-next', color="light", className="mr-1"),
                                    dbc.Button("Last Image", id='img-last', color="light", className="mr-1"),
                                    dbc.Label("View Image #", className="mr-1"),
                                    dcc.Input(id='img-range', type='number', min=1, max=1000, step=1) 
                                ], width=6,),
                                dbc.Col([
                                    dcc.Graph(
                                        id="dataset-view-image",
                                        # figure = go.Figure(px.imshow(datasetInstance.getNextImage()))
                                    )
                                ], width=6,)
                            ]),
                        ],)
                    ]),
                    common_layout.get_emptyrow(),
                    dbc.Row([
                    dbc.Col([ dbc.Card([
                        dbc.CardHeader("Basic Configurations"),
                        html.Div([
                            dbc.Alert(
                                id="basic-config-toast",
                                is_open=False,
                                duration=2000,
                            ),
                        ]),
                        dbc.CardBody([
                            dbc.FormGroup([
                                dbc.Label("DataSet path", width=4),
                                dbc.Col(
                                    dbc.Input(type="text", id="dataset-path", placeholder="Enter path to read dataset", disabled=True
                                ), width=8, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("Set Training Data Percentage", width=4),
                                dbc.Col(
                                    dcc.Slider(id='dataset-training-percent', tooltip = { 'always_visible': True, 'placement': 'bottom' }, min=5, max=80, step=5, value=30, marks={5: '5%', 10: '10%', 15: '15%', 20: '20%', 25: '25%', 30: '30%', 35: '35%', 40: '40%', 45: '45%', 50: '50%', 55: '55%', 60: '60%', 65: '65%', 70: '70%', 75: '75%', 80: '80%'},
                                ), width=8, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("Batch Size", width=4),
                                dbc.Col(
                                    dcc.Input(type="text", id='dataset-batch-size', placeholder="0"
                                ), width=8, ),
                            ], row=True,),
                        ],)
                    ]) ], width=6),
                    
                    dbc.Col([dbc.Card([
                        dbc.CardHeader("Camera Configurations"),
                        html.Div([
                            dbc.Alert(
                                id="camera-config-toast",
                                is_open=False,
                                duration=2000,
                            ),
                        ]),
                        dbc.CardBody([
                            dbc.FormGroup([
                                dbc.Label("Camera Type", width=4),
                                dbc.Col(
                                    dbc.Input(type="text", id="camera-type", placeholder="CameraType"
                                ), width=8, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("Width", width=4),
                                dbc.Col(
                                    dbc.Input(type="text", id="camera-width", placeholder="0"
                                ), width=8, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("Height", width=4),
                                dbc.Col(
                                    dbc.Input(type="text", id="camera-height", placeholder="0"
                                ), width=8, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("Frames per second", width=4),
                                dbc.Col(
                                    dbc.Input(type="text", id="camera-fps", placeholder="0"
                                ), width=8, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("Color encoding", width=4),
                                dbc.Col(
                                    dbc.Checklist(options=[{"label": "RGB", "value": 1}], value=[1], id="camera-colorEncoding",
                                ), width=8, ),
                            ], row=True,),
                        ],)
                    ]),], width=6),]),
                    common_layout.get_emptyrow(),

                    dbc.Row([
                    dbc.Col([dbc.Card([
                        dbc.CardHeader("ORB Configurations"),
                        html.Div([
                            dbc.Alert(
                                id="orb-config-toast",
                                is_open=False,
                                duration=2000,
                            ),
                        ]),
                        dbc.CardBody([
                            dbc.FormGroup([
                                dbc.Label("nFeatures", width=4),
                                dbc.Col(
                                    dbc.Input(type="text", id="orb-nFeatures", placeholder="0"
                                ), width=8, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("scaleFactor", width=4),
                                dbc.Col(
                                    dbc.Input(type="text", id="orb-scaleFactor", placeholder="0"
                                ), width=8, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("nLevels", width=4),
                                dbc.Col(
                                    dbc.Input(type="text", id="orb-nLevels", placeholder="0"
                                ), width=8, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("iniThFAST", width=4),
                                dbc.Col(
                                    dbc.Input(type="text", id="orb-iniThFast", placeholder="0"
                                ), width=8, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("minThFAST", width=4),
                                dbc.Col(
                                    dbc.Input(type="text", id="orb-minThFast", placeholder="0"
                                ), width=8, ),
                            ], row=True,),
                        ],)
                    ]),], width=6),
                    
                    
                    dbc.Col([dbc.Card([
                        dbc.CardHeader("Viewer Configurations"),
                        html.Div([
                            dbc.Alert(
                                id="viewer-config-toast",
                                is_open=False,
                                duration=2000,
                            ),
                        ]),
                        dbc.CardBody([
                            dbc.FormGroup([
                                dbc.Label("KeyFrameSize", width=4),
                                dbc.Col(
                                    dbc.Input(type="text", id="viewer-kfs", placeholder="0.05"
                                ), width=8, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("KeyFrameLineWidth", width=4),
                                dbc.Col(
                                    dbc.Input(type="text", id="viewer-kflw", placeholder="1"
                                ), width=8, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("GraphLineWidth", width=4),
                                dbc.Col(
                                    dbc.Input(type="text", id="viewer-glw", placeholder="0.9"
                                ), width=8, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("PointSize", width=4),
                                dbc.Col(
                                    dbc.Input(type="text", id="viewer-ps", placeholder="2"
                                ), width=8, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("CameraSize", width=4),
                                dbc.Col(
                                    dbc.Input(type="text", id="viewer-cs", placeholder="0.08"
                                ), width=8, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("CameraLineWidth", width=4),
                                dbc.Col(
                                    dbc.Input(type="text", id="viewer-clw", placeholder="3"
                                ), width=8, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("ViewpointX", width=4),
                                dbc.Col(
                                    dbc.Input(type="text", id="viewer-cpX", placeholder="0"
                                ), width=8, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("ViewpointY", width=4),
                                dbc.Col(
                                    dbc.Input(type="text", id="viewer-vpY", placeholder="-0.7"
                                ), width=8, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("ViewpointZ", width=4),
                                dbc.Col(
                                    dbc.Input(type="text", id="viewer-vpZ", placeholder="-1.8"
                                ), width=8, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("ViewpointF", width=4),
                                dbc.Col(
                                    dbc.Input(type="text", id="viewer-cpF", placeholder="500"
                                ), width=8, ),
                            ], row=True,),
                        ],)
                    ]) ], width=6)]),
                ], className= 'col-12'),

                # html.Div([], className = 'col-2'), # Blank 2 column

            ],
            className = 'row'), # Internal row
            common_layout.get_emptyrow(),

        ],
        className = 'col-10',
        style = common_layout.externalgraph_colstyling), # External 10-column

        html.Div([], className = 'col-1'), # Blank 1 column

        html.Div([html.P(id="detections")], className= 'col-6'),

    ],
    className = 'row',
    style = common_layout.externalgraph_rowstyling
    ),

    #####################
    #Row 7
    common_layout.get_emptyrow(),

])