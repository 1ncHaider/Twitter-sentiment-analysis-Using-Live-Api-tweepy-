import joblib

def predict_sentiment(text, model_path='models/sentiment_model.pkl'):
    model = joblib.load(model_path)
    prediction = model.predict([text])[0]
    sentiment_map = {0: "Negative", 1: "Positive"}
    return sentiment_map.get(prediction, "Neutral/Unknown")

if __name__ == "__main__":
    sample_text = input("Enter text to analyze sentiment: ")
    result = predict_sentiment(sample_text)
    print(f"Sentiment: {result}")
