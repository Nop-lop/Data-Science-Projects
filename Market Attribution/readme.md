## Market Attribution
A SQL project focussing on the market attribution and funnel of CoolTshirts

----
#### Content
* [Introduction](#introduction)
* [Technologies and Sources](#technology_and_Sources)
* [Presentation](#presentation)

----
### Introduction
<aside>
💡 CoolTShirts, is an innovative apparel shop, is running a bunch of marketing campaigns. In this project, I’ll be helping them assess and improve their marketing campaigns
</aside>

This project used data from the database, __*Page_visits*__ ,to assess the effectiveness of marketing campaigns.

The database has the following columns and used the schema that follows:

- `user_id` - A unique identifier for each visitor to a page
- `timestamp` - The time at which the visitor came to the page
- `page_name` - The title of the section of the page that was visited
- `utm_source` - Identifies which touchpoint sent the traffic (e.g. google, email, or facebook)
- `utm_medium` - Identifies what type of link was used (e.g. cost-per-click or email)
- `utm_campaign` - Identifies the specific ad or email blast (e.g. retargetting-ad or weekly-newsletter)

Database Schema
page_visits
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
The SQL queries, along with snapshots of the query results, can be found as attachments to this repository.The static version of the presentation is presented [here](https://github.com/Nop-lop/Data-Science-Projects/files/10421300/Marketing.Attribution.pdf))
