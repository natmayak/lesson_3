class Product:
    def __init__(self, name, price, discount=0, stock=0, max_discount=20.0):
        self.name = name.strip()
        if not len(self.name) >= 2:
            raise ValueError('Too short name')
        self.price = abs(float(price))
        self.stock = abs(int(stock))
        self.max_discount = abs(int(max_discount))
        if self.max_discount > 99:
            raise ValueError('Discount is too big')
        self.discount = abs(float(discount))
        if self.discount > self.max_discount:
            self.discount = self.max_discount

    def sell(self, items_count=1):
        if items_count > self.stock:
            raise ValueError('Item is not in stock at the moment')
        self.stock -= items_count

    def discounted(self):
        return self.price - self.price * self.discount / 100

    def __repr__(self):
        return f'<Product name: {self.name}, price: {self.price}, stock: {self.stock}>'

class Phone(Product):
    def __init__(self, name, price, colour, discount=0, stock=0, max_discount=20.0):
        super().__init__(name, price, discount, stock, max_discount)
        self.colour = colour

    def __repr__(self):
        return f'<Phone name: {self.name}, price: {self.price}, stock: {self.stock}>'

class Table(Product):
    def __init__(self, name, price, colour, material, discount=0, stock=0, max_discount=20.0):
        super().__init__(name, price, discount, stock, max_discount)
        self.colour = colour
        self.material = material

    def __repr__(self):
        return f'<Table name: {self.name}, price: {self.price}, stock: {self.stock}>'


my_phone = Phone('iPhone', 70000, 'black')
print(my_phone)
print(my_phone.colour)

my_table = Table('Kitchen table', 50000, 'birch', 'wood')
print(my_table)
print(my_table.colour)
print(my_table.material)