import pandas as pd
from config import PATH_DATASET1


def get_data_from_csv(path):

    return pd.read_csv(path)


def get_total_value1(sd, ed, df):

    df = df[(df['date'] >= sd) & (df['date'] <= ed)]

    return df


def get_category1(df):

    return list(df['category1'].unique())


if __name__ == '__main__':

    df_ = get_data_from_csv(PATH_DATASET1)
    print(df_)