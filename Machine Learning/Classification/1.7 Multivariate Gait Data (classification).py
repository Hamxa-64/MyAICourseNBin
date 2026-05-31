import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
path_to_file = 'gait.csv'
df = pd.read_csv(path_to_file)

#  Basic info
print('Head: ', df.head())
print('Shape:', df.shape)
print('Columns:', df.columns)

#seaborn graph
plt.figure(figsize=(6,4))
sns.boxplot(x='condition', y='angle', data=df)

plt.title("Joint Angle Distribution across Conditions")
plt.xlabel("Walking Condition")
plt.ylabel("Angle")

plt.show()

# Define features and target
# (condition is target)
feature_names = [col for col in df.columns if col != 'condition']

X = df[feature_names].copy()
y = df['condition'].copy()

print("X shape:", X.shape)
print("y shape:", y.shape)

# Train-test split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.8, random_state=42
)

# Import models
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC

# Initialize models
random_forest = RandomForestClassifier()
svm = SVC()
gradient_boosting = GradientBoostingClassifier()

#  Train models
random_forest.fit(X_train, y_train)
svm.fit(X_train, y_train)
gradient_boosting.fit(X_train, y_train)

# Predictions
rf_preds = random_forest.predict(X_test)
svm_preds = svm.predict(X_test)
gb_preds = gradient_boosting.predict(X_test)

# Accuracy
from sklearn.metrics import accuracy_score

print("\n--- Model Accuracies ---")
print("Random Forest Accuracy:", accuracy_score(y_test, rf_preds))
print("SVM Accuracy:", accuracy_score(y_test, svm_preds))
print("Gradient Boosting Accuracy:", accuracy_score(y_test, gb_preds))