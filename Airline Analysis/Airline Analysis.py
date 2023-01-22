# -*- coding: utf-8 -*-

# -- Sheet --

# # 🛩 Airline Analysis


# In this project, I'll take on the role of a Data Scientist that works for a travel agency and needs to know the ins and outs of airline prices for our clients. I want to make sure that I can find the best deal for our clients and help them to understand how airline prices change based on different factors.
# 
# I will look into my favorite airline. The data include:
# - `miles`: miles traveled through the flight
# - `passengers`: number of passengers on the flight
# - `delay`: take-off delay in minutes
# - `inflight_meal`: is there a meal included in the flight?
# - `inflight_entertainment`: are there free entertainment systems for each seat?
# - `inflight_wifi`: is there complimentary wifi on the flight?
# - `day_of_week`: day of the week of the flight
# - `weekend`: did this flight take place on a weekend?
# - `coach_price`: the average price paid for a coach ticket
# - `firstclass_price`: the average price paid for first-class seats
# - `hours`: how many hours the flight took
# - `redeye`: was this flight a redeye (overnight)?
# 
# In this project, I'll explore a dataset for the first time and get to know each of the features. The goal is simply to explore and get to know the data using whatever methods come to mind.


# ### Loading Data & Data Summary


import pandas as pd
import numpy as np

# Read in Data
flight = pd.read_csv("flight.csv")
print(flight.head(10))

# data summary
print(f'Shape of the dataframe = {flight.shape}')
print(f'The dataset has {flight.shape[0]} rows and {flight.shape[1]} columns')

# Checking for any null values
col_is_null = flight.isnull().sum()
print(f'Columns with their corresponding count of null values :{col_is_null}')
# No null values found

# Checking data type of every column
print(flight.dtypes)

# Checking the 7 point stats for the dataset
flight.describe()

# The mean of the miles is higher than the median while Passengers, Delay, First Class Price and Hours are below the median.

# These features prima facie seem to have outliers

# # Uni-variate Analysis
# 
# We are going to look at individual variables for a better inspection
# 
# 1. What do coach ticket prices look like? What are the high and low values? What would be considered the average? Does $500 seem like a good price for a coach ticket?
#    
# 2. What do coach ticket prices for flights over 8 hrs long look like? What are the high, low, and average prices for 8-hour-long flights? Does a \$500 ticket seem more reasonable than before?
#    
# 3. How are flight delay times distributed? Let’s say there is a short amount of time between two connecting flights, and a flight delay would put the client at risk of missing their connecting flight. You want to better understand how often there are large delays so you can correctly set up connecting flights. What kinds of delays are typical?
# 
# __Note__: From the `.describe()` results, delays have a mean value of 13 mins, with a maximum of 1560 mins, which is an extreme outlier and disorients our plot. We can look at a delay plot with delays < 500 mins. Check the delay boxplot to see the outliers


import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(21,21))
#subplot 1: Coach prices
plt.subplot(3,2,1)
sns.histplot(flight.coach_price, color = 'blue')
plt.axvline(flight.coach_price.mean(),color='black')
plt.title('Coach prices')

# subplot 2: Boxplot for coach prices
plt.subplot(3,2,2)
sns.boxplot(flight['coach_price'], color = 'blue')
plt.title('Coach prices')

# Subplot 3: Coach prices for 8hr flights
plt.subplot(3,2,3)
sns.histplot(flight.coach_price[flight.hours == 8], color = 'green')
hr_mean = np.mean(flight.coach_price[flight.hours == 8])
plt.axvline(hr_mean,color='red')
plt.title('Coach prices for 8hr flights')

# Subplot 4: Coach prices for 8hr long flights
plt.subplot(3,2,4)
sns.boxplot(flight.coach_price[flight.hours == 8], color = 'green')
plt.title('Coach prices for 8hr flights')

#subplot 5: boxplot for coach prices of 8hr flights
plt.subplot(3,2,5)
sns.histplot(flight.delay[flight.delay <= 500], color = 'red')
plt.axvline(flight.delay.mean(), color = 'purple')
plt.title('Flight delays under 500 mins')

# Subplot 6: Box plot for flight delays
plt.subplot(3,2,6)
sns.boxplot(flight.delay[flight.delay <= 500], color = 'red')
plt.title('Flight delays under 500 mins')

plt.show()
plt.clf()

# ## Bivariate Analysis
# 
# 1. Let's explore the relationship between coach and first-class prices of each flight. Do flights with higher coach prices always have higher first-class prices as well?
# 2. What about the relationship between coach prices and inflight features - inflight mean, entertainment and WiFi? Which features are associated with the highest increase in price?
# 3. How does the number of passengers change in relation to the length of flights?


# Scatterplot: first class prices vs coach regression model
plt.figure(figsize=(10,8))
sns.lmplot(data = flight, x= 'coach_price', y= 'firstclass_price', line_kws={'color':'red'})
plt.title('First class vs Coach prices')

plt.show()
plt.clf()

# Histogram: Coach prices vs inflight features scatter plot with hues for features
plt.figure(figsize=(15,6))
plt.subplot(1,3,1)
sns.histplot(data = flight, x=flight.coach_price, hue = 'inflight_entertainment')

plt.subplot(1,3,2)
sns.histplot(data = flight, x=flight.coach_price, hue = 'inflight_meal')

plt.subplot(1,3,3)
sns.histplot(data = flight, x=flight.coach_price, hue = 'inflight_wifi')

plt.show()
plt.clf()

# Displot: No of passengers vs flight length
plt.figure(figsize=(10,8))
sns.displot(data = flight, y = 'passengers', x = 'hours', color='purple')
plt.show()

# ## Multivariate Analysis
# 1. We are going to analyse the relationship between coach and first-class prices on weekends compared to weekdays
# 2. How do coach prices differ for redeyes vs non-redeyes on each day of the week?
# 3. 


# coach prices vs first-class on weekends vs weekdays
plt.figure(figsize=(10,8))
sns.scatterplot(data = flight, y = 'firstclass_price', x = 'coach_price', hue='weekend')
plt.show()
plt.clf()

# coach prices variation in overnight flights over the week
plt.figure(figsize=(10,8))
sns.violinplot(data = flight, y = 'redeye', x = 'coach_price', hue='weekend', split = True , color='green')
plt.show()
plt.clf()

