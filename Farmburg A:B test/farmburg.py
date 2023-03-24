# Import libraries
import codecademylib3
import pandas as pd
import numpy as np

# Read in the  file as 
abdata = pd.read_csv('clicks.csv')
print(abdata.head())

Xtab = pd.crosstab(abdata.group,abdata.is_purchase)
print(Xtab)

# all groups have 1666 users, with Group A having the highest purchase count and proportion

#chi-square test
from scipy.stats import chi2_contingency
chi2, pval, dof, expected = chi2_contingency(Xtab)
print('The pval for the chi-square test is',pval)
# at 0.05 sig-threshold, test is significant

num_visits = len(abdata)
print('Total number of weekly visitors:',num_visits)

#group A subscriptions
num_sales_needed_099 = np.ceil(1000/0.99)
print('No of $0.99 sales needed:',num_sales_needed_099)

p_sales_needed099 = num_sales_needed_099/num_visits
print('Proportion of weekly visitors needed to make  revenue, from group A ($0.99) subscription:',p_sales_needed099)

#group B subscriptions
num_sales_needed_199 = np.ceil(1000/1.99)
print('No of $1.99 sales needed:',num_sales_needed_199)

p_sales_needed_199 = num_sales_needed_199/num_visits
print('Proportion of weekly visitors needed to make  revenue, from group B ($1.99) subscription:',p_sales_needed_199)

#group C subscriptions
num_sales_needed_499 = np.ceil(1000/4.99)
print('No of $4.99 sales needed:',num_sales_needed_499)

p_sales_needed_499 = num_sales_needed_499/num_visits
print('Proportion of weekly visitors needed to make  revenue, from group C ($4.99) subscription:',p_sales_needed_499)

# Binom test for Group A
from scipy.stats import binom_test
samp_size099 = len(abdata[abdata.group=='A'])
sales_099 = len(abdata[(abdata.group=='A')&(abdata.is_purchase=='Yes')])
# you can also use: np.sum(abdata.group=='A') for samp_size099

# null hypothesis is equal to sales needed, alternative = '>'
pvalueA = binom_test(sales_099,samp_size099,p=p_sales_needed099, alternative = 'greater')
print('The p-value for Group A binom test is:',pvalueA)

# Binom test for Group B
from scipy.stats import binom_test
samp_size199 = len(abdata[abdata.group=='B'])
sales_199 = len(abdata[(abdata.group=='B')&(abdata.is_purchase=='Yes')])

# null hypothesis is equal to sales needed, alternative = '>'
pvalueB = binom_test(sales_199,samp_size199,p=p_sales_needed_199, alternative = 'greater')
print('The p-value for Group B binom test is:',pvalueB)

# Binom test for Group C
from scipy.stats import binom_test
samp_size499 = len(abdata[abdata.group=='C'])
sales_499 = len(abdata[(abdata.group=='C')&(abdata.is_purchase=='Yes')])

# null hypothesis is equal to sales needed, alternative = '>'
pvalueC = binom_test(sales_499,samp_size499,p=p_sales_needed_499, alternative = 'greater')
print('The p-value for Group C binom test is:',pvalueC)
 
