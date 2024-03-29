# Loan Repayment Prediction using Neural Networks

## Project Overview:
Our objective is to predict whether borrowers will repay their loans using historical data obtained from LendingClub. By leveraging machine learning techniques, specifically Artificial Neural Networks (ANN), we aim to develop a model capable of accurately classifying loan repayment statuses.
  
## Data:
Our dataset comprises a subset of the LendingClub DataSet obtained from Kaggle. It includes various features such as loan amount, term, interest rate, employment details, income, loan purpose, etc. The dataset is substantial, containing numerous features and loan repayment statuses.

## Data Exploration and Preprocessing:
* **Missing Values:** Handled missing data using appropriate methods.
* **Categorical Features:** Converted categorical features into numerical using one-hot encoding.
* **Normalization:** Scaled numerical features to enhance model performance.
* **Exploratory Analysis:** Examined correlations between features and loan repayment status.

## Model Use:
* **Neural Network Architecture:** Designed a multi-layer ANN model tailored to dataset characteristics.
* **Training:** Trained the model using TensorFlow/Keras with appropriate loss functions and optimizers.
* **Evaluation:** Evaluated model performance using classification metrics such as accuracy, precision, recall, and F1-score.
* **Prediction:** Demonstrated model predictions on sample data, showing its ability to predict loan repayment status accurately.

## Conclusions:
* **Model Performance:** Achieved a high accuracy rate (89%) in predicting loan repayment.
* **Key Features:** Identified important features influencing loan repayment, including loan grade, zip code, and debt-to-income ratio.
* **Potential Improvements:** Suggested strategies for refining lending practices and risk management based on model insights.

## Project Needs:
* Python 3.x
* Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, TensorFlow, Keras
* Access to LendingClub loan dataset
* Understanding of data preprocessing, ANN architecture, and classification algorithms
