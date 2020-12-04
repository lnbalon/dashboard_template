import dash_html_components as html
import dash_core_components as dcc
from functions import get_category1, get_category2, get_category3
import pandas as pd
from config import PATH_DATASET1

df = pd.read_csv(PATH_DATASET1)
CATEGORY1 = sorted(get_category1(df))
CATEGORY2 = sorted(get_category2(df))
CATEGORY3 = sorted(get_category3(df))


def logo_container():

    logo = html.Div(className='logo-container',
                    children=[
                        html.Img(className='logo-image',
                                 src='assets/logo.jpeg')
                    ])

    return logo


def app_name_container():

    app_name = html.Div(className='title-container',
                        children=['Sample Dashboard Template'])

    return app_name


def category1_selector_container():

    element = html.Div(className='category1-selector',
                       children=[
                           html.Div('Select Category',
                                    style={'font': 'Helvetica',
                                           'font-size': '12px',
                                           'margin-bottom': '5px'}),

                           dcc.Dropdown(id='demo-dropdown',
                                        options=[{'label': x, 'value': x} for x in CATEGORY1],
                                        value=CATEGORY1[0],
                                        style={'font': 'Helvetica',
                                               'font-size': '11px',
                                               'width': '150px'})
                       ])

    return element


def category2_selector_container():

    element = html.Div(className='category2-selector',
                       children=[
                           html.Div('Select Category',
                                    style={'font': 'Helvetica',
                                           'font-size': '12px',
                                           'margin-bottom': '5px'}),

                           dcc.RadioItems(id='demo-checklist',
                                          options=[{'label': x, 'value': x} for x in CATEGORY2],
                                          value=CATEGORY2[0],
                                          labelStyle={'display': 'block'},
                                          style={'font': 'Helvetica',
                                                 'font-size': '11px',
                                                 'width': '150px'})
                       ])

    return element


def summary_container1():

    element = html.Div(className='summary-container1',
                       children=['summary container'])

    return element


def summary_container2():

    element = html.Div(className='summary-container2',
                       children=['summary container'])

    return element
