import numpy
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/workspaces/Data-Science-Projects/Predict Wine Quality with Regularization/wine_quality.csv")
#print(df.head())
y = df['quality']
features = df.drop(columns = ['quality'])


# 1. correlation matrix to identify best regularization method
colors = sns.diverging_palette(150, 275, s=80, l=55, n=9, as_cmap=True)
sns.heatmap(df.corr(), center = 0, cmap=colors, robust=True)
plt.show()

#2. Data Transformation: Standardized scaler
#print(df.describe())
from sklearn.preprocessing import StandardScaler
ssfit = StandardScaler().fit(features)
X = ssfit.transform(features)

# 3. Train-test split
from sklearn.model_selection import train_test_split
