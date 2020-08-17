import pandas as pd 
 
df = pd.read_csv('data/survey_results_public.csv')
schema_df = pd.read_csv('data/survey_results_schema.csv')

df.head(10) # prints first 10 rows. By default it prints 5 rows
df.tail(10) # prints last 10 rows. By default it prints 5 rows

df.shape # Used for finding dimenstions of data
df.info() # Used to find information of data like Number of row, columns and types of data......

pd.set_option('display.max_columns', 25) # shows 25 Columns whe we print dataframe..
pd.set_option('display.max_rows', 25) # shows 25 rows whe we print dataframe..

# to convert dict to dataframe
dict_to_df = pd.DataFrame({'first':['kaushal', 'pinkal','pinkal'], 'last': ['khokhar', 'khokhar', 'khokhar']})

# to get 'first' column.
dict_to_df['first']
dict_to_df[['first', 'last']] # to get multiple column

df.columns # to get name of columns

# loc and iloc used to access rows 
# iloc to get row by interger 
df.iloc[0] # to get first row
df.iloc[[0, 1]] # to get first and second row
df.iloc[[0, 1], 0] # to get first and second row of 1st columns
df.iloc[0:1, 0] # to get first and second row of 1st columns

# used to get row by its name
df.loc[0] # to get first row.
# Here loc has alos integer arguments, becuase we have not specified name of rows
dict_to_df.loc[[0, 1], 'first'] # to get first and second row of column name with first

dict_to_df['first'].value_counts() # returns a count of various unique data in specified column
# Above code gives following asnwer
# Kaushal 1
# Pinkal 2

