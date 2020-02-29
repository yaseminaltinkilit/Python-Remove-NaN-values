import pandas as pd 

csv_file = pd.read_csv("Your csv Path",sep=',', error_bad_lines=False, index_col=False, dtype='unicode')

print (csv_file.head()) # Check the data
print(csv_file.columns) # Check name of the columns

print(csv_file.isnull().values.any()) # Is there any none values?
print(csv_file.isnull().sum()) # Sum of the none values

dr_drop=csv_file.columns[csv_file.isna().any()].tolist() # None values column names 

csv_file.drop(dr_drop,1,inplace=True) # Delete none values

#Control all the processes is True
print(csv_file.head())
print(csv_file.isnull().values.any())
print(csv_file.isnull().sum())