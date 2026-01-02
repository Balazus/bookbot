import sys

# from typing import Dict
from stats import _sort_dict_by_lettercount, _wordcounter

book_path = ""


def _main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {_wordcounter()} total words")
    print("--------- Character Count -------")
    dict = _sort_dict_by_lettercount()
    for i in dict:
        print(f"{i['char']}: {i['num']}")
    # print(dict)
    print("============= END ===============")


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

elif len(sys.argv) == 2:
    book_path = sys.argv[1]

_main()

# _main()
