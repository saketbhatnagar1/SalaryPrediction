

'''
This model predicts the salary of the employ based on experience using simple linear regression model.
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import requests
import json


dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)


y_pred = regressor.predict(X_test)


pickle.dump(regressor, open('model.pkl','wb'))


model = pickle.load( open('model.pkl','rb'))
print(model.predict([[1.8]]))
