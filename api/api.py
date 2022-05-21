# Group 28
# Tantus Choomphupan    ID: i6286789
# Dominic Verschoor     ID: i6267365

import datetime

import flask
from flask import request, make_response, render_template
from controller import getallmenu, getmenu, getorder, initKitchen, getnewestorder, createorder, cancelorder

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
    pizzastr = ""
    for menu in menu_list:
        pizzastr += repr(menu) + "<br>"
    return make_response(pizzastr, 200)


# 2 GET/pizza/?id=x TODO: Completed
@app.route('/api/v1/pizza/', methods=['GET'])
def get_pizza_by_id():
    if 'id' in request.args:
        findID = int(request.args['id'])
    else:
        return make_response("ID not found", 300)

    if getmenu(findID) is None:
        return make_response("Pizza not found", 300)

    findMenu = repr(getmenu(findID))
    return make_response(findMenu, 200)


# 3 GET/order/?id=x TODO: Completed
@app.route('/order/', methods=['GET'])
def get_order_by_id():
    if 'id' in request.args:
        findID = int(request.args['id'])
    else:
        return make_response("ID not found", 300)

    if getorder(findID) is None:
        print("No ID in list")
        return make_response("Order not found", 300)

    findOrder = getorder(findID)
    return make_response(repr(findOrder), 200)


# 4 POST/order TODO: Completed
@app.route('/orderpost', methods=['POST'])
def create_order():
    try:
        pizzas = request.form["pizzas"]
        takeaway = request.form["takeaway"]
        payment_type = request.form["payment_type"]
        customer_id = request.form["customer_id"]
        note = request.form["note"]
        delivery_address = request.form["delivery_address"]
        createorder(pizzas, bool(takeaway), payment_type, int(customer_id), note, delivery_address)
        print("Create complete")

    except:
        return make_response("The format of the object is not valid", 400)

    return make_response(repr(getnewestorder()), 200)


# Rendering User interface for making order TODO: Completed
@app.route('/orderpost', methods=['GET'])
def create_order_page():
    return render_template("create_order.html")


# 5 PUT/order/cancel/?id=x&status="cancelled" TODO: Completed
@app.route('/order/cancel/', methods=['PUT'])
def cancel_order():
    if 'id' in request.args:
        findID = int(request.args['id'])
    else:
        return make_response("ID not found", 300)

    toCancel = getorder(findID)

    if toCancel is None:
        return make_response("Order ID not found in server database.", 404)

    if toCancel.status != "In Progress":
        return make_response("Unable to cancel an already canceled or delivered order.", 422)

    if datetime.datetime.now() - toCancel.order_time >= datetime.timedelta(0, 5 * 60):
        return make_response("Unable to cancel your order after 5 minute have elapsed.", 412)

    return make_response(repr(cancelorder(findID)), 200)


# 6 GET/order/deliverytime/?id=x TODO: Completed
@app.route('/order/deliverytime/', methods=['GET'])
def get_order_deliverytime():
    if 'id' in request.args:
        findID = int(request.args['id'])
    else:
        return make_response("ID not found", 300)

    if getorder(findID) is None:
        return make_response("Order not found", 404)

    findOrder = getorder(findID)
    return make_response(repr(findOrder), 200)


app.run()
