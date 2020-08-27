from ..classes.phrase import Phrase


class Phrases:
    def __init__(self, wordlist, word_count, separator, phrase_count):
        self.word_count = word_count
        self.separator = separator
        self.phrase_count = 0
        self.phrase_objects = []

        for i in range(phrase_count):
            self.phrase_objects.append(
                Phrase(wordlist, word_count, separator)
            )
            self.phrase_count += 1

    def as_dict(self):
        return {
            "word_count": self.word_count,
            "separator": self.separator,
            "phrase_count": self.phrase_count,
            "phrases": [phrase_obj.as_dict() for phrase_obj in self.phrase_objects],
        }
