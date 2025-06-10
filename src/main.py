import os
from src import collect_tweets, preprocess, train_model, predict

def main():
    # Step 1: Collect tweets
    print("Collecting tweets...")
    collect_tweets.fetch_tweets("OpenAI", 100)

    # Step 2: Preprocess tweets
    print("Preprocessing tweets...")
    preprocess.preprocess()

    # Step 3: Train sentiment model
    print("Training model...")
    train_model.train_model()

    # Step 4: Predict sentiment on sample text
    print("Predicting sentiment for sample text...")
    sample_text = "I love using OpenAI's tools!"
    sentiment = predict.predict_sentiment(sample_text)
    print(f"Sample Text: {sample_text}\nPredicted Sentiment: {sentiment}")

if __name__ == "__main__":
    main()
