#!/usr/bin/env python
import json
import argparse
from pathlib import Path
from diceware.parse_wordlist import from_file as parse_wordlist
from diceware.classes.phrases import Phrases


def main():
    # CONSOLE UI
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

    # GENERATE
    kwargs = {
        "wordlist": parse_wordlist(Path(args.wordlist)),
        "word_count": args.words,
        "separator": args.separator,
        "phrase_count": args.count
    }
    phrases_dict = Phrases(**kwargs).as_dict()
    phrases = [phrase["phrase"] for phrase in phrases_dict["phrases"]]

    # CONSOLE OUTPUT
    if args.raw:
        for p in phrases:
            print(f"{p}")
    else:
        print("\nLength\tPassphrase\n" +
              "------\t----------\n")
        for p in phrases:
            length = len(p)
            print(f"{length}\t{p}")
        print()


if __name__ == "__main__":
    main()
