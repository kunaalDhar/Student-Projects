import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
from datetime import date

warnings.filterwarnings("ignore")

# Load dataset
data = pd.read_csv("used_cars_data.csv")

# Basic inspection
print(data.head())
print(data.tail())
print(data.info())
print(data.shape)
print(data.nunique())

# Missing values
print(data.isnull().sum())
print((data.isnull().sum() / len(data)) * 100)

# Remove S.No column
data = data.drop(['S.No.'], axis=1)

# Create car age column
current_year = date.today().year
data['Car_Age'] = current_year - data['Year']

# Extract brand and model
data['Brand'] = data.Name.str.split().str.get(0)
data['Model'] = data.Name.str.split().str.get(1) + data.Name.str.split().str.get(2)

# Fix inconsistent brand names
data["Brand"].replace({
    "ISUZU": "Isuzu",
    "Mini": "Mini Cooper",
    "Land": "Land Rover"
}, inplace=True)

print(data.describe().T)
print(data.describe(include='all').T)

# Separate categorical and numerical columns
cat_cols = data.select_dtypes(include=['object']).columns
num_cols = data.select_dtypes(include=np.number).columns.tolist()

print("Categorical Variables:", cat_cols)
print("Numerical Variables:", num_cols)

# Distribution plots
for col in num_cols:
    print(col)
    print('Skew :', round(data[col].skew(), 2))

    plt.figure(figsize=(15,4))

    plt.subplot(1,2,1)
    data[col].hist(grid=False)

    plt.subplot(1,2,2)
    sns.boxplot(x=data[col])

    plt.show()

# Log transformation
def log_transform(data, cols):
    for col in cols:
        if (data[col] == 1.0).all():
            data[col + "_log"] = np.log(data[col] + 1)
        else:
            data[col + "_log"] = np.log(data[col])

log_transform(data, ['Kilometers_Driven','Price'])

sns.histplot(data["Kilometers_Driven_log"])
plt.show()

# Pairplot
sns.pairplot(data=data.drop(['Kilometers_Driven','Price'],axis=1))
plt.show()