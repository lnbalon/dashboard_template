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