# from typing_extensions import Counter

book_dir = "books/frankenstein.txt"
counted_let_list = []
lettercount = []


def _get_book_text():
    with open(book_dir) as f:
        book = f.read()
        return book


def _wordcounter():
    wc = len(_get_book_text().split())
    return wc


def _lettercounter():
    loca = list(_get_book_text().lower())
    lecount = {}
    for i in loca:
        if i in lecount:
            lecount[i] += 1
        elif i not in lecount:
            lecount[i] = 1
    return lecount


def _list_to_dict():
    lettercount = _lettercounter()
    for i in lettercount:
        let_dict = {"char": i, "num": lettercount[i]}
        counted_let_list.append(let_dict)
    return counted_let_list


def sort_on(item):
    return item["num"]


def _sort_dict_by_lettercount():
    _list_to_dict()
    counted_let_list.sort(reverse=True, key=sort_on)
    return counted_let_list
