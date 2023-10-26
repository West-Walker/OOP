import random

class WordFinder:
    def __init__(self, file_path):
        self.words = self.load_words(file_path)
        print(f"{len(self.words)} words read")

    def load_words(self, file_path):
        with open(file_path, 'r') as file:
            words = [line.strip() for line in file]
        return words

    def random(self):
        if self.words:
            return random.choice(self.words)
        else:
            return "No words available"


class SpecialWordFinder(WordFinder):
    def load_words(self, file_path):
        with open(file_path, 'r') as file:
            words = [line.strip() for line in file if line.strip() and not line.startswith('#')]
        return words