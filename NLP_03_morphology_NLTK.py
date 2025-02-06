import re
def simple_tokenize(text):
    return re.findall(r'\b\w+\b', text)

def simple_stem(word):
    suffixes = ('ing', 'ed', 'es', 's')
    for suffix in suffixes:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word
text = "Running wolves are faster than jumping foxes."
words = simple_tokenize(text)
print("Original Words:", words)
stemmed_words = [simple_stem(word) for word in words]
print("Stemmed Words:", stemmed_words)
