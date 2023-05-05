class BagOfWord:
    def __init__(self):
        # self.words = {}
        self.__words = {}  # deny access from out => private

    def add(self, word):
        self.__words[word.lower()] = self.__words.get(word.lower(), 0)+1


word = BagOfWord()
word.add('Mostafa')
print(word.__words)
