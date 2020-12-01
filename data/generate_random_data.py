import random
import pandas as pd


def generate_random_dataframe(num_rows, seed=73):

    df = pd.DataFrame()
    df['date'] = pd.date_range(start='2019-01-01', 
                               periods=num_rows,
                               freq='D')

    return df


if __name__ == '__main__':
    
    df_ = generate_random_dataframe(365)
    df_.to_csv('dataset1.csv', index=False)

