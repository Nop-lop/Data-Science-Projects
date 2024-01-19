### Analyzing A/B Test Results for FarmBurg Upgrade Package Pricing

#### Description:

This repository contains code and analysis for determining the optimal price point for a FarmBurg upgrade package.

#### Key Steps:

1. Data Exploration:
Examined user data from an A/B test with three price points: $0.99, $1.99, and $4.99.
  ```{python}
    import pandas as pd
    
    # Read in the CSV file
    abdata = pd.read_csv('clicks.csv')
    
    # View the first few rows
    print(abdata.head())
```

2. Initial Chi-Square Test:
   Found significant differences in purchase rates, but a Chi-Square test wasn't the most appropriate approach for the business question.

    ```{python}
      from scipy.stats import chi2_contingency
  
      # Create a contingency table
      Xtab = pd.crosstab(abdata.group, abdata.is_purchase)
      print(Xtab)
  
      # Perform the chi-square test
      chi2, pval, dof, expected = chi2_contingency(Xtab)
      print('The pval for the chi-square test is', pval)
      
    ```

3. Reframing the Question:
   Focused on determining the price point that would generate a minimum revenue of $1,000 per week.

4. Calculating Necessary Purchase Rates:
   Determined the number of sales needed at each price point to meet the revenue target.
    ```
      num_visits = len(abdata)
      print('Total number of weekly visitors:', num_visits)
      
      # Calculate sales and proportions needed for each price point
      for price in [0.99, 1.99, 4.99]:
        num_sales_needed = np.ceil(1000 / price)
        sales_proportion = num_sales_needed / num_visits
        print(f'Proportion of weekly visitors needed for ${price:.2f} price: {sales_proportion:.4f}')
    ```

5. Binomial Tests:
   Conducted binomial tests to compare observed purchase rates in each group to the required purchase rates.
    ```
    from scipy.stats import binom_test

    # Conduct binomial tests for each group
    for group in ['A', 'B', 'C']:
      samp_size = len(abdata[abdata.group == group])
      sales = len(abdata[(abdata.group == group) & (abdata.is_purchase == 'Yes')])
      p_value = binom_test(sales, samp_size, p=sales_proportion, alternative='greater')
      print(f'The p-value for Group {group} binom test is: {p_value:.4f}')

    ```
   
6. Conclusion:
   Based on the results (p-value < 0.05 only for Group C), recommended charging $4.99 for the upgrade package.

7. Files:

- [clicks.csv](https://github.com/Nop-lop/Data-Science-Projects/blob/33c43071f1ddf1d3294ac6a5dc8be484b94e253f/Farmburg%20A%3AB%20test/clicks.csv)): Contains user data from the A/B test.
- [farmburg.py](https://github.com/Nop-lop/Data-Science-Projects/blob/33c43071f1ddf1d3294ac6a5dc8be484b94e253f/Farmburg%20A%3AB%20test/farmburg.py): Python code for conducting the analysis (including Chi-Square and binomial tests).

8. Dependencies:

- pandas
- scipy.stats

9. To Run the Analysis:
    - Install dependencies: pip install pandas scipy
    - Run the Python code: python farmburg.py

10. Additional Notes:
    Consider exploring other pricing strategies or conducting further tests to validate the findings.
