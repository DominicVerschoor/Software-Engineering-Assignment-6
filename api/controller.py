from api.kitchen import Order, all_order
from api.kitchen import all_menu


# For Order get time to delivery
def gettimetodelivery(order: Order):
    time = 0
    for menu in order.menu_list:
        time += menu.preptime

    if not order.takeaway:
        time += 15

    return time


def getallmenu():
    return all_menu


def getmenu(id: int):
    result = []
    for menu in all_menu:
        if menu['id'] == id:
            result.append(menu)

    return result


def getorder(id: int):

    for order in all_order:
        if order['id'] == id:
            return order

def getdeliverytime(id: int):
    result = []
    for order in all_order:
        if order['id'] == id:
            find_order = order
            delivery_time = order.time_to_delivery
            result.append(find_order)
            result.append(delivery_time)





