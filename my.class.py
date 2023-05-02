class BagOfWord:
    def __init__(self):
        self.words = {}

    def add(self, word):
        self.words[word.lower()] = self.words.get(word.lower(), 0)+1


word = BagOfWord()
word.add('Mostafa')
print(word.words)
