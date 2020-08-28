from ..classes.phrases import Phrases
from ..parse_wordlist import from_file as parse_wordlist_from_file

# __init__ args: wordlist, word_count, separator, phrase_count


def parse_wordlist():
    return parse_wordlist_from_file(
        "wordlists\\eff_short_wordlist_1.txt")


def test_phrases_is_instance_of_Phrases():
    wordlist = parse_wordlist()
    phrases_obj = Phrases(wordlist=wordlist, word_count=5,
                          separator=".", phrase_count=7)
    assert isinstance(phrases_obj, Phrases)


def test_phrases_as_dict_method_returns_dict():
    wordlist = parse_wordlist()
    phrases_obj = Phrases(wordlist=wordlist, word_count=5,
                          separator=".", phrase_count=7)
    output = phrases_obj.as_dict()
    assert isinstance(output, dict)


def test_phrases_as_dict_method_returns_dict_containing_word_count():
    wordlist = parse_wordlist()
    phrases_obj = Phrases(wordlist=wordlist, word_count=5,
                          separator=".", phrase_count=7)
    output = phrases_obj.as_dict()
    assert "word_count" in output
    assert isinstance(output["word_count"], int)


def test_phrases_as_dict_method_returns_dict_containing_phrase_count(
):
    wordlist = parse_wordlist()
    phrases_obj = Phrases(wordlist=wordlist, word_count=5,
                          separator=".", phrase_count=7)
    output = phrases_obj.as_dict()
    assert "phrase_count" in output
    assert isinstance(output["phrase_count"], int)


def test_phrases_as_dict_method_returns_dict_containing_separator(
):
    wordlist = parse_wordlist()
    phrases_obj = Phrases(wordlist=wordlist, word_count=5,
                          separator=".", phrase_count=7)
    output = phrases_obj.as_dict()
    assert "separator" in output
    assert isinstance(output["separator"], str)


def test_phrases_as_dict_method_returns_dict_containing_phrases(
):
    wordlist = parse_wordlist()
    phrases_obj = Phrases(wordlist=wordlist, word_count=5,
                          separator=".", phrase_count=7)
    output = phrases_obj.as_dict()
    assert "phrases" in output
    assert isinstance(output["phrases"], list)
