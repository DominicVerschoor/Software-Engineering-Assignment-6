
from kitchen import Order, Menu


# For Order get time to delivery
def gettimetodelivery(order: Order):
    time = 0
    for menu in order.menu_list:
        time += menu.preptime

    if not order.takeaway:
        time += 15

    return time


def getallmenu():
    return Menu.all_menu


def getmenu(id: int):
    for menu in Menu.all_menu:
        if menu.id == id:
            return menu

    return None


def getorder(id: int):
    print(Order.all_order)
    for order in Order.all_order:
        print(order.id)
        if order.id == id:
            return order

    return None


def getdeliverytime(id: int):
    result = []
    for order in Order.all_order:
        if order['id'] == id:
            find_order = order
            delivery_time = order.time_to_delivery
            result.append(find_order)
            result.append(delivery_time)


def initKitchen():
    pizza0 = Menu(0, "Margarita", False, 8.99, ["Tomato", "Mozerella", "Basil"], 10)
    Menu.all_menu.append(pizza0)
    pizza1 = Menu(1, "Pepperoni", False, 12.49, ["Tomato", "Mozerella", "Pepperoni"], 12)
    Menu.all_menu.append(pizza1)
    pizza2 = Menu(2, "Hawaiian", False, 14.99, ["Tomato", "American Cheese", "Ham", "Pineapple"], 15)
    Menu.all_menu.append(pizza2)
    pizza3 = Menu(3, "Vegie Deluxe", True, 8.99, ["Tomato", "Mozerella", "Sweet Peper", "Olives"], 10)
    Menu.all_menu.append(pizza3)
    pizza4 = Menu(4, "Triple Cheese", True, 12.49, ["Mozerella", "Parmesan", "American Cheese"], 15)
    Menu.all_menu.append(pizza4)


def createorder(pizzas, takeaway: bool, payment_type: str, customer_id: int, note: str, delivery_address):
    menu_list, total_cooktime = convertorder(pizzas)
    newOrder = Order()
    newOrder.__int__(customer_id, takeaway, payment_type, delivery_address, menu_list, note, total_cooktime)
    Order.all_order.append(newOrder)


def convertorder(pizzas: str):
    pizzas_list = list(pizzas.split(","))
    temp = []
    cooktime = 0
    for i in range(len(pizzas_list)):
        menu = Menu.all_menu[int(pizzas_list[i])]
        temp.append(menu)
        cooktime = cooktime + menu.preptime

    return temp, cooktime


def getnewestorder():
    return Order.all_order[len(Order.all_order)-1]
