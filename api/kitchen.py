from _datetime import datetime
from api.controller import gettimetodelivery

all_menu = []
all_order = []

class Menu:

    def __init__(self, id: int, name: str, vegetarian: bool, price: float, ingredient: str, preptime: float):
        self.id = id
        self.name = name
        self.vegetarian = vegetarian
        self.price = price
        self.ingredient = ingredient
        self.preptime = preptime

    def __repr__(self):
        return f"User {self.id}, {self.name}"


class Order:
    current_order_id = 0

    def __int__(self, customer_id: int, takeaway: bool, payment_type: str, address, menu_list, note: str):
        self.id = Order.current_order_id
        self.customer_id = customer_id
        self.status = "In Progress"
        self.order_time = datetime.now()
        self.takeaway = takeaway
        self.payment_type = payment_type
        self.address = address
        self.menu_list = menu_list
        self.note = note
        self.time_to_delivery = gettimetodelivery(self)
        Order.current_order_id += 1

    def __repr__(self):
        return f"Order {self.id}, {self.customer_id}, {self.status}"
