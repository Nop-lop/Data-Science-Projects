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


<aside>
 Codeflix requires a minimum subscription length of 31 days, so a user can never start and end their subscription in the same month

</aside>

Database Schema
subscriptions
| name | type |
|:------|:------|
| page_name | TEXT |
| timestamp |	TEXT |
| user_id | INTEGER |
| utm_campaign | TEXT |
| utm_source|	TEXT |
| Rows: 5692 | 

-> SQL queries are used to explore the data and calculate top 5 campaigns with the highest % of purchases

### Technologies and Sources
* SQL
* Microsoft Excel
* Microsoft PowerPoint

This project can be found on [Codecademy](https://www.codecademy.com/)'s Analyze Data with SQL course.

### Presentation
The SQL queries, along with snapshots of the query results, can be found as attachments to this repository.The static version of the presentation is presented [here](https://github.com/Nop-lop/Data-Science-Projects/blob/e437f84b2ffaad10067f1da2b95b58ea8159b3a8/Market%20Attribution/Marketing%20Attribution.pdf)
