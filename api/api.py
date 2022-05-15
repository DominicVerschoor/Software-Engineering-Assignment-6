import flask
from flask import jsonify, request, make_response, render_template
from controller import getallmenu, getmenu, getorder, initKitchen, getnewestorder, createorder

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    initKitchen()
    return "<h1>Pizza Restaurant</h1><p>This site is a prototype API for ordering pizza via web client</p>"


# 1 GET/pizza - return all pizza TODO: Completed
@app.route('/api/v1/pizza', methods=['GET'])
def all_pizza():
    menu_list = getallmenu()
    str = ""
    for menu in menu_list:
        str += repr(menu) + "<br>"
    print(str)
    return make_response(str, 200)


# 2 GET/pizza/?id=x TODO: Completed
@app.route('/api/v1/pizza/', methods=['GET'])
def get_pizza_by_id():
    if 'id' in request.args:
        findID = int(request.args['id'])
    else:
        return make_response("ID not found", 300)
    print(findID)
    if getmenu(findID) is None:
        return make_response("Pizza not found", 300)

    findMenu = repr(getmenu(findID))
    return make_response(findMenu, 200)


# 3 GET/order/?id=x TODO: Static problem + method not calling
@app.route('/order/find/', methods=['GET'])
def get_order_by_id():
    print("HELP?")
    if 'id' in request.args:
        findID = int(request.args['id'])
    else:
        return make_response("ID not found", 300)

    print(findID)
    print("Helppp")
    if getorder(findID) is None:
        return make_response("Order not found", 300)

    findOrder = getorder(findID)
    return make_response(findOrder, 200)


# 4 POST/order TODO: Completed
@app.route('/order', methods=['POST'])
def create_order():
    try:
        pizzas = request.form["pizzas"]
        takeaway = request.form["takeaway"]
        payment_type = request.form["payment_type"]
        customer_id = request.form["customer_id"]
        note = request.form["note"]
        delivery_address = request.form["delivery_address"]
        createorder(pizzas, bool(takeaway), payment_type, int(customer_id), note, delivery_address)
    except:
        return make_response("The format of the object is not valid", 400)

    return make_response(repr(getnewestorder()), 200)


# Rendering User interface for making order TODO: Completed
@app.route('/order/', methods=['GET'])
def create_order_page():
    return render_template("create_order.html")


# 5 PUT/order/cancel/?id=x&status="cancelled" TODO: Ongoing
@app.route('/order/cancel/', methods=['PUT'])
def cancel_order():
    pass


@app.route('/order/cancel/', methods=['GET'])
def cancel_order_page():
    return make_response()


# 6 GET/order/deliverytime/?id=x
@app.route('/order/deliverytime/', methods=['GET'])
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


app.run()
