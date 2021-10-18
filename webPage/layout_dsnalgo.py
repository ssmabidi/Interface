from dash_bootstrap_components._components.Button import Button
import dash_core_components as dcc
import dash_html_components as html

import layouts_common as common_layout
import globals

import dash_bootstrap_components as dbc

def get_buttons():
    return html.Div([ #Internal row
        html.Div([
            dbc.Button('Next Image', color='light', className='mr-1', id='next_image', n_clicks=0),
            dbc.Button("Previous Image", color="light", className="mr-1", id='prev_image', n_clicks=0),
            dbc.Button("First Image", color='light', className='mr-1', id='first_image', n_clicks=0),
            dbc.Button("Last Image", color="light", className="mr-1", id='last_image', n_clicks=0),
            dbc.Button("Random Image", color="light", className="mr-1", id='rand_image', n_clicks=0),
            dbc.Button("Ground Truth", color="light", className="mr-1", id='ground_truth', n_clicks=0),
        ], className='col-9'),
        html.Div([
            dbc.Button('Apply Algo', color='light', className='mr-1', id='apply_algo', n_clicks=0),
            dbc.Button('Batch Apply Algo', color='light', className='mr-1', id='batch_apply_algo', n_clicks=0),
        ], className='col-3'),
    ], className = 'row')



####################################################################################################
# 001 - dataSets and Algorithms
####################################################################################################

dsAndAlgosPage = html.Div([

    #####################
    #Row 1 : Header
    common_layout.get_header(),

    #####################
    #Row 2 : Nav bar
    common_layout.get_navbar('dsAndAlgos'),

    #####################
    #Row 3
    common_layout.get_emptyrow(),

    #####################
    #Row 4 : Selections
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
                            dcc.Dropdown(id = 'dataset-dropdown',
                                options = globals.availableDatasets,
                                value = None,
                                placeholder = "Select a Dataset",
                                style = {'font-size': '13px', 'color' : common_layout.corporate_colors['medium-blue-grey'], 'white-space': 'nowrap', 'text-overflow': 'ellipsis'}
                            )
                        ], style = {'width' : '70%', 'margin-top' : '5px'})
                    ], style = {'margin-top' : '10px', 'margin-bottom' : '5px', 'text-align' : 'left', 'paddingLeft': 5})
                ], className = 'col-4' ), # Filter part 1

                #Filter pt 2
                html.Div([
                    html.Div([
                        html.H5(children='Select an Algorithm:', style = {'text-align' : 'left', 'color' : common_layout.corporate_colors['medium-blue-grey']}),
                        #Algorithm selection
                        html.Div([
                            dcc.Dropdown(id = 'algorithm-dropdown',
                                options = globals.availableAlgorithms,
                                value = None,
                                placeholder = "Select an Algorithm",
                                style = {'font-size': '13px', 'color' : common_layout.corporate_colors['medium-blue-grey'], 'white-space': 'nowrap', 'text-overflow': 'ellipsis'}
                            )
                        ], style = {'width' : '70%', 'margin-top' : '5px'})
                    ], style = {'margin-top' : '10px', 'margin-bottom' : '5px', 'text-align' : 'left', 'paddingLeft': 5})
                ], className = 'col-4'), # Filter part 2

                html.Div([], className = 'col-2') # Blank 2 columns

            ], className = 'row') # Internal row

        ],
        className = 'col-12',
        style = common_layout.filterdiv_borderstyling) # External 12-column

    ], className = 'row sticky-top'), # External row

    #####################
    #Row 5
    common_layout.get_emptyrow(),

    #####################
    # #Row 6 : Images and Buttons
    html.Div([ # External row

        html.Div([], className = 'col-1'), # Blank 1 column

        html.Div([ # External 10-column
            html.H2(children = "Testbench Visualization", style = {'color' : common_layout.corporate_colors['white']}),
    
            html.Div([ # Internal row
                # Dataset Image Column
                html.Div([
                    dcc.Graph(
                        id="dataset-image",
                        # figure = go.Figure(px.imshow(datasetInstance.getNextImage()))
                )], className= 'col-6'),

                # html.Div([], className = 'col-2'), # Blank 2 column

                # Algorithm Image Column
                html.Div([
                    dcc.Graph(
                        id="algorithm-image",
                        # figure = go.Figure(px.imshow(datasetInstance.getCurrImage()))
                )], className= 'col-6'),

            ],
            className = 'row'), # Internal row

            common_layout.get_emptyrow(),
            get_buttons(),
            common_layout.get_emptyrow(),


        ],
        className = 'col-10',
        style = common_layout.externalgraph_colstyling), # External 10-column

        html.Div([], className = 'col-1'), # Blank 1 column

        html.Div(id="detections0", className= 'col-6', style = {'backgroundColor' : 'white'}),
        html.Div([html.Div(id="detections")], className= 'col-6', style = {'backgroundColor' : 'white'}),

        html.Div(id="batchDetections", className= 'col-6', style = {'backgroundColor' : 'white'}),
        
    ],
    className = 'row',
    style = common_layout.externalgraph_rowstyling
    ), # External row
    
    #####################
    #Row 7
    common_layout.get_emptyrow(),

])