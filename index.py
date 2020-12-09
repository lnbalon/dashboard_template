import dash
import flask
import dash_html_components as html
from layout import *
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
summary4 = summary_container4()
summary5 = summary_container5()
summary6 = summary_container6()
summary7 = summary_container7()
plot1 = plot_container1()
plot2 = plot_container2()
plot3 = plot_container3()
footer = get_footer()

app.layout = html.Div(className='container',
                      children=[
                          logo,
                          app_name,
                          summary1,
                          summary2,
                          summary3,
                          summary4,
                          summary5,
                          summary6,
                          summary7,
                          selector1,
                          selector2,
                          selector3,
                          plot1,
                          plot2,
                          plot3,
                          footer
                      ])

register_callbacks(app)

if __name__ == '__main__':

    app.run_server(debug=True)
