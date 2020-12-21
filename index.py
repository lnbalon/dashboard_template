import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from callbacks import register_callbacks
from app import app

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)