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

print '\n\n\nQ2'

# Question 2

# Get the Value Counts for Unique Restaurant Name
# Create a Series with just the unique RESTAURANTS
total_resturants = df['RESTAURANT'].unique()
num_total_restaurants = len(total_resturants)
print num_total_restaurants
print '\n\n\nQ3'

# Question 3

# Get the unique Resturant Names and full Name
ids_restaurants = df[['DBA', 'RESTAURANT']].drop_duplicates('RESTAURANT')

# Create  a mask to repersent only the Names that appear more than once
chain_mask = (ids_restaurants['DBA'].value_counts() > 1)

# Apply the Mask to get a DataFrame of the Chains
# Set the Name of the Restaurant as the Index
# Create a series with just the RESTAURANT and the index will be DBA
chains = ids_restaurants.set_index('DBA')['RESTAURANT'][chain_mask]


# Print the number of unique chains
num_chains = len(chains.reset_index()['DBA'].value_counts())
print num_chains
print '\n\n\nQ4'

# Question 4

# Reset the index
# chains.reset_index()['DBA'].value_counts()[:20].plot(kind='bar')
# plt.show()

print '\n\n\nQ5'

# Question 5

print float(num_chains) / float(num_total_restaurants)
print '\n\n\nQ6'

# Question 6

# Get all non chain Resturants

# Create a new DF with just the necessary columns and index as the DBA
restaurants_boros = df[['DBA', 'RESTAURANT', 'BORO']].drop_duplicates('RESTAURANT')

# Create a mask for the non chain restaurants
# Non chain restaurants will only appear once
non_chain_boro_mask = (restaurants_boros['DBA'].value_counts() < 2)

# Set the index to be DBA so the mask works
clean_restaurants_boros = restaurants_boros.set_index('DBA')

# Apply the mask
non_chains_boros = clean_restaurants_boros['BORO'][non_chain_boro_mask]

# Plot the non chains by boro
# non_chain_boros['BORO'].value_counts().plot(kind='bar')
print non_chains_boros.value_counts()
print '\n\n\nQ7'

# Question 7

# Get the number of chain restaurants by boro
# Create a mask for chain restaurants
chain_boro_mask = (restaurants_boros['DBA'].value_counts() > 1)

# Apply the mask to get the chains in each boro
clean_restaurant_boros = restaurants_boros.set_index('DBA')
chain_boros = clean_restaurant_boros['BORO'][chain_boro_mask]

# Divide the number of non chains by boro by the number of chains
# Create two series and divide them to create a new series
percent_independents = non_chains_boros.value_counts() / chain_boros.value_counts()
print percent_independents[:5]
print '\n\n\nQ8'

# Question 8
# Create a DF with Cusines and Uniques IDS
# Drop all duplicate restaurants based on repeating ids
ids_cuisines = df[["RESTAURANT", 'CUISINE']].drop_duplicates('RESTAURANT')

# Plot the values of each cuisine 
# Grap a series (column) and plot the value counts
# ids_cusines['CUISINE'].value_counts().plot(kind='bar')
print ids_cuisines['CUISINE'].value_counts()

# Question 9
# Question 10
# Question 11
# Question 12