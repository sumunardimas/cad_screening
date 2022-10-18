import dash
import flask
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css']
app = dash.Dash("apex", external_stylesheets=external_stylesheets)
server = flask.Flask(app)
