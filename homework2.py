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

# Create a new DF with just the necessary columns and index as the DBA
restaurants_boros = df[['DBA', 'RESTAURANT', 'BOROUGH']].drop_duplicates(subset='RESTAURANT')

# Set the index to be DBA so the mask works
clean_restaurant_boros = restaurant_boros.set_index('DBA')

# Create a mask for the non chain restaurants
# Non chain restaurants will only appear once
non_chain_boro_mask = (clean_restaurants_boros['DBA'].value_counts() < 2)

# Apply the mask
non_chains_boros = clean_restaurant_boros[non_chain_boro_mask]

# Plot the non chains by boro
non_chain_boros['BOROUGH'].value_counts().plot(kind='bar')

# Question 7

# Get the number of chain restaurants by boro
# Create a mask for chain restaurants
chain_boro_mask = (restaurants_boros['DBA'].value_counts() > 1)

# Apply the mask to get the chains in each boro
clean_restaurant_boros = restaurant_boros.set_index('DBA')
chain_boros = clean_restaurant_boros[chain_boro_mask]

# Divide the number of non chains by boro by the number of chains

# Question 8
# Question 9
# Question 10
# Question 11
# Question 12