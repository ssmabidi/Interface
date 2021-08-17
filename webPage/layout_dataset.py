import dash_html_components as html

import layouts_common as common_layout

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
    #Row 3 : Filters
    html.Div([ # External row
        html.H1(children='Dataset Page'),
        html.Br()

    ],
    className = 'row sticky-top'), # External row

    #####################
    #Row 4
    common_layout.get_emptyrow(),

    #####################
    #Row 5 : Charts
    html.Div([ # External row

        html.Br()

    ])

])