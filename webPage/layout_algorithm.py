import dash_html_components as html

import layouts_common as common_layout

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
        html.Div([], className = 'col-1'), # Blank 1 column

        html.Div([ # External 10-column
            html.H2(children = "Algorithm Configurations", style = {'color' : common_layout.corporate_colors['white']}),
    
            html.Div([ # Internal row
                # Dataset Image Column
                html.Div([
                #     dcc.Graph(
                #         id="dataset-image",
                #         # figure = go.Figure(px.imshow(datasetInstance.getNextImage()))
                # )
                ], className= 'col-6'),

                # html.Div([], className = 'col-2'), # Blank 2 column

                # Algorithm Image Column
                html.Div([
                #     dcc.Graph(
                #         id="algorithm-image",
                #         # figure = go.Figure(px.imshow(datasetInstance.getCurrImage()))
                # )
                ], className= 'col-6'),

            ],
            className = 'row'), # Internal row

        ],
        className = 'col-10',
        style = common_layout.externalgraph_colstyling), # External 10-column

        html.Div([], className = 'col-1'), # Blank 1 column

        html.Div([html.P(id="detections")], className= 'col-6'),

    ],
    className = 'row sticky-top'), # External row

    #####################
    #Row 5
    common_layout.get_emptyrow(),

    #####################
    #Row 6 : Charts
    html.Div([ # External row

        html.Br()

    ])

])