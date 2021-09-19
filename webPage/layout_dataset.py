import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash_html_components.Div import Div

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
            html.H2(id = "config-header", style = {'color' : common_layout.corporate_colors['white']}),
    
            html.Div([ # Internal row
                # Dataset Image Column
                html.Div([
                     dbc.Card([
                        dbc.CardHeader("Basic Configurations"),
                        dbc.CardBody([
                            dbc.FormGroup([
                                dbc.Label("DataSet path", width=2),
                                dbc.Col(
                                    dbc.Input(type="text", id="dataset-path", placeholder="Enter path to read dataset"
                                ), width=10, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("Set Training Data Percentage", width=2),
                                dbc.Col(
                                    dcc.Slider(id='dataset-training-percent', min=5, max=80, step=5, value=30, marks={5: '5%', 10: '10%', 15: '15%', 20: '20%', 25: '25%', 30: '30%', 35: '35%', 40: '40%', 45: '45%', 50: '50%', 55: '55%', 60: '60%', 65: '65%', 70: '70%', 75: '75%', 80: '80%'},
                                ), width=10, ),
                            ], row=True,),
                        ],)
                    ]),
                    common_layout.get_emptyrow(),
                    dbc.Card([
                        dbc.CardHeader("Camera Configurations"),
                        dbc.CardBody([
                            dbc.FormGroup([
                                dbc.Label("Camera Type", width=2),
                                dbc.Col(
                                    dbc.Input(type="text", id="dataset-path", placeholder="Pinhole"
                                ), width=10, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("Width", width=2),
                                dbc.Col(
                                    dbc.Input(type="text", id="dataset-path", placeholder="1920"
                                ), width=10, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("Height", width=2),
                                dbc.Col(
                                    dbc.Input(type="text", id="dataset-path", placeholder="1080"
                                ), width=10, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("Frames per second", width=2),
                                dbc.Col(
                                    dbc.Input(type="text", id="dataset-path", placeholder="30"
                                ), width=10, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("Color encoding", width=2),
                                dbc.Col(
                                    dbc.Checklist(options=[{"label": "RGB", "value": 1}], value=[1], id="checklist-input",
                                ), width=10, ),
                            ], row=True,),
                        ],)
                    ]),
                    common_layout.get_emptyrow(),
                    dbc.Card([
                        dbc.CardHeader("ORB Configurations"),
                        dbc.CardBody([
                            dbc.FormGroup([
                                dbc.Label("nFeatures", width=2),
                                dbc.Col(
                                    dbc.Input(type="text", id="dataset-path", placeholder="1000"
                                ), width=10, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("scaleFactor", width=2),
                                dbc.Col(
                                    dbc.Input(type="text", id="dataset-path", placeholder="1.2"
                                ), width=10, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("nLevels", width=2),
                                dbc.Col(
                                    dbc.Input(type="text", id="dataset-path", placeholder="8"
                                ), width=10, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("iniThFAST", width=2),
                                dbc.Col(
                                    dbc.Input(type="text", id="dataset-path", placeholder="20"
                                ), width=10, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("minThFAST", width=2),
                                dbc.Col(
                                    dbc.Input(type="text", id="dataset-path", placeholder="7"
                                ), width=10, ),
                            ], row=True,),
                        ],)
                    ]),
                    common_layout.get_emptyrow(),
                    dbc.Card([
                        dbc.CardHeader("Viewer Configurations"),
                        dbc.CardBody([
                            dbc.FormGroup([
                                dbc.Label("KeyFrameSize", width=2),
                                dbc.Col(
                                    dbc.Input(type="text", id="dataset-path", placeholder="0.05"
                                ), width=10, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("KeyFrameLineWidth", width=2),
                                dbc.Col(
                                    dbc.Input(type="text", id="dataset-path", placeholder="1"
                                ), width=10, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("GraphLineWidth", width=2),
                                dbc.Col(
                                    dbc.Input(type="text", id="dataset-path", placeholder="0.9"
                                ), width=10, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("PointSize", width=2),
                                dbc.Col(
                                    dbc.Input(type="text", id="dataset-path", placeholder="2"
                                ), width=10, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("CameraSize", width=2),
                                dbc.Col(
                                    dbc.Input(type="text", id="dataset-path", placeholder="0.08"
                                ), width=10, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("CameraLineWidth", width=2),
                                dbc.Col(
                                    dbc.Input(type="text", id="dataset-path", placeholder="3"
                                ), width=10, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("ViewpointX", width=2),
                                dbc.Col(
                                    dbc.Input(type="text", id="dataset-path", placeholder="0"
                                ), width=10, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("ViewpointY", width=2),
                                dbc.Col(
                                    dbc.Input(type="text", id="dataset-path", placeholder="-0.7"
                                ), width=10, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("ViewpointZ", width=2),
                                dbc.Col(
                                    dbc.Input(type="text", id="dataset-path", placeholder="-1.8"
                                ), width=10, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("ViewpointF", width=2),
                                dbc.Col(
                                    dbc.Input(type="text", id="dataset-path", placeholder="500"
                                ), width=10, ),
                            ], row=True,),
                        ],)
                    ])
                ], className= 'col-12'),

                # html.Div([], className = 'col-2'), # Blank 2 column

            ],
            className = 'row'), # Internal row

        ],
        className = 'col-10',
        style = common_layout.externalgraph_colstyling), # External 10-column

        html.Div([], className = 'col-1'), # Blank 1 column

        html.Div([html.P(id="detections")], className= 'col-6'),

    ],
    className = 'row',
    style = common_layout.externalgraph_rowstyling
    )

])