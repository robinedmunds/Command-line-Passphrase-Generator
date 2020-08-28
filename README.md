# Command-line Diceware Passphrase Generator

## About

Command-line passphrase generator written by [Robin Edmunds](https://tersedigital.com) in Python3. Inspired by the work of [Arnold G. Reinhold](http://world.std.com/~reinhold/). Code structured in such a way as to make for easy code re-use in an API.

## Usage

Untested below Python v3.8

`python diceware-cmd.py`

    usage: diceware-cmd.py [-h] [-w WORDS] [-s SEPARATOR] [-c COUNT] [-r] [-l WORDLIST]

    optional arguments:
      -h, --help            show this help message and exit
      -w WORDS, --words WORDS
                            Number of words in each passphrase. (Default: 4)
      -s SEPARATOR, --separator SEPARATOR
                            Character to use as separator between words. NOTE: Special characters may need to be enclosed
                            in quotes. (Default: space)
      -c COUNT, --count COUNT
                            Number of passphrases to generate. (Default: 20)
      -r, --raw             Raw passphrase output omitting phrase lengths. (Default: False)
      -l WORDLIST, --wordlist WORDLIST
                            Wordlist file location. (Default: "wordlists/eff_short_wordlist_1.txt")

## Wordlists

[Arnold G. Reinhold](http://world.std.com/~reinhold/) has more wordlists linked on his website including lists in other languages.

The wordlists included in this repo are not mine. See respective attributions and licenses below.

| Name                       | Owner                                                 | License                                                         |
| -------------------------- | ----------------------------------------------------- | --------------------------------------------------------------- |
| eff_large_wordlist.txt     | [EFF](https://www.eff.org/dice)                       | [CC BY 3.0 US](https://creativecommons.org/licenses/by/3.0/us/) |
| eff_short_wordlist_1.txt   | [EFF](https://www.eff.org/dice)                       | [CC BY 3.0 US](https://creativecommons.org/licenses/by/3.0/us/) |
| eff_short_wordlist_2_0.txt | [EFF](https://www.eff.org/dice)                       | [CC BY 3.0 US](https://creativecommons.org/licenses/by/3.0/us/) |
| reinhold.txt               | [Arnold G. Reinhold](http://world.std.com/~reinhold/) | [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)       |

["Diceware" is a trademark of A G Reinhold](http://world.std.com/~reinhold/)

## Testing

Run `pytest` in parent directory
