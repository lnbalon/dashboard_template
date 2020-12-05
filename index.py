import dash
import flask
import dash_html_components as html
from layout import logo_container, app_name_container, summary_container1, summary_container2, \
    category1_selector_container, category2_selector_container, summary_container3, date_selector_container
from callbacks import register_callbacks

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)

logo = logo_container()
app_name = app_name_container()
selector1 = category1_selector_container()
selector2 = category2_selector_container()
selector3 = date_selector_container()
summary1 = summary_container1()
summary2 = summary_container2()
summary3 = summary_container3()

app.layout = html.Div(className='container',
                      children=[
                          logo,
                          app_name,
                          summary1,
                          summary2,
                          summary3,
                          selector1,
                          selector2,
                          selector3
                      ])

register_callbacks(app)

if __name__ == '__main__':

    app.run_server(debug=True)
