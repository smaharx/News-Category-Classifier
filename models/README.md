# Model Artifacts

This directory contains the serialized artifacts used by the Streamlit application.

## Files

- `model.pkl` — trained news-category classification model.
- `vectorizer.pkl` — TF-IDF vectorizer used to transform input text before classification.

## Usage

The application loads these files directly from this directory. Keep both files present when running the application.

These are generated model artifacts, not source code. They should not be edited manually.

## Compatibility

The artifacts were created with scikit-learn 1.8.0. The project pins that version in `requirements.txt` to keep the runtime aligned with the serialized artifacts.
