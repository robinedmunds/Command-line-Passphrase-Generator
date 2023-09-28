from os import PathLike

Wordlist = dict[int, str]


def from_file(dicewareFile: str | PathLike) -> Wordlist | None:
    """Takes diceware wordlist file path. Returns dictionary object.

    Loads diceware formatted wordlist file into memory and returns dictionary
    object. Format: {1111: "lake"}
    """
    try:
        file = open(dicewareFile, "r")
        wordlist: Wordlist = {}

        for line in file:
            fields = line.split("\t")
            key = int(fields[0])
            word = fields[1].strip()
            # word = fields[1].replace("\r\n", "").replace("\n", "")
            wordlist[key] = word

        if len(wordlist) not in [6**n for n in range(4, 9)]:
            raise Exception

        return wordlist

    except FileNotFoundError:
        print("Diceware file not found. Check location and try again.")

    except ValueError:
        print("Diceware file is invalid or of incorrect length.")

    exit()
