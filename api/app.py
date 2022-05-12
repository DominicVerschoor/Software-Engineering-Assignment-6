import flask
from flask import jsonify, request
from api.controller import getallmenu, getmenu, getorder

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Pizza Restaurant</h1><p>This site is a prototype API for ordering pizza via web client</p>"


@app.route('/api/v1/pizza', methods=['GET'])
def all_pizza():
    return jsonify(getallmenu)


@app.route('/api/v1/pizza/', methods=['GET'])
def get_pizza_by_id():
    if 'id' in request.args:
        findID = int(request.args['id'])
    else:
        return "ID not found"

    if len(getmenu(findID)) == 0:
        return jsonify("Pizza not found")

    return jsonify(getmenu(findID))


@app.route('/api/v1/order/', methods=['GET'])
def get_order_by_id():
    if 'id' in request.args:
        findID = int(request.args['id'])
    else:
        return "ID not found"

    if len(getorder(findID)) == 0:
        return jsonify("ID not valid")

    return jsonify(getorder(findID))

@app.route('/api/v1/order/deliverytime/', methods=['GET'])
def get_order_deliverytime():
    result = []
    if 'id' in request.args:
        findID = int(request.args['id'])
    else:
        return "ID not found"

    if len(getorder(findID)) == 0:
        return jsonify("ID not valid")

    result.append(getorder(findID))



    return jsonify(result)