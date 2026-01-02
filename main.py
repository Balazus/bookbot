# from typing import Dict

from stats import _sort_dict_by_lettercount, _wordcounter, book_dir


def _main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_dir}...")
    print("----------- Word Count ----------")
    print(f"Found {_wordcounter()} total words")
    print("--------- Character Count -------")
    dict = _sort_dict_by_lettercount()
    for i in dict:
        print(f"{i['char']}: {i['num']}")
    # print(dict)
    print("============= END ===============")


_main()
