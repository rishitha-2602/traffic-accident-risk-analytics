# Traffic & Accident Risk Analytics

An AI-powered data science project for analyzing Texas traffic crash records and building machine-learning models to support accident-risk or crash-severity analysis.

## Project Overview

This project analyzes Texas CRIS crash records from Dallas and Tarrant Counties covering 2021–2025. It uses data preprocessing, exploratory data analysis, machine learning, and interactive visualizations to investigate traffic crash patterns.

## Objectives

- Analyze crash patterns over time and across locations.
- Examine the relationships between crash characteristics and severity.
- Develop and evaluate a machine-learning prediction model.
- Present analytical findings through an interactive Streamlit application.
- Assess model reliability and document limitations.

## Technologies

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Streamlit
- Jupyter Notebook / Google Colab

## Project Structure

- `app/` — Streamlit application
- `notebooks/` — Data exploration, cleaning, feature engineering, and modeling
- `data/` — Raw, processed, and external data
- `src/` — Reusable Python modules
- `models/` — Saved model artifacts
- `reports/` — Evaluation results, visualizations, and audit reports
- `tests/` — Project tests

## Getting Started

1. Clone this repository.
2. Install the dependencies listed in `requirements.txt`.
3. Obtain the required datasets and place them in the documented locations.
4. Run the notebooks in the appropriate order if reproducing the analysis.
5. Launch the Streamlit application using the documented entry-point command.

## Evaluation

Report the final model's actual test-set accuracy, balanced accuracy, macro F1-score, confusion matrix, and relevant class-level metrics. Include the evaluation period and limitations.

## Limitations

Model predictions depend on the available data, feature quality, and evaluation methodology. Predictions should not be interpreted as guarantees that an accident will occur or be prevented.

## Data Sources

Texas Department of Transportation Crash Records Information System (CRIS). Document the dataset years, geographic coverage, and applicable access or sharing restrictions.

## Project Limitations

Historical crash records alone do not establish the probability of a crash occurring at every road location and time. Reliable crash-occurrence prediction requires appropriate non-crash observations and compatible exposure or traffic data. Historical hotspot analysis and crash-severity prediction should be distinguished from future crash-occurrence prediction.
