# Liquor Sales Analysis in Iowa, USA

This project focuses on analyzing liquor sales data from Iowa, USA, spanning from 2012 to 2020. The primary objectives are to identify the most popular product per zip code and compute the sales percentage for each store within the timeframe of 2016-2019. Python's Pandas library is utilized for data manipulation and analysis, while Matplotlib and Seaborn are employed for visualization purposes.

## Dataset Overview

The dataset used in this analysis is sourced from liquor sales records in Iowa, USA, covering the years 2012 to 2020. It includes various attributes such as date, store location, zip code, item number, bottles sold, sale dollars, etc. The initial exploration involves understanding the data structure, identifying missing values, and cleaning the dataset for further analysis.

## Data Cleaning and Preparation

The following steps were undertaken to clean and prepare the dataset:

* Identification and removal of rows with missing store locations as it directly impacts the analysis.
* Removal of duplicate rows to ensure data integrity.
* Imputation of remaining missing values.
* Conversion of the 'date' column to datetime format for proper time-series analysis.

The cleaned dataset is then saved to a new CSV file for future reference and analysis.

## Task 1: Most Popular Item per Zip Code

In this task, we aim to determine the most popular item in each zip code. The steps involved are as follows:

* Sorting the dataset by zip code.
* Grouping the data by zip code and identifying the item with the maximum bottles sold in each zip code.
* Visualization of the findings through a scatterplot, highlighting the top-selling items for each zip code.

The analysis results are presented visually in "FIGURE_1.png", showcasing the top-selling products and their corresponding zip codes.

## Task 2: Sales Percentage per Store (2016-2019)

For this task, the objective is to compute the sales percentage per store within the timeframe of 2016-2019. The process includes:

* Extraction of the year from the 'date' column and filtering the data for the specified timeframe.
* Calculation of total sales within the selected period.
* Aggregation of sales data per store and computation of sales percentage.
* Visualization of the sales percentage using a horizontal bar plot.

The results are illustrated in "FIGURE_2.png", demonstrating the sales percentage distribution among the top-selling stores during the specified years.

## Conclusion

This analysis provides valuable insights into liquor sales trends in Iowa, USA. By identifying the most popular products per zip code and computing the sales percentage per store, stakeholders can make informed decisions regarding inventory management, marketing strategies, and business expansion. The code and findings presented in this project contribute to a deeper understanding of consumer preferences and market dynamics in the liquor industry.