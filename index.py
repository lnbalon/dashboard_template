import dash
import flask
import dash_html_components as html
from layout import create_header

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)

header = create_header()

app.layout = html.Div(className='container',
                      children=[
                          header
                      ]
)

if __name__ == '__main__':

    app.run_server(debug=True)
