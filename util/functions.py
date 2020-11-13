from unicodedata import normalize


def format(language, author, data, flag, url_name, id=1):
    return {
        '_id': id,
        'language': language,
        'author': author,
        'flag': flag,
        'url_name': url_name,
        'data': data
    }


def filter(data):
    return normalize('NFKC', data)
