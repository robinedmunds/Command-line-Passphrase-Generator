from typing import TypedDict, Final
from math import floor, log
from ..die_roll import die_roll


class Word_as_dict(TypedDict, total=True):
    word: str
    word_list_key: int


class Word:
    def __init__(self, wordlist) -> None:
        self.word: str
        self.wordlist_key: int
        DIE_SIDES: Final[int] = 6

        roll_count: int = floor(log(len(wordlist), DIE_SIDES))
        word_key_list: tuple[str, ...] = tuple(
            [str(die_roll(DIE_SIDES)) for _ in range(roll_count)])
        word_key_string: str = "".join(word_key_list)
        word_key_int: int = int(word_key_string)

        self.word = wordlist[word_key_int]
        self.wordlist_key = word_key_int

    def as_dict(self) -> Word_as_dict:
        return {
            "word": self.word,
            "word_list_key": self.wordlist_key
        }
