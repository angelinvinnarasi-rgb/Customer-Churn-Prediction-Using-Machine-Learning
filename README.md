# Customer Churn Prediction Using Machine Learning

## Overview

### Problem Statement

Customer churn is a major challenge for telecom companies because losing customers can affect revenue and business growth. This project aims to analyze customer demographic, service, contract, and billing information to identify customers who are likely to churn.

### Project Type

- Supervised Learning - Classification

### Objective

The primary objective of this project is to build a machine learning classification model that predicts whether a telecom customer is likely to churn based on customer and service-related information.

---

## Dataset Information

### Dataset Source

**Dataset Source:** IBM GitHub Repository

**Dataset Name:** Telco Customer Churn

**Source URL:**  
https://github.com/IBM/telco-customer-churn-on-icp4d/blob/master/data/Telco-Customer-Churn.csv

### Dataset Description

The Telco Customer Churn dataset contains customer demographic information, subscribed services, contract details, payment methods, and billing information. The target variable indicates whether a customer has churned or not.

### Dataset Size

| **Attribute** | **Value** |
|---|---|
| Records | 7,043 |
| Features | 20 input features |
| Total Columns | 21 |
| Target Variable | Churn |

---

## Project Workflow

### 1. Exploratory Data Analysis (EDA)

Performed:

- Dataset Overview
- Missing Value Analysis
- Correlation Analysis
- Distribution Analysis
- Churn Distribution Analysis
- Categorical Feature Analysis
- Numerical Feature Analysis
- Data Visualizations

### Key Insights

- The dataset contains 7,043 customer records.
- The dataset has more customers who stayed than customers who churned.
- Month-to-month contract customers showed a higher churn count.
- Customers using fiber optic internet showed a higher churn count.
- Electronic check users showed a higher churn count.
- Customers with lower tenure generally showed higher churn.
- Churned customers generally had higher monthly charges.

---

### 2. Data Preprocessing

Performed:

- Missing Value Analysis
- Duplicate Checking
- Outlier Detection
- Skewness Analysis
- Label Encoding
- One-Hot Encoding
- Train-Test Split

The dataset contained no duplicate records and no missing values initially. `TotalCharges` was converted from categorical/string format to numeric format during preprocessing.

---

### 3. Feature Engineering & Selection

Performed:

- Target Label Encoding
- One-Hot Encoding
- Correlation Analysis
- SelectKBest Feature Selection

### Final Features Used

- SeniorCitizen
- tenure
- MonthlyCharges
- TotalCharges
- TotalCharges_log

Five features were selected using SelectKBest with the ANOVA F-test (`f_classif`).

---

### 4. Model Building

Models Implemented:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. Support Vector Machine (SVM)
5. K-Nearest Neighbors (KNN)
6. Gradient Boosting

---

### 5. Model Evaluation

#### Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

### Model Comparison

| **Model** | **Accuracy** | **Precision** | **Recall** | **F1 Score** | **ROC-AUC** |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 79.21% | 65.52% | 45.72% | 53.86% | 82.72% |
| Decision Tree | 71.89% | 47.01% | 46.26% | 46.63% | 64.67% |
| Random Forest | 77.15% | 59.29% | 44.39% | 50.76% | 77.64% |
| SVM | 73.46% | 0.00% | 0.00% | 0.00% | 79.53% |
| KNN | 76.44% | 57.55% | 42.78% | 49.08% | 75.04% |
| Gradient Boosting | 79.42% | 64.89% | 48.93% | 55.79% | 82.92% |

### Best Model

**Selected Model:** Gradient Boosting

**Reason for Selection:**

- Achieved the highest ROC-AUC of **82.92%**.
- Achieved the highest F1 Score of **55.79%** among the evaluated models.
- Achieved the highest recall of **48.93%** among the evaluated models.
- Training and testing accuracy showed a relatively small difference, indicating reasonable generalization.

---

## Deployment

### Framework Used

- Flask
- Python
- Pandas
- Pickle

### Model Export

The trained Gradient Boosting model was exported as:

```text
models/gradient_boosting_model.pkl

### API Endpoint

```http
POST /predict
```

### Sample Request

```json
{
    "SeniorCitizen": 0,
    "tenure": 24,
    "MonthlyCharges": 70.50,
    "TotalCharges": 1692.00,
    "TotalCharges_log": 7.44
}
```

### Sample Response

```json
{
    "prediction": 0
}
```

### Prediction Meaning

- `0` → Customer is predicted to stay
- `1` → Customer is predicted to churn

---

## Docker Containerization

### Build Docker Image

```bash
docker build -t customer-churn-prediction .
```

### Run Docker Container

```bash
docker run -p 5000:5000 customer-churn-prediction
```

### API Testing

**API URL:**

```text
http://127.0.0.1:5000/predict
```

**Test Response:**

```json
{
    "prediction": 0
}
```

### Screenshot Evidence

#### Docker Build Success

![Docker Build Success](outputs/docker_build_success.png)

#### Docker Run Success

![Docker Run Success](outputs/docker_run_success.png)

#### API Testing Output

![API Testing Output](outputs/api_testing_output.png)

---

## Installation & Setup

### Clone Repository

```bash
git clone <repository-url>
cd Customer_Churn_Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

#### Flask

```bash
python app.py
```

The Flask application runs on:

```text
http://127.0.0.1:5000
```

---

## Project Structure

```text
Customer_Churn_Prediction/
│
├── data/
│   └── Telco-Customer-Churn.csv
│
├── models/
│   └── gradient_boosting_model.pkl
│
├── notebooks/
│   └── customer churn prediction.ipynb
│
├── outputs/
│   ├── docker_build_success.png
│   ├── docker_run_success.png
│   └── api_testing_output.png
│
├── templates/
│   └── index.html
│
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## Results

- Evaluated multiple classification models using Accuracy, Precision, Recall, F1 Score, and ROC-AUC.
- Gradient Boosting achieved a ROC-AUC of **82.92%** and an F1 Score of **55.79%**.
- Successfully exported the trained model as a `.pkl` file.
- Successfully developed and tested the Flask REST API.
- Successfully containerized the application using Docker.

---

## Future Improvements

- Add more customer and service-related data.
- Try advanced machine learning algorithms.
- Deploy on cloud platforms.
- Implement model monitoring and automatic retraining.

---

## Author

**Student Name:** Elaiyarasi E

**Batch:** DS AN B03

**Program:** Data Science Mini Project

**Project Title:** Customer Churn Prediction Using Machine Learning

**Submission Date:** 26/09/2026