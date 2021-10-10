import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import dash
import dash_table
from dash_table.Format import Format, Group
import dash_table.FormatTemplate as FormatTemplate
from datetime import datetime as dt
from app import app

####################################################################################################
# 000 - FORMATTING INFO
####################################################################################################

####################### Corporate css formatting
corporate_colors = {
    'dark-blue-grey' : 'rgb(62, 64, 76)',
    'medium-blue-grey' : 'rgb(77, 79, 91)',
    'superdark-green' : 'rgb(41, 56, 55)',
    'dark-green' : 'rgb(57, 81, 85)',
    'medium-green' : 'rgb(93, 113, 120)',
    'light-green' : 'rgb(186, 218, 212)',
    'pink-red' : 'rgb(255, 101, 131)',
    'dark-pink-red' : 'rgb(247, 80, 99)',
    'white' : 'rgb(251, 251, 252)',
    'light-grey' : 'rgb(208, 206, 206)'
}

externalgraph_rowstyling = {
    'margin-left' : '15px',
    'margin-right' : '15px'
}

externalgraph_colstyling = {
    'border-radius' : '10px',
    'border-style' : 'solid',
    'border-width' : '1px',
    'border-color' : corporate_colors['superdark-green'],
    'background-color' : corporate_colors['superdark-green'],
    'box-shadow' : '0px 0px 17px 0px rgba(186, 218, 212, .5)',
    'padding-top' : '10px'
}

filterdiv_borderstyling = {
    'border-radius' : '0px 0px 10px 10px',
    'border-style' : 'solid',
    'border-width' : '1px',
    'border-color' : corporate_colors['light-green'],
    'background-color' : corporate_colors['light-green'],
    'box-shadow' : '2px 5px 5px 1px rgba(255, 101, 131, .5)'
    }

navbarcurrentpage = {
    'text-decoration' : 'underline',
    'text-decoration-color' : corporate_colors['pink-red'],
    'text-shadow': '0px 0px 1px rgb(251, 251, 252)'
    }
################################################################################################################################################## SET UP END

####################################################################################################
# 000 - DEFINE REUSABLE COMPONENTS AS FUNCTIONS
####################################################################################################

#####################
# Header with logo
def get_header():

    header = html.Div(
        [
            html.Div([], className = 'col-2'), #Same as img width, allowing to have the title centrally aligned
            html.Div(
                [html.H1(children='Testbench for UAVs', style = {'textAlign' : 'center'})],
                className='col-8',
                style = {'paddingTop' : '1%'}
            ),
        ],
        className = 'row',
        style = {'height' : '4%', 'background-color' : corporate_colors['superdark-green']}
    )

    return header

#####################
# Nav bar
def get_navbar(p = 'dsAndAlgos'):

    selectedDsAndAlgos = None
    selectedDatasets = None
    selectedAlgorithms = None

    if p == 'dsAndAlgos':
        selectedDsAndAlgos =  navbarcurrentpage
    elif p == 'datasets':
        selectedDatasets = navbarcurrentpage
    else:
        selectedAlgorithms = navbarcurrentpage

    navbar = html.Div(
        [
            html.Div([], className = 'col-3'),
            html.Div(
                [dcc.Link(html.H4(children = 'DataSets and Algorithms', style = selectedDsAndAlgos), href='/apps/dsAndAlgos')],
                className='col-2'
            ),
            html.Div(
                [dcc.Link(html.H4(children = 'Datasets', style = selectedDatasets), href='/apps/datasets')],
                className='col-2'
            ),
            html.Div(
                [dcc.Link(html.H4(children = 'Algorithms', style = selectedAlgorithms), href='/apps/algorithms')],
                className='col-2'
            ),
            html.Div([], className = 'col-3')
        ],
        className = 'row',
        style = {'background-color' : corporate_colors['dark-green'],'box-shadow': '2px 5px 5px 1px rgba(255, 101, 131, .5)'}
    )
   
    return navbar

#####################
# Empty row

def get_emptyrow(h='45px'):
    """This returns an empty row of a defined height"""

    emptyrow = html.Div([html.Div([html.Br()], className = 'col-12')], className = 'row', style = {'height' : h})

    return emptyrow
