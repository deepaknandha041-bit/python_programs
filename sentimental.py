from textblob import TextBlob
def analyze_sentiment(text):
    blob = TextBlob(text)
    print(f"Text: {text}")
    print(f"Polarity: {'Positive' if blob.sentiment.polarity > 0 else 'Negative' if blob.sentiment.polarity < 0 else 'Neutral'}")
    print(f"Subjectivity: {'Objective' if blob.sentiment.subjectivity == 0 else 'Subjective'}")
    print()
text1 = "I love Python programming, it's so much fun!"
text2 = "This movie was really boring and disappointing."
text3 = "The weather today is nice."

analyze_sentiment(text1)
analyze_sentiment(text2)
analyze_sentiment(text3)
