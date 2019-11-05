# Multiple Linear Regression, with appended p_value regression, and appended p_value with adjusted R squar regression.

# Remember!
# Linearity
# Homoscedasticity
# Multivariate normality
# Independence of error
# Lack of multicollinearity


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv' )
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

print(dataset.head())
print('\n')

print('X')
print(X[:10])
print('\n')

print('y')
print(y[:10])
print('\n')

# Encoding categorical data
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer 
ct = ColumnTransformer( 
    [ ("Step_Name", OneHotEncoder(),[-1] ) ],
     remainder='passthrough'
    )
X = ct.fit_transform(X)

print('X')
print(X[:10])
print('\n')

# Avoiding the Dummy Variable Trap
X = X[:, 1:]

print('X')
print(X[:10])
print('\n')

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0 )

print('X_train')
print(X_train[:10])
print('\n')

print('y_train')
print(y_train[:10])
print('\n')

print('X_test')
print(X_test[:10])
print('\n')

print('y_test')
print(y_test[:10])
print('\n')

# # Feature Scaling
# from sklearn.preprocessing import StandardScaler
# sc_X = StandardScaler()
# X_train = sc_X.fit_transform(X_train )
# X_test = sc_X.transform(X_test )
# sc_y = StandardScaler()
# y_train = sc_y.fit_transform(y_train.reshape(-1, 1) )

# print('X_train')
# print(X_train[:10])
# print('\n')

# print('y_train')
# print(y_train[:10])
# print('\n')

# print('X_test')
# print(X_test[:10])
# print('\n')

# print('y_test')
# print(y_test[:10])
# print('\n')

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train )

# Predicting the Test set results
y_pred = regressor.predict(X_test )

print('y_pred')
print(y_pred[:10])
print('\n')

def plot_train_test(X_train, X_test, y_train, y_test):
    # Training set Viz
    plt.subplot(231)
    plt.scatter( X_train[:,2], y_train, color="blue" )
    plt.title('R&D (Training set)')
    plt.xlabel('$ Spend')
    plt.ylabel('Profit')

    plt.subplot(232)
    plt.scatter( X_train[:,3], y_train, color="green" )
    plt.title('Marketing (Training set)')
    plt.xlabel('$ Spend')
    plt.ylabel('Profit')

    plt.subplot(233)
    plt.scatter( X_train[:,4], y_train, color="purple" )
    plt.title('Administration (Training set)')
    plt.xlabel('$ Spend')
    plt.ylabel('Profit')

    # Test set Viz
    plt.subplot(234)
    plt.scatter( X_test[:,2], y_test, color="blue" )
    plt.title('R&D (Test set)')
    plt.xlabel('$ Spend')
    plt.ylabel('Profit')

    plt.subplot(235)
    plt.scatter( X_test[:,3], y_test, color="green" )
    plt.title('Marketing (Test set)')
    plt.xlabel('$ Spend')
    plt.ylabel('Profit')

    plt.subplot(236)
    plt.scatter( X_test[:,4], y_test, color="purple" )
    plt.title('Administration (Test set)')
    plt.xlabel('$ Spend')
    plt.ylabel('Profit')

    plt.show()
    return

def plot_train_test_pred(X_train, X_test, y_train, y_test, y_pred):
    # Training set Viz
    plt.subplot(231)
    plt.scatter( X_train[:,2], y_train, color="blue" )
    plt.title('R&D (Training set)')
    plt.xlabel('$ Spend')
    plt.ylabel('Profit')

    plt.subplot(232)
    plt.scatter( X_train[:,3], y_train, color="green" )
    plt.title('Marketing (Training set)')
    plt.xlabel('$ Spend')
    plt.ylabel('Profit')

    plt.subplot(233)
    plt.scatter( X_train[:,4], y_train, color="purple" )
    plt.title('Administration (Training set)')
    plt.xlabel('$ Spend')
    plt.ylabel('Profit')

    # Test set Viz with predictions
    plt.subplot(234)
    plt.scatter( X_test[:,2], y_test, color="blue" )
    plt.scatter( X_test[:,2], y_pred, color="red" )
    plt.title('R&D (Test set)')
    plt.xlabel('$ Spend')
    plt.ylabel('Profit')

    plt.subplot(235)
    plt.scatter( X_test[:,3], y_test, color="green" )
    plt.scatter( X_test[:,3], y_pred, color="red" )
    plt.title('Marketing (Test set)')
    plt.xlabel('$ Spend')
    plt.ylabel('Profit')

    plt.subplot(236)
    plt.scatter( X_test[:,4], y_test, color="purple" )
    plt.scatter( X_test[:,4], y_pred, color="red" )
    plt.title('Administration (Test set)')
    plt.xlabel('$ Spend')
    plt.ylabel('Profit')

    plt.show()
    return

# plot_train_test(X_train, X_test, y_train, y_test)
# plot_train_test_pred( X_train, X_test, y_train, y_test, y_pred)

# Assessing the Prediction Error (pred - test)
y_error = y_pred - y_test
y_percent_error = (y_pred - y_test) / y_test
y_pred_sumErrors = sum(y_percent_error) / len(y_percent_error)

print('y_error\n',y_error)
print('y_percent_error\n',y_percent_error)
print('y_pred_sumErrors:\n',y_pred_sumErrors)
print('\n')

# Backward Elimination for Model improvement -
# Need for a constants column

X_train = np.append( arr=np.ones((40,1)).astype(int), values = X_train, axis = 1 )
print('X_train')
print(X_train[:10])
print('\n')

import statsmodels.api as sm
# Creat optimal matrix of features for independent variables with high impact on profit
X_opt = X_train[:, [0, 1, 2, 3, 4, 5]]
X_opt = np.array(X_opt, dtype=float)
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
summary = regressor_OLS.summary()
print(summary)

# First Removal of highest P-value independent variable
X_opt = X_train[:, [0, 1, 3, 4, 5]]
X_opt = np.array(X_opt, dtype=float)
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
summary = regressor_OLS.summary()
print(summary)

# Second Removal of highest P-value independent variable
X_opt = X_train[:, [0, 3, 4, 5]]
X_opt = np.array(X_opt, dtype=float)
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
summary = regressor_OLS.summary()
print(summary)

# Third Removal of highest P-value independent variable
X_opt = X_train[:, [0, 3, 5]]
X_opt = np.array(X_opt, dtype=float)
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
summary = regressor_OLS.summary()
print(summary)