import json
import argparse
from diceware.parse_wordlist import from_file as parse_wordlist
from diceware.classes.phrases import Phrases


def main():
    help = json.loads(open("args.json", "r").read())
    parser = argparse.ArgumentParser(
        description=help["description"]
    )
    parser.add_argument(
        "-w", "--words", type=int, default=4, help=help["words"]
    )
    parser.add_argument(
        "-s", "--separator", type=str, default=" ", help=help["separator"]
    )
    parser.add_argument(
        "-c", "--count", type=int, default=20, help=help["count"]
    )
    parser.add_argument(
        "-r", "--raw", default=False, action="store_true", help=help["raw"]
    )
    parser.add_argument(
        "-l", "--wordlist", type=str,
        default="wordlists/eff_short_wordlist_1.txt", help=help["wordlist"]
    )
    args = parser.parse_args()
    kwargs = {
        "words": args.words,
        "separator": args.separator,
        "count": args.count,
        "wordlist": parse_wordlist(args.wordlist)
    }


if __name__ == "__main__":
    main()
