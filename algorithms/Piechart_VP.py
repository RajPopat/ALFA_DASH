import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table
from dash.exceptions import PreventUpdate

import numpy as np
import pandas as pd

import utils.dash_reusable_components as drc
class Piechart_VP:

    @staticmethod
    def getAlgoProps(options,colorscales):        
        
        return html.Div([
            drc.NamedDropdown(name="Select Feature/Values/(continous data)",
                                        id="feature",                                            
                                        clearable=True,
                                        searchable=True,
                                        options=options,
                                        value=None,
                                        multi=False
                                    ),
            drc.NamedDropdown(name="Select Reference/Names/(Nominal data)",
                                        id="reference",                                            
                                        clearable=True,
                                        searchable=True,
                                        options=options,
                                        value=None,
                                        multi=False
                                    ),
            html.Button('Generate a pie chart', id='generate-piechart-plot',n_clicks=0)
            ]            
            )
