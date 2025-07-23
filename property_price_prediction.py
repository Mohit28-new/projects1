import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, root_mean_squared_error

df = pd.read_csv('data_file.csv')

df.head()

df = df.dropna()

df.info()

df.describe()

x = df.drop('median_house_value', axis=1)
y = df['median_house_value']

num_features = x.select_dtypes(include = ['int64', 'float64']).columns.tolist()
cat_features = x.select_dtypes(include = ['object','bool']).columns.tolist()

numeric_pipeline = Pipeline([('scaler', StandardScaler())])

categorical_pipeline = Pipeline([('encoder', OneHotEncoder(handle_unknown='ignore'))])

prepossing_pipeline = ColumnTransformer([('num',numeric_pipeline, num_features),
                                         ('cat',categorical_pipeline, cat_features)])

model = Pipeline([('preprocessing', prepossing_pipeline),('regrssion', LinearRegression())])

x_train, x_test, y_train, y_test =train_test_split(x,y, test_size = 0.2, random_state= 42)

model.fit(x_train, y_train)

y_predict = model.predict(x_test)

mae = mean_absolute_error(y_test,y_predict)
mse = root_mean_squared_error(y_test, y_predict)
rmse= np.sqrt(mse)
r2 = r2_score(y_test, y_predict)

print(f"mean absolute error: {mae}")
print(f"mean squared error:{mse}")
print(f"root mean squared error: {rmse}")
print(f"r2 score:{r2}")

plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_predict)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted Values')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
plt.show()