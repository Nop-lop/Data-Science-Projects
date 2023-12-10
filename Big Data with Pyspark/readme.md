# Analysing Common Crawl Data with Pyspark

In this project, I analyse a small portion of the dataset provided by [Common Crawl](https://commoncrawl.org/) using PySpark. The dataset I’ll be working with, the domain graph, contains a record of every domain on the internet and the count of subdomains associated with the site.

The general  web domain follows a format similar to the one shown here;
![Alt text](domainformats.svg) 

#### Common Crawl
The Common crawl is a non-profit organisation that crawls, archives, and analyzes content on all public websites. The Common Crawl maintains petabytes (thousands of terabytes!) of web content and insights derived from their analyses, all of which is made publicly available for research and educational purposes.

#### Analysis Process
1. Initialising Spark Session and Analysing common crawl data with Resilient Distributed Datasets (RDDs)
2. Inspect and Exploring Domains with PySpark dataframes and SQL
3. Reading and Writing our Dataset to Disk via Parquets
4. Querying Domains with PySpark Dataframes and SQL

#### Results
- Employ the prowess of PySpark DataFrames and SQL to wrangle over 2.5 million domain records, unearthing insights through adroit queries and data wrangling techniques.
- Leveraged PySpark's parallel computing capabilities to distribute data across multiple machine and significantly reducing processing times
- Eliminated over 95% of data inconsistencies, bolstering the quality of analyzed and aggregated data, ensuring consistent and realible analysis.
