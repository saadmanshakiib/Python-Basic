from collections import Counter

text = "Natural Language Processing is fun!"

print(text.lower())
print(text.upper())
print(len(text))

print(text.replace(" ","-"))
print(text.split())

text2 = "I love NLP because NLP helps computers understand language"

words = Counter(text2)
print("Total Words : ", words)

reviews = [
    "I love this phone",
    "The battery is terrible",
    "Great camera but poor battery"
]

for r in reviews:
    print(r.lower())

    import re

    text = "Visit https://example.com!!!   I LOVE NLP.  It's amazing :)"

    text = text.lower()
    text = re.sub(r"https?://\S+", "", text)  # remove URLs
    text = re.sub(r"[^\w\s]", "", text)  # remove punctuation
    text = re.sub(r"\s+", " ", text).strip()  # normalize spaces

    print(text)