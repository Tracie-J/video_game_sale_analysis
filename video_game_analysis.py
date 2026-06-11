# Imports
import pandas as pd

# Show all dataframe
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)

# Read in data
df = pd.read_csv('video_games_sales.csv', sep=';', usecols=lambda x: 'Unnamed' not in x)
print(df.head())

# Check column names, Check to see if these match with dataset source
print(df.columns.tolist())

# General look at data
print(df.info(verbose=True))