## Predicting Wine Quality with Regularization

The data we're working with is from the Wine Quality Dataset in the UCI Machine Learning Repository. We’re looking at the red wine data in particular and while the original dataset has a 1-10 rating for each wine, we’ve made it a classification problem with a wine quality of good (>5 rating) or bad (<=5 rating).

The goals of this project are to:

1. Implement different logistic regression classifiers
2. Find the best ridge-regularized classifier using hyperparameter tuning
3. Implement a tuned lasso-regularized feature selection method

### Main Features
- 11 input variables (based on physicochemical tests):
`fixed acidity`, `volatile acidity`, `citric acid`, `residual sugar`, `chlorides`, `free sulfur dioxide`, `total sulfur dioxide`, `density`, `pH`, `sulphates` and `alcohol`.

- An output variable, `quality` (0 for bad and 1 for good)
