# -*- coding: utf-8 -*-
"""solution.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/123LaI7xYtkD6YNbaH-Kfpr8xfbX5rbdM
"""

import requests
from bs4 import BeautifulSoup

url = str(input())
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

products = soup.find_all("article")
ti = [product.get_text(strip=True) for product in products]
print(ti)

from textblob import TextBlob
from nltk.corpus import wordnet

pip install nltk

import nltk
nltk.download('wordnet')

for text in ti:
    blob = TextBlob(text)
    p_score = blob.sentiment.polarity
    n_score = 1 - p_score
    sub_score = blob.subjectivity
    asl= sum(len(sentence) for sentence in text.split()) / len(text.split())
    complex_words = 0
    if wordnet.synsets(text) and text not in common_words:  # Check for wordnet presence and common word exclusion
            complex_words += 1
    wc = sum(len(sentence.split()) for sentence in text.split()) / len(
        text.split("."))
    spw= sum(
        [len(w) for w in text.split() if w.isalpha()]
    ) / len(text.split())
    pp = sum(
        1 for word in text.split() if word in ["I", "me", "my", "myself", "you", "your", "yourself"]
    )
    awl= sum(len(w) for w in text.split()) / len(text.split())
    fi = 0.4 * (asl + complex_words / len(text.split()))
    print(f"\nText: {text}")
    print(f"Positive Score: {p_score}")
    print(f"Negative Score: {n_score}")
    print(f"Subjectivity Score: {sub_score}")
    print(f"Average Sentence Length: {asl}")
    print(f"Percentage of Complex Words: {complex_words / len(text.split()) * 100:.2f} %")
    print(f"FOG Index: {fi:.2f}")
    print(f"Complex Word Count: {complex_words}")
    print(f"Word Count: {len(text.split())}")
    print(f"Syllables per Word: {spw:.2f}")
    print(f"Personal Pronouns: {pp}")
    print(f"Average Word Length: {awl:.2f}")