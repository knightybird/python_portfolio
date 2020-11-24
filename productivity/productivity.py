import datetime
import pandas as pd
import matplotlib as plt

import pandas_datareader as pdr

CSV_DATA = 'C:\\Users\\nicho\\Desktop\\python_portfolio\\productivity\\2019-Productivity.csv'


df = pd.read_csv(CSV_DATA)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)


print('Number of colums in Dataframe : ', len(df.columns))
print('Number of rows in Dataframe : ', len(df.index))
# print(df)
df_stats = df['Total_Prod.'].sum()


# df_stats['Total_Prod.'] = df['Total_Prod.'].sum
print(df_stats)

