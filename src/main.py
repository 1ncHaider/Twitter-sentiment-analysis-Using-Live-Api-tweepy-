from src.collect_tweets import fetch_tweets
from src.preprocess import preprocess
from src.train_model import train_model
from src.predict import predict_sentiment

def main():
    print("Collecting tweets...")
    fetch_tweets("OpenAI", 100)

    print("Preprocessing tweets...")
    preprocess()

    print("Training model...")
    train_model()

    print("Predicting sentiment for sample text...")
    sample_text = "I love using OpenAI's tools!"
    sentiment = predict_sentiment(sample_text)
    print(f"Sample Text: {sample_text}\nPredicted Sentiment: {sentiment}")

if __name__ == "__main__":
    main()
