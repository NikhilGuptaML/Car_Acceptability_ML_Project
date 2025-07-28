# 🚗 Car Evaluation - End-to-End Machine Learning Project

This is my first end-to-end Machine Learning project where I work on the Car Evaluation dataset to predict the **acceptability of cars** (unacc, acc, good, v-good) based on various categorical features such as safety, buying price, and more.

🔧 **Note**: This project does not include model deployment or UI integration — it focuses entirely on a clean modular ML pipeline.

---

## 📁 Project Structure

Car_Evaluation_ML_Project/<br>
│<br>
├── main.py # Runs the complete training pipeline<br>
├── README.md # This file<br>
├── requirements.txt # Project dependencies<br>
├── notebook/ # Jupyter notebook(s) used for EDA and  including all the steps in a single file to understand flow of the project<br>
│<br>
├── src/<br>
│ ├── components/<br>
│ │ ├── data_ingestion.py # Handles data loading and splitting<br>
│ │ ├── data_transformation.py # Handles preprocessing & encoding<br>
│ │ └── model_trainer.py # Trains and evaluates ML models<br>
│ │<br>
│ ├── train_pipeline.py # Optional: Train pipeline logic<br>
│ ├── predict_pipeline.py # Optional: For future use<br>
│ ├── utils.py # Helper functions (e.g., save/load models)<br>
│ ├── logger.py # Logging utility<br>
│ └── exception.py # Custom exception handling<br>
│<br>
├── logs/ # Stores logs for debugging<br>
├── artifact/ # Stores trained models, transformed data, etc.<br>
└── .gitignore # Files to ignore in GitHub<br>


---

## 📊 Dataset Information

- **Dataset**: [UCI Car Evaluation Dataset](https://archive.ics.uci.edu/ml/datasets/Car+Evaluation)
- **Features**:
  - `buying`, `maint`, `doors`, `persons`, `lug_boot`, `safety`
- **Target**:
  - `acceptability` (unacc, acc, good, v-good)

For detailed dataset attribute information and origin, see car.names.
---

## ✅ Steps Implemented

1. **Data Ingestion**
   - Reads the CSV file
   - Splits data into train/test
   - Saves raw, train, and test files

2. **Data Transformation**
   - One-hot encodes categorical features

3. **Model Training**
   - Trains a `RandomForestClassifier`
   - Evaluates performance using classification metrics

4. **Jupyter Notebook**
   - EDA and feature understanding
   - Baseline modeling for validation

---

## 📦 How to Run

1. Install dependencies:

pip install -r requirements.txt


2. How to Run

python main.py

## Future Improvements
Add model deployment using Streamlit/FastAPI

Track experiments using MLflow or DVC

Use feature importance plots

Add CI/CD for automation

📌 Goals of this Project
Understand and practice a modular ML pipeline

Learn how to structure folders and scripts like real-world projects

Get comfortable debugging and using Git/GitHub

🙋‍♂️ Author
Nikhil Gupta — B.Tech AI-ML student @ VIPS-TC

This is part of my self-learning journey toward mastering Machine Learning and Deep Learning

GitHub: NikhilGuptaML
