import plotly.offline as pyo
import plotly.graph_objects as go
from functions import get_data_from_csv
from config import PATH_DATASET1
import pandas as pd


if __name__ == '__main__':
    df = get_data_from_csv(PATH_DATASET1)

    # print(df.head())
    x = df['value1']
    y = df['value2']

    data = [go.Scatter(x=x, y=y, mode='markers')]
    layout = go.Layout(title='value1 vs. value2',
                       xaxis={'title': 'value1'},
                       yaxis={'title': 'value2'},
                       hovermode='closest ')

    fig = go.Figure(data=data, layout=layout)
    pyo.plot(fig, filename='scatter.html')