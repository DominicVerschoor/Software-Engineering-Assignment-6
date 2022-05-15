
from kitchen import Order, all_order, all_menu, Menu


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
    for menu in all_menu:
        if menu.id == id:
            return menu

    return None


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

def initKitchen():
    global all_menu
    pizza0 = Menu(0, "Margarita", False, 8.99, ["Tomato", "Mozerella", "Basil"], 10)
    all_menu.append(pizza0)
    pizza1 = Menu(1, "Pepperoni", False, 12.49, ["Tomato", "Mozerella", "Pepperoni"], 12)
    all_menu.append(pizza1)
    pizza2 = Menu(2, "Hawaiian", False, 14.99, ["Tomato", "American Cheese", "Ham", "Pineapple"], 15)
    all_menu.append(pizza2)
    pizza3 = Menu(3, "Vegie Deluxe", True, 8.99, ["Tomato", "Mozerella", "Sweet Peper", "Olives"], 10)
    all_menu.append(pizza3)
    pizza4 = Menu(4, "Triple Cheese", True, 12.49, ["Mozerella", "Parmesan", "American Cheese"], 15)
    all_menu.append(pizza4)


def createorder():
