import flask
from flask import jsonify, request

app = flask.Flask(__name__)
app.config["DEBUG"] = True

books = [
    {'id': 0,
     'title': 'Story of my life',
     'author': 'AATA FRO REAT  ',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/api/v1/resources/books/all', methods=['GET'])
def getBook():
    return jsonify(books)


@app.route('/api/v1/resources/books/', methods=['GET'])
def getSpecificBook():
    if 'id' in request.args:
        findID = int(request.args['id'])
    else:
        return "ID not provided"

    result = []
    for book in books:
        if book['id'] == findID:
            result.append(book)

    if len(result) == 0:
        return "Cannot find any book with this ID: " + str(findID)

    return jsonify(result)



app.run()
