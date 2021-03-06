#! /usr/bin/python
# -*- coding: utf-8 -*-

from atexit import register
from re import compile
from MyThread import MyThread
from time import ctime
from urllib.request import urlopen as uopen


REGEX = compile(b"#([\d,]+) in Books")
AMIZ = "http://amazon.com/dp/"
ISBNS = {
    "0132269937" : "Core Python Programming",
    "0132356139" : "Python Web Development with Django",
    "0137143419" : "Python Fundamentals"
}

def getRanking(isbn):
    try:
        page = uopen("%s%s"%(AMIZ, isbn))       # or str.format
        data = page.read()
        return REGEX.findall(data)[0]
    except:
        return None
    finally:
        if page in locals():
            page.close()


def _showRanking(isbn):
    print("- %r ranked %s" % (ISBNS[isbn], getRanking(isbn)))

def main():
    print("At", ctime(), "on Amazon")
    threads = []
    for isbn in ISBNS:
        threads.append(MyThread(func = _showRanking, args = (isbn,), name = _showRanking.__name__))

    for thread in threads:
        thread.start()

@register
def _atexit():
    print("all done at:", ctime())

if __name__ == "__main__":
    main()