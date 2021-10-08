import os
import dash_core_components as dcc
import dash_html_components as html
import dash

from app import app
from app import server

from layout_dsnalgo import dsAndAlgosPage
from layout_dataset import datasetsPage
from layout_algorithm import algorithmsPage

import callbacks
import globals


import dash_uploader as du


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(
     dash.dependencies.Output('page-content', 'children'),
     [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
     if pathname == '/apps/dsAndAlgos':
          return dsAndAlgosPage
     elif pathname == '/apps/datasets':
          return datasetsPage
     elif pathname == '/apps/algorithms':
          return algorithmsPage
     else:
          return dsAndAlgosPage # This is the "default page"

if __name__ == '__main__':

     globals.yoloInstance.load_network()


     # Dash uploader creates folder if it does not exist
     du.configure_upload(app, globals.upload_dir)

     app.run_server(debug=False, dev_tools_hot_reload=False)
