# Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

# Loading the penguins dataset from a CSV file
penguins_data = pd.read_csv('penguins.csv')

# Displaying the first few rows of the dataset
penguins_data.head()

# Displaying general information about the dataset, including column types and missing values
penguins_data.info()

# Checking the distribution of the target variable ('species')
penguins_data.species.value_counts()

# Checking for missing values in the dataset
penguins_data.isnull().sum()

# Filling missing values in numerical columns with the mean of each respective column
for column_name in penguins_data.select_dtypes(include='float', exclude='object'):
    penguins_data[column_name] = penguins_data[column_name].fillna(penguins_data[column_name].mean())

# Filling missing values in 'sex' column using forward fill method
penguins_data['sex'] = penguins_data['sex'].ffill()

# Creating a scatter plot to visualize the relationship between bill length and bill depth, colored by species
sns.scatterplot(x='bill_length_mm', y='bill_depth_mm', hue='species', data=penguins_data, style='species')

# Importing LabelEncoder to convert categorical features into numerical values
from sklearn.preprocessing import LabelEncoder

# Encoding 'sex' and 'island' columns into numerical values
label_encoder = LabelEncoder()
for col in ['sex', 'island']:
    penguins_data[col] = label_encoder.fit_transform(penguins_data[col])

# Importing StandardScaler to standardize the numerical features (scaling the data to mean=0, std=1)
from sklearn.preprocessing import StandardScaler

# Standardizing the selected numerical columns
scaler = StandardScaler()
for col in ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']:
    penguins_data[col] = scaler.fit_transform(penguins_data[[col]])

# Importing PCA (Principal Component Analysis) for dimensionality reduction
from sklearn.decomposition import PCA

# Separating features (X) and target variable (Y)
X = penguins_data.drop('species', axis=1)  # All columns except 'species'
Y = penguins_data['species']  # Target variable 'species'

# Applying PCA to reduce dimensions to 3 principal components
PCA_TR = PCA(n_components=3)
X_train = PCA_TR.fit_transform(X)

# Displaying the explained variance ratio of the 3 principal components
PCA_TR.explained_variance_ratio_

# Displaying the components (eigenvectors) for the first 3 principal components
PCA_TR.components_

# Creating a DataFrame to visualize the components and their contributions to each feature
pd.DataFrame(PCA_TR.components_, columns=X.columns, index=['PC-1', 'PC-2', 'PC-3'])

# Initializing various machine learning models for classification
LRM = LogisticRegression()
DTC = DecisionTreeClassifier()
RFC = RandomForestClassifier()
KNC = KNeighborsClassifier()
NBC = GaussianNB()

# Setting up StratifiedKFold cross-validation (10-fold, shuffling the data with a fixed random seed)
SKF = StratifiedKFold(n_splits=10, shuffle=True, random_state=10)

# Performing cross-validation on each model and printing the average accuracy score
print(f'LogisticRegression : {round(cross_val_score(LRM, X_train, Y, cv=SKF, scoring="accuracy").mean() * 100, 2)}%')
print(f'DecisionTreeClassifier : {round(cross_val_score(DTC, X_train, Y, cv=SKF, scoring="accuracy").mean() * 100, 2)}%')
print(f'RandomForestClassifier : {round(cross_val_score(RFC, X_train, Y, cv=SKF, scoring="accuracy").mean() * 100, 2)}%')
print(f'KNeighborsClassifier : {round(cross_val_score(KNC, X_train, Y, cv=SKF, scoring="accuracy").mean() * 100, 2)}%')
print(f'GaussianNB : {round(cross_val_score(NBC, X_train, Y, cv=SKF, scoring="accuracy").mean() * 100, 2)}%')
