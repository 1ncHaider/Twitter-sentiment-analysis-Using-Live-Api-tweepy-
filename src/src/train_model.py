import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib

def label_sentiment(text):
    # Simple rule-based labeling for demo
    positive_keywords = ['love', 'amazing', 'wonderful', 'fantastic', 'helpful']
    negative_keywords = ['terrible', 'hate', 'worst', 'disappointed', 'bug', 'crash']

    text_lower = text.lower()
    if any(word in text_lower for word in positive_keywords):
        return 1
    elif any(word in text_lower for word in negative_keywords):
        return 0
    else:
        return 2  # Neutral/unknown

def train_model(input_csv='data/cleaned_tweets.csv', model_path='models/sentiment_model.pkl'):
    df = pd.read_csv(input_csv)

    # Label sentiments
    df['sentiment'] = df['cleaned'].apply(label_sentiment)

    # Filter out neutral tweets (label 2) for training
    df = df[df['sentiment'] != 2]

    X = df['cleaned']
    y = df['sentiment']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    pipeline = Pipeline([
        ('vect', CountVectorizer()),
        ('clf', LogisticRegression(solver='liblinear'))
    ])

    pipeline.fit(X_train, y_train)
    print(f"Training accuracy: {pipeline.score(X_train, y_train):.2f}")
    print(f"Test accuracy: {pipeline.score(X_test, y_test):.2f}")

    # Save the model
    joblib.dump(pipeline, model_path)
    print(f"Model saved to {model_path}")

if __name__ == "__main__":
    train_model()
