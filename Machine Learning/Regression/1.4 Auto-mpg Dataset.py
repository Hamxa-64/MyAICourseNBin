import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#load csv 
path_to_file = 'auto-mpg[1].csv'
df = pd.read_csv(path_to_file, delimiter=',')

print("df.head:  ", df.head())
print("df.shape:  ", df.shape)
print("df.describe :", df.describe())


#Data Cleaning
df['horsepower'] = pd.to_numeric(df['horsepower'], errors='coerce')
df = df.dropna()
df = df.drop(['car name'], axis=1)

print("\nAfter cleaning shape:", df.shape)
print("Missing values:\n", df.isnull().sum())

import seaborn as sns

variables = ['cylinders', 'displacement', 'horsepower','weight', 'acceleration', 'model year', 'origin']
for var in variables:
    plt.figure()
    sns.scatterplot(x= var, y= 'mpg', data=df)
    plt.title(f'Regression plot of {var} and mpg')
    plt.show()

#heatmap for correlation
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()

#features and targets 
X = df.drop('mpg', axis=1)
y = df['mpg']

#train test split
SEED = 24
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.3, 
                                                    random_state=SEED)
print("\nX_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)

#model train
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

print("regressor.intercept: ", regressor.intercept_)
print("regressor.coeff : ", regressor.coef_)

feature_names = X.columns
model_coefficients = regressor.coef_

coefficients_df = pd.DataFrame(
    data=model_coefficients,
    index=feature_names,
    columns=['Coefficient value']
)

print(coefficients_df)

#prediction
y_pred = regressor.predict(X_test)

results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

print("Actual vs Predicted.....\n", results)

#metrices performance

from sklearn.metrics import mean_squared_error,root_mean_squared_error,mean_absolute_error,r2_score
mse  = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae  = mean_absolute_error(y_test, y_pred)
r2   = r2_score(y_test, y_pred)

print("\n Model Performance")
print(f"MSE  : {mse:.4f}")
print(f"RMSE : {rmse:.4f}")
print(f"MAE  : {mae:.4f}")
print(f"R2 Score : {r2:.4f}")

#actual vs predicted plots

plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel("Actual MPG")
plt.ylabel("Predicted MPG")
plt.title("Actual vs Predicted MPG")
plt.show()

