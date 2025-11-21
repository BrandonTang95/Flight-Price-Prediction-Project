# Flight-Price-Prediction-Project

## 📌 Project Overview
This study analyzes flight booking data obtained from the **EaseMyTrip** website to discover valuable insights for potential passengers. The project involves comprehensive statistical hypothesis testing and utilizes **Linear Regression** to predict flight ticket prices based on various factors.

## 🎯 Research Objectives
The primary aim of this study is to answer the following questions regarding flight pricing dynamics:
* **Airline Variance:** Does the price vary significantly between different airlines?
* **Booking Timing:** How is the price affected when tickets are bought 1 or 2 days before departure versus far in advance?
* **Time of Day:** Does ticket price change based on specific departure and arrival times?
* **Route Analysis:** How does the price change based on Source and Destination cities?
* **Class Distinction:** What is the price variance between Economy and Business class?

## 📊 Dataset & Methodology
**Data Collection**
* **Source:** Secondary data scraped from the EaseMyTrip website.
* **Tool Used:** Octoparse scraping tool.
* **Scope:** Flight travel between **India's top 6 metro cities**.
* **Timeline:** Data collected over 50 days, from **February 11th to March 31st, 2022**.
* **Volume:** A total of **300,261** distinct flight booking options.

The data was collected in two distinct subsets (Economy and Business class) and merged into a cleaned dataset containing 11 distinct features.

## 📂 Data Dictionary
The cleaned dataset consists of **300,261 data points** and **11 features**. Below is a detailed description of the features used in the analysis:

| Feature | Description | Type |
| :--- | :--- | :--- |
| **Airline** | The name of the airline company (6 unique carriers). | Categorical |
| **Flight** | The specific flight code for the plane. | Categorical |
| **Source City** | The city from which the flight takes off (6 unique cities). | Categorical |
| **Departure Time** | Derived feature grouping time periods into bins (6 unique time labels). | Categorical |
| **Stops** | The number of stops between source and destination (3 distinct values). | Categorical |
| **Arrival Time** | Derived feature grouping time intervals into bins (6 distinct time labels). | Categorical |
| **Destination City** | The city where the flight lands (6 unique cities). | Categorical |
| **Class** | The seat class (Business or Economy). | Categorical |
| **Duration** | Total amount of time taken to travel between cities (in hours). | Continuous |
| **Days Left** | Derived feature calculated by subtracting the trip date by the booking date. | Continuous |
| **Price** | The target variable storing the ticket price. | Continuous |
