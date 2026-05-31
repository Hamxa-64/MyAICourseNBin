import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, LabelEncoder

path_to_file = 'adult.csv'
df = pd.read_csv(path_to_file, delimiter=',')

df.columns = df.columns.str.strip()
df = df.apply(lambda col: col.str.strip() if col.dtype == 'object' else col)

print("df.columns:", df.columns.tolist())

# Missing values
df.replace('?', np.nan, inplace=True)
df.dropna(inplace=True)
print("Shape after dropping:", df.shape)


ohe = OneHotEncoder(sparse_output=False)
workclass_encoded = ohe.fit_transform(df[['workclass']])
workclass_df = pd.DataFrame(
    workclass_encoded,
    columns=ohe.get_feature_names_out(['workclass']),
    index=df.index
)
df = pd.concat([df.drop('workclass', axis=1), workclass_df], axis=1)
print("Workclass done")

# ---- Education - OrdinalEncoder ----
categories_order = [[
    'Preschool', '1st-4th', '5th-6th', '7th-8th',
    '9th', '10th', '11th', '12th', 'HS-grad',
    'Some-college', 'Assoc-voc', 'Assoc-acdm',
    'Bachelors', 'Masters', 'Prof-school', 'Doctorate'
]]
oe = OrdinalEncoder(categories=categories_order)
df['education_ord'] = oe.fit_transform(df[['education']])
print("Education done ")
df.drop('education', axis=1, inplace=True)

ohe2 = OneHotEncoder(sparse_output=False)
maritalstatus_encoded = ohe2.fit_transform(df[['marital.status']])
maritalstatus_df = pd.DataFrame(
    maritalstatus_encoded,
    columns=ohe2.get_feature_names_out(['marital.status']),
    index=df.index
)
df = pd.concat([df.drop('marital.status', axis=1), maritalstatus_df], axis=1)
print("Marital.status done ")
print(df.filter(like='marital').head())


ohe3 = OneHotEncoder(sparse_output=False)
relationship_encoded = ohe3.fit_transform(df[['relationship']])
relationship_df = pd.DataFrame(
    relationship_encoded,
    columns=ohe3.get_feature_names_out(['relationship']),
    index=df.index
)
df = pd.concat([df.drop('relationship', axis=1), relationship_df], axis=1)
print("Relationship done")
print(df.filter(like='relationship').head())


ohe4 = OneHotEncoder(sparse_output=False)
race_encoded = ohe4.fit_transform(df[['race']])
race_df = pd.DataFrame(
    race_encoded,
    columns=ohe4.get_feature_names_out(['race']),
    index=df.index
)
df = pd.concat([df.drop('race', axis=1), race_df], axis=1)
print("Race done ")
print(df.filter(like='race').head())

ohe5 = OneHotEncoder(sparse_output=False)
sex_encoded = ohe5.fit_transform(df[['sex']])
sex_df = pd.DataFrame(
    sex_encoded,
    columns=ohe5.get_feature_names_out(['sex']),
    index=df.index
)
df = pd.concat([df.drop('sex', axis=1), sex_df], axis=1)
print(df.filter(like='sex').head())

ohe6 = OneHotEncoder(sparse_output=False)
nativecountry_encoded = ohe6.fit_transform(df[['native.country']])
nativecountry_df = pd.DataFrame(
    nativecountry_encoded,
    columns=ohe6.get_feature_names_out(['native.country']),
    index=df.index
)
df = pd.concat([df.drop('native.country', axis=1), nativecountry_df], axis=1)
print(df.filter(like='native.country').head())


ohe7 = OneHotEncoder(sparse_output=False)
occupation_encoded = ohe7.fit_transform(df[['occupation']])
occupation_df = pd.DataFrame(
    occupation_encoded,
    columns=ohe7.get_feature_names_out(['occupation']),
    index=df.index
)

df = pd.concat([df.drop('occupation', axis=1), occupation_df], axis=1)

print("Occupation done")
print(df.filter(like='occupation').head())

#label income applied labelencoding technique 
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()

df['income_encoded'] = le.fit_transform(df['income'])

print("Class labels mapping:", dict(zip(le.classes_, le.transform(le.classes_))))
print(df[['income', 'income_encoded']].head())

# Encode target
df['income_encoded'] = le.fit_transform(df['income'])


#countplot to check income imblance
plt.figure(figsize=(6,4))
sns.countplot(x='income', data=df)
plt.title('Income Distribution')
plt.xlabel('Income')
plt.ylabel('Count')
plt.show()

#boxplot
plt.figure(figsize=(6,4))
sns.boxplot(x='income', y='age', data=df)
plt.title('Age vs Income')
plt.xlabel('Income')
plt.ylabel('Age')
plt.show()

#heatmap 
plt.figure(figsize=(10,6))
sns.heatmap(df.drop(columns=['income']).corr(), cmap='coolwarm', annot=False)
plt.title('Correlation Heatmap')
plt.show()

# FINAL CHECK: ensure no object columns remain
print("Remaining object columns:", df.select_dtypes(include='object').columns)


# FEATURE & TARGET SEPARATION

# AFTER (correct) - exclude both income columns
feature_names = [col for col in df.columns if col not in ['income_encoded', 'income']]

X = df[feature_names].copy()
y = df['income_encoded'].copy()

print("NaN check:", X.isnull().sum().sum())
print("Shape:", X.shape)


# TRAIN TEST SPLIT
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.7, random_state=42
)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#models
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

Logireg = LogisticRegression(max_iter=1000, class_weight='balanced')
rand_for = RandomForestClassifier(random_state=42, class_weight='balanced')
Grad_bost = GradientBoostingClassifier()

#TRAINING
Logireg.fit(X_train, y_train)
rand_for.fit(X_train, y_train)
Grad_bost.fit(X_train, y_train)

#PREDICTIONS

Lr_preds = Logireg.predict(X_test)
rf_preds = rand_for.predict(X_test)
Gb_preds = Grad_bost.predict(X_test)

#METRICS

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

print("Logistic Regression Accuracy:", accuracy_score(y_test, Lr_preds))
print("Random Forest Accuracy:", accuracy_score(y_test, rf_preds))
print("Gradient Boosting Accuracy:", accuracy_score(y_test, Gb_preds))


print("Logistic Regression Report")
print(classification_report(y_test, Lr_preds))

print("Random Forest Report")
print(classification_report(y_test, rf_preds))

print("Gradient Boosting Report")
print(classification_report(y_test, Gb_preds))


plt.figure(figsize=(5,4))
sns.heatmap(confusion_matrix(y_test, rf_preds), annot=True, fmt='d', cmap='Blues')
plt.title('Random Forest Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# MODEL COMPARISON PLOT

models = ['Logistic Regression', 'Random Forest', 'Gradient Boosting']
accuracies = [
    accuracy_score(y_test, Lr_preds),
    accuracy_score(y_test, rf_preds),
    accuracy_score(y_test, Gb_preds)
]

plt.figure(figsize=(6,4))
sns.barplot(x=models, y=accuracies)
plt.title('Model Accuracy Comparison')
plt.ylabel('Accuracy')
plt.xlabel('Models')
plt.show()