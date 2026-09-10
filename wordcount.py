import string
from collections import Counter

def count_words(filepath):
    with open(filepath, 'r', encoding="utf-8") as f:
        text = f.read().lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    return Counter(words)

if __name__ == "__main__":
    result = count_words("test.txt")
    print(result.most_common(10))
