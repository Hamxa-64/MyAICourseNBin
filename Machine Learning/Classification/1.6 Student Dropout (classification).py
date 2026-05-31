import pandas as pd
import numpy as np

path_to_file = 'studentdropout.csv'
df = pd.read_csv(path_to_file, delimiter=';')
print('df :', df)

print('df.head:  ', df.head())
print('df.tail:  ', df.tail())
print('df.describe :' , df.describe())
print('df.info:   ', df.info())
print('df.shape:  ', df.shape)

feature_names = [col for col in df.columns if col != 'Target']
 
X = df[feature_names].copy()
y = df["Target"].copy()
 
print("X:  ", X)
print("y:  ", y)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
 
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)
print(X_scaled[0])


from sklearn.model_selection import train_test_split


X_train_scaled, X_test_scaled, y_train, y_test = train_test_split(X_scaled,
                                                                   y,
                                                              train_size=.7,
                                                            random_state=25)
 
print(f"Train size: {round(len(X_train_scaled) / len(X) * 100)}% \n\
Test size: {round(len(X_test_scaled) / len(X) * 100)}%")

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

logistic_regression = LogisticRegression()
svm = SVC()
tree = DecisionTreeClassifier()
 
logistic_regression.fit(X_train_scaled, y_train)
svm.fit(X_train_scaled, y_train)
tree.fit(X_train_scaled, y_train)
 
log_reg_preds = logistic_regression.predict(X_test_scaled)
svm_preds = svm.predict(X_test_scaled)
tree_preds = tree.predict(X_test_scaled)

from sklearn.metrics import classification_report
 
model_preds = {
    "Logistic Regression": log_reg_preds,
    "Support Vector Machine": svm_preds,
    "Decision Tree": tree_preds
}
 
for model, preds in model_preds.items():
    print(f"{model} Results:\n{classification_report(y_test, preds)}", sep="\n\n")