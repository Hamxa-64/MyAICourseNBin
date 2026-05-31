import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

#Load Dataset

path_to_file = 'StudentsPerformance[1].csv'
df = pd.read_csv(path_to_file, delimiter=',')

print("df.head:\n", df.head())
print("df.shape:", df.shape)
print("df.describe:\n", df.describe())


#Label Encoding - Gender
le = LabelEncoder()
df['gender_encoded'] = le.fit_transform(df['gender'])

print("Gender labels mapping:", dict(zip(le.classes_, le.transform(le.classes_))))
print(df[['gender', 'gender_encoded']].head())

df = df.drop('gender', axis=1)  # Original drop karo ✅

# ================================
# 3 - Label Encoding - Lunch
# ================================
le = LabelEncoder()
df['lunch_encoded'] = le.fit_transform(df['lunch'])

print("Lunch labels mapping:", dict(zip(le.classes_, le.transform(le.classes_))))
print(df[['lunch', 'lunch_encoded']].head())

df = df.drop('lunch', axis=1)  # Original drop karo ✅

# ================================
# 4 - Label Encoding - Test Preparation Course
# ================================
le = LabelEncoder()
df['tpc_encoded'] = le.fit_transform(df['test preparation course'])

print("Test preparation course labels mapping:", dict(zip(le.classes_, le.transform(le.classes_))))
print(df[['test preparation course', 'tpc_encoded']].head())

df = df.drop('test preparation course', axis=1)  # Original drop karo ✅

# ================================
# 5 - OneHot Encoding - Race/Ethnicity
# ================================
ohe = OneHotEncoder(sparse_output=False)
race_encoded = ohe.fit_transform(df[['race/ethnicity']])

race_df = pd.DataFrame(
    race_encoded,
    columns=ohe.get_feature_names_out(['race/ethnicity'])
)

df = pd.concat([df.drop('race/ethnicity', axis=1), race_df], axis=1)  # Original drop karo ✅

# ================================
# 6 - OneHot Encoding - Parental Level of Education
# ================================
ohe = OneHotEncoder(sparse_output=False)
ploe_encoded = ohe.fit_transform(df[['parental level of education']])

parentallevelofeducation_df = pd.DataFrame(
    ploe_encoded,
    columns=ohe.get_feature_names_out(['parental level of education'])
)

df = pd.concat([df.drop('parental level of education', axis=1), parentallevelofeducation_df], axis=1)  

print("\ndf after encoding:\n", df.head())
print("df.dtypes:\n", df.dtypes)

# ================================
# 7 - Features aur Target
# ================================
y = df['math score']
X = df.drop(['math score', 'reading score', 'writing score'], axis=1)

print("\nX.shape:", X.shape)
print("X columns:\n", X.columns.tolist())

# ================================
# 8 - Train Test Split
# ================================
SEED = 24

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=SEED
)

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)

# ================================
# 9 - Linear Regression
# ================================
regressor = LinearRegression()
regressor.fit(X_train, y_train)

print("\nregressor.intercept:", regressor.intercept_)
print("regressor.coef:", regressor.coef_)

# ================================
# 10 - Coefficients
# ================================
feature_names = X.columns
model_coefficients = regressor.coef_

coefficients_df = pd.DataFrame(
    data=model_coefficients,
    index=feature_names,
    columns=['Coefficient value']
)
print("\nCoefficients:\n", coefficients_df)

# ================================
# 11 - Prediction
# ================================
y_pred = regressor.predict(X_test)

# ================================
# 12 - Evaluation
# ================================
mse  = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2   = r2_score(y_test, y_pred)

print("\n===== Model Evaluation =====")
print(f"MSE  : {mse:.4f}")
print(f"RMSE : {rmse:.4f}")
print(f"R2 Score : {r2:.4f}")

# ================================
# 13 - Actual vs Predicted Plot
# ================================
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Math Score")
plt.ylabel("Predicted Math Score")
plt.title("Actual vs Predicted Math Score")
plt.show()