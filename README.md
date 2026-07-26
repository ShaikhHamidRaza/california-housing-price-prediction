## California Housing Price Prediction

Machine Learning project that predicts California house prices using the California Housing dataset from Scikit-learn.
The project demonstrates a complete end-to-end ML pipeline, including data preprocessing, feature engineering, model training, evaluation, and comparison of multiple regression algorithms .

## Project Overview

Housing price prediction is a classic regression problem in machine learning.
The goal of this project is to build models that can estimate median house value based on features such as:

Median income
Average rooms
Average bedrooms
Population
House age
Latitude and longitude

This project compares multiple regression models to identify the best performing algorithm.

## Dataset

The dataset used is California Housing Dataset from Scikit-learn.

Key details:

20,640 housing records
8 numerical features
Target variable: Median House Value

Features include:

Feature	Description
MedInc	Median income in block
HouseAge	Median age of houses
AveRooms	Average number of rooms
AveBedrms	Average bedrooms
Population	Population of block
AveOccup	Average occupancy
Latitude	Location latitude
Longitude	Location longitude
## Exploratory Data Analysis (EDA)

The following analysis was performed:

Correlation heatmap
Feature distribution analysis
Target variable distribution
Scatter plots between key variables and house price

Key insight:

Median Income showed the strongest correlation with house prices.

## Feature Engineering

Additional features were created to improve model performance:

rooms_per_household
bedrooms_per_room
population_per_household

Feature engineering helps the model better understand relationships in the data.

## Machine Learning Models Used

The following regression algorithms were trained and compared:

Linear Regression
Decision Tree Regressor
Random Forest Regressor
Gradient Boosting Regressor

A preprocessing pipeline was used including:

Feature scaling
Data splitting
Model training
## Model Evaluation

Models were evaluated using:

RMSE (Root Mean Squared Error)
R² Score

Example results:

Model	RMSE	R²
Linear Regression	~0.73	0.57
Decision Tree	~0.60	0.64
Random Forest	~0.50	0.72
Gradient Boosting	~0.49	0.74

Random Forest and Gradient Boosting performed best.

## Model Optimization

Model performance was improved using:

Cross Validation
GridSearchCV for hyperparameter tuning

Best hyperparameters were selected automatically.

## Feature Importance

Feature importance analysis showed:

Top predictors of house prices:

Median Income
Latitude
Longitude
Average Rooms

This helps interpret how the model makes predictions.

## Model Saving

The final trained model was saved using Joblib.

joblib.dump(best_model, "housing_price_model.pkl")

This allows future predictions without retraining.

## Project Structure
california-housing-price-prediction
│
├── housing_model.py
├── notebook.ipynb
├── housing_price_model.pkl
├── requirements.txt
└── README.md
## Technologies Used

Programming Language

Python

Libraries

Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
Joblib

Tools

Jupyter Notebook
Git
GitHub
## How to Run the Project

Clone the repository

git clone https://github.com/ShaikhHamidRaza/california-housing-price-prediction

Install dependencies

pip install -r requirements.txt

Run the notebook or script

python housing_model.py
## Future Improvements

Possible improvements:

Deploy model using Streamlit web app
Use advanced models like XGBoost
Train deep learning regression model
Perform hyperparameter tuning with RandomizedSearchCV
## Author

Hamid Raza
BCA Student | Aspiring AI/ML Engineer

GitHub
https://github.com/ShaikhHamidRaza

LinkedIn
https://linkedin.com/in/shaikhhamidraza
