import dash
import dash_table
from dash.exceptions import PreventUpdate
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

import numpy as np
import pandas as pd

import utils.dash_reusable_components as drc

from DataGuru import DataGuru

class DecisionTree_VP:

    @staticmethod

    def getAlgoProps(colorscales,globalData):        

        df=globalData.dataGuru.getDF()
        options=df.columns
        options=[{'label':i,'value':i} for i in options]

        x,y=df.shape

        return html.Div([
                        drc.NamedDropdown(name="Reference",
                        id="reference",                                            
                        clearable=True,
                        searchable=True,
                        options=options,
                        value=None,
                        multi=False
                        ),
                        
                        html.Div(id='features'),
                        
                        dcc.Checklist(
                        id='selectall',
                        options=[{'label': 'All features', 'value':'ALL'}],
                        value=[],
                        ),
                        
                        #max for max_depth is number of rows 
                        drc.NamedDropdown(name="max_depth",
                        id="max_depth",                                            
                        clearable=True,
                        searchable=True,
                        options=[{'label': str(i), 'value':i} for i in range(1,x)],
                        value=None,
                        multi=False
                        ),
                        
                        html.Br(),
                        html.Br(),

                        
                        html.Div(className='rowhalf2',children=[
                            
                            html.Div(className='colhalf2',children=[html.Br(),html.Br(),
                            dcc.RadioItems(id='setcreation',
                            options=[
                            {'label': 'Cross-validation     _._._._._._._._._._._ \n _._._._._._._._._._._  ', 'value':'cross'},    
                            {'label': 'Percentage Split ', 'value': 'percentage'},
                            ],
                            value='cross'
                            ),]),
                            
                            html.Div(className='colhalf2',children=[
                            html.Div(id='selection')
                            ])


                    ]),
            html.Br(),
            html.Br(),
            html.Div(id='buttonspace')
            ]            
            )
        

