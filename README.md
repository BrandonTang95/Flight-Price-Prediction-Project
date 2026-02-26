# ✈️ Flight Price Analysis & Prediction Web App

## 📌 Project Overview
This project analyzes flight booking data from India's top 6 metro cities to discover pricing insights and deploys a predictive machine learning model via a custom web application. What began as comprehensive exploratory data analysis (EDA) and statistical hypothesis testing evolved into a full-stack deployment. The final product utilizes an optimized **Random Forest** regression model served through a **Flask** backend, allowing users to input flight details and receive real-time price estimations.

![Web App Interface](screenshot.png)

## 🛠️ Tech Stack
* **Backend:** Python, Flask
* **Machine Learning:** Scikit-Learn, Pandas, NumPy, Joblib
* **Frontend:** HTML5, CSS3, Jinja2
* **Model Architecture:** Random Forest Regressor integrated with a Scikit-Learn `ColumnTransformer` Pipeline for automated scaling (`StandardScaler`) and encoding (`OneHotEncoder`).

## 🚀 Local Installation & Usage
To run this application locally on your machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/BrandonTang95/Flight-Price-Prediction-Project.git](https://github.com/BrandonTang95/Flight-Price-Prediction-Project.git)
   cd Flight-Price-Prediction-Project
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Flask server:**
   ```bash
   python app.py
   ```

4. **Access the web app:**
   Open your browser and navigate to `http://127.0.0.1:5000`

## 🧠 Machine Learning Optimization
The production model was trained on a cleaned dataset of over 300,000 flight records. To ensure the model was lightweight enough for web deployment while maintaining high accuracy, the Random Forest architecture was optimized by:
* Restricting maximum tree depth (`max_depth=15`) and limiting estimators (`n_estimators=30`) to prevent overfitting.
* Bundling the raw data preprocessing and the model into a single serialized `.pkl` file to seamlessly handle raw HTML form inputs.
* Applying `joblib` compression (level 3) to reduce the production model file size by 98% (from ~900MB to ~15MB).

## 🎯 Research Objectives
During the EDA phase, the primary aim was to answer the following questions regarding flight pricing dynamics:
* **Airline Variance:** Does the price vary significantly between different airlines?
* **Booking Timing:** How is the price affected when tickets are bought 1 or 2 days before departure versus far in advance?
* **Time of Day:** Does ticket price change based on specific departure and arrival times?
* **Route Analysis:** How does the price change based on Source and Destination cities?
* **Class Distinction:** What is the price variance between Economy and Business class?

## 📂 Data Dictionary
The final cleaned dataset utilized for model training consists of **9 predictor features** and **1 target variable**:

| Feature | Description | Type |
| :--- | :--- | :--- |
| **Airline** | The name of the airline company (6 unique carriers). | Categorical |
| **Source** | The city from which the flight takes off (6 unique cities). | Categorical |
| **Departure Time** | Derived feature grouping time periods into bins (6 unique time labels). | Categorical |
| **Stops** | The number of stops between source and destination (0, 1, or 2+). | Numeric |
| **Arrival Time** | Derived feature grouping time intervals into bins (6 distinct time labels). | Categorical |
| **Destination** | The city where the flight lands (6 unique cities). | Categorical |
| **Class** | The seat class (Business or Economy). | Categorical |
| **Duration** | Total amount of time taken to travel between cities (in minutes). | Numeric |
| **Days Left** | Number of days between the booking date and the departure date. | Numeric |
| **Price** | **(Target Variable)** The ticket price in INR. | Numeric |

## 📜 Credits
* **Dataset Author:** Shubham Bathwal (via Kaggle)
* **Original Platform:** EaseMyTrip
