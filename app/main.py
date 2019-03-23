from flask import Flask, render_template

from app.ozon import create_book, add_book, search_book


def main():
    app = Flask(__name__)
    container = []
    anna_karenina_tags = ['поезд', 'любовь', 'толстой']
    war_and_piece_tags = ['война', 'любовь', 'толстой']

    wp = create_book('War And Peace', 'Tolstoy', war_and_piece_tags)
    anna = create_book('Anna Karenina', 'Tolstoy', anna_karenina_tags)


    container = add_book(container, wp)
    container = add_book(container, anna)



    @app.route('/')
    def index():
        from flask import request
        search = request.args.get('search')
        if search:
            results = search_book(container, search)
            return render_template('in.html', books=results)
        return render_template('in.html', books=container, search=search)


    app.run(port=9876, debug=True)


if __name__ == '__main__':
    main()
