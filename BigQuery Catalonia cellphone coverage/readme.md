![Alt text](image.png)
## Catalonia Cellphone Coverage
This project is a cloud-based project that demonstrates end-to-end data processing, analysis, visualization and ML API skills using GCP services.

#### Inspiration 🍀
After diving into the essentials of cloud computing with Google's [Cloud Digital Leader Learning Path](https://cloud.google.com/learn/certification/cloud-digital-leader), I couldn't resist rolling up my sleeves and putting those newfound skills to the test in an exciting cloud-based project. The dataset also qualifies as bigdata with over +11M rows of data across 20 features, and having learned parallel computing with PySpark, this project is a great fit to combine these skills.

#### Dataset 🀄︎
The GenCat Mobile Coverage app, initiated by the Government of Catalonia, utilizes crowdsourced data collection via an Android app to assess the state of mobile network coverage in the region. The dataset, spans from 2015 to 2017, records citizens' data on coverage levels, operators (Movistar, Vodafone, Orange, Yoigo), network types (2G, 3G, 4G), and device locations. The data aims to analyze mobile coverage quality, filter data by technology, and identify areas needing improvement. 

The ultimate goal is to enhance the efficiency of basic services for the public. Identical datasets are hosted in BigQuery's US and EU regions, with recommended source citation provided by the Government of Catalonia.

[EU Region - Catalonia Mobile Coverage](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=catalonian_mobile_coverage_eu&t=mobile_data_2015_2017&page=table)

[US Region - Catalonia Mobile Coverage](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=catalonian_mobile_coverage&t=mobile_data_2015_2017&page=table)

Source: [Government of Catalonia. Digital Policies and Public Administration](https://analisi.transparenciacatalunya.cat/en/Ci-ncia-i-Tecnologia/Dades-recollides-per-l-aplicaci-Cobertura-M-bil-20/g9ma-vbt8)

`Disclaimer`: This is a public bigquery dataset and is usable under MIT open source license

#### Project Structure 
The key stages include:

1. Data Ingestion using BigQuery

    The data is hosted among many other publicly available datasets, so the ingestion process has been heavily covered for us. An automated set-up for notifications when the data is updated is placed so any needed amends can be made promtly.

2. Data Wrangling & Transformation using BigQuery SQL

    There are some questions we would like to ask our dataset and necessary reformatting to be conducted for consistent and reliable analytics. Consider this as an EDA but with BigQuery SQL. A fleshed out wrangling and exploratory process can be found in the [write up documentation](writeup.md)
3. Data Visualization via Looker Studio to share key insights
4. Automated Data Processing with Cloud Composer / Cloud Function to set-up continuous clean data flow and notification systems
5. ML component that implements a simple model with either BigQuery ML or Vertex AI

#### Results & Conclusion
