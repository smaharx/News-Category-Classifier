# 📰 News Category Classifier

![Python](https://img.shields.io/badge/Python-3-blue)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![Scikit--learn](https://img.shields.io/badge/ML-Scikit--learn-orange)
![NLP](https://img.shields.io/badge/NLP-TF--IDF-purple)
![License](https://img.shields.io/badge/License-MIT-green)
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://news-len.streamlit.app/)

## 🚀 Live Demo

**Try the application:** [NewsLens](https://news-len.streamlit.app/)

Classify news text into Politics, Technology, Entertainment, and Business directly in your browser.

News Category Classifier is a Machine Learning and NLP application that classifies news text into four categories: **Politics, Technology, Entertainment, and Business**. The project combines text preprocessing, TF-IDF feature extraction, a trained Naive Bayes classifier, and a Streamlit interface to provide an interactive news classification experience.

---

## Overview

News articles contain large amounts of unstructured text, making automatic categorization a useful Natural Language Processing task.

This project processes news text, converts it into numerical features using **TF-IDF vectorization**, and uses a trained **Multinomial Naive Bayes** model to predict the most likely news category.

The trained model and vectorizer are stored as serialized artifacts and loaded by the Streamlit application at runtime.

---

## Key Features

- 📰 Classifies news text into four categories
- 🧹 Text preprocessing and normalization
- 🔤 TF-IDF based feature extraction
- 🤖 Multinomial Naive Bayes classification
- 📊 Prediction confidence display when supported by the model
- 🖥️ Interactive Streamlit web interface
- 💾 Serialized model and vectorizer artifacts
- 📓 Jupyter Notebook for model development and experimentation

---

## System Architecture

The application follows a simple machine-learning inference pipeline:

1. **Input Layer** — User enters a news headline or article through the Streamlit interface
2. **Preprocessing Layer** — Text is normalized and cleaned before classification
3. **Feature Extraction Layer** — The saved TF-IDF vectorizer transforms the text into numerical features
4. **Prediction Layer** — The saved Multinomial Naive Bayes model predicts the news category
5. **Presentation Layer** — Streamlit displays the predicted category and confidence when available

```text
User Input
    │
    ▼
Text Preprocessing
    │
    ▼
TF-IDF Vectorizer
    │
    ▼
Trained Naive Bayes Model
    │
    ▼
Predicted Category
    │
    ▼
Streamlit UI
```

---

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Web Framework | Streamlit |
| Machine Learning | Scikit-learn |
| NLP / Feature Extraction | TF-IDF |
| Classification Algorithm | Multinomial Naive Bayes |
| Data Processing | Pandas, NumPy |
| Development | Jupyter Notebook |
| Model Storage | Python Pickle |

---

## Project Structure

```text
News-Category-Classifier/
│
├── app.py                    # Streamlit application
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
├── news_classifier.ipynb     # Model development and experimentation
│
├── models/
│   ├── model.pkl             # Trained classification model
│   ├── vectorizer.pkl        # Trained TF-IDF vectorizer
│   └── README.md             # Model artifact documentation
│
├── .editorconfig             # Editor configuration
└── .gitignore                # Git ignore rules
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/ubedullah-mahar/News-Category-Classifier.git
cd News-Category-Classifier
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate on Linux / macOS:

```bash
source .venv/bin/activate
```

Activate on Windows:

```bash
.venv\Scripts\activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

No environment variables or external database configuration are required for the current application.

The application expects the trained model artifacts to be available at:

```text
models/model.pkl
models/vectorizer.pkl
```

These files are included in the repository and are required for inference.

---

## Running the Application

Launch the Streamlit application:

```bash
streamlit run app.py
```

After Streamlit starts, open the displayed local URL in your browser.

Enter a news headline or article into the text area and select **Classify News** to receive the predicted category.

---

## Model Development

The `news_classifier.ipynb` notebook contains the model-development workflow, including:

- Loading and preprocessing news data
- Text cleaning
- TF-IDF feature extraction
- Train/test splitting
- Training multiple classification approaches
- Comparing model performance
- Selecting the model used for the application

The trained artifacts used by the application are stored separately in the `models/` directory.

---

## Model Artifacts

The `models/` directory contains the serialized files required by the application:

| File | Purpose |
|---|---|
| `model.pkl` | Trained Multinomial Naive Bayes classifier |
| `vectorizer.pkl` | Trained TF-IDF vectorizer |

The artifacts were created using scikit-learn 1.8.0, which is pinned in `requirements.txt` to maintain compatibility with the serialized objects.

See `models/README.md` for additional details.

---

## Future Improvements

Potential improvements for future versions include:

- Add automated tests for preprocessing and prediction
- Improve model evaluation and reporting
- Add support for additional news categories
- Improve input validation and error handling
- Add a dedicated model-training pipeline
- Add reproducible dataset and training documentation
- Introduce automated CI checks for pull requests
- Improve application UI and prediction explanations

---

## Contributing

Contributions are welcome.

Please read `CONTRIBUTING.md` before submitting changes.

---

## Security

If you discover a potential security issue, please avoid publicly exposing sensitive details.

See `SECURITY.md` for the reporting guidance.

---

## Authors

**Ubedullah Mahar**

GitHub: [@ubedullah-mahar](https://github.com/ubedullah-mahar)

---

## License

This repository does not currently specify an open-source license.