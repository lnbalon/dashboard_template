import dash
import flask
from layout import *

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

page1_layout = html.Div(className='container1',
                        children=[
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
                          footer,
                      ])
