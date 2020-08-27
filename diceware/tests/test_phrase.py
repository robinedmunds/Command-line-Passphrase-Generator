from ..classes.phrase import Phrase
from ..parse_wordlist import from_file as parse_wordlist_from_file


def test_phrase_word_count():
    wordlist = parse_wordlist_from_file(
        "wordlists\\eff_short_wordlist_1.txt")

    phrase_obj = Phrase(wordlist, 3, ".")
    assert phrase_obj.word_count == 3


def test_phrase_words_match_count():
    wordlist = parse_wordlist_from_file(
        "wordlists\\eff_short_wordlist_1.txt")

    phrase_obj = Phrase(wordlist, 3, ".")
    assert len(phrase_obj.word_objects) == 3


def test_phrase_words_separator():
    wordlist = parse_wordlist_from_file(
        "wordlists\\eff_short_wordlist_1.txt")

    phrase_obj = Phrase(wordlist, 3, ".")
    assert phrase_obj.separator == "."
