class Pants:
    def __init__(self, pants_colour, pants_waist_size, pants_length, pants_price):
        self.colour = pants_colour
        self.waist_size = pants_waist_size
        self.length = pants_length
        self.price = pants_price

    def change_price(self, new_price):
        self.price = new_price

    def discount_price(self, discount):
        return self.price * (1 - discount)


pants = Pants('red', 35, 36, 15.12)
print('pants', pants.colour, pants.waist_size, pants.length, pants.price)
pants.change_price(10)
print('price to be 10', pants.price)
print('price to be 9', pants.discount_price(.1))

print('You made it to the end of the check. Nice job!')


class SalesPerson:
    def __init__(self, first_name, last_name, employee_id, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.employee_id = employee_id
        self.salary = salary
        self.pants_sold = []
        self.total_sales = 0

    def sell_pants(self, pants_object):
        self.pants_sold.append(pants_object)

    def display_sales(self):
        for sold_pants in self.pants_sold:
            print('color: {}, waist_size: {}, length: {}, price: {}'
                  .format(sold_pants.colour, sold_pants.waist_size, sold_pants.length, sold_pants.price))

    def calculate_sales(self):
        total = 0
        for sold_pants in self.pants_sold:
            total += sold_pants.price
        self.total_sales = total
        return self.total_sales

    def calculate_commission(self, commission_percentage):
        total_sales = self.calculate_sales()
        return round(total_sales*commission_percentage, 2)


pants_one = Pants('red', 35, 36, 15.12)
pants_two = Pants('blue', 40, 38, 24.12)
pants_three = Pants('tan', 28, 30, 8.12)
print('pants_one: ', pants_one.colour, pants_one.waist_size, pants_one.length, pants_one.price)
print('pants_two: ', pants_two.colour, pants_two.waist_size, pants_two.length, pants_two.price)
print('pants_three: ', pants_three.colour, pants_three.waist_size, pants_three.length, pants_three.price)

salesperson = SalesPerson('Amy', 'Gonzalez', 2581923, 40000)
print('salesperson details: ', salesperson.first_name, salesperson.last_name, salesperson.employee_id, salesperson.salary,
      salesperson.pants_sold, salesperson.total_sales)
salesperson.sell_pants(pants_one)
print('first pants sold should be red: ', salesperson.pants_sold[0].colour)
salesperson.sell_pants(pants_two)
salesperson.sell_pants(pants_three)

print('total pants sold should be 3: ', len(salesperson.pants_sold))
print('total sales should be 47.36: ', salesperson.calculate_sales())
print('total sales should be 47.36: ', salesperson.calculate_sales())
print('total sales should be 47.36: ', salesperson.total_sales)
print('sales commission should be 4.74: ', salesperson.calculate_commission(.1))
