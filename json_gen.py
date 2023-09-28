from diceware.parse_wordlist import from_file as parse_wordlist_from_file
from diceware.classes.phrases import Phrases
import json


def main():
    wordlist = parse_wordlist_from_file("wordlists\\eff_short_wordlist_1.txt")

    # wordlist, word_count, separator
    phrases_obj = Phrases(wordlist, 4, ",", 2)

    f = open("output.json", "w")
    f.write(json.dumps(phrases_obj.as_dict(), indent=2))
    f.close()


if __name__ == "__main__":
    main()
