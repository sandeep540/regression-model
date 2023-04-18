import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle


df = pd.read_csv("student_scores.csv")

df.head() 

# print(df.corr())
# print(df.describe())

y = df['Scores'].values.reshape(-1, 1) # type: ignore
X = df['Hours'].values.reshape(-1, 1) # type: ignore

# print(df['Hours'].values) # [2.5 5.1 3.2 8.5 3.5 1.5 9.2 ... ]
# print(df['Hours'].values.shape) # (25,)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

regressor = LinearRegression()

regressor.fit(X_train, y_train)

filename = 'finalized_model.pkl'
pickle.dump(regressor, open(filename, 'wb'))

# print(regressor.intercept_)
# print(regressor.coef_)

score = regressor.predict([[5.0]]) # type: ignore
print(score) # 94.80663482



