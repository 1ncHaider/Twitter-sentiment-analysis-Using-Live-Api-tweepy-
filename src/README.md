# Twitter Sentiment Analysis (Simulated)

This project performs sentiment analysis on simulated tweet data. It simulates collecting tweets (without using the Twitter API), preprocesses the text, trains a simple sentiment model, and predicts sentiments.

## Features

- Simulated tweet collection (no Twitter API needed)
- Text preprocessing using NLTK
- Sentiment model training with scikit-learn
- Sentiment prediction on new text
- Easily switch to live Twitter data by integrating Tweepy and Twitter API keys

## Setup

1. Clone the repo or download files.

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
## Run the pipeline:

bash
Copy
Edit
python main.py
## How to Use Live Twitter API (Optional)
If you want to collect live tweets instead of simulated data:

Create a Twitter Developer account:

Visit https://developer.twitter.com/

Apply for a developer account if you don’t have one.

# Create a Twitter App:

In the Developer Portal, create a new app.

Generate your API Key, API Secret Key, Access Token, and Access Token Secret.

# Set up environment variables:

- Create a .env file in the root directory with the following content:

- ini
- Copy
- Edit
- API_KEY=your_api_key_here
- API_SECRET=your_api_secret_here
- ACCESS_TOKEN=your_access_token_here
- ACCESS_SECRET=your_access_token_secret_here
* Important: Add .env to your .gitignore file to keep your keys safe and private * 

## Install Tweepy:

bash
Copy
Edit
pip install tweepy python-dotenv
Update src/collect_tweets.py to use Tweepy (replace the simulated script).

# Project Structure
src/collect_tweets.py — Simulate or collect tweets

src/preprocess.py — Clean and preprocess tweets

src/train_model.py — Train sentiment classifier

src/predict.py — Predict sentiment of new tweets

data/ — Raw and cleaned tweet data

models/ — Saved model files

main.py — Run entire pipeline

## Contributing
Feel free to contribute by:

Adding new features

Improving the sentiment model

Integrating other data sources

## License
MIT License — see LICENSE file for details.

yaml
Copy
Edit

---







