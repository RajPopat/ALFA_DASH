import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table
from dash.exceptions import PreventUpdate

import numpy as np
import pandas as pd

import utils.dash_reusable_components as drc

class Scatter3D_VP:
	
    @staticmethod
    def getAlgoProps(options,colorscales):
        valueX = None
        valueY = None
        valueZ = None
        hoverVal = None
        sizeVal = None
        colorVal = None
        return html.Div([
            drc.NamedDropdown(name="Feature on the x axis",
                                        id="featureX",                                            
                                        clearable=True,
                                        searchable=True,
                                        options=options,
                                        value=valueX,
                                        multi=False
                                    ),
            drc.NamedDropdown(name="Feature on the y axis",
                                        id="featureY",                                            
                                        clearable=True,
                                        searchable=True,
                                        options=options,
                                        value=valueY,
                                        multi=False
                                    ),
            drc.NamedDropdown(name="Feature on the z axis",
                                        id="featureZ",                                            
                                        clearable=True,
                                        searchable=True,
                                        options=options,
                                        value=valueZ,
                                        multi=False
                                    ),
            
            drc.NamedDropdown(name="Hover feature",
                                        id="featureHover",                                            
                                        clearable=True,
                                        searchable=True,
                                        options=options,
                                        value=hoverVal,
                                        multi=True
                                    ),
            drc.NamedDropdown(name="Size feature",
                                        id="featureSize",                                            
                                        clearable=True,
                                        searchable=True,
                                        options=options,
                                        value=sizeVal,
                                        multi=False
                                    ),

            drc.NamedDropdown(name="Reference feature for color mapping",
                                        id="featureColor",                                            
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

            html.Button('Generate a 3D scatter plot', id='generate-scatter-plot3',n_clicks=0)
            ]            
            )