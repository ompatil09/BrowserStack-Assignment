import logging
from collections import Counter
from utils import clean_text


def analyze_titles(titles):
    combined = " ".join(titles)
    cleaned = clean_text(combined)
    words = cleaned.split()

    counter = Counter(words)

    logging.info("\n--- Repeated Words (>2 occurrences) ---")
    for word, count in counter.items():
        if count > 2:
            logging.info(f"{word} - {count}")
