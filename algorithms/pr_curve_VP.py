import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table
from dash.exceptions import PreventUpdate

import numpy as np
import pandas as pd

import utils.dash_reusable_components as drc

class PR_Curve_VP:

    @staticmethod
    def getAlgoProps(options,colorscales):        
        valueX = None
        valueY = None
        hoverVal = None
        colorVal = None
        sizeVal = None
        return html.Div([
            drc.NamedDropdown(name="Features",
                                        id="featureX",                                            
                                        clearable=True,
                                        searchable=True,
                                        options=options,
                                        value=valueX,
                                        multi=True
                                    ),
            

            drc.NamedDropdown(name="Reference",
                                        id="featureColor",                                            
                                        clearable=True,
                                        searchable=True,
                                        options=options,
                                        value=colorVal,
                                        multi=False
                                    ),

            drc.NamedDropdown(name="Reference Class",
                                        id="subClass",                                            
                                        clearable=True,
                                        searchable=True,
                                        options=options,
                                        value=colorVal,
                                        multi=False
                                    ),

            drc.NamedDropdown(name="Color Scale",
                                        id="colorscale",                                            
                                        clearable=True,
                                        searchable=True,
                                        options=[{"value": x, "label": x} 
                                                 for x in colorscales],
                                        value='viridis'
                                    ),

            html.Button('Precision-Recall Analysis', id='generate-pr-curve',n_clicks=0)
            ]            
            )
        

