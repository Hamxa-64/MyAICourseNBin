import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


path_to_file = 'data-2.csv'
df = pd.read_csv(path_to_file, delimiter=',')
print("df:  ", df)
print("df.head : ", df.head())
print("df.shape :", df.shape)
print("df.describe :", df.describe())
print("df.info: ", df.info)
print("df.columns: ", df.columns)


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['diagnosis_encoded'] = le.fit_transform(df['diagnosis'])

print("diagnosis labels mapping:", dict(zip(le.classes_, le.transform(le.classes_))))
print(df[['diagnosis', 'diagnosis_encoded']].head())

df = df.drop('diagnosis', axis=1)

#plots 
variables = ["id","radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean","compactness_mean","concavity_mean","concave points_mean","symmetry_mean","fractal_dimension_mean","radius_se","texture_se","perimeter_se","area_se","smoothness_se","compactness_se","concavity_se","concave points_se","symmetry_se","fractal_dimension_se","radius_worst","texture_worst","perimeter_worst","area_worst","smoothness_worst","compactness_worst","concavity_worst","concave points_worst","symmetry_worst","fractal_dimension_worst"]
for var in variables:
    plt.figure()
    sns.scatterplot(x= var, y= 'diagnosis_encoded', data=df, hue= 'diagnosis_encoded')
    plt.title(f'classification plot of {var} and diagnosis')
    plt.show()

sns.heatmap(df.corr(), cmap='coolwarm')
plt.show()


df = df.drop(columns=['Unnamed: 32'], errors='ignore')


feature_names = [col for col in df.columns if col != 'diagnosis_encoded']

X = df[feature_names].copy()
y = df['diagnosis_encoded'].copy()

print("NaN check:", X.isnull().sum().sum())  
print("Shape:", X.shape)                     

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.7, random_state=42
)

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier


Logireg = LogisticRegression(max_iter=1000)
rand_for = RandomForestClassifier()
Grad_bost = GradientBoostingClassifier()


Logireg.fit(X_train, y_train)
rand_for.fit(X_train,y_train)
Grad_bost.fit(X_train, y_train)

Lr_preds = Logireg.predict(X_test)
rf_preds = rand_for.predict(X_test)
Gb_preds = Grad_bost.predict(X_test)

from sklearn.metrics import accuracy_score

print("Logistic regression Accuracy:", accuracy_score(y_test, Lr_preds))
print("Random Forest Accuracy:", accuracy_score(y_test, rf_preds))
print("Gradient Booster Accuracy:", accuracy_score(y_test, Gb_preds))


models = ['Logistic Regression', 'Random Forest', 'Gradient Boosting']
accuracies = [
    accuracy_score(y_test, Lr_preds),
    accuracy_score(y_test, rf_preds),
    accuracy_score(y_test, Gb_preds)
]

plt.figure()
sns.barplot(x=models, y=accuracies)
plt.title('Model Accuracy Comparison')
plt.ylabel('Accuracy')
plt.show()