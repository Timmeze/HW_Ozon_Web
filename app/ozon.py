def create_book(title, author, tags):
    return {
        'title': title,
        'author': author,
        'tags': tags
    }

def add_book(container, book):
    copy = container[:]
    copy.append(book)
    return copy
def search_book(container, item):
    clear_item = item#.replace("#", " ").strip().lower()
    result = []
    for book in container:
        if book['title'] == clear_item:
            result.append(book)
            continue
        for book in container:
            if clear_item in book['tags']:
                result.append(book)
                continue
        return result

    return result

