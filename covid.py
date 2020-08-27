# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('covidfinal1.csv')
X = dataset.iloc[:, :-2]
y = dataset.iloc[:, 14]
x=dataset.iloc[:, 2]


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
print(X_train)
print(X_test)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

y_pred = regressor.predict([[1,1,0,1,1,1,1,1,1,1,1,1,1,1]])

print(y)
plt.plot(x, y)
plt.show()