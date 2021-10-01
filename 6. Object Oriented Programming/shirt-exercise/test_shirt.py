class Shirt:
    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        return self.price * (1 - discount)


shirt_one = Shirt('red', 'S', 'long-sleeve', 25)
print('shirt price', shirt_one.price)
shirt_one.change_price(10)
print('shirt price', shirt_one.price)
# shirt_one.price = shirt_one.discount(0.12)
# print('discount price', shirt_one.price)
print(shirt_one.discount(0.12))

shirt_two = Shirt('orange', 'L', 'short-sleeve', 10)

total = shirt_one.price + shirt_two.price
print('total_shirt_price', total)

total_discount = shirt_one.discount(0.14) + shirt_two.discount(0.06)
print('total_discounted_shirt_price_', total_discount)

from shirt_unit_test import run_tests

run_tests(shirt_one, shirt_two, total, total_discount)

