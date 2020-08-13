# -*- coding: utf-8 -*-
"""model_procrastination.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mr2ldjespcmkrMajvjmno7rKb0D3yHb3
"""

import numpy as np
import pandas as pd
import sklearn 
import matplotlib.pyplot as plt
from google.colab import files
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.linear_model import Ridge
def train_val_test_split(dataset):
  rows = X.shape[0]
  return np.split(dataset, [int(rows * 0.8), int(rows * 0.9)])
def abline(slope, intercept):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '-', color='black', label='Predicted Score as a Function of X')
files.upload() # upload studentAssesment_formatted.csv
dataset = pd.read_csv('studentAssesment_formatted.csv')
X, y = dataset['date_submitted'].values, dataset['final_score'].values
X = X.reshape(-1, 1)
X_train, X_val, X_test = train_val_test_split(X)
y_train, y_val, y_test = train_val_test_split(y)
model=Ridge(fit_intercept=False)
model.fit(X_train,y_train)
X, y = dataset['date_submitted'].values, dataset['final_score'].values
X = X.reshape(-1, 1)
yhat_train = model.predict(X_train)
r = r2_score(yhat_train, y_train)
# r **= 0.5
w = model.coef_
plt.figure()
plt.scatter(X, y)
abline(w, 0)
plt.axis([0, 15, 0, 100])
plt.show()

print("our mean squared error is: {}".format(mean_squared_error(yhat_train, y_train)))
print("our r value is: {}".format(r))
print("our coefficient for the x-term is: {}".format(model.coef_[0]))
print("our intercept of the function is: {}".format(model.intercept_))
print("Judging by the output, we realize that our function is as follows:")
a = r'f(x) = 13.97x'
ax = plt.axes([0,0,0.3,0.3]) #left,bottom,width,height
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')
plt.text(0.4,0.4,'$%s$' %a,size=20,color="black")