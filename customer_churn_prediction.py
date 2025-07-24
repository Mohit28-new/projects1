import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

df = pd.read_csv('customer_churn.csv')

df.head()

df = df.dropna()

df.info()

df.drop("customerID", axis=1, inplace=True)

df.describe()   
df['churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

x = df.drop(['churn', 'Churn'], axis =1)
y = df['churn']

numerical_features = x.select_dtypes(include=['int64', 'float64']).columns.tolist()
categorical_features = x.select_dtypes(include=['object']).columns.tolist()

numeric_pipeline = Pipeline([('scaler', StandardScaler())])
categorical_pipeline = Pipeline([('encoder', OneHotEncoder(handle_unknown='ignore'))])


preprocessing_pipeline = ColumnTransformer(transformers =[('num', numeric_pipeline, numerical_features),
    ('cat', categorical_pipeline, categorical_features)])


model = Pipeline([
    ('preprocessing', preprocessing_pipeline),  
    ('classifier', RandomForestClassifier(random_state=42))])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model.fit(x_train, y_train)

y_predict = model.predict(x_test)

accuracy = accuracy_score(y_test, y_predict)
conf_matrix = confusion_matrix(y_test, y_predict)
print(f"Accuracy: {accuracy}")
print("Confusion Matrix:")
print(conf_matrix)
print("Classification Report:")
print(classification_report(y_test, y_predict))
print(x.columns)


plt.figure(figsize=(10, 6))

sns.countplot(x='Churn', data=df)
plt.title("Churn Distribution")
plt.show()
