import numpy as np
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
plt.clf()

#2. Data Transformation: Standardized scaler
#print(df.describe())
from sklearn.preprocessing import StandardScaler
ssfit = StandardScaler().fit(features)
X = ssfit.transform(features)

# 3. Train-test split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 99)

# 4. Fitting a Logistic Regression model without regularization
from sklearn.linear_model import LogisticRegression
clf_no_reg = LogisticRegression(penalty = None)
clf_no_reg.fit(x_train, y_train)

# 5. Plotting coefficients vs. features
predictors = features.columns
coefficients = clf_no_reg.coef_.ravel()
coef = pd.Series(coefficients,predictors).sort_values()
coef.plot(kind='bar', title = 'Coefficients (no regularization)')
plt.tight_layout()
plt.show()
plt.clf()

# 6. Train and Test performance
from sklearn.metrics import f1_score
pred_train = clf_no_reg.predict(x_train)
pred_test = clf_no_reg.predict(x_test)
print('Training Score ',f1_score(y_train, pred_train))
print('Testing Score', f1_score(y_test, pred_test))

# 7. & 8. Fit the model with default Ridge Regularization and get scores
clf_default = LogisticRegression()
clf_default.fit(x_train, y_train)

y_pred_train = clf_default.predict(x_train)
y_pred_test = clf_default.predict(x_test)
print('Training Score with Ridge reg. ',f1_score(y_train, y_pred_train))
print('Testing Score with Ridge reg.', f1_score(y_test, y_pred_test))

''' No significant differences in scores between No-Regularization and Regularized models
Increasing regularization effect by increasing alpha hyperparam, or for sklean decreasing C, is best.
How far down do we go? We try a coarse grained search'''

# 9. Coarse grained hyperparameter tuning
training_array = []
test_array = []
C_array = [0.0001, 0.001, 0.01, 0.1, 1]
for c_val in C_array:
  clf = LogisticRegression(C = c_val)
  clf.fit(x_train, y_train)
  y_pred_trains = clf.predict(x_train)
  y_pred_tests = clf.predict(x_test)
  training_array.append(f1_score(y_train, y_pred_trains))
  test_array.append(f1_score(y_test, y_pred_tests))

# 10. Plotting train and test scores as a function of C
plt.plot(C_array,training_array)
plt.plot(C_array,test_array)
plt.xscale('log')
plt.ylabel('F1 Scores')
plt.xlabel('C values')
plt.legend()
plt.show()
plt.clf()

# From the interactive plot we can see that the optimal c-value is around 0.001; a fine
# grained search of 100 values between 0.0001 and 0.01 isn't a bad starting point

# 11. Fine Grained hyperparameter tuning with GridSearch CV
c_array = np.logspace(-4,-2,100)
tuning_C = {'C': c_array}

from sklearn.model_selection import GridSearchCV
clf_gs = LogisticRegression()
gs = GridSearchCV(estimator = clf_gs, param_grid = tuning_C, scoring = 'f1', cv = 5)
gs.fit(x_train, y_train)

# 12. Optimal C-value and its associated score
print(gs.best_params_, gs.best_score_)

# 13. Using this optimal C-value on our test data set to obtain its f1 score
clf_best_ridge = LogisticRegression(C = gs.best_params_['C'])
clf_best_ridge.fit(x_train, y_train)
y_best_pred = clf_best_ridge.predict(x_test)
print('Optimal ridge reg. f1 score', f1_score(y_test, y_best_pred))

# Going back to our correlation matrix; we could see that the variable pairs fixed_Acidity and 
# citric acid and density and fixed_acidity are highly correlated. This suggests the model might
# benefit from l1 regularization for feature selection


# 14. Implementing L1 Regularization with Hyperparameter tuning
from sklearn.linear_model import LogisticRegressionCV

cval_arr = np.logspace(-2, 2, 100)
for cval in cval_arr:
  clf_l1 = LogisticRegressionCV(Cs=cval, cv = 5, penalty = 'l1', scoring = 'f1', solver='liblinear')

## 15. Optimal C value and corresponding coefficients
print('Best C value', clf_l1.Cs_)
print('Best fit coefficients', clf_l1.coef_)


## 16. Plotting the tuned L1 coefficients
coefficients = clf_l1.coef_.ravel()
coef = pd.Series(coefficients,predictors).sort_values()

plt.figure(figsize = (12,8))
coef.plot(kind='bar', title = 'Coefficients for tuned L1')
plt.tight_layout()
plt.show()
plt.clf()
