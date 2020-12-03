import dash_html_components as html
import dash_core_components as dcc
from config import APP_NAME
from functions import get_category1, get_category2, get_category3
import pandas as pd
from config import PATH_DATASET1

df = pd.read_csv(PATH_DATASET1)
CATEGORY1 = sorted(get_category1(df))
CATEGORY2 = sorted(get_category2(df))
CATEGORY3 = sorted(get_category3(df))

def create_header():

    header = html.Div(className='banner-container',
                      children=['banner area'])

    return header


def create_selector():

    selector = html.Div(className='selector-container',
                        children=['selector area'])

    return selector


def create_summary():

    summary = html.Div(className='summary-container',
                       children=['summary area'])

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
