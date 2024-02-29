import numpy
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/workspaces/Data-Science-Projects/Predict Wine Quality with Regularization/wine_quality.csv")
print(df.head())

# assuming data is clean; correlation matrix to identify best regularization method
colors = sns.diverging_palette(150, 275, s=80, l=55, n=9, as_cmap=True)
sns.heatmap(df.corr(), center = 0, cmap=colors, robust=True)
plt.show()