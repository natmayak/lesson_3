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

iPhone = Product('iPhone', 70000, stock=10)
print(iPhone)
iPhone.sell(5)
print(iPhone)
