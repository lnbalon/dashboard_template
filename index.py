import dash
import flask
import dash_html_components as html
from layout import *
from callbacks import register_callbacks

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server, suppress_callback_exceptions=True)


logo = logo_container()
app_name = app_name_container()
link1 = link1_container()


app.layout = html.Div(className='container',
                      children=[
                          logo_container(),
                          app_name_container(),
                          link1_container(),
                          dcc.Location(id='url', refresh=False),
                          html.Div(id='page-content')
                      ])

register_callbacks(app)

if __name__ == '__main__':

    app.run_server(debug=True)
