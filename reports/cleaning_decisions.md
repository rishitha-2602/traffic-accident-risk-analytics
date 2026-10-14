# Data Cleaning and Preparation Decisions

## Dataset
Texas CRIS crash records for Dallas and Tarrant counties, 2021–2025.

## Data integrity checks
- Combined annual datasets while preserving the union of available columns.
- Added Source_Year to identify the source year of each record.
- Validated crash IDs and crash dates.
- Compared observed severity codes against the CRIS lookup definitions.
- Preserved raw data without modifying the original annual CSV files.

## Cleaning decisions
- Retained all 450,491 crash records.
- No rows were removed during this stage.
- Standardized Crash_Date to a datetime representation.
- Preserved columns introduced in later annual schemas.
- Retained the 2025 record with severity code 95 for investigation.
  This code was not found in the standard CRIS severity lookup, so it
  has not been silently deleted or recoded.
- Missing values are documented for further investigation rather than
  automatically filled or treated as zero.

## Important modeling consideration
Crash severity is the prediction target. Outcome-derived fields, such as
fatality indicators and injury counts, must not be used as predictors
when they would reveal the outcome.
