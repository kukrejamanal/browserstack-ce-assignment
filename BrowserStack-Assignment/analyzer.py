from collections import Counter
import re


def analyze_titles(articles):

    words = []

    for article in articles:

        title = article["translated_title"].lower()

        extracted_words = re.findall(r"\b[a-zA-Z]+\b", title)

        words.extend(extracted_words)

    word_count = Counter(words)

    repeated_words = {
        word: count
        for word, count in word_count.items()
        if count > 1
    }

    return repeated_words