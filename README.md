# Traffic & Accident Risk Analytics

An AI-powered data science project that analyzes Texas traffic crash records and applies machine learning to understand crash patterns and predict crash severity.

## 🌐 Live Project Website

**Access the interactive application here:**

👉 [**Traffic & Accident Risk Analytics – Live Dashboard**](https://traffic-accident-risk-analytics.streamlit.app/)

The application is hosted using Streamlit Community Cloud. Visitors can open the website directly in their browser without installing Python or downloading the project.

### How to Access the Website

1. Click the **Live Dashboard** link above.
2. Wait for the Streamlit application to load.
3. Explore the available visualizations, crash statistics, and analytical results.
4. Use the interactive dashboard to investigate traffic crash patterns and model outputs.

*Note: The application may take a little time to start if it has been inactive.*

## Project Overview

This project analyzes Texas Department of Transportation Crash Records Information System (CRIS) data from Dallas and Tarrant Counties covering 2021–2025.

The project combines data preprocessing, exploratory data analysis, feature engineering, machine learning, model evaluation, and interactive visualizations to investigate traffic crash patterns and severity.

The goal is to develop a data-driven analytical system that helps users understand historical crash trends and evaluate the reliability of machine-learning predictions.

## Project Objectives

- Analyze traffic crash patterns across different years and locations.
- Identify temporal and geographic trends in crash records.
- Investigate relationships between crash characteristics and injury severity.
- Develop and evaluate machine-learning models for crash-severity prediction.
- Assess model performance, class-level results, and prediction reliability.
- Present analytical findings through an interactive Streamlit dashboard.

## How the Project Works

The project follows these major stages:

### 1. Data Collection

- Obtain Texas CRIS crash records for Dallas and Tarrant Counties.
- Work with historical crash records from 2021 through 2025.
- Organize the datasets by year and data category.

### 2. Data Preprocessing

- Inspect dataset structure, data types, and missing values.
- Validate crash identifiers and dates.
- Handle missing and inconsistent values.
- Prepare a cleaned dataset for further analysis.

### 3. Exploratory Data Analysis (EDA)

- Analyze yearly and monthly crash trends.
- Examine crash severity distributions.
- Investigate crash patterns by time and location.
- Create visualizations to communicate important findings.

### 4. Feature Engineering

- Extract useful information from crash dates and times.
- Prepare temporal and geographic features.
- Encode categorical variables.
- Separate training, validation, and testing data chronologically.

### 5. Machine Learning

- Develop a Random Forest classification model.
- Train the model using historical crash records.
- Evaluate its ability to classify crash severity.
- Compare model results using appropriate evaluation metrics.

### 6. Model Evaluation and Trustworthy AI

- Evaluate accuracy, balanced accuracy, and macro F1-score.
- Examine class-level precision, recall, and F1-score.
- Investigate performance differences across groups.
- Document model limitations and potential reliability concerns.

### 7. Interactive Dashboard

- Present crash statistics and visualizations.
- Allow users to explore historical crash patterns.
- Display analytical and model evaluation results.
- Provide an accessible interface through the published Streamlit website.

## Technologies Used

- **Programming:** Python
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Web Application:** Streamlit
- **Development Environment:** Jupyter Notebook, Google Colab
- **Version Control:** Git and GitHub

## Project Structure

traffic-accident-risk-analytics/
│
├── app/
│   └── app.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
│   ├── 01_project_setup.ipynb
│   ├── 02_data_acquisition_and_inspection.ipynb
│   ├── ...
│
├── src/
│   └── model_pipeline.py
│
├── reports/
│   ├── visualizations
│   ├── evaluation_results
│   └── audit_reports
│
├── requirements.txt
├── README.md
└── .gitignore

## Run the Project Locally

### Prerequisites

- Python 3.10 or a compatible version
- Git
- Required project datasets

### Step 1: Clone the Repository

```bash
git clone https://github.com/rishitha-2602/traffic-accident-risk-analytics.git
```

### Step 2: Navigate to the Project

```bash
cd traffic-accident-risk-analytics
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Mac/Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Run the Streamlit Application

```bash
streamlit run app/app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

**Important:** The application requires its referenced datasets and other necessary files to be available in the expected project locations. Follow the repository's data instructions before running it locally.

## Model Evaluation

The project evaluates model performance using:

- Accuracy
- Balanced Accuracy
- Macro F1-score
- Class-wise Precision
- Class-wise Recall
- Confusion Matrix

Evaluation results should be interpreted alongside class imbalance and the model's ability to identify serious and fatal crashes. The evaluation period must be specified when reporting metrics.

## Data Sources

**Texas Department of Transportation (TxDOT)**

Crash Records Information System (CRIS).

Geographic coverage: Dallas and Tarrant Counties, Texas.

Data period: 2021–2025.

## Limitations

- The analysis is limited to the available crash records from Dallas and Tarrant Counties.
- Missing and inconsistent records may affect analytical results.
- Class imbalance can affect the model's ability to identify less frequent severe crashes.
- Model predictions are not guarantees that an accident will occur or be prevented.
- Historical crash records alone do not establish the probability of a crash occurring at a particular road location and time.
- Reliable crash-occurrence prediction requires appropriate non-crash observations and compatible exposure or traffic data.

Historical crash-pattern analysis and crash-severity prediction should not be confused with future crash-occurrence prediction.

## Repository

**GitHub Source Code:**

[https://github.com/rishitha-2602/traffic-accident-risk-analytics](https://github.com/rishitha-2602/traffic-accident-risk-analytics)

**Live Application:**

[Open Traffic & Accident Risk Analytics](https://traffic-accident-risk-analytics.streamlit.app/)

## Project Team

- Rishitha Gaddam
- Seera Sai Surya Siddhardha
- Kalakata Keerthi

University of North Texas, 
Department of Data Science


*This project was developed as a collaborative academic data science project.*
