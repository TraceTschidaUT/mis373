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

# Find how many rows are in the Series
num_total_restaurants = len(total_resturants)

# Print the number of Restaurants
print num_total_restaurants

print '\n\n\nQ3'

# Question 3

# Get the unique Resturant Names and full Name
# Get only the unique restaurants
ids_restaurants = df[['DBA', 'RESTAURANT']].drop_duplicates('RESTAURANT')

# Create  a mask to repersent only the Names that appear more than once
chain_mask = (ids_restaurants['DBA'].value_counts() > 1)

# Apply the Mask to get a DataFrame of the Chains
# Set the Name of the Restaurant as the Index
# Create a series with just the RESTAURANT and the index will be DBA
chains = ids_restaurants.set_index('DBA')['RESTAURANT'][chain_mask]

# Get the number of chains by counting the total occurance of each chain name
num_chain_restaurants = chains.reset_index()['DBA'].value_counts().sum()
num_chains = len(chains.reset_index()['DBA'].value_counts())

# Print the number of unique chains
print num_chains

print '\n\n\nQ4'

# Question 4

# Reset the index to a count
# Get the number of occurances for each chain name
# Plot the top 20
chains.reset_index()['DBA'].value_counts()[:20].plot(kind='bar')
plt.show()

print '\n\n\nQ5'

# Question 5

print float(num_chain_restaurants) / float(num_total_restaurants)
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

# Apply the mask to the chain name as index and values as boros
# Select out only the non chains
non_chains_boros = clean_restaurants_boros['BORO'][non_chain_boro_mask]

# Plot the non chains by boro
non_chains_boros.value_counts().drop(labels='Missing').plot(kind='bar')
plt.show()
print '\n\n\nQ7'

# Question 7

# Get the number of total restaurants per boro
total_restaurants_by_boro = df[['DBA', 'RESTAURANT', 'BORO']].drop_duplicates(subset='RESTAURANT')

# Get a series with just the boro and the DBA as the index
total_names_by_boro = total_restaurants_by_boro.set_index('DBA')['BORO']

# Divide the number of non chains by boro series by the number of total restaurants in each boro series
# Create two series and divide them to create a new series
percent_independents = non_chains_boros.value_counts().drop(labels='Missing') / \
                        total_names_by_boro.value_counts().drop(labels='Missing')
percent_independents.plot(kind='bar')
plt.show()
print '\n\n\nQ8'

# Question 8
# Create a DF with Cusines and Uniques IDS
# Drop all duplicate restaurants based on repeating ids
ids_cuisines = df[["RESTAURANT", 'CUISINE DESCRIPTION']].drop_duplicates('RESTAURANT')

# Plot the values of each cuisine 
# Grap a series (column) and plot the value counts
cuisine_value_counts = ids_cuisines['CUISINE DESCRIPTION'].value_counts()
cuisine_value_counts[:20].plot(kind='bar')
plt.show()
print '\n\n\nQ9'

# Question 9

# Get a df of restaurants cuisine and violation code
# Drops restaurants that appear more than once either for multiple violations or multiple inspections
df_ids_cuisines_violations = df[["RESTAURANT", 'CUISINE DESCRIPTION', 'VIOLATION CODE', 'INSPECTION DATE']] \
                                .drop_duplicates(subset=['RESTAURANT', 'INSPECTION DATE'])

df_cuisines_violations = df[['CUISINE DESCRIPTION', 'VIOLATION CODE']]

# Create a mask of the null Violation codees in a series
# True and false values are based on index
# Index is numerical not strings
mask_violation = (df['VIOLATION CODE'].isnull())
print mask_violation[:10]

# Apply the mask
df_null_cuisines_violation = df_cuisines_violations[mask_violation]

# Get the popularity of the cuisines
s_null_violation_value_count = df_null_cuisines_violation['CUISINE DESCRIPTION'].value_counts()
s_null_violation_value_count[:20].plot(kind='bar')
plt.show()
print '\n\n\nQ10'


# Question 10

# Get a df of restaurants cuisine and violation code
df_ids_cuisines_violations = df[["RESTAURANT", 'CUISINE DESCRIPTION', 'VIOLATION CODE','INSPECTION DATE']] \
                                .drop_duplicates(subset=['RESTAURANT', 'INSPECTION DATE'])


# Create a mask for cuisines that have atleast 20 inspecitions
mask_cuisines_20_inspections = (df_ids_cuisines_violations['CUISINE DESCRIPTION'].value_counts() >= 20)

# Apply the mask to filter out the cuisines w/o 20+ inspections
# Filter out total count of cuisiens without violations and total count of cuisines
s_cuisines_violations = s_null_violation_value_count[mask_cuisines_20_inspections]
s_cuisines_total = cuisine_value_counts[mask_cuisines_20_inspections]

# Find the ratio of total count of cuisines without violations to total count of cuisines
s_cleanest_cuisines = s_cuisines_violations / s_cuisines_total
print s_cleanest_cuisines.sort_values(ascending=False)[:10]
print('\n\n\nQ11')

# Question 11

# Get a table of the violations, and boros
df_violations_per_boro = df[['VIOLATION CODE', 'BORO']]

# Add a dummy count to the df
list_dummy = [1 for x in range(len(df_violations_per_boro))]
df_violations_per_boro = df_violations_per_boro.assign(DUMMY=list_dummy)

# Create a pivot table for the violatoions and boros
pivot_violations_per_boro = pd.pivot_table(df_violations_per_boro,
    index='VIOLATION CODE', columns='BORO', values='DUMMY', aggfunc=sum)

# Get the max value's index (violation code) for each column (boro)
series_max_violations_per_boro = pivot_violations_per_boro.idxmax().drop(labels='Missing')
print series_max_violations_per_boro
print '\n\n\nQ12'

# Question 12

# Get overall frequencies: 
# Figure out how common each violation is, over the entire dataset
s_violationFrequency = df['VIOLATION CODE'].value_counts()

# Normalize: Consider the table of number of violations by boro that
# you created for the previous question. For each borough, divide the
# number of violations of each type by the total number of violations for
# that type; i.e., divide the series of violations by violationFrequency.
# We want to do this for each borough.

# Divide each cell by its corresponding total of violations
def normalize(s):
    ''' s: Series \n
        normalize(s) -> Series
    '''
    # Pandas matches up the indexes of each series 
    # the Series have the same index
    # The index is the violation code
    return s / s_violationFrequency

# Normalize every series (column) 
# Divide the violation count in the boro by the total number of that violation in the dataset
df_normalized_violations_per_boro = pivot_violations_per_boro.apply(normalize)

# Get the most violational per boro normalized by total number of violations
series_max_violations_per_boro_normalized = df_normalized_violations_per_boro.idxmax() \
                                                .drop('Missing')
                                                
print series_max_violations_per_boro_normalized


