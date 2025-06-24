<<<<<<< HEAD
# 📊 U.S. Data Job Market Analysis (2022–2025)


[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white&style=for-the-badge)]
[![Pandas](https://img.shields.io/badge/Pandas-1.5.0-lightgray?logo=pandas&logoColor=white&style=for-the-badge)]
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-white?logo=matplotlib&logoColor=black&style=for-the-badge)]
[![SciPy](https://img.shields.io/badge/SciPy-1.x-blue?logo=scipy&logoColor=white&style=for-the-badge)]

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)

[![CI Pipeline](https://github.com/ElisabethDi/US-Job_Market_Analysis-2022_to_2025/actions/workflows/ci.yml/badge.svg)](https://github.com/ElisabethDi/US-Job_Market_Analysis-2022_to_2025/actions/workflows/ci.yml)













This project provides a thorough analysis of U.S. data job listings from 2022 to 2025, offering valuable insights into the data job market, including job locations, remote-work trends, employment type,job platform, salary distributions and skill trends for Data Analyst, Data Engineer, and Data Scientist roles.

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Dataset Information](#dataset-information)  
3. [Tools & Technologies](#tools--technologies-used)  
4. [Analysis Sections](#analysis-sections)  
   - [Data Cleaning](#1-data-cleaning)  
   - [Top Locations – Data Positions (2022–2025)](#2-job-locations-2022–2025)  
   - [Remote Work Trends (2022–2025)](#3-remote-work-trends-2022–2025) 
   - [Remote vs On-site Salary (Analyst Roles)](#4-median-analyst-salary-by-seniority--remote-status-2022–2025)  
   - [Employment Type Distribution (2022–2025)](#5-employment-type-distribution-2022–2025) 
   - [Top Job Boards – Analyst Salaries (2022–2025)](#6-top-job-boards-for-analyst-positions-2022–2025)  
   - [Top 5 In‑Demand Skills (2022–2025)](#7-top-5-in-demand-skills-for-data-positions-2022–2025)  
   - [Trending Skills (Monthly Trends)](#8-trending-in-demand-skills-monthly)  
   - [Salary Distribution Across Roles (2022–2025)](#9-salary-distribution-across-data-roles-2022–2025)  
   - [Salary vs Skills – Analyst Positions](#10-highest-paid-and-most-in-demand-skills-for-analyst-positions)  
   - [Analyst Proficiency Skills](#11-most-valuable-skills-for-analysts-2022–2025)  
5. [Final Summary & Key Takeaways](#final-summary--key-takeaways)  



## 📌 Project Overview
This project includes:

- **Data Cleaning & Preparation** 

    - standardized and sanitized raw job listings.

- **Exploratory Data Analysis (EDA) including:**

    - Job locations: highest-demand regions and cities.

    - Remote vs. on-site trends.

    - Employment type breakdown.

- **Role‑Specific Insights** 

    - including  Analysts, Engineers, Scientists roles.

- **Skills & Salary Analyses** 
    - evolving skill demand and their impact on compensation.

- **Final Summary** 

    - synthesizing key findings across the analyses.

## 📂 Dataset Information
- Source: Kaggle public dataset: *lukebarousse/data‑analyst‑job‑postings‑google‑search*

- Creator: Luke Barousse

- File: gsearch_jobs.csv (~62,000 rows spanning 2022–2025)

- Format: Cleaned pandas DataFrame, saved as df_clean.pkl



## 🛠️ Tools & Technologies

- Data Processing: [`python`](...), [`NumPy`](...)

- Visualization: [`matplotlib`](...), [`seaborn`](...)

- Stats: [`SciPy`](...)

- Environment: [`python`](...), [`Jupyter Notebook`](...), [`Conda`](...)

- Documentation: Markdown

## 🔍 Analysis Sections


### 1. Data Cleaning

Steps included:

- Importing data via Kaggle API

- Exploring structure and cleaning

- Converting timestamps, extracting date parts

- Data transformation, handling empty strings, normalizing titles, and saving cleaned datasets

See detailed steps in the notebook: [Data Cleaning Procesures](EDA_US_Data_Job_Listing_intro.ipynb)


### 2. Job Locations (2022–2025)

**Method:**
- Counted and ranked top 10 locations each year.
- Standardized columns names.

**Insight:** 
- Bar charts reveals: 
    - “Anywhere” (remote) leads; 
    - Oklahoma City,OK and Kanas City Mo (2022-2024) 
    - Denver CO (2024-2025)
    
See detailed steps in the notebook: [U.S. Job Locations (2022-2025 )](2022_to_2025_EDA_US_Data_Job_Listing_Intro.ipynb)

![Bar Charts: 2022_2025 Job Locations Bar Charts](Top_US_Data_Job_Locations(2022-2025).png)

**Conclusion:** Analysis reveals “Anywhere” (remote) remains the top location for data professionals, regional markets in states like Oklahoma and Colorado are gaining importance.


### 3. Remote Work Trends (2022–2025)

**Method:** 
- Compared remote vs. on‑site percentages over time.
- Count remote vs. non-remote positions.
- Map Boolean values to descriptive labels.
- Visualize results in pie charts.

**Insight:** Remote share is declining year over year.

See detailed steps in the notebook: [Remote Work Trends (2022-2025)](2022_to_2025_EDA_US_Data_Job_Listing_Intro.ipynb)

![Pie ChartS: 2022-2025 Remote Work Trend](U.S._Data_Job_Posting_Remote_Work_Availability(2022-2025).png)


**Conclusion:** Organizations are trending back toward in‑office roles.


### 4. Median Analyst Salary: Seniority and Remote Status (2023)

**Method:** 
- Filtered analysts roles. 
- Grouped by seniority and remote status.
- Compute median salaries by group.
- Standardized column names.

**Insight:** 
- **2022**: Remote roles paid more across all seniority levels.

- **2023**: Only Director and Principal positions continued to favor remote work; other levels showed minimal differences.

- **2024**: Notable remote salary advantages appeared at the Intern and Mid-Level tiers.

- **2025**: Only Lead-level remote roles reported higher median salaries.

See detailed steps in the notebook: [U.S. Median Analyst Salary: Remote and Seniority Status (2023)](2023_EDA_US_Data_Job_Listings_Intro.ipynb)

![Bar Charts: U.S Remote and Seniority Status with Salary Data (2023)](U.S._Analyst_Job_for_Remote_and_Seniority_Status_with_Salary(2023).png)

**Conclusion:** While pay differentials exist for remote work at certain seniority levels, no consistent trend links seniority and remote status. Notably, remote postings declined from 50 % in 2022 to 29 % in 2024, indicating a move toward on-site roles.


### 5. Employment Type Distribution (2022-2025)

**Method:** 
- Counted and ranked employment types (Full-Time, Contract, Part-Time, etc.)
- Visualized the results.

**Insight:** Full-time dominates; part-time surged in 2025, overtaking contracts.

See detailed steps in the notebook: [Employment Type Distribution (2022-2025)](2022_to_2025_EDA_US_Data_Job_Listing_Intro.ipynb)

![Bar Chart: Employment Type Distribution (2022-2025)](U.S._Data_Job_Posting_by_Employment_Type(2022-2025).png)

**Conclusion:** Full-time employment continues to dominate the data job market, while part-time roles are seeing growing acceptance; contract positions remain present but secondary.


### 6. Top Job Boards for Analyst Positions (2024)

**Method:** 

- Filtered for analyst roles with valid salary and website data. 
- Counted postings per site, calculated median salary.

- Standardized column names.

**Insight:** 

- LinkedIn leads in both count and pay.

- ai-jobs.net and Recruiters.com pay more for niche roles.

- Indeed remains steady but ranks below LinkedIn.

See detailed steps in the notebook:[Top Job Boards for Analyst Positions (2024)](2024_EDA_US_Data_Jobs_Listings_Intro.ipynb)

![Bar Chart: Top Job Boards for Analyst Position](Top_Job_Posting_Site_with_Median_Salary(2023).png)

**Conclusion:** Specialized platforms may offer higher salaries, however, their smaller user base and focus on niche job positions may limit their reach and appeal to a broader range of job seekers.


### 7. Top 5 In‑Demand Skills (2023)

**Method:** 
- Identify top roles each year.

- Exploded skill lists.

- Count skill occurrences per title.

- Calculate skill percentages.

- Standardized naming for clarity

**Insight:**

- SQL is foundational for Analysts and Engineers

- Power BI overtook Excel in 2024 for Business Analysts

- Python remains the primary language for Data Scientists.

See detailed steps in the notebook: [Competitive Skills for Data Roles (2023)](2023_US_Job_Listing_Skills_Analysis.ipynb)

![Bar Chart: Top 5 skills for Data Roles](Top_5_In-Demand_Skills_for_Data_Positions(2023).png)

**Conclusion:** SQL and Python maintain foundational importance, with visualization tools like Power BI and Tableau gaining traction in specific roles.


### 8. 2024 Trending Skills (Monthly Demand)

**Method:** 
- Monthly pivot: aggregate monthly mentions.

- Add total rows for yearly sums.

- Sort by popularity. 

- Normalize percentages for core skills. 

- Restructure for clarity.

**Insight:**
- SQL skills are consistently in high demand, with a steady monthly demand rate.

- Excel and Python skills remain stable with a reliable demand and minimal fluctuations.

- Power BI and Tableau skills, on the other hand, experience periodic spikes in demand, but do not maintain a consistent level of demand.

See detailed steps in the notebook: [Trending Data Skills for 2024](2024_US_Job_Listing_Skill_Analysis.ipynb)

![Line Chart: Trending Data Skills for 2024](U.S._Data_Job_Posting_Trending_Skills_for_Data_Roles(2024).png)

**Conclusion:** Foundational skills such as SQL, Python and Excel are prioritized across all years, while visualization tools show variable demand linked to organizational needs.


### 9. Salary Distribution Across Data Roles (2023)

**Method:** 
- Identify the top five most common data roles and filter accordingly.

- Calculate median salaries.

- Sort by compensation.

**Insight:**
- Data Scientists: upward skew + rising salaries.

- Engineers: right-skew, dip in 2025 low end.

- Analysts: expanding range and more upper outliers.

- Business Analysts: median stable ($96–$103K), with top-end stretches.

- Healthcare Analysts: tight cores, occasional high-end pay.

See detailed steps in the notebook: [Salary Distribution Across Data Roles (2023)](2023_US_Job_Listing_Skills_Analysis.ipynb)

![Box Chart: Salary Distribution Across Data Roles (2023)](U.S._Data_Job_Posting_Salary_Distribution(2023).png)

**Conclusion:** While median salaries remain stable, the right-skew in distributions highlights lucrative opportunities at senior or specialized levels. Data roles demonstrate increasing upper-end salary variance, reflecting high-growth positions in the field.


### 10. Top‑Paying and Most‑In‑Demand Analyst Skills (2024)

**Method:** 
- Filtered analyst postings by salary validity.

- Exploded skill lists.

- Calculate median pay per skill and it's frequency.

- Identify the top 10 by compensation and skill demand.


**Insight:**
- Top paid by year:

    - 2022 – MSSQL

    - 2023 – Ruby / TypeScript

    - 2024 – GraphQL

    - 2025 – PySpark

- Consistent skills in both demand and pay: 
    - SQL 

    - Python 

    - Power BI 

    - Tableau

See detailed steps in the notebook: [Top Paying and Most‑In‑Demand Analyst Skills (2024)](2024_US_Job_Listing_Skill_Analysis.ipynb)

![Bar Chart: Top Paying and In Demand Analyst Skills (2024)](U.S._Data_Skill_Ranking_for_Most_Paid_Most_In_Demand(2024).png)

**Conclusion:** Blending foundational skills with niche tech elevates earning potential.


### 11. Most Valuable Skills for Analysts Roles (2023)
This Analysis will explore which of these skills are the most valuable in U.S. job market for 2023

**Method**

- Filtered analyst job postings.

- Validated skill entries

- Expanded skill lists separately.

- Calculate skill counts and salaries.

- Calculate skill frequencies percentage.

- Exclude low frequency skills.

**Insight**

- SQL: Most valuable skill, but lags in compensation.

- Python: Gaining ground, highest compensation in 2023 and 2025.

- Tableau & Power Bi: Compensate well, used by specialized analysts.

- Excel: Struggling to gain traction, low mentions and salary.

See detailed steps in the notebook: [Most Valuable Skills for Analysts Roles (2023)](2023_US_Job_Listing_Skills_Analysis.ipynb)

![Scatter Plot: Most Valuable Skills for Analyst Roles (2023)](U.S._Analyst_Roles_Most_Valuable_Skills(2023).png)

**Conclusion**
This analysis reveals that the most in-demand skills for analysts are SQL and Python. Python is emerging as a top contender and as a consequence, it is also the highest compensated. While Tableau and Power Bi are important tools, their demand and compensation vary. In contrast, Excel lags behind in both mentions and salary compensation. These findings provide valuable insights for analysts and employers alike to stay ahead in the competitive job market.



## 📋 Final Summary and Key Takeaways

### Key Takeaways:

This analysis highlights the evolving dynamics of the U.S. data job market from 2022 to 2025. The most significant insights are:

- **Shift Back to On-Site Roles:** After an initial surge in remote work, the job market is seeing a shift back to on-site roles, indicating a renewed emphasis on in-person collaboration and face-to-face interactions.

- **Emerging Hubs for Job Growth:** Cities like Oklahoma City, Kansas City, Denver, and Colorado Springs are emerging as hubs for job growth and opportunity, offering access to top talent.

- **Essential and Specialized Skills:**  The most in-demand skills for analysts are SQL and Python, while specialization in niche technologies like GraphQL and PySpark can drive top-tier pay and higher job satisfaction.

- **Salary Potential:**  Standard roles have steady salaries, but specialization and seniority can lead to significant salary growth and greater job satisfaction for data professionals.

## Final Summary
These findings highlight the key trends and insights from the analysis of the U.S. data job market from 2022 to 2025.

### Key Trends:

- 📉 **Remote work has declined since 2022.** 
    - This suggests companies are prioritizing on-site collaboration and face-to-face interactions.

- 🏙️ **Regional hubs emerging.** 
    - Cities like Oklahoma City, Kansas City, Denver, and Colorado Springs offer attractive alternatives to traditional tech hubs. 

- 👥 **Full-time roles dominate employment type:**
	- The data job market is characterized by a preference for full-time employment, with part-time work experiencing growth.

### Essential Skills:

- 💡**Core skills (SQL, Excel, Python) remain essential**
	- Data professionals should prioritize developing these skills to drive career advancement and higher salaries.


- 🎯 **Specialist tools (e.g., PySpark, GraphQL) offer higher earning potential.**
	- Specialization in these tools can be a key factor in driving career advancement and salary growth for analyst roles.


 In the data analytics field, staying aligned with industry trends and demands requires a commitment to ongoing learning and professional development.


### Data Limitations ###

- **Role Definition Variability:** The classification of "Analyst" roles varies across platforms, encompassing a wide range of specialized positions. This variability can affect the consistency of job titles and responsibilities.

- **Sample Size Variability:** Platforms with smaller sample sizes may not fully represent the overall job market.

- **Salary Data Completeness:** Not all job postings include salary information, leading to potential biases in the median salary calculations.

- **Geographical Distribution:** The analysis does not account for geographical differences in salary, which can significantly impact median salary figures.

- **Job Description Variability:** Job descriptions vary widely across platforms, making it challenging to ensure consistency in role definitions and responsibilities.



=======
# US-Job_Market_Analysis
U.S. Job Market Analysis for Data positions from the years of 2022 to 2025
>>>>>>> 741404d1097e03d9920b7c66afa529bf1d7d1906
