from typing import TypedDict
from .word import Word, Word_as_dict

Wordlist = dict[int, str]


class Phrase_as_dict(TypedDict, total=True):
    word_count: int
    separator: str
    phrase: str
    words: list[Word_as_dict]


class Phrase:
    def __init__(self, wordlist: Wordlist, word_count: int,
                 separator: str) -> None:
        self.word_count: int = word_count
        self.separator: str = separator
        self.word_objects: list[Word] = []

        for _ in range(word_count):
            self.word_objects.append(
                Word(wordlist)
            )

    def as_string(self) -> str:
        words: list[str] = [word_obj.word for word_obj in self.word_objects]

        return self.separator.join(words)

    def as_dict(self) -> Phrase_as_dict:
        return {
            "word_count": self.word_count,
            "separator": self.separator,
            "phrase": self.as_string(),
            "words": [word_obj.as_dict() for word_obj in self.word_objects]
        }
