# Header
from pandas import Series, DataFrame
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('NYC_Restaurants.csv', dtype=unicode)

# Question 1

# Add a new Column
df['RESTAURANT'] = df['DBA'] + ' ' + df['BUILDING'] + ' ' + df['STREET'] + ' ' + df['ZIPCODE']

# Print the first 10
print df['RESTAURANT'][:10]

print '\n\n\n'

# Question 2

# Get the Value Counts for Unique Restaurant Name
# Create a Series with just the unique RESTAURANTS
unique_resturants = df['RESTAURANT'].unique()
num_unique_restaurants = len(unique_resturants)
print num_unique_restaurants
print '\n\n\n'

# Question 3

# Get the unique Resturant Names and full Name
ids_restaurants = df[['DBA', 'RESTAURANT']].drop_duplicates(subset='RESTAURANT')

# Create  a mask to repersent only the Names that appear more than once
chain_mask = (ids_restaurants['DBA'].value_counts() > 1)

# Apply the Mask to get a DataFrame of the Chains
# Set the Name of the Restaurant as the Index
# Create a series with just the RESTAURANT and the index will be DBA
chains = ids_restaurants.set_index('DBA')['RESTAURANT'][chain_mask]


# Print the number of unique indexes
num_chains = len(chains)
print num_chains


# Question 4

# Reset the index
chains.reset_index()['DBA'].value_counts()[:20].plot(kind='bar')
plt.show()

# Question 5

print num_chains / num_unique_restaurants

# Question 6

# Get all non chain Resturants
non_chain_mask = (df[['DBA', 'RESTAURANT']].drop_duplicates(subset='RESTAURANT')['DBA'].value_counts() < 2)
print non_chain_mask

# Question 7
# Question 8
# Question 9
# Question 10
# Question 11
# Question 12