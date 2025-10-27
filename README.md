# UK YouTuber Sponsorship Analysis (2024)

An analysis of top UK YouTubers in 2024, identifying key influencers for marketing campaigns using data from Kaggle and the YouTube API, with visualizations in Power BI.

---

## Problem Statement

The Head of Marketing needs to identify the most influential UK-based YouTubers to collaborate with for marketing campaigns in 2024. Making data-driven decisions is crucial to maximize the effectiveness and return on investment (ROI) of these campaigns.

## Objective

The goal is to create a comprehensive analysis and an interactive dashboard that provides insights into the top UK YouTubers. The solution should identify top-performing channels based on metrics like subscriber count, total video views, and the total number of videos uploaded, enabling the marketing team to make informed decisions.

## Data Collection & Summary

This project utilizes a hybrid approach for data collection:

1.  **Initial Seeding:** A foundational dataset was sourced from Kaggle, containing a list of 100 top UK influencers.
2.  **Data Enrichment:** A Python script was developed to interact with the **YouTube Data API v3**. This script extracts the latest channel statistics (subscribers, total views, total videos) for the YouTubers identified in the initial dataset.
3.  **Combined Dataset:** The enriched data is combined into a single, clean CSV file (`youtube_data_from_python.csv`) which serves as the single source of truth for the analysis.

## Project Workflow

The project follows a structured workflow from data acquisition to final analysis:

1.  **Data Ingestion:** Combine the static Kaggle data with fresh data from the YouTube API.
2.  **Data Loading:** Import the cleaned CSV data into a SQL Server database.
3.  **Data Transformation & Quality Assurance:** In SQL Server, a view is created to transform the raw data into a clean, analysis-ready format. Data quality tests are performed to ensure accuracy and consistency (checking for row counts, column counts, data types, and duplicates).
4.  **Data Visualization:** The cleaned data is connected to Power BI to build an interactive dashboard. DAX measures are used to calculate key performance indicators (KPIs).
5.  **Analysis & Recommendation:** The dashboard and underlying data are used to identify top performers and provide strategic recommendations for marketing collaborations.

![Workflow](assets/images/kaggle_to_powerbi.gif)

## Key Insights (Data-Driven)

The analysis of **100** top UK YouTubers has revealed the following key figures:

*   **Top Channel by Subscribers:** **NoCopyrightSounds** leads the pack with **33,600,000** subscribers.
*   **Top Channel by Views:** **DanTDM** commands the highest viewership with **19,775,951,435** total views.
*   **Top Channel by Video Count:** **24 News HD** is the most prolific creator with **165,103** videos.

These insights are critical for identifying channels that offer the best potential for reach and engagement.

## Tools and Technologies

| Tool           | Purpose                                                    |
|----------------|------------------------------------------------------------|
| **Python**     | Data enrichment via the YouTube API (using `google-api-python-client`). |
| **SQL Server** | Data cleaning, transformation, and quality assurance.      |
| **Power BI**   | Building the interactive dashboard and data visualization. |
| **Git & GitHub**| Version control and project hosting.                       |

## Conclusion and Recommendations

The analysis indicates that different YouTubers offer different strengths. 
*   For maximum **subscriber reach**, `NoCopyrightSounds` is the top choice. 
*   For campaigns targeting the highest **eyeball count**, `DanTDM` is the clear leader. 
*   For partnerships requiring a high volume of content, `24 News HD` presents a unique opportunity.

It is recommended to align the choice of YouTuber with the specific goals of the marketing campaign (e.g., brand awareness vs. high-frequency product placement). This data-driven approach ensures that marketing efforts are targeted and effective.