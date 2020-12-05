import dash_html_components as html
import dash_core_components as dcc
from functions import get_category1, get_category2, get_category3
import pandas as pd
from config import PATH_DATASET1
import datetime

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
                           html.Div('Select Category 1',
                                    style={'font-weight': 'Bold',
                                           'font-size': '12px',
                                           'margin-bottom': '5px'}),

                           dcc.Dropdown(id='demo-dropdown',
                                        options=[{'label': x, 'value': x} for x in CATEGORY1],
                                        value=CATEGORY1[0],
                                        style={'font-size': '12px',
                                               'width': '150px'})
                       ])

    return element


def category2_selector_container():

    element = html.Div(className='category2-selector',
                       children=[
                           html.Div('Select Category 2',
                                    style={'font-weight': 'Bold',
                                           'font-size': '12px',
                                           'margin-bottom': '5px'}),

                           dcc.RadioItems(id='demo-checklist',
                                          options=[{'label': x, 'value': x} for x in CATEGORY2],
                                          value=CATEGORY2[0],
                                          labelStyle={'display': 'block'},
                                          style={'font-size': '12px',
                                                 'width': '150px'})
                       ])

    return element


def date_selector_container():

    element = html.Div(className='date-selector',
                       children=[
                           html.Div('Select Date Range',
                                    style={'font-weight': 'Bold',
                                           'font-size': '12px',
                                           'margin-bottom': '5px'}),

                           dcc.DatePickerRange(
                               id='date-range',
                               min_date_allowed=datetime.date(1995, 8, 5),
                               max_date_allowed=datetime.date(2017, 9, 19),
                               initial_visible_month=datetime.date(2017, 8, 5),
                               end_date=datetime.date(2017, 8, 25),
                               style={'font-size': '12px'}
                           )
                       ])

    return element


def summary_container1():

    element = html.Div(className='summary-container1',
                       children=[
                           html.Div('Category 1:',
                                    style={'font-size': '14px',
                                           'font-weight': 'normal'}),

                           html.Div(id='category1',
                                    style={'font-size': '24px',
                                           'font-weight': 'bold',
                                           'margin-top': '15px',
                                           'margin-left': '10px'}),
                       ])

    return element


def summary_container2():

    element = html.Div(className='summary-container2',
                       children=[
                           html.Div('Category 2:',
                                    style={'font-size': '14px',
                                           'font-weight': 'normal'}),

                           html.Div(id='category2',
                                    style={'font-size': '24px',
                                           'font-weight': 'bold',
                                           'margin-top': '15px',
                                           'margin-left': '10px'}),
                       ])

    return element


def summary_container3():

    element = html.Div(className='summary-container3',
                       children=[
                           html.Div('Value 1:',
                                    style={'font-size': '14px',
                                           'font-weight': 'normal'}),

                           html.Div(id='value1',
                                    style={'font-size': '24px',
                                           'font-weight': 'bold',
                                           'margin-top': '15px',
                                           'margin-left': '10px'}),
                       ])

    return element


def summary_container4():

    element = html.Div(className='summary-container4',
                       children=[
                           html.Div('Value 1:',
                                    style={'font-size': '14px',
                                           'font-weight': 'normal'}),

                           html.Div(id='start-date',
                                    style={'font-size': '24px',
                                           'font-weight': 'bold',
                                           'margin-top': '15px',
                                           'margin-left': '10px'}),
                       ])

    return element


def summary_container5():

    element = html.Div(className='summary-container5',
                       children=[
                           html.Div('Date End:',
                                    style={'font-size': '14px',
                                           'font-weight': 'normal'}),

                           html.Div(id='end-date',
                                    style={'font-size': '24px',
                                           'font-weight': 'bold',
                                           'margin-top': '15px',
                                           'margin-left': '10px'}),
                       ])

    return element