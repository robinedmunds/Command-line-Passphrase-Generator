from diceware.parse_wordlist import from_file as parse_wordlist_from_file
from diceware.classes.word import Word


def main():
    wordlist = parse_wordlist_from_file("wordlists\\eff_short_wordlist_1.txt")
    word_obj = Word(wordlist=wordlist)
    print(word_obj.word, word_obj.wordlist_key)


if __name__ == "__main__":
    main()
