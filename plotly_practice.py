import plotly.offline as pyo
import plotly.graph_objects as go
from functions import get_data_from_csv
from config import PATH_DATASET1
import pandas as pd

df = get_data_from_csv(PATH_DATASET1)



if __name__ == '__main__':

    print(df.head())