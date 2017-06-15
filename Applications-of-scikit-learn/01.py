import pandas as pd
user_cols = ['user_id', 'age','gender','occupation','zip_code']

movieusers = pd.read_table('http://bit.ly/movieusers', sep = '|', header = None, names = user_cols)

ufo = pd.read_csv('http://bit.ly/uforeports')

#print ufo['City']
#print ufo.City - only for non-space names or non buit-in attribute name



