import datetime


class Order:
    all_order = []
    current_order_id = 0

    def __int__(self, customer_id: int, takeaway: bool, payment_type: str, address, menu_list, note: str, total_cooktime: float):
        self.id = Order.current_order_id
        self.customer_id = customer_id
        self.status = "In Progress"
        self.order_time = datetime.datetime.now()
        self.takeaway = takeaway
        self.payment_type = payment_type
        self.address = address
        self.menu_list = menu_list
        self.note = note
        self.total_cooktime = total_cooktime
        if takeaway:
            self.delivery_time = self.order_time + datetime.timedelta(0, total_cooktime*60)
        else:
            self.delivery_time = self.order_time + datetime.timedelta(0, total_cooktime*60) + datetime.timedelta(0, 30*60)
        Order.current_order_id += 1

    def __repr__(self):
        return f"Order ID: {self.id},<br> Customer ID: {self.customer_id},<br> Status: {self.status},<br> Order at: {self.order_time},<br> " \
               f"Note: {self.note},<br> Takeaway: {self.takeaway},<br> Payment: {self.payment_type},<br> Address: {self.address},<br> " \
               f"Pizza ordered: {self.menu_list} <br><br>, Order at: {self.order_time},<br> Delivery Time: {self.delivery_time} "


class Menu:
    all_menu = []

    def __init__(self, id: int, name: str, vegetarian: bool, price: float, ingredient, preptime: float):
        self.id = id
        self.name = name
        self.vegetarian = vegetarian
        self.price = price
        self.ingredient = ingredient
        self.preptime = preptime

    def __repr__(self):
        return f"Pizza ID: {self.id},<br> Name: {self.name},<br> Vegetarian: {self.vegetarian},<br> Price: {self.price} €<br> " \
               f"Toppings: {self.ingredient}<br> Preparation time: {self.preptime} minutes<br><br>"
