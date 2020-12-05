from dash.dependencies import Input, Output, State
import pandas as pd
from config import PATH_DATASET1

df = pd.read_csv(PATH_DATASET1)


def register_callbacks(app):

    # category1
    @app.callback(
        Output('category1', 'children'),
        [Input('demo-dropdown', 'value')])
    def output_category1(category1):
        return category1

    # category2
    @app.callback(
        Output('category2', 'children'),
        [Input('demo-checklist', 'value')])
    def output_category1(category2):
        return category2

    # value1
    @app.callback(
        Output('value1', 'children'),
        [Input('demo-dropdown', 'value'),
         Input('demo-checklist', 'value'),
         Input('date-range', 'start_date'),
         Input('date-range', 'end_date')])
    def output_value1(category1, category2, sd, ed):
        sd = pd.to_datetime(sd)
        ed = pd.to_datetime(ed)
        df['date'] = pd.to_datetime(df['date'])
        df_new = df[(df['category1'] == category1) & (df['category2'] == category2)]
        df_new = df_new[(df['date'] >= sd) & (df['date'] <= ed)]
        value1 = df_new['value1'].sum()

        return "{:,}".format(value1)

    # date selector
    @app.callback(
        [Output('start-date', 'children'),
         Output('end-date', 'children')],
        [Input('date-range', 'start_date'),
         Input('date-range', 'end_date')])
    def output_date(sd, ed):
        return sd, ed



