# SentifyMaster: Sentiment Analysis using Twitter's API


## Overview

SentifyMaster employs natural language processing (NLP) techniques and machine learning algorithms to classify the sentiment of tweets obtained through Twitter's API. It preprocesses the text data, extracts features using CountVectorizer, handles imbalanced data, and performs classification using Support Vector Machine (SVM).

## Project Structure

- **`SentifyMaster.ipynb`:** Jupyter Notebook containing the core implementation of the sentiment analysis model.
  
- **`data/`:** Directory containing the dataset (`sentiments.csv`) used for training and evaluation. The data is sourced from Kaggle and is included in the repository.

- **`README.md`:** This file, providing an overview of the project, its features, project structure, and usage instructions.

## Features

- **Text Preprocessing:** Utilizes NLP techniques such as lemmatization and stop-word removal for text preprocessing.
  
- **Feature Extraction:** Converts text data into numerical feature vectors using CountVectorizer.
  
- **Handling Imbalanced Data:** Addresses imbalanced data using SMOTE to enhance model performance.
  
- **Support Vector Machine:** Implements classification using Support Vector Machine (SVM) for sentiment analysis.


## Evaluation

The performance of the sentiment analysis model is evaluated using metrics such as precision, recall, and F1-score. Additionally, a confusion matrix is generated to visualize the model's performance.

## Contributing

Contributions to SentifyMaster are welcome! Whether you're interested in fixing a bug, adding a new feature, or improving the project documentation, we'd love to have your help.

Feel free to fork the repository, make your changes, and submit a pull request. We appreciate any contributions that help make SentifyMaster better for everyone.

Let's collaborate and make SentifyMaster even more powerful! 🚀

## Usage

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/NabilYimer/SentifyMaster-Twitter-Sentiment-Analysis.git
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    This will install all the necessary dependencies for running the project.
