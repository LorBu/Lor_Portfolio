# Yelp Reviews - NLP Project

## Project Overview
Our objective is to build a classification model capable of accurately predicting the rating corresponding to a Yelp review. By analyzing the text content of reviews, we aim to uncover insights into customer sentiments and engagement levels, helping businesses make informed decisions to improve user experiences and drive growth.

## Data
- **Yelp Review Dataset:** The dataset consists of Yelp reviews spanning multiple years. It includes textual content, star ratings, and engagement metrics such as 'cool', 'useful', and 'funny' votes, providing a rich source of data for our NLP project.

## Data Exploration
- **Initial Dataset Inspection:** We start by loading the Yelp review dataset and conduct an initial inspection to understand its structure and contents.
- **Review Length Distribution:** We explore the distribution of review lengths to gain insights into the text data's characteristics.
- **Relationship with Star Ratings:** Analyzing the relationship between review length and star ratings helps us understand potential correlations between textual content and user ratings.

## NLP Classification
- **Feature Extraction:** We use CountVectorizer to convert text data into numerical features, enabling us to train machine learning models.
- **Model Training:** Employing Multinomial Naive Bayes classifier, we train the model to predict star ratings based on review text.
- **Performance Evaluation:** We assess the model's performance using metrics like precision, recall, and F1-score to gauge its effectiveness in classifying reviews.

## Subset Analysis
- **Focus:** Focusing on reviews with extreme ratings (1-star and 5-star), we conduct further analysis to evaluate the model's performance within this subset.
- **Evaluation:** This allows us to assess the model's ability to distinguish between highly negative and highly positive sentiments.

## TF-IDF Transformation
- **Incorporation:** Incorporating TF-IDF (Term Frequency-Inverse Document Frequency) into our classification pipeline, we explore its impact on model performance.
- **Importance Weighing:** This transformation helps weigh the importance of words in the reviews, potentially improving the model's ability to capture meaningful features.

## Conclusion
Our NLP project provides valuable insights into sentiment analysis and classification of Yelp reviews. By leveraging NLP techniques, we gain a deeper understanding of customer sentiments and engagement levels, enabling businesses to make data-driven decisions to enhance user experiences and drive growth.

## Project Needs
- Python 3.x
- Libraries: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
- Access to the Yelp review dataset
- Understanding of NLP concepts and classification algorithms