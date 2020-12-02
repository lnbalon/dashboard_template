import dash
import flask
import dash_html_components as html
from layout import create_header, create_selector, create_summary, create_footer

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)

header = create_header()
summary = create_summary()
selector = create_selector()
footer = create_footer()

app.layout = html.Div(className='container',
                      children=[
                          header,
                          summary,
                          selector,
                          footer
                      ]
)

if __name__ == '__main__':

    app.run_server(debug=True)
