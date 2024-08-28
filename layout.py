#!/usr/bin/env python3
import dash
from dash import html
from dash import dcc
import pandas as pd

app_html_layout = html.Div([
    
    html.Center(html.Img(src='', style={'height':'75px','margin-right':'50%', 'margin-left':'40%', 'textAlign': 'center'})),

    html.Center(html.H1("Skrining Risiko Penyakit Jantung Koroner")),

    html.Center(html.Div("Masukkan data pasien berdasarkan kolom yang tersedia!")),
    html.Table([ html.Tbody([

         html.Tr([
            html.Td( html.B('NIK:'), style={'width':'25%'} ),
            html.Td( dcc.Input(id='personnummer', type='number'), style={'width':'55%'} ),
                
            ]),
         html.Tr([
            html.Td( html.B('Usia:'), style={'width':'25%'} ),
            html.Td( dcc.Input(id='age', type='number'
                ), style={'width':'55%'} ),
            ]),
        html.Tr([
            html.Td( html.B('Jenis Kelamin:'), style={'width':'25%'} ),
            html.Td(dcc.Dropdown(id='sex',
        options=[
            {'label': 'Pilih salah satu', 'value': ''},
            {'label': 'Laki-laki', 'value': '1'},
            {'label': 'Perempuan', 'value': '0'},
        ],
        value=''
        )),
            ]),
        
        html.Tr([
            html.Td( html.B('Tekanan darah istirahat:'), style={'width':'25%'} ),
            html.Td( dcc.Input(id='trestbps', type='number'
                ), style={'width':'55%'} ),
            ]),
        html.Tr([
            html.Td( html.B('Serum Kolesterol:'), style={'width':'25%'} ),
            html.Td( dcc.Input(id='chol', type='number'
                ), style={'width':'55%'} ),
            ]),
        html.Tr([
            html.Td( html.B('Gula Darah Puasa:'), style={'width':'25%'} ),
            html.Td(dcc.Dropdown(id='fbs',
        options=[
            {'label': 'Pilih salah satu', 'value': ''},
            {'label': 'Lebih dari 120 mg/dl', 'value': '1'},
            {'label': 'Kurang dari 120 mg/dl', 'value': '0'},
        ],
        value=''
        )),
            ]),
                html.Tr([
            html.Td( html.B('Elektrokardiogram saat Istirahat:'), style={'width':'25%'} ),
            html.Td(dcc.Dropdown(id='restecg',
        options=[
            {'label': 'Pilih salah satu', 'value': ''},
            {'label': 'Normal', 'value': '0'},
            {'label': 'Memiliki kelainan gelombang ST-T (inversi gelombang T dan/atau elevasi atau depresi gelombang ST) > 0.05 mV)', 'value': '1'},
            {'label': 'Menunjukkan hipertrofi ventrikel kiri yang mungkin atau pasti berdasarkan kriteria Estes', 'value': '2'},
        ],
        value=''
        )),
            ]),
        html.Tr([
            html.Td( html.B('Denyut Jantung Maksimal:'), style={'width':'25%'} ),
            html.Td( dcc.Input(id='thalach', type='number'
                ), style={'width':'55%'} ),
            html.Td( html.P(id='value-hr',children=''), style={'width':'10%'} ),
            ]),
        html.Tr([
            html.Td( html.B('Apakah angina dipicu ketika beraktivitas?:'), style={'width':'25%'} ),
            html.Td(dcc.Dropdown(id='exang',
        options=[
            {'label': 'Pilih salah satu', 'value': ''},
            {'label': 'Ya', 'value': '1'},
            {'label': 'Tidak', 'value': '0'},
        ],
        value=''
        )),
            ]),       
        html.Tr([
            html.Td( html.B('Jenis nyeri dada:'), style={'width':'25%'} ),
            html.Td(dcc.Dropdown(id='cp',
        options=[
            {'label': 'Pilih salah satu', 'value': ''},
            {'label': 'Tidak nyeri dada', 'value': '0'},
            {'label': 'Angina tipikal', 'value': '1'},
            {'label': 'Angina atipikal', 'value': '2'},
            {'label': 'Nyeri bukan angina', 'value': '3'},
            {'label': 'Asimtomatis', 'value': '4'},
        ],
        value=''
        )),
            ]),
        
        ]),
        html.Tr([
            html.Td( html.B('Kemiringan Segmen-ST saat beraktivitas:'), style={'width':'25%'} ),
            html.Td(dcc.Dropdown(id='slope',
        options=[
            {'label': 'Pilih salah satu', 'value': ''},
            {'label': 'Meningkat', 'value': '1'},
            {'label': 'Datar', 'value': '2'},
            {'label': 'Menurun', 'value': '3'},
        ],
        value=''
        )),
            ]),

        html.Tr([
        html.Td( html.B('Jumlah pembuluh darah utama dengan fluoroskopi (0-3):'), style={'width':'25%'} ),
        html.Td( dcc.Input(id='ca', type='number'
            ), style={'width':'55%'} ),
        ]),

        html.Tr([
        html.Td( html.B('ST (Nilai numerik diukur dalam depresi)'), style={'width':'25%'} ),
        html.Td( dcc.Input(id='oldpeak', type='number'
            ), style={'width':'55%'} ),
        ]),

    ], style={'width':'80%', 'padding':'20px', 'margin':'auto', 'margin-top':'40px'}),
    
    html.Center( 
        html.Div([
            html.Br(),
            html.Button('Lakukan Skrining', id='submit', style={'margin':'0 auto', 'width':'20%', 'background-color':'Green', 'color':'white', 'class':'btn-secondary'}),
            html.H4(html.B('Patient Prediction', id='classification-result', style={'color':'#800000'})),
        ])
    ),

], style={'columnCount': 1})