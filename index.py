import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from callbacks import register_callbacks
from app import app
from layout import *

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return page1_layout
    elif pathname == '/page-2':
        return page2_layout
    else:
        return '404'


register_callbacks(app)


if __name__ == '__main__':
    app.run_server(debug=True)