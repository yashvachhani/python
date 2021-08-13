import pandas as pd
df = pd.read_csv('survey_results_public.csv')
print(df)

# gives shiiape of dataframe
print(df.shape)

# gives information about dataframe and datatype
print(df.info())

# change visual settings for dataframe
pd.set_option('display.max_columns',None)   # None for all colume and number like 8, 9, 100 if manualy set colume

print(df)


# get secound dataframe
schema_df = pd.read_csv("survey_results_schema.csv")
pd.set_option('display.max_rows',None)

print(schema_df)

# see some rows first rows and last rows

print(schema_df.head(10))
print(schema_df.tail(10))
