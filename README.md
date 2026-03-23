Wind Farm Digital Twin using Machine Learning
Overview
This project develops a digital twin model for wind turbines using machine learning. It predicts power output, evaluates performance, and detects anomalies using SCADA-like data.

Problem Statement
Wind farms often face inefficiencies in power generation, lack of real-time monitoring, unexpected failures, and high maintenance costs. This project addresses these issues using a data-driven approach.

Approach
The system combines supervised learning for prediction, unsupervised learning for anomaly detection, and data analysis for performance evaluation.

Features
Power Prediction Linear Regression is used to model the relationship between wind speed and power output.

Model Evaluation Performance is measured using R² Score, MAE, and MSE.

Performance Analysis Wind speed vs power trends are analyzed to identify deviations.

Anomaly Detection Isolation Forest and DBSCAN are used to detect abnormal behavior.

Performance Scoring Turbines are classified as Good, Moderate, or Poor based on performance.

Digital Twin Simulation Expected and actual outputs are compared to simulate turbine behavior.

Technologies Used
Python, Pandas, NumPy, Scikit-learn, Matplotlib, Streamlit

Project Structure
I4.ipynb – data analysis and modeling app.py – Streamlit dashboard SCADA_dataset.csv – dataset

Results
High prediction accuracy (R² ≈ 0.94–0.95) Effective anomaly detection and performance monitoring

Applications
Wind farm monitoring, predictive maintenance, energy optimization, smart grid systems
