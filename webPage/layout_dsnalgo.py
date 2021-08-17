import dash_core_components as dcc
import dash_html_components as html
from dash_html_components.Div import Div

import plotly.express as px
import plotly.graph_objects as go

import layouts_common as common_layout





####################################################################################################
# TODO: - Testing!! This part of code should be refactored out of this file and placed somewhere
# ------- else
####################################################################################################


# TODO: Is this the best way to import interfaces?
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from zurichDataset import ZurichDataset

import base64
from io import BytesIO
def pil_to_b64(im, enc_format="png", **kwargs):
    """
    Converts a PIL Image into base64 string for HTML displaying
    :param im: PIL Image object
    :param enc_format: The image format for displaying. If saved the image will have that extension.
    :return: base64 encoding
    """

    buff = BytesIO()
    im.save(buff, format=enc_format, **kwargs)
    encoded = base64.b64encode(buff.getvalue()).decode("utf-8")

    return encoded

datasetInstance = ZurichDataset({"dataPath" : '/home/shahamat/Datasets/AGZ'}) #TODO: Read dataset path from user



img_rgb = [[[255, 0, 0], [0, 255, 0], [0, 0, 255]],
           [[0, 255, 0], [0, 0, 255], [255, 0, 0]]]


####################################################################################################
# TODO: - End here!!
####################################################################################################



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
    #Row 3 : Selections
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
                                options = common_layout.availableDatasets,
                                value = [''],
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
                                options = common_layout.availableAlgorithms,
                                value = [''],
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
    #Row 4
    common_layout.get_emptyrow(),

    #####################
    # #Row 5 : Charts
    html.Div([ # External row

        html.Div([], className = 'col-1'), # Blank 1 column

        html.Div([ # External 10-column

            html.H2(children = "Testbench Visualization", style = {'color' : common_layout.corporate_colors['white']}),

    
            html.Div([ # Internal row

                # Chart Column
                html.Div([
                    dcc.Graph(
                        id="dataset-image",
                        figure = go.Figure(px.imshow(datasetInstance.getNextImage()))),
                ], className= 'col-5'),
                
                html.Div([], className = 'col-2'), # Blank 2 column

                # Chart Column
                html.Div([
                    dcc.Graph(
                        id="algorithm-image",
                        figure = go.Figure(go.Image(z=img_rgb))),
                ], className= 'col-5'),

            ],
            className = 'row'), # Internal row

        ],
        className = 'col-10',
        style = common_layout.externalgraph_colstyling), # External 10-column

        html.Div([], className = 'col-1'), # Blank 1 column

    ],
    className = 'row',
    style = common_layout.externalgraph_rowstyling
    ), # External row

])
