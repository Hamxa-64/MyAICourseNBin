import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

path_to_file = 'Recipe Reviews and User Feedback Dataset.csv'
df = pd.read_csv(path_to_file, delimiter=',')
print("df : ",  df)
print("Head:  ", df.head())
print("shape: ", df.shape)
print("columns :", df.columns)
print("info :", df.info)
print("descibe :", df.describe())
print("Tail :", df.tail())

#catplot
sns.catplot(x='stars', data=df, kind='count')

plt.title("Distribution of Ratings (Stars)")
plt.show()

#count plot 
plt.figure(figsize=(6,4))
sns.countplot(x='stars', data=df)

plt.title("Distribution of Ratings (Stars)")
plt.xlabel("Stars")
plt.ylabel("Count")

plt.show()

# Drop useless + text columns pehle
df = df.drop(columns=['Unnamed: 0','comment_id','user_id','recipe_code','recipe_name','user_name','text'])

# Feature selection (same style)
feature_names = [col for col in df.columns if col != 'stars']

# Define X and y
X = df[feature_names].copy()
y = df['stars'].copy()

print("X:  ", X)
print("y:  ", y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.7, random_state=42
)

from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression


rand_for = RandomForestClassifier()
Grad_bost = GradientBoostingClassifier()
Logireg = LogisticRegression(max_iter=1000)


rand_for.fit(X_train,y_train)
Grad_bost.fit(X_train, y_train)
Logireg.fit(X_train, y_train)


rf_preds = rand_for.predict(X_test)
Gb_preds = Grad_bost.predict(X_test)
Lr_preds = Logireg.predict(X_test)

from sklearn.metrics import accuracy_score

print("Random Forest Accuracy:", accuracy_score(y_test, rf_preds))
print("Gradient Booster Accuracy:", accuracy_score(y_test, Gb_preds))
print("Logistic regression Accuracy:", accuracy_score(y_test, Lr_preds))
