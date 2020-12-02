import dash_html_components as html
import dash_core_components as dcc
from config import APP_NAME


def create_header():

    header = html.Div(className='banner-container',
                      children=[
                          html.Img(
                              className='banner-image',
                              src='assets/logo.png'
                          ),

                          html.Div(
                              className='banner-title',
                              children=[html.H1(children=[APP_NAME])]
                          )
                      ]
                      )

    return header


def create_selector():

    selector = html.Div(className='selector-container')

    return selector


def create_summary():

    summary = html.Div(className='summary-container')

    return summary


def create_chart1():

    chart1 = html.Div(className='chart-area1')

    return chart1


def create_chart2():

    chart2 = html.Div(className='chart-area2')

    return chart2


def create_chart3():

    chart3 = html.Div(className='chart-area3')

    return chart3


def create_footer():

    footer = html.Div(className='footer')

    return footer
