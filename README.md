# 📱 Spam SMS Detector

A machine learning-powered web app that detects whether an SMS message is spam or not. Built with Python, Streamlit, and scikit-learn, this project demonstrates real-time classification with probability scores and sample message testing.

---

## 📽️ Demo Video

[Click to watch the demo](https://raw.githubusercontent.com/Bhoomika08-MAY/CODSOFT/main/assets/demo.mp4)

---

## 🧠 Features

- 🔍 Real-time spam detection using TF-IDF and Naive Bayes
- 📊 Probability score for prediction confidence
- 📝 Sample message buttons for quick testing
- 📁 Clean UI with organized assets and code structure

---

## 🛠️ Tech Stack

- Python
- Streamlit
- scikit-learn
- pandas
- Git & GitHub

---

## 📂 Project Structure

| 📁 Folder/File             | 📝 Description                                                  |
|---------------------------|-----------------------------------------------------------------|
| `app.py`                  | Main Streamlit app for spam detection UI and prediction logic  |
| `train_model.py`          | Script to train and save the TF-IDF vectorizer and model        |
| `spam.csv`                | Dataset containing labeled SMS messages                        |
| `tfidf_vectorizer.pkl`    | Saved TF-IDF vectorizer used for transforming input text        |
| `requirements.txt`        | List of Python dependencies for easy setup                     |
| `.gitignore`              | Specifies files/folders to exclude from Git tracking            |
| `README.md`               | Project overview, demo link, and usage instructions             |
| `assets/demo.mp4`         | Demo video showcasing the app in action                         |

---

## 📦 Installation

```bash
pip install -r requirements.txt
streamlit run app.py
