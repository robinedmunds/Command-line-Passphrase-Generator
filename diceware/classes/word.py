from math import floor, log
from ..die_roll import die_roll


class Word:
    def __init__(self, wordlist):
        self.word = None
        self.wordlist_key = None

        wordlist_length = len(wordlist)

        roll_count = floor(log(wordlist_length, 6))
        word_key_list = [str(die_roll()) for i in range(roll_count)]
        word_key_string = "".join(word_key_list)
        word_key_int = int(word_key_string)

        self.word = wordlist[word_key_int]
        self.wordlist_key = word_key_int

    def as_dict(self):
        return {
            "word": self.word,
            "word_list_key": self.wordlist_key
        }
