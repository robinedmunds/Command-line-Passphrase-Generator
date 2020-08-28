from ..classes.phrase import Phrase
from ..parse_wordlist import from_file as parse_wordlist_from_file

# __init__ args: wordlist, word_count, separator


def parse_wordlist():
    return parse_wordlist_from_file(
        "wordlists\\eff_short_wordlist_1.txt")


def test_phrase_word_count():
    wordlist = parse_wordlist()
    phrase_obj = Phrase(wordlist, 3, ".")
    assert phrase_obj.word_count == 3


def test_phrase_words_match_count():
    wordlist = parse_wordlist()
    phrase_obj = Phrase(wordlist, 3, ".")
    assert len(phrase_obj.word_objects) == 3


def test_phrase_words_separator():
    wordlist = parse_wordlist()
    phrase_obj = Phrase(wordlist, 3, ".")
    assert phrase_obj.separator == "."


def test_phrase_as_dict_method_returns_dict():
    wordlist = parse_wordlist()
    phrase_obj = Phrase(wordlist, 3, ".")
    assert isinstance(phrase_obj.as_dict(), dict)


def test_phrase_as_string_method_returns_string():
    wordlist = parse_wordlist()
    phrase_obj = Phrase(wordlist, 3, ".")
    assert isinstance(phrase_obj.as_string(), str)
