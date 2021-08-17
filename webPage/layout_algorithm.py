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
    #Row 3 : Filters
    html.Div([ # External row
        html.H1(children='Algorithm Page'),
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