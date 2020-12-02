import dash
import flask
import dash_html_components as html
from layout import create_header, create_selector

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)

header = create_header()
selector = create_selector()

app.layout = html.Div(className='container',
                      children=[
                          header,
                          selector
                      ]
)

if __name__ == '__main__':

    app.run_server(debug=True)
