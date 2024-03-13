## Ecommerce Analysis and Linear Regression Model

### Overview:
This project is part of my coursework in 'Advanced Python for Machine Learning'. It involves analyzing data from an Ecommerce company based in New York City, which sells clothing online and provides in-store style and clothing advice sessions. The goal is to determine whether the company should focus its efforts on improving the mobile app experience or the website.

### Data:
The dataset ('Ecommerce Customers.csv') contains information about customers, including their average session length, time spent on the app and website, length of membership, and yearly amount spent.

### Approach:
#### Data Exploration:
* Used pandas to load the dataset and inspected its structure using head(), info(), and describe() functions.
* Explored relationships between different variables using seaborn visualizations like joint plots, pair plots, and lmplots.
#### Model Training:
* Employed scikit-learn's Linear Regression model to predict the yearly amount spent by customers.
* Selected features including average session length, time on app, time on website, and length of membership.
* Split the data into training and testing sets and trained the model on 70% of the data.
#### Evaluation and Insights:
* Evaluated the model's performance using metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE).
* Analyzed model coefficients to understand the importance of different features.
* Concluded that length of membership and time spent on the app have the most significant impact on yearly amount spent.
* Recommended focusing efforts on improving the mobile app experience based on the model's insights.

### Future Steps:
* Continuously monitor customer behavior and feedback to refine strategies.
* Consider further development of both the mobile app and website to align their functionalities and user experiences.
* Explore additional features or models to enhance prediction accuracy.

### Files:
* Ecommerce Analysis.ipynb: Jupyter Notebook containing the code for data analysis, model training, and evaluation.
* Ecommerce Customers.csv: Dataset used for analysis.

### Requirements:
* Python 3.x
* Libraries: pandas, matplotlib, seaborn, numpy, scikit-learn
