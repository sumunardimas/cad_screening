#!/usr/bin/env python3
import dash
from dash import html
from dash import dcc
import pandas as pd

app_html_layout = html.Div([

    html.Img(src='https://carenusa.id/img/apex.png', style={'height':'75px', 'margin':'auto', 'textAlign': 'center'}),

    html.Center(html.H1("Screening for Patient at Risk for CHD")),

    html.Center(html.Div("Insert patient details in the following fields. Once you have succesfully fill in the fields, click the button to display the prediction results")),
    html.Table([ html.Tbody([

         html.Tr([
            html.Td( html.B('Personnummer:'), style={'width':'25%'} ),
            html.Td( dcc.Input(id='personnummer', type='number'), style={'width':'55%'} ),
                
            ]),
         html.Tr([
            html.Td( html.B('Age:'), style={'width':'25%'} ),
            html.Td( dcc.Input(id='age', type='number'
                ), style={'width':'55%'} ),
            ]),
        html.Tr([
            html.Td( html.B('Gender:'), style={'width':'25%'} ),
            html.Td(dcc.Dropdown(id='sex',
        options=[
            {'label': 'Select one option', 'value': ''},
            {'label': 'Male', 'value': '1'},
            {'label': 'Female', 'value': '0'},
        ],
        value=''
        )),
            ]),
        
        html.Tr([
            html.Td( html.B('Resting Blood Pressure:'), style={'width':'25%'} ),
            html.Td( dcc.Input(id='trestbps', type='number'
                ), style={'width':'55%'} ),
            ]),
        html.Tr([
            html.Td( html.B('Cholestrol Serum:'), style={'width':'25%'} ),
            html.Td( dcc.Input(id='chol', type='number'
                ), style={'width':'55%'} ),
            ]),
        html.Tr([
            html.Td( html.B('Fasting Blood Sugar:'), style={'width':'25%'} ),
            html.Td(dcc.Dropdown(id='fbs',
        options=[
            {'label': 'Select one option', 'value': ''},
            {'label': 'More than 120 mg/dl', 'value': '1'},
            {'label': 'Less than than 120 mg/dl', 'value': '0'},
        ],
        value=''
        )),
            ]),
                html.Tr([
            html.Td( html.B('Resting ECG Results:'), style={'width':'25%'} ),
            html.Td(dcc.Dropdown(id='restecg',
        options=[
            {'label': 'Select one option', 'value': ''},
            {'label': 'Normal', 'value': '0'},
            {'label': 'Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)', 'value': '1'},
            {'label': 'Showing probable or definite left ventricular hypertrophy by Estes criteria', 'value': '2'},
        ],
        value=''
        )),
            ]),
        html.Tr([
            html.Td( html.B('Maximum Heart Rate Achieved:'), style={'width':'25%'} ),
            html.Td( dcc.Input(id='thalach', type='number'
                ), style={'width':'55%'} ),
            html.Td( html.P(id='value-hr',children=''), style={'width':'10%'} ),
            ]),
        html.Tr([
            html.Td( html.B('Does angina induced during exercise?:'), style={'width':'25%'} ),
            html.Td(dcc.Dropdown(id='exang',
        options=[
            {'label': 'Select one option', 'value': ''},
            {'label': 'Yes', 'value': '1'},
            {'label': 'No', 'value': '0'},
        ],
        value=''
        )),
            ]),       
        html.Tr([
            html.Td( html.B('Chest pain type?:'), style={'width':'25%'} ),
            html.Td(dcc.Dropdown(id='cp',
        options=[
            {'label': 'Select one option', 'value': ''},
            {'label': 'No chest pain', 'value': '0'},
            {'label': 'Typical angina', 'value': '1'},
            {'label': 'Atypical angina', 'value': '2'},
            {'label': 'Non-anginal pain', 'value': '3'},
            {'label': 'Asymptomatic', 'value': '4'},
        ],
        value=''
        )),
            ]),
        
        ]),
        html.Tr([
            html.Td( html.B('Slope:'), style={'width':'25%'} ),
            html.Td(dcc.Dropdown(id='slope',
        options=[
            {'label': 'Select one option', 'value': ''},
            {'label': 'Upsloping', 'value': '1'},
            {'label': 'Flat', 'value': '2'},
            {'label': 'Downsloping', 'value': '3'},
        ],
        value=''
        )),
            ]),

        html.Tr([
        html.Td( html.B('CA:'), style={'width':'25%'} ),
        html.Td( dcc.Input(id='ca', type='number'
            ), style={'width':'55%'} ),
        ]),

        html.Tr([
        html.Td( html.B('Oldpeak:'), style={'width':'25%'} ),
        html.Td( dcc.Input(id='oldpeak', type='number'
            ), style={'width':'55%'} ),
        ]),

    ], style={'width':'80%', 'padding':'20px', 'margin':'auto', 'margin-top':'40px'}),
    
    html.Center( 
        html.Div([
            html.Br(),
            html.Button('Start', id='submit', style={'margin':'0 auto', 'width':'20%', 'background-color':'Green', 'color':'white', 'class':'btn-secondary'}),
            html.H4(html.B('Patient Prediction', id='classification-result', style={'color':'#800000'})),
        ])
    ),

], style={'columnCount': 1})