from typing import TypedDict
from .phrase import Phrase, Phrase_as_dict

Wordlist = dict[int, str]


class Phrases_as_dict(TypedDict, total=True):
    word_count: int
    separator: str
    phrase_count: int
    phrases: list[Phrase_as_dict]


class Phrases:
    def __init__(self, wordlist: Wordlist, word_count: int, separator: str,
                 phrase_count: int):
        self.word_count: int = word_count
        self.separator: str = separator
        self.phrase_count: int = 0
        self.phrase_objects: list[Phrase] = []

        for _ in range(phrase_count):
            self.phrase_objects.append(
                Phrase(wordlist, word_count, separator)
            )
            self.phrase_count += 1

    def as_dict(self) -> Phrases_as_dict:
        return {
            "word_count": self.word_count,
            "separator": self.separator,
            "phrase_count": self.phrase_count,
            "phrases": [phrase_obj.as_dict() for phrase_obj in
                        self.phrase_objects],
        }
