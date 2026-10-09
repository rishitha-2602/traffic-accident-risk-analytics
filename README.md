# AI-Powered Traffic Congestion and Road Accident Risk Prediction & Analytics System

## 1. Project Overview

This project aims to develop a data-driven traffic and road-safety analytics system using historical crash records and compatible traffic, weather, and geographic information where available.

Beyond conventional accident analysis and machine-learning prediction, the project will investigate the reliability of crash-severity predictions. It will evaluate whether models maintain their performance across different years and geographic areas and whether uncertain predictions can be identified before they are used for decision support.

The system will combine exploratory data analysis, machine learning, reliability evaluation, geographic analysis, and an interactive dashboard.

## 2. Problem Statement

Road accidents are a major public safety concern. Historical crash patterns can be associated with temporal, environmental, roadway, and geographic factors. Machine-learning models may help analyze these patterns, but their predictions can become less reliable when applied to data from later years or different locations.

This project will analyze available crash records for Dallas and Tarrant Counties, Texas, and investigate the performance and reliability of selected machine-learning models. In addition to predictive performance, the study will examine probability calibration, temporal and geographic generalization, and selective prediction, in which a model abstains from making predictions for cases identified as uncertain.

An interactive analytics dashboard will communicate historical crash patterns, model performance, prediction uncertainty, and research limitations.

## 3. Project Objectives

1. Collect and inspect publicly available historical crash records.
2. Clean and prepare the data for analysis and modeling.
3. Explore crash patterns by time, severity, location, weather, and roadway conditions where available.
4. Identify historical crash hotspots using appropriate geographic analysis.
5. Develop and compare baseline and advanced machine-learning models for crash-severity classification.
6. Evaluate model generalization using temporal and, where feasible, geographic testing.
7. Assess probability calibration and investigate uncertainty-aware selective prediction.
8. Identify influential features and explain model outputs.
9. Develop an interactive dashboard for presenting analytical findings and model reliability.

## 4. Research Questions

RQ1: How does crash-severity classification performance change when models are evaluated on later years rather than a random test sample?

RQ2: How does model performance change when tested on a geographic area that was not represented in model training, where the data supports this evaluation?

RQ3: How well calibrated are the models' predicted probabilities under different evaluation conditions?

RQ4: Can selective prediction reduce errors by allowing a model to abstain on uncertain cases, and what proportion of cases can still receive predictions at different error levels?

RQ5: Which available temporal, environmental, roadway, and geographic features contribute most to model predictions?

## 5. Initial Study Scope

Geographic area: Dallas and Tarrant Counties, Texas.

Target period: January 1, 2021, through December 31, 2025, subject to data availability.

Primary dataset: Publicly available crash-level records from the Texas Department of Transportation.

Additional data: Compatible traffic, weather, roadway, and geographic data where available and feasible within the project timeline.

Primary prediction task: Crash-severity classification, subject to the actual fields and definitions available in the dataset.

Additional analysis: Historical crash patterns, geographic hotspots, model reliability, and uncertainty-aware decision support.

## 6. Research Methodology

### Phase 1: Data Collection and Validation
Obtain available crash records, inspect the data dictionary, verify severity definitions, and assess missing values, duplicates, class imbalance, and data coverage.

### Phase 2: Data Cleaning and Exploratory Analysis
Standardize relevant fields, examine crash patterns, investigate relationships between features and severity, and visualize historical geographic concentrations.

### Phase 3: Feature Engineering and Leakage Prevention
Create suitable temporal and geographic features where justified. Exclude target-derived information and variables unavailable at the intended prediction time. Fit preprocessing steps using training data only.

### Phase 4: Machine-Learning Models
Establish a baseline model and compare it with suitable alternatives such as Logistic Regression and Random Forest. Consider a boosting model if time and data permit.

### Phase 5: Generalization Evaluation
Compare random-split results with time-based testing. Perform geographic holdout testing if county coverage and sample sizes support a meaningful comparison.

### Phase 6: Trustworthiness and Uncertainty Evaluation
Evaluate macro-F1, per-class recall, and other appropriate classification metrics. Assess probability calibration using suitable metrics such as Brier score. Investigate selective prediction through risk-versus-coverage analysis, choosing thresholds using validation data rather than the final test set.

### Phase 7: Explainability and Geographic Analysis
Analyze influential model features and visualize historical crash concentrations. Clearly distinguish associations from causal explanations.

### Phase 8: Dashboard and Reporting
Build an interactive dashboard using Streamlit and Plotly. Present historical patterns, model comparisons, calibration, geographic results, and uncertainty-related limitations.

## 7. Technology Stack

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Plotly
- GeoPandas or Folium, where appropriate
- SHAP, if suitable for the selected models
- Streamlit
- Google Colab
- Git and GitHub

## 8. Expected Research Contribution

The project will provide a reproducible empirical evaluation of crash-severity model performance and reliability under different temporal and geographic testing conditions. It will also investigate whether a selective prediction approach can reduce errors by withholding predictions for uncertain cases.

The literature review will compare the proposed study with existing research and establish the specific contribution supported by the available data and experiments. No claim of being the first study of its kind will be made without sufficient evidence.

## 9. Limitations and Responsible Use

Historical crash records alone do not directly support prediction of whether a crash will occur at every road location and time. Crash-occurrence prediction requires suitable non-crash observations and relevant exposure or traffic data.

Model confidence is not a guarantee of correctness. Results may be affected by missing data, reporting practices, class imbalance, limited geographic coverage, and changes over time. Geographic and temporal comparisons will be reported only when supported by the data.

The system is intended for academic research and decision support, not as a substitute for professional road-safety assessments.

## 10. Project Status

Phase 1: Initial project setup completed.

Phase 2: Dataset acquisition and inspection pending.
