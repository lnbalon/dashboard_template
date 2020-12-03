import dash_html_components as html
import dash_core_components as dcc
from config import APP_NAME
from functions import get_category1, get_category2
import pandas as pd
from config import PATH_DATASET1

df = pd.read_csv(PATH_DATASET1)
CATEGORY1 = sorted(get_category1(df))
CATEGORY2 = sorted(get_category2(df))


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

    selector = html.Div(className='selector-container',
                        children=[

                            # category1 selector
                            html.Div(id='category1-selector',
                                     children=[

                                         html.Div('Select Category1:',
                                                  style={'font-family': 'Arial',
                                                         'font-size': '12px',
                                                         'margin-top': '12px',
                                                         'margin-left': '5px',
                                                         'white-space': 'nowrap'}),

                                         dcc.Dropdown(
                                             className='dropdown',
                                             id='categorySelector1',
                                             options=[{'label': x, 'value': x} for x in CATEGORY1],
                                             value=CATEGORY1[0],
                                             style={'margin-top': '12px',
                                                    'margin-bottom': '10px'}),

                                         html.Div(style={'width': '90%',
                                                         'margin': 'auto',
                                                         'border-bottom': '1px solid black'})
                                     ])

                        ])

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
