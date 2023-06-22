import pandas as pd

# Read data from a CSV file
df = pd.read_csv('data.csv')

# Display the first few rows
print(df.head())

# Accessing columns
column_names = df.columns
print(column_names)

# Accessing specific columns
column = df['column_name']
print(column)

# Filtering rows based on condition
filtered_df = df[df['column'] > 10]
print(filtered_df)

# Adding a new column
df['new_column'] = [1, 2, 3, 4, 5]
print(df)

# Dropping columns
df = df.drop(['column1', 'column2'], axis=1)
print(df)

# Sorting by column
sorted_df = df.sort_values('column')
print(sorted_df)

# Grouping and aggregation
grouped_df = df.groupby('column').mean()
print(grouped_df)

# Handling missing values
df = df.dropna()  # Drop rows with missing values
df = df.fillna(0)  # Fill missing values with a specific value

# Writing data to a CSV file
df.to_csv('output.csv', index=False)

# Basic statistics
mean = df['column'].mean()
median = df['column'].median()
std = df['column'].std()
