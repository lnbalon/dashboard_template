import random
import pandas as pd


def generate_random_dataframe(num_rows, seed=73):

    df = pd.DataFrame()
    df['date'] = pd.date_range(start='2019-01-01', 
                               periods=num_rows,
                               freq='D')

    df['category1'] = [['AAA', 'BBB', 'CCC'][random.randrange(3)] for x in range(num_rows)]
    
    df['category2']  = [['XXXX', 'YYYY', 'ZZZZ', 'WWWW'][random.randrange(4)] for x in range(num_rows)]
     
    df['category3']  = [['fjkdfd', 'qewert', 'fjlsdeiq', 'bacwep'][random.randrange(4)] for x in range(num_rows)]
      
    df['value1'] = [random.randrange(10000, 12e5) for x in range(num_rows)]

    df['value2'] = [random.randrange(80000, 11e5) for x in range(num_rows)]
    
    df['value3'] = [random.randrange(100000, 12e6) for x in range(num_rows)]

    df['value4'] = [random.randrange(1, 10000)/10000 for x in range(num_rows)]


    return df


if __name__ == '__main__':
    
    df_ = generate_random_dataframe(365)
    df_.to_csv('dataset1.csv', index=False)

