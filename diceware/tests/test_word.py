from ..classes.word import Word
from ..parse_wordlist import from_file as parse_wordlist_from_file

# __init__ args: wordlist


def parse_wordlist():
    return parse_wordlist_from_file(
        "wordlists\\eff_short_wordlist_1.txt")


def test_word_word_is_type_string():
    wordlist = parse_wordlist()

    word_obj = Word(wordlist)
    assert isinstance(word_obj.word, str)


def test_word_wordlist_key_is_type_int():
    wordlist = parse_wordlist()

    word_obj = Word(wordlist)
    assert isinstance(word_obj.wordlist_key, int)


def test_word_as_dict_method_returns_dict():
    wordlist = parse_wordlist_from_file(
        "wordlists\\eff_short_wordlist_1.txt")

    word_obj = Word(wordlist)
    assert isinstance(word_obj.as_dict(), dict)
