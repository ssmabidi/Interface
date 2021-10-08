import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import layouts_common as common_layout

import globals

import dash_uploader as du


####################################################################################################
# 003 - Algorithms
####################################################################################################

algorithmsPage = html.Div([

    #####################
    #Row 1 : Header
    common_layout.get_header(),

    #####################
    #Row 2 : Nav bar
    common_layout.get_navbar('algorithms'),

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
                        html.H5(children='Select an Algorithm:', style = {'text-align' : 'left', 'color' : common_layout.corporate_colors['medium-blue-grey']}),
                        #DataSet selection
                        html.Div([
                            dcc.Dropdown(id = 'dataset-config-dropdown',
                                options = globals.availableAlgorithms,
                                value = None,
                                placeholder = "Select an Algorithm",
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
                                dbc.Label("Upload Config File", width=2),
                                dbc.Col([
                                    du.Upload(id='upload-config-file',
                                        text='Drag and Drop Here to upload! or click to Select File!',
                                        max_file_size=1800,  # 1800 Mb
                                        # filetypes=['csv', 'zip'],
                                        upload_id=globals.session_Id,  # Unique session id
                                    ),
                                    html.Div(id="callback-config-output", className= 'col-6'),
                                    ],
                                width=10, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("Upload Data File", width=2),
                                dbc.Col([
                                    du.Upload(id='upload-data-file',
                                        text='Drag and Drop Here to upload! or click to Select File!',
                                        max_file_size=1800,  # 1800 Mb
                                        # filetypes=['csv', 'zip'],
                                        upload_id=globals.session_Id,  # Unique session id
                                    ),
                                    html.Div(id="callback-data-output", className= 'col-6'),
                                    ],
                                width=10, ),
                            ], row=True,),
                            dbc.FormGroup([
                                dbc.Label("Upload Weights File", width=2),
                                dbc.Col([
                                    du.Upload(id='upload-weights-file',
                                        text='Drag and Drop Here to upload! or click to Select File!',
                                        max_file_size=1800,  # 1800 Mb
                                        upload_id=globals.session_Id,  # Unique session id
                                    ),
                                    html.Div(id="callback-weights-output", className= 'col-6'),
                                    ],# style={
                                        #     'width': '100%',
                                        #     'height': '60px',
                                        #     'lineHeight': '60px',
                                        #     'borderWidth': '1px',
                                        #     'borderStyle': 'dashed',
                                        #     'borderRadius': '5px',
                                        #     'textAlign': 'center',
                                        #     'margin': '10px'
                                        #      },
                                    # dcc.Upload( [html.Div(['Drag and Drop or ', html.A('Select File')])], ),
                                    # html.Div(id='output-data-upload'),
                                    # dbc.Input(type="text", id="dataset-path", placeholder="Enter path to read dataset" ),
                                width=10, ),
                            ], row=True,),

                            dbc.FormGroup([
                                dbc.Label("Set Threshold", width=2),
                                dbc.Col(
                                    dcc.Slider(id='dataset-training-percent', tooltip = { 'always_visible': True, 'placement': 'bottom' }, min=0, max=1, step=0.05, value=0.5, marks={0.0: '0.0', 0.1: '0.1', 0.2: '0.2', 0.3: '0.3', 0.4: '0.4', 0.5: '0.5', 0.6: '0.6', 0.7: '0.7', 0.8: '0.8', 0.9: '0.9', 1.0: '1.0'},
                                ), width=10, ),
                            ], row=True,),
                            

                            html.H2("File List"),
                            html.Ul(id="file-list"),
                        ],)
                    ]),
                    common_layout.get_emptyrow(),
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
    ),

    #####################
    #Row 7
    common_layout.get_emptyrow(),

])