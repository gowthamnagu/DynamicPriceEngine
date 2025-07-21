## 📰 Dynamic Price Engine

To build a machine learning-powered engine that predicts the optimal ride fare dynamically based on various real-time and historical features such as demand, supply, location, customer loyalty, ride duration, and more.

## Problem Statement
In ride-hailing platforms (e.g., Uber, Ola), pricing depends on fluctuating factors like:
- Number of available drivers and riders (supply-demand)
- Time of the day
- Ride duration
- Loyalty status
- Ratings
Manually defining pricing rules is inefficient. This project builds a regression model to learn the optimal ride cost based on past data and generalize it to new ride requests.

## 🧠 Project Overview
The Dynamic Pricing Engine is a machine learning-based system designed to predict real-time ride fares for transportation services based on dynamic features such as demand, supply, customer loyalty, time of booking, and more.Using real-world-like ride data, the project builds multiple regression models to learn patterns in ride pricing and deploys them via an interactive Streamlit web app where users can input trip details and receive instant fare predictions.

## 🚀 End-to-End Data Science Pipeline

- 📌 **Problem Definition**: Predict ride fare dynamically using user and ride details.
- 📥 **Data Collection**: Dataset with riders, drivers, ratings, loyalty, etc.
- 🧹 **Data Preprocessing**:
  - Label encoding for categorical features
  - Feature selection & transformation
- 🧠 **Model Training**:
  - Trained 3 models: Linear Regression, Random Forest, Gradient Boosting
- 📊 **Model Evaluation**:
  - Metrics: MAE, RMSE, R² Score
  - Saved using `joblib`
- 🌐 **Deployment**:
  - Built Streamlit app with real-time fare predictions
  - UI with model selection & dynamic inputs
- 🗃️ **Versioning**:
  - Code managed using Git
  - Requirements tracked with `requirements.txt`

## 🛠️ Tech Stack

- **Python 3.11**
- **Streamlit** — Web UI for interactive model prediction
- **Pandas, NumPy, Seaborn, Matplotlib, Scikit-learn,** — Data preprocessing and utilities
- **Linear Regression, Random Forest Regression, XGBoost** - ML Algorithms used for training models
  
## 🚀 Installation    

- **Clone the repository**
    
       git clone https://dagshub.com/gowthambreeze/dynamicfarepricing.git

- **Set up a virtual environment** 

        conda create -p venv python=3.11 -y
        conda activate venv/

- **Install dependencies** 

        pip install -r requirements.txt

 
## ▶️ Running the Application

Run the main file to start the application:

    streamlit run app.py


## 📄 License

This project is open-source under the MIT License.


## 🙋‍♂️ Contributions

Feel free to fork the repository, make improvements, and create pull requests!
---
Let me know if you want a downloadable PDF version of this `README.md` or help linking your GitHub repo to GitHub Pages for a live project site.

