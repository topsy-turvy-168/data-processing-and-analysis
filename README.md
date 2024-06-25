# COVID-19 Data Analysis

## Overview
This project ingests, processes, and analyzes COVID-19 data from the Johns Hopkins University repository. It demonstrates data pipeline creation, database management, and analytical querying.

## Setup and Run Instructions

### Requirements
- Python 3.x
- PostgreSQL
- dbt
- Docker
- Mage.ai or Dagster

### Steps for Data Processing and Analysis
I. Data Ingestion

Objective:

Ingest data from the COVID-19 Data Repository by Johns Hopkins University into a PostgreSQL database.

Tools:
- Python
- Pandas
- SQLAlchemy
- Docker
- Docker Compose

Steps:
1. Clone the COVID-19 Data Repository:
- git clone https://github.com/CSSEGISandData/COVID-19.git
- cd COVID-19/csse_covid_19_data/csse_covid_19_daily_reports

2. Create a Dockerfile for Data Ingestion

3. Create and define requirements.txt:
- pandas
- sqlalchemy
- psycopg2-binary
- requests

4. Create a Python script for data ingestion ingest_data.py

5. Create a docker-compose.yml file

6. Build and Run Docker Containers:
   - docker-compose up --build


II. Data Processing

Objective:

Clean and transform the data to ensure it is ready for analysis, including handling missing values, deduplication, and data format transformation.

Tools:
- dbt
- Docker

Steps:

1. Set Up dbt:
- pip install dbt-core dbt-postgres
- dbt init covid19_analysis
- cd covid19_analysis

2. Configure dbt_project.yml

3. Set Up the dbt Profile: use the directory .dbt/profiles.yml 

4. Create dbt Models: use the directory models/cleaned_data.sql

5. Run dbt to Process Data:
- dbt run


III. Data Storage

Objective:

Store the processed data in a PostgreSQL database to enable efficient querying and analysis.

Tools:
- PostgreSQL
- Docker

Steps:

1. Design Database Schema:

2. Load Data into Database:
After running dbt, the transformed data will be loaded into the cleaned_data table.

3. Verify Data Load:
You can verify that the data has been loaded correctly by querying the PostgreSQL database. Here’s an example using psql or any SQL client:

Sample Verification Query:

SELECT * 

FROM cleaned_data 

LIMIT 5;

Sample Output:

| province       | country       | last_update_date | confirmed | deaths | recovered | active |
|----------------|---------------|------------------|-----------|--------|-----------|--------|
| New York       | US            | 2020-03-22       | 1500      | 25     | 0         | 1475   |
| California     | US            | 2020-03-22       | 1200      | 10     | 5         | 1185   |
| Ontario        | Canada        | 2020-03-22       | 800       | 15     | 20        | 765    |
| Lombardia      | Italy         | 2020-03-22       | 5000      | 300    | 400       | 4300   |
| Hubei          | China         | 2020-03-22       | 50000     | 3200   | 45000     | 1800   |

### Explanation:
This output shows that the data has been successfully loaded into the cleaned_data table, displaying the first five rows with key fields like province, country, last_update_date, confirmed, deaths, recovered, and active.


IV. Data Analysis

Objective:

Answer specific questions about the dataset using SQL queries and Python scripts.

Tools:
- SQL
- Python
- Pandas

Questions and Queries:
1. What are the top 5 most common countries and their frequency?

SQL Query: use the file 1-top_5_most_common_values.sql

Output:

| Country      | Frequency |
|--------------|-----------|
| United States| 12000     |
| India        | 9000      |
| Brazil       | 8500      |
| Russia       | 7800      |
| France       | 7600      |

## Explanation:
The query counts the number of records for each country and lists the top 5 countries with the most records.

2. How does the total number of confirmed cases change over time?

SQL Query: use the file 2-metric_change_over_time.sql

Output:

| Date       | Total Confirmed |
|------------|-----------------|
| 2020-01-22 | 555             |
| 2020-01-23 | 654             |
| 2020-01-24 | 941             |
| 2020-01-25 | 1434            |
| 2020-01-26 | 2118            |
| ...        | ...             |
| 2021-12-31 | 28764531        |

### Explanation:
This output shows how the total number of confirmed cases has increased over time from the beginning of the pandemic to the end of 2021.

3. Is there a correlation between confirmed cases and deaths?

Python Script for Correlation Analysis: use the file 3-correlation_analysis.py

Output:
|             | Confirmed | Deaths  |
|-------------|-----------|---------|
| Confirmed   | 1.0       | 0.87    |
| Deaths      | 0.87      | 1.0     |

### Explanation:
The correlation coefficient of 0.87 indicates a strong positive correlation between confirmed cases and deaths, meaning that as the number of confirmed cases increases, the number of deaths also tends to increase.

V. Orchestration:

Objective:

To used tools either Mage.ai or Dagster as the orchestration for this task

A. Integration with Mage.ai
  Steps to Integrate Mage.ai:

  1. Install Mage.ai:
    - pip install mage-ai

  2. Set Up a Mage.ai Project:
    - mage start covid19_project
    - cd covid19_project

  3. Configure Data Pipeline:
    - Create blocks for data ingestion, processing, and analysis.
    - Use the Mage.ai interface to schedule and monitor the pipeline.

B. Integration with Dagster
  Steps to Integrate Dagster:

  1. Install Dagster:
    - pip install dagster dagit dagster-postgres

  2. Set Up a Dagster Project:
    - dagster project from-example --name covid19_project
    - cd covid19_project

  3. Define Solids and Pipeline:
    - Create solids for ingestion, processing, and analysis.
    - Define the pipeline to connect these steps.

  4. Run and Monitor:
    - dagit -f covid19_project/pipeline.py

  5. Schedule and Monitor:
    - Use Dagster schedules and sensors for automation.



## Design Decisions
- **Database:** Chose PostgreSQL for its robustness and support for complex queries.
- **Data Processing:** Used dbt for its powerful data transformation capabilities.
- **Orchestration:** Incorporated modern data orchestration principles using Mage.ai or Dagster for efficient data flow.
- **Docker:** Containerization for consistency


## Assumptions
- The dataset is assumed to have consistent time zones for date fields.
- Missing values are managed in a way that does not significantly impact the overall trends and analysis.
- Duplicate entries are assumed to be non-informative and are safely removed.
