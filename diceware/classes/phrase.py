from .word import Word


class Phrase:
    def __init__(self, wordlist, word_count, separator):
        self.word_count = word_count
        self.separator = separator
        self.word_objects = []

        for i in range(word_count):
            self.word_objects.append(
                Word(wordlist)
            )
