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

Run the pipeline:
python main.py
How to Use Live Twitter API (Optional)
If you want to collect live tweets instead of simulated data:

Create a Twitter Developer account:

Visit https://developer.twitter.com/

Apply for a developer account if you don’t have one.

Create a Twitter App:

In the Developer Portal, create a new app.

Generate your API Key, API Secret Key, Access Token, and Access Token Secret.

Set up environment variables:

Create a .env file in the root directory:
