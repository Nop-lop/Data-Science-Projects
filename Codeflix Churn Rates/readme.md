## Codeflix Churn Rate
A SQL project focussing on the churn rate for Codeflix, a video streaming start-up that is 4 months into launching.
As the data analyst, I am tasked by the management to look into subscription performance as main stakeholders are excited about our growth! 😊

----
#### Content
* [SCHEMA](#schema)
* [Technologies and Sources](#Technologies_and_Sources)
* [Presentation](#presentation)

----
### SCHEMA
The marketing team are particularly interested in how the churn rates compare between two `segment` users. The dataset provided contains the subsciprtion data for the distinct channels.

The SQL table, __`subscriptions`__ , is used to assess the churn and has 4 columns;

- `id` - A unique identifier for the subscriber
- `subscription_start` - The start date for the subscription
- `subscription_end` - The end date for the subscription
- `segment` - This identifies which segment the subscriber belongs to


__Note__: Codeflix requires a minimum subscription length of 31 days, so a user can never start and end their subscription in the same month

Database Schema
| name | type |
|:------|:------|
| id | INTEGER |
| subscription_start |	TEXT |
| subscription_end | TEXT |
| segment | INTEGER |
| Rows: 2000 | 

-> SQL queries are used to explore the data and calculate the churn rates of segments 30 and 70 between January and March, 2017

### Technologies and Sources
* SQL
* Microsoft Excel
* Canva

This project can be found on [Codecademy](https://www.codecademy.com/)'s Analyze Data with SQL course.

### Presentation

The SQL queries and their results have been attached to this repo. Here is a summary of the analysis [Codeflix Board.pdf](https://github.com/Nop-lop/Data-Science-Projects/files/10475778/Codeflix.Board.pdf)

