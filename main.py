from diceware.parse_wordlist import from_file as parse_wordlist_from_file
from diceware.classes.phrase import Phrase


def main():
    wordlist = parse_wordlist_from_file("wordlists\\eff_short_wordlist_1.txt")

    # wordlist, word_count, separator
    phrase_obj = Phrase(wordlist, 6, ",")

    print(phrase_obj.as_string())


if __name__ == "__main__":
    main()
