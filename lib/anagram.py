# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()
    
    def match(self, words):
        return [word for word in words if word.lower() != self.word and sorted(word.lower()) == sorted(self.word)]
        