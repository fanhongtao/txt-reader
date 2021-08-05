import hashlib
import pathlib
import re
import sys

from app.const import const

class Book:
    def __init__(self):
        super().__init__()
        self.name = ''   # 书名
        self.path = ''   # 路径
        self.id  = ''    # 路径对应的 MD5，用作已知的唯一标识

class BookIndex:
    def __init__(self):
        super().__init__()
        self.count = 0      # 编号
        self.content = ''   # 内容


def get_book_list():
    book_list = []
    directory = pathlib.Path(const.BOOK_PATH)
    for path in sorted(directory.rglob('*')):
        if path.is_file():
            if path.name.lower().endswith('.txt'):
                book = Book()
                book.name = path.stem
                book.path = path
                book.id = hashlib.md5(str(path).encode(encoding='UTF-8')).hexdigest()
                book_list.append(book)
    return book_list


def get_book_index(id):
    book_index = []
    list = get_book_list()
    for book in list:
        if book.id == id:
            book_index = _get_book_index(book)
            return book, book_index
    print("Can't find book with id: " + id)
    return None, book_index

def _get_book_index(book):
    count = 0
    line_num = 0
    book_index = []
    with open(book.path) as f:
        for line in f:
            line_num = line_num + 1
            if re.match('第(\d+|(一|二|三|四|五|六|七|八|九|零|十|百|千)+)章', line):
                count = count + 1
                index = BookIndex()
                index.count = count
                index.content = line
                index.line_num = line_num
                book_index.append(index)
    return book_index


def get_book_content(id, index):
    book_content = []
    book, book_index = get_book_index(id)
    if not book is None:
        book_content = _get_book_content(book, book_index, index)
    return book, book_content, len(book_index)

def _get_book_content(book, book_index, index):
    curr_line = book_index[index - 1].line_num - 1
    if index < len(book_index):
        next_line = book_index[index].line_num - 1
    else:
        next_line = sys.maxsize

    book_content = []
    with open(book.path) as file:
        for dummy_n, line in zip(range(curr_line), file):
            pass
        for dummy_n, line in zip(range(next_line - curr_line), file):
            line = line.rstrip('\r\n')
            book_content.append(line)
    return book_content
