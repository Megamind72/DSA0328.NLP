from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

words = ["running", "flies", "easily", "cats", "happily", "denied", "relational"]

stemmed_words = [stemmer.stem(word) for word in words]

print("Original Words → Stemmed Words")
for word, stemmed in zip(words, stemmed_words):
    print(f"{word} → {stemmed}")
