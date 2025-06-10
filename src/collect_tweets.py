import csv

def fetch_simulated_tweets():
    # Simulated tweet texts
    tweets = [
        "I love this product! It's amazing.",
        "This is terrible, I hate it.",
        "I'm not sure how I feel about this.",
        "Absolutely wonderful experience!",
        "This is the worst service ever.",
        "Meh. It was okay, not great.",
        "OpenAI's tools are so helpful.",
        "I'm very disappointed in the update.",
        "Fantastic support from the team.",
        "Terrible bug, made everything crash."
    ]

    # Write simulated tweets to CSV
    with open('data/tweets.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['text'])
        for tweet in tweets:
            writer.writerow([tweet])

    print(f"Saved {len(tweets)} simulated tweets to data/tweets.csv")

if __name__ == "__main__":
    fetch_simulated_tweets()
