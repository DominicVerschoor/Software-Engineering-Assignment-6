# Group 28
# Tantus Choomphupan    ID: i6286789
# Dominic Verschoor     ID: i6267365


from kitchen import OrderItem, Menu


# For Order get time to delivery
def gettimetodelivery(order: OrderItem):
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
    initOrder()
    for order in OrderItem.all_order:
        if order.id == id:
            return order

    return None


def getdeliverytime(id: int):
    result = []
    for order in OrderItem.all_order:
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


def initOrder():
    order0 = OrderItem(1001, True, "Creditcard", ["Maastricht", "Dorpstraat", "126"], "somthing", "No onion", 35)
    OrderItem.all_order.append(order0)
    order1 = OrderItem(1002, False, "Creditcard", ["Maastricht", "Centrum", "95/1"], "somthing", "Super spicy", 20)
    OrderItem.all_order.append(order1)
    order2 = OrderItem(1003, True, "Cash", ["Maastricht", "Mainstrat", "50/3"], "somthing", "", 40)
    OrderItem.all_order.append(order2)
    order3 = OrderItem(1001, False, "Cash", ["Maastricht", "Sittraat", "3"], "somthing", "Extra veggie", 50)
    OrderItem.all_order.append(order3)


def createorder(pizzas, takeaway: bool, payment_type: str, customer_id: int, note: str, delivery_address):
    menu_list, total_cooktime = convertorder(pizzas)
    newOrder = OrderItem(customer_id, takeaway, payment_type, delivery_address, menu_list, note, total_cooktime)
    OrderItem.all_order.append(newOrder)


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
    return OrderItem.all_order[len(OrderItem.all_order) - 1]


def cancelorder(id: int):
    toCancel = OrderItem.all_order[id]
    toCancel.status = "Cancelled"
    return toCancel
