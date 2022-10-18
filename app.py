#!/usr/bin/env python3
import layout
import dash
from dash.dependencies import Input, Output, State
from pathlib import Path
import numpy as np
import pandas as pd
import pickle

THIS_FILE_PATH = str(Path(__file__).parent.absolute())+"/"
filename_to_load = THIS_FILE_PATH + "rfmodel.pickle"

dataset_colnames =     ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca']
sample = None 



loaded_model = None
with open(filename_to_load, "rb") as readFile:
    loaded_model = pickle.load(readFile)

external_stylesheets = ['https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css']

app = dash.Dash("apex", external_stylesheets=external_stylesheets)
server = app.server

app.layout = layout.app_html_layout

@app.callback(     
    Output(component_id='classification-result', component_property='children'),
    [Input(component_id='submit', component_property='n_clicks')],
    [State('age', 'value'),
    State('sex', 'value'),
    State('cp', 'value'),
    State('trestbps', 'value'),
    State('chol', 'value'),
    State('fbs', 'value'),
    State('restecg', 'value'),
    State('thalach', 'value'),
    State('exang', 'value'),
    State('oldpeak', 'value'),
    State('slope', 'value'),
    State('ca', 'value'),
    ]
)

def execute_classification(n_clicks, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca):

    if(n_clicks == None):
        return "-"
    else:
        data_from_user = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca]
        global sample
        sample = pd.DataFrame(data=[data_from_user], columns=dataset_colnames)

        prediction = loaded_model.predict(sample)

        prediction_labels = ["Not at risk for CAD", "At risk for CAD"]
        return "The predicted state for the patient is "+ str(prediction[0]) +"-" + prediction_labels[prediction[0]]


if __name__ == "__main__":
    app.run_server(debug=True)