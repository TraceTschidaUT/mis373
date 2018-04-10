from pandas import Series, DataFrame
import pandas as pd
from patsy import dmatrices
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn import neighbors, metrics, model_selection, naive_bayes
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')
# %pylab inline

def is_currency(s):
    '''Takes in an element of the series and outputs if it is a currency'''
    return (s.isupper() and len(s) == 3)

# Create the currency conversions for both pledged and goal
# Conversion valid April 10, 2018 @ 12:00 PM Central Time
currency_conversions = {
    'USD': 1.000000,
    'GBP': 1.41540,
    'CAD': 0.793289,
    'EUR': 1.23490,
    'AUD': 0.776080,
    'SEK': 0.120317,
    'NZD': 0.736415,
    'DKK': 0.165835,
    'NOK': 0.128176,
    'CHF': 1.04558,
    'MXN': 0.0547386,
    'SGD': 0.763829,
    'HKD': 0.127393,
    'JPY': 0.00931953
}

def currency_conversion(df):
    '''Takes in an df and outputs the conversion'''
    for k,v in currency_conversions.iteritems():
        
        # Create a make for the currency
        mask_currency = (df['currency'] == k)
        df.loc[mask_currency, 'usd_goal_current'] = df['goal'] * v
        df.loc[mask_currency, 'usd_pledged_current'] = df['pledged']  * v
    return df

def clean_states(e):
    '''Takes in an elements and returns if it is in a clean state'''
    return (e in ['failed', 'successful', 'suspended', 'canceled'])


def get_month(e):
    '''Takes in a datetime element and returns the month'''
    return e.month

# Load the csv
df = pd.read_csv('ks-projects-201801.csv')

# Convert the currency into today's price
df = currency_conversion(df)

# Convert the deadline and launched columns into dtype: datetime
df['deadline'] = pd.to_datetime(df['deadline'], format='%Y-%m-%d')
df['launched'] = pd.to_datetime(df['launched'], format='%Y-%m-%d %H:%M:%S')

# Add a 'month' and 'year' coloumn to the df
df['month_deadline'] = df['deadline'].map(get_month)
df['month_launched'] = df['launched'].map(get_month)

# Add an average pledge per backer
df['average_pledged'] = df['pledged'] / df['backers']

# Get a baseline for the ML
# The first part is going to predict based off of cateogrical variables: 
# category, month-launched, month-deadline

# There are 6 states: failed, successful, canceled, undefied, lived, suspended
# For classification purposes 1.0 = successful, 0.0 = failed, suspended, canceled
# Create a mask of just the clean states
mask_clean_states = (df['state'].map(clean_states))
df_clean_states = df[mask_clean_states]

# Get the value counts for the clean states
vc_clean_states = df_clean_states['state'].value_counts()

# Find the baseline by dividing the total of project by the number of successful projects
# baseline = 0.359806607575
num_total_projects = vc_clean_states.sum()
num_successful_projects = vc_clean_states['successful']
baseline = float(num_successful_projects) / float(num_total_projects)

# Create a dummy binary variable for success or fail/cancel/suspended
df_clean_states['target'] = 0.0
mask_target = df_clean_states['state'] == 'successful'
df_clean_states.loc[mask_target, 'target'] = 1.0

# Start with simple KNN with two features: Number of Backers and Goal Amount
def accuracy(X, y, nn):

    model = neighbors.KNeighborsClassifier(n_neighbors=nn, weights='uniform')
    accuracies = []

    kfold = model_selection.StratifiedKFold(n_splits=3, shuffle=True).split(X, y)
    for train, holdout in kfold:
        # Select the training and testing data using the indicies from kfold
        X_train = X.iloc[train]
        X_holdout = X.iloc[holdout]
        y_train = y[train]
        y_holdout = y[holdout]

        # Fit the model
        model.fit(X_train, y_train)

        # Compute the accuracy
        current_accuracy = metrics.accuracy_score(y_holdout, model.predict(X_holdout))
        accuracies.append(current_accuracy)
        
    return accuracy

'''
# Create a design matrice
Y, X = dmatrices('target ~ 0 + backers + usd_goal_real', df_clean_states, return_type='dataframe')
y = Y['target'].values
# sc = scatter(df_clean_states['backers'], df_clean_states['usd_goal_real'], c=y, cmap='bwr')


# Create sample nn
nn = [15]
scores = [accuracy(X, y, num_nbrs) for num_nbrs in nn]
print scores
'''

# Best Nearest Neighbor Numbers: Up to 100 nn they were all about the same accuracy between 91% and 93% 
# So you are best just using around 15 backers becuase it is faster
# Starts to see small dips over 100 nn
# Looks like the more backers and lower goal means that you have the best shot
# But that makes sense, and is only after the fact
# Backers is continuous not categorical

# What about the category, main category, and goal amount
# Can we predict if the project will be successfully funded
# We first need to discretize the goal amount
# Create 20 bins of the goal amount
# usd_goal_real is discrete not catoegorical
df['goal_binned'] = pd.qcut(df['usd_goal_real'], 10)

# Create a list of categorical columns that will be used
categorical_columns = ['goal_binned', 'category', 'main_category']

# Create a df that includes the dummy variables
df_dummies = pd.get_dummies(df[categorical_columns], prefix=categorical_columns, columns=categorical_columns)

# Get the categories with the most funding
temp = df.groupby('main_category')['usd_goal_real'].mean().sort_values(ascending=False)


# Maybe use the test data for the live ones?


# Possible Features:
# Month launched and deadline
# Goal Amount
# Number of Backers
# Country of Origin
# Category and Main Category
