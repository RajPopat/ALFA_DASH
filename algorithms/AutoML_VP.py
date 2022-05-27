import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table
from dash.exceptions import PreventUpdate

import numpy as np
import pandas as pd

import utils.dash_reusable_components as drc
class AutoML_VP:

    @staticmethod
    def getAlgoProps(colorscales,globalData):        
        df=globalData.dataGuru.getDF()
        options=df.columns
        options=[{'label':i,'value':i} for i in options]
            
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
        

