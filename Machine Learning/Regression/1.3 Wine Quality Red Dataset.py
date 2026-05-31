import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

path_to_file = 'winequality-red[1].csv'
df = pd.read_csv(path_to_file, delimiter=';')

print("df.head :",df.head())
print("df.shape:  ", df.shape)
print("df.describe:  ", df.describe())

import seaborn as sns

variables = ['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol']
for var in variables:
    plt.figure()
    sns.regplot(x=var,y='quality', data= df)
    plt.title(f'Regression plot of {var} and quality')

    plt.show()

plt.figure(figsize=(12,8))
sns.heatmap(df.corr(), annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

sns.boxplot(x='quality', y='alcohol', data=df)
plt.title('Alcohol vs Quality')
plt.show()
read = input("Wait here: \n")

y = df['quality']
X= df[['fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol']]

SEED= 42
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.3, 
                                                    random_state=SEED)
print("X.shape:     \n", X.shape )  

from sklearn.ensemble import RandomForestRegressor 

regressor = RandomForestRegressor(n_estimators=100, random_state=42)
regressor.fit(X_train, y_train)

feature_names = X.columns
feature_importances = regressor.feature_importances_

coefficients_df = pd.DataFrame(data=feature_importances,
                               index=feature_names,
                               columns=['Feature Importance'])
print(coefficients_df)

y_pred = regressor.predict(X_test)
y_pred = regressor.predict(X_test)
results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print("Actual vs Predicted.....\n" , results)

from sklearn.metrics import mean_absolute_error, mean_squared_error,root_mean_squared_error
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f'Mean absolute error: {mae:.2f}')
print(f'Mean squared error: {mse:.2f}')
print(f'Root mean squared error: {rmse:.2f}')

actual_minus_predicted = sum((y_test - y_pred)**2)
actual_minus_actual_mean = sum((y_test - y_test.mean())**2)
r2 = 1 - actual_minus_predicted/actual_minus_actual_mean
print('R²:', r2)





