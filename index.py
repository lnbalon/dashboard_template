import dash
import flask
import dash_html_components as html
from layout import logo_container, app_name_container, summary_container1, summary_container2

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)

logo = logo_container()
app_name = app_name_container()
summary1 = summary_container1()
summary2 = summary_container2()

app.layout = html.Div(className='container',
                      children=[
                          logo,
                          app_name,
                          summary1,
                          summary2
                      ])

if __name__ == '__main__':

    app.run_server(debug=True)
