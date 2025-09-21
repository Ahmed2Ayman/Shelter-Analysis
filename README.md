# Homelessness Shelter Occupancy Analysis Dashboard

<img width="683" height="368" alt="Shelter Dashboard " src="https://github.com/user-attachments/assets/85ca3be0-c0c5-42af-bce5-eb03cf6a5c90" />


## 📝 Project Overview

This project involved creating a comprehensive Power BI dashboard to analyze homelessness shelter data across various US cities. The primary goal was to identify trends in occupancy rates, understand demographic distributions, and provide actionable insights into shelter utilization.

## 🛠️ Tools & Technologies

-   **Data Transformation:** Python (Pandas)
-   **Data Storage:** Snowflake
-   **Data Modeling & Visualization:** Power BI
-   **Data Source:** CSV File (`homelessness_shelter_data.csv`)

## ✨ Key Features

-   **KPI Dashboard:** At-a-glance cards for key metrics like Total Occupancy, Overall Capacity, and Average Occupant Age.
-   **Trend Analysis:** A time-series chart showing occupancy rates and capacity over time.
-   **Geospatial Analysis:** A map visualizing occupied beds by state.
-   **Interactive Filtering:** Slicers to filter the entire dashboard by year, state, and season.
-   **Detailed View:** A table providing a granular look at each individual shelter's performance.

## ⚙️ Project Steps

1.  **Data Modeling:** Designed a star schema with one fact table (`fact_shelter_occupancy`) and four dimension tables (`dim_date`, `dim_shelter`, `dim_location`, `dim_season`).
2.  **ETL Process:** Developed a Python script to clean the raw CSV, transform the data to fit the star schema, and generate the final CSV files for loading.
3.  **Data Warehousing:** Loaded the transformed dimension and fact tables into a Snowflake data warehouse.
4.  **Dashboard Creation:** Connected Power BI to Snowflake, established relationships based on the star schema, and built all the visuals and interactive features.
