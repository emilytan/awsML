class Clothing:

    def __init__(self, color, size, style, price):
        self.color = color
        self.size = size
        self.style = style
        self.price = price

    def change_price(self, price):
        self.price = price

    def calculate_discount(self, discount):
        return self.price * (1 - discount)

    def calculate_shipping(self, weight, rate):
        return weight * rate


class Shirt(Clothing):

    def __init__(self, color, size, style, price, long_or_short):
        Clothing.__init__(self, color, size, style, price)
        self.long_or_short = long_or_short

    def double_price(self):
        self.price = 2 * self.price


class Pants(Clothing):

    def __init__(self, color, size, style, price, waist):
        Clothing.__init__(self, color, size, style, price)
        self.waist = waist

    def calculate_discount(self, discount):
        return self.price * (1 - discount / 2)


class Blouse(Clothing):
    def __init__(self, color, size, style, price, country_of_origin):
        Clothing.__init__(self, color, size, style, price)
        self.country_of_origin = country_of_origin

    def triple_price(self):
        return self.price * 3

# TODO: Write a class called Blouse, that inherits from the Clothing class
# and has the the following attributes and methods:
#   attributes: color, size, style, price, country_of_origin
#     where country_of_origin is a string that holds the name of a
#     country
#
#   methods: triple_price, which has no inputs and returns three times
#     the price of the blouse
#

# TODO: Add a method to the clothing class called calculate_shipping.
#   The method has two inputs: weight and rate. Weight is a float
#   representing the weight of the article of clothing. Rate is a float
#   representing the shipping weight. The method returns weight * rate


clothing = Clothing('orange', 'M', 'stripes', 35)
blouse = Blouse('blue', 'M', 'luxury', 40, 'Brazil')
pants = Pants('black', 32, 'baggy', 60, 30)
print('color should be orange: ', clothing.color)
print('price should be 35: ', clothing.price)
print('color should be blue: ', blouse.color)
print('size should be M: ', blouse.size)
print('style should be luxury: ', blouse.style)
print('price should be 40: ', blouse.price)
print('country_of_origin should be Brazil: ', blouse.country_of_origin)
clothing_shipping = clothing.calculate_shipping(.5, 3)
print('clothing shipping should be {}: '.format(.5 * 3), clothing_shipping)
blouse_shipping = blouse.calculate_shipping(.5, 3)
print('blouse shipping should be {}: '.format(.5 * 3), blouse_shipping)

pants_discount = pants.calculate_discount(0.5)
print('pants price: ', pants.price)
print('pants discount: ', pants_discount)
blouse_discount = blouse.calculate_discount(0.5)
print('blouse price: ', blouse.price)
print('pants discount: ', blouse_discount)

# child pants override parents method of calculate_discount; it only affects the child methods