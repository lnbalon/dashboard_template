import dash_html_components as html
from functions import get_category1, get_category2, get_category3
import pandas as pd
from config import PATH_DATASET1

df = pd.read_csv(PATH_DATASET1)
CATEGORY1 = sorted(get_category1(df))
CATEGORY2 = sorted(get_category2(df))
CATEGORY3 = sorted(get_category3(df))


def logo_container():

    logo = html.Div(className='logo-container',
                    children=['logo goes here'])

    return logo


def app_name_container():

    app_name = html.Div(className='title-container',
                        children=['TITLE GOES HERE'])

    return app_name


def summary_container1():

    element = html.Div(className='summary-container1',
                       children=['summary container'])

    return element


def summary_container2():

    element = html.Div(className='summary-container2',
                       children=['summary container'])

    return element
