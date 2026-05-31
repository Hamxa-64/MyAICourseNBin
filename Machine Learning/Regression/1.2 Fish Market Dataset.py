import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import OneHotEncoder

path_to_file = 'Fish[1].csv'
df = pd.read_csv(path_to_file)

print("df.head: ", df.head())
print("df.shape: ",df.shape)

import seaborn as sns

variables = ['Length1', 'Length2', 'Length3', 'Height', 'Width']
for var in variables:
    plt.figure()
    sns.regplot(x=var, y='Weight', data=df)
    plt.title(f'Regression plot of {var} and Weight')

plt.show()

sns.boxplot(x='Species', y='Weight', data=df)
plt.title("Species vs Weight")
plt.show()


#Onehotencoding for Species column

ohe = OneHotEncoder(sparse_output=False)

species_encoded = ohe.fit_transform(df[['Species']])

species_df = pd.DataFrame(
    species_encoded,
    columns=ohe.get_feature_names_out(['Species'])
)

df = pd.concat([df.drop('Species', axis=1), species_df], axis=1)


#Features and Target 

y = df['Weight']
X = df.drop('Weight', axis=1)


#Train Test Split 

SEED = 42
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=SEED
)

print("X.shape: ", X.shape)


#Linear Regression

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


#Prediction 

y_pred = regressor.predict(X_test)

results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

print("Actual vs Predicted.....\n", results)


#Evaluation 

from sklearn.metrics import mean_absolute_error, mean_squared_error

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')


actual_minus_predicted = sum((y_test - y_pred)**2)
actual_minus_actual_mean = sum((y_test - y_test.mean())**2)

r2 = 1 - actual_minus_predicted / actual_minus_actual_mean

print('R²:', r2)