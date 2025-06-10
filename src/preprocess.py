import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk

# Download NLTK stopwords once
nltk.download('stopwords')

def clean_text(text):
    # Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
    # Remove mentions and hashtags
    text = re.sub(r'@\w+|#', '', text)
    # Remove non-alphabetic characters
    text = re.sub(r'[^A-Za-z\s]', '', text)
    # Lowercase
    text = text.lower()

    stop_words = set(stopwords.words('english'))
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]

    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]

    return ' '.join(tokens)

def preprocess_csv(input_path='data/tweets.csv', output_path='data/cleaned_tweets.csv'):
    df = pd.read_csv(input_path)
    df['cleaned'] = df['text'].apply(clean_text)
    df.to_csv(output_path, index=False)
    print(f"Preprocessed tweets saved to {output_path}")

if __name__ == "__main__":
    preprocess_csv()
