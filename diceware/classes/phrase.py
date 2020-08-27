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

    def as_string(self):
        words = [word_obj.word for word_obj in self.word_objects]
        return self.separator.join(words)

    def as_dict(self):
        return {
            "word_count": self.word_count,
            "separator": self.separator,
            "phrase": self.as_string(),
            "words": [word_obj.as_dict() for word_obj in self.word_objects]
        }
