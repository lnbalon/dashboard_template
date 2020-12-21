from dash.dependencies import Input, Output, State
import plotly.offline as pyo
import plotly.graph_objects as go
import pandas as pd
from config import PATH_DATASET1
import warnings
import dash
from page1_layout import page1_layout

warnings.filterwarnings('ignore')

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
        [Output('value1', 'children'),
         Output('value2', 'children'),
         Output('value4', 'children')],
        [Input('demo-dropdown', 'value'),
         Input('demo-checklist', 'value'),
         Input('date-range', 'start_date'),
         Input('date-range', 'end_date')])
    def output_value1(category1, category2, sd, ed):
        sd = pd.to_datetime(sd)
        ed = pd.to_datetime(ed)
        df['date'] = pd.to_datetime(df['date'])
        df_new = df[(df['category1'] == category1) & (df['category2'] == category2)]
        df_new_ = df_new[(df['date'] >= sd) & (df['date'] <= ed)]
        value1 = df_new_['value1'].sum()
        value2 = df_new_['value2'].sum()
        value4 = df_new_['value4'].mean()
        return "{:,}".format(value1), "$ {:,.0f}K".format(value2/1000), "{:.1f}%".format(value4*100)

    # date selector
    @app.callback(
        [Output('start-date', 'children'),
         Output('end-date', 'children')],
        [Input('date-range', 'start_date'),
         Input('date-range', 'end_date')])
    def output_date(sd, ed):
        return sd, ed

    # update the scatter plot
    @app.callback(
        [Output('scatter1', 'figure'),
         Output('time-series1', 'figure'),
         Output('pie-chart1', 'figure')],
        [Input('demo-dropdown', 'value'),
         Input('demo-checklist', 'value'),
         Input('date-range', 'start_date'),
         Input('date-range', 'end_date')])
    def output_value1(category1, category2, sd, ed):
        sd = pd.to_datetime(sd)
        ed = pd.to_datetime(ed)
        df['date'] = pd.to_datetime(df['date'])
        df_new = df[(df['category1'] == category1) & (df['category2'] == category2)]
        df_new_ = df_new[(df['date'] >= sd) & (df['date'] <= ed)]

        x = df_new_['value1']
        y = df_new_['value2']

        data = [go.Scatter(x=x,
                           y=y,
                           mode='markers',
                           marker=dict(
                               size=12,
                               color='rgb(12,34,129)',
                               symbol='pentagon',
                               line={'width': 2}),
                           hovertemplate='<i>value1</i>: $%{x:.2f} <br>' + '<i>value2</i>: %{y:.2f}'
                           )]

        layout = go.Layout(title='value1 vs. value2',
                           xaxis={'title': 'value1'},
                           yaxis={'title': 'value2'},
                           autosize=True,
                           hovermode='closest')

        fig = go.Figure(data=data, layout=layout)

        # time series
        data2 = [go.Scatter(x=df_new_['date'],
                            y=df_new_['value3'],
                            mode='lines',
                            )]

        layout2 = go.Layout(title='date vs. value3',
                            xaxis={'title': 'date'},
                            yaxis={'title': 'value3'},
                            autosize=True,
                            hovermode='closest')
        fig2 = go.Figure(data=data2, layout=layout2)

        # donut chart
        grouped = df_new_.groupby('category3', as_index=False)['value3'].sum()
        data3 = [go.Pie(labels=grouped['category3'], values=grouped['value3'], hole=0.45)]
        layout3 = go.Layout(title='category3 distribution')
        fig3 = go.Figure(data=data3, layout=layout3)

        return fig, fig2, fig3

    # Update the index
    @app.callback(dash.dependencies.Output('page-content', 'children'),
                  [dash.dependencies.Input('url', 'pathname')])
    def display_page(pathname):
        if pathname == '/page-1':
            return page1_layout
