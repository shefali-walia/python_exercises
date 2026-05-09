import numpy as np
import numpy.random as random
import pandas as pd
from pandas import Series, DataFrame

# Pandas is a library that handles Python data as a number table, graphing can also be done.
# Series and Dataframe are data structures in pandas.

#SERIES
# series is like a one-dimensional numpy array with labels for indices
series1 = Series([1, 1, 2, 4, 5 ,8, 19]) # if indices not mentioned, it is 0,1,2...
print(series1)

series2 = Series([2, 4, 5, 6], index = ['p', 'q', 'r', 's']) # if indices are mentioned, it is as mentioned.
print(series2)

print('Element: ', series2.values) #all elements (values) in series1
print('Indices: ', series2.index) #all indices in series1
print(series1[3], series2['p']) #accessing element by index

#DATAFRAME
# A DataFrame object is basically a two-dimensional data column.
# With the print function, the data is displayed in a tabular format.

data = {
    'ID':['100', '101', '102', '103', '104'],
    'City':['Tokyo', 'Osaka', 'Kyoto', 'Hokkaido', 'Tokyo'],
    'Birth_year':[1990, 1989, 1992, 1997, 1982],
    'Name':['Hiroshi', 'Akiko', 'Yuki', 'Satoru', 'Steve']
}  
#it is a dictionary with keys as column names and values as list of column values.
df = DataFrame(data)
print(df)
print(df.head()) # shows the first 5 rows of the dataframe if not specified, otherwise shows the specified number of rows.
# df.tail() shows the last 5 rows of the dataframe  

df_i = DataFrame(data, index = ['a', 'b', 'c', 'd', 'e']) 
print(df_i)
print(df_i['City']) #accessing a column by its name
print(df_i[['City', 'Birth_year']]) #accessing multiple columns by their names
print(df_i.City) #accessing a column by its name using dot notation
print("ELement: ", df_i.values) #all elements in the dataframe
print("Indices: ", df_i.index) #all indices in the dataframe
print("Column Names: ", df_i.columns) #all column names in the dataframe

# For large dataframes, it may be partially omitted so you can speficy no. of columns or rows to display
pd.set_option('display.max_columns', 10) 
pd.set_option('display.max_rows', 10)