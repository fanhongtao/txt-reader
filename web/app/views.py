import os

from flask import send_from_directory
from flask import render_template, request
from app import app

from app.data.book import get_book_list, get_book_index, get_book_content

@app.route('/')
@app.route('/index')
def index():
    template = 'index.html';
    book_list = get_book_list()
    kwargs = {
        'title': '书籍列表',
        'book_list': book_list
    }
    return render_template(template, **kwargs)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/book-index')
def bookindex():
    id = request.args.get('id')
    template = 'book-index.html';
    book, book_index = get_book_index(id)
    kwargs = {
        'title': book.name,
        'book': book,
        'book_index': book_index
    }
    return render_template(template, **kwargs)


@app.route('/book-content')
def bookcontent():
    id = request.args.get('id')
    index = int(request.args.get('index'))
    template = 'book-content.html';
    book, book_content, index_len = get_book_content(id, index)
    kwargs = {
        'title': book.name,
        'book': book,
        'pre_index': index - 1 if index > 1 else 0,
        'next_index': index + 1 if index < index_len else 0,
        'book_content': book_content
    }
    return render_template(template, **kwargs)

