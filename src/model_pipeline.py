"""Reusable baseline modeling pipeline for crash severity prediction."""

from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


NUMERIC_FEATURES = [
    "Crash_Month",
    "Crash_DayOfWeek",
    "Is_Weekend",
    "Crash_Hour",
    "Latitude",
    "Longitude",
]

CATEGORICAL_FEATURES = [
    "Time_Period",
    "City_ID",
    "Light_Cond_ID",
    "Intrsct_Relat_ID",
]

FEATURE_COLUMNS = NUMERIC_FEATURES + CATEGORICAL_FEATURES
TARGET_COLUMN = "Severity_Target"


def build_preprocessor():
    """Create the preprocessing steps used by Logistic Regression and RF."""

    numeric_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ])

    categorical_transformer = Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ])

    return ColumnTransformer([
        ("numeric", numeric_transformer, NUMERIC_FEATURES),
        ("categorical", categorical_transformer, CATEGORICAL_FEATURES),
    ])


def build_random_forest():
    """Build the Random Forest pipeline using notebook parameters."""

    return Pipeline([
        ("preprocessor", build_preprocessor()),
        ("model", RandomForestClassifier(
            n_estimators=150,
            class_weight="balanced_subsample",
            min_samples_leaf=2,
            n_jobs=-1,
            random_state=42,
        )),
    ])
